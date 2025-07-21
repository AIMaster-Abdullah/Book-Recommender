# Book Recommendation System

A personalized book recommendation system based on user interests using Natural Language Processing (NLP) and semantic search with sentence embeddings.

---

## Features

- Clean and preprocess book data
- Generate embeddings for book descriptions using Sentence Transformers
- Use FAISS for fast similarity search
- Interactive web interface built with Gradio
- Command-line interface (CLI) for local usage

---

## Installation

1. Clone the repository:

git clone https://github.com/yourusername/book-recommender.git
cd book-recommender

```

2. Install the dependencies:

```
pip install -r requirements.txt


### Web Interface
Run the web app with:

bash
Copy
Edit
python recommender_web.py
This will start a local web server and open the recommendation interface in your browser.

## Command-Line Interface (CLI)
Run the CLI app with:

bash
Copy
Edit
python recommender_cli.py
Follow the prompts in the terminal to enter your preferences and get book recommendations.

## Project Structure
books.csv: Dataset containing books and their descriptions

recommender_web.py: Web interface implemented with Gradio

recommender_cli.py: Command-line interface implementation

requirements.txt: Project dependencies

book_cleaned.csv, book_embed.npy, book_faiss.idx: Generated files for cleaned data and search index

## Notes
Ensure the books.csv file is placed in the data/ folder or update the file path accordingly in the scripts.

The first run may take some time to clean the data and build the search index.

For best results, provide specific topics or genres when searching (e.g., "psychology", "adventure", "AI").

## License
MIT License

## Contact
For questions or feedback, please contact:

## Abdullah Ibrahem Mohammed AL-Mashni
## 📧 abdullahalmashni2003@gmail.com

yaml
Copy
Edit
