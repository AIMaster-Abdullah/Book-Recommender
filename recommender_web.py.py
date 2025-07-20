import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss
import os
import re
from nltk.corpus import stopwords
from spellchecker import SpellChecker
import unicodedata
from contractions import fix
import nltk
import spacy
import gradio as gr

# تحميل نموذج اللغة من Spacy
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    import spacy.cli
    spacy.cli.download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

spell = SpellChecker()

file_path = "/content/books.csv"
cleaned_file = "book_cleaned.csv"
embed_file = "book_embed.npy"
faiss_file = "book_faiss.idx"

# تنظيف النص
def clean_text_simple(text):
    text = str(text).lower()
    text = re.sub(r'<.*?>', ' ', text)
    text = re.sub(r'http\S+|www\S+', '', text)
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'(.)\1{2,}', r'\1\1', text)
    text = re.sub(r'\s+', ' ', text).strip()
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    return text

# التصفية والاختزال (lemmatization)
def clean_and_lemma(text):
    doc = nlp(text)
    tokens = [
        token.lemma_ for token in doc
        if not token.is_stop and not token.is_punct and not token.is_space and token.is_alpha and len(token.text) > 1
    ]
    return ' '.join(tokens)

# تصحيح الأخطاء الإملائية
def fix_spelling(text):
    words = text.split()
    corrected = [spell.correction(word) for word in words]
    return ' '.join(corrected)

# تنظيف البيانات
def clean_data(df, use_spell=False):
    df = df.dropna(subset=['Book', 'Description'])
    df['full_text'] = df['Book'].astype(str) + ". " + df['Description'].astype(str)
    df['cleaned'] = df['full_text'].apply(clean_text_simple)
    if use_spell:
        df['cleaned'] = df['cleaned'].apply(fix_spelling)
    df['cleaned'] = df['cleaned'].apply(clean_and_lemma)
    return df

# تحميل الكتب أو تنظيفها أول مرة
def load_books():
    if os.path.exists(cleaned_file):
        data = pd.read_csv(cleaned_file)
    else:
        if not os.path.exists(file_path):
            print("Error: book.csv not found.")
            exit()
        data = pd.read_csv(file_path)
        data = clean_data(data)
        data.to_csv(cleaned_file, index=False)
    return data

# إنشاء أو تحميل الفهرس
def load_or_create_index(data, model):
    if os.path.exists(embed_file) and os.path.exists(faiss_file):
        emb = np.load(embed_file).astype('float32')
        index = faiss.read_index(faiss_file)
    else:
        emb_list = model.encode(data['cleaned'].tolist(), show_progress_bar=True)
        emb = np.array(emb_list).astype('float32')
        index = faiss.IndexFlatL2(emb.shape[1])
        index.add(emb)
        np.save(embed_file, emb)
        faiss.write_index(index, faiss_file)
    return index

# نظام التوصية
def recommend_books(topics, count, min_rating, genres):
    if not topics.strip():
        return "Please enter at least one topic."

    topic_list = [t.strip().lower() for t in topics.split(',') if t.strip()]
    genre_list = [g.strip().lower() for g in genres.split(',') if g.strip()]
    user_text = '. '.join(topic_list)

    user_emb = model.encode([user_text]).astype('float32')
    dists, ids = index.search(user_emb, int(count))

    results = ""
    for i in ids[0]:
        book = books.iloc[i]
        rate = float(book['Avg_Rating'])
        genre = str(book['Genres']).lower()

        if rate < min_rating:
            continue
        if genre_list and not any(g in genre for g in genre_list):
            continue

        results += f"Title: {book['Book']}\n"
        results += f"Genres: {book['Genres']}\n"
        results += f"Rating: {book['Avg_Rating']}\n"
        results += f"Summary: {book['Description'][:300]}...\n\n---\n\n"

    if not results:
        return "No books found matching your filters."
    return results

# تشغيل الواجهة
books = load_books()
model = SentenceTransformer('all-MiniLM-L6-v2')
index = load_or_create_index(books, model)

gr.Interface(
    fn=recommend_books,
    inputs=[
        gr.Textbox(label="Topics (comma-separated)", placeholder="Fantasy, science fiction, historical fiction"),
        gr.Slider(1, 20, step=1, label="Number of books"),
        gr.Slider(0, 5, step=0.5, label="Minimum Rating"),
        gr.Textbox(label="Genres (optional)", placeholder="Fantasy, Classics, Young Adult")
    ],
    outputs="text",
    title="Book Recommendation System",
    description="Get book recommendations based on your interests."
).launch()
