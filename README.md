# Book Recommendation System

This project provides personalized book recommendations based on user interests using Natural Language Processing (NLP) and semantic search with sentence embeddings.

---

## Features

- Clean and preprocess book data
- Generate embeddings for book descriptions using Sentence Transformers
- Use FAISS for fast similarity search
- Interactive web interface built with Gradio
- Command-line interface (CLI) for local usage

---

# #Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/book-recommender.git
cd book-recommender
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Usage
Web Interface
Run the web app using:

bash
Copy
Edit
python recommender_web.py
This will start a local web server and open a browser window with the recommendation interface.

Command Line Interface (CLI)
Run the CLI app using:

bash
Copy
Edit
python recommender_cli.py
Follow the prompts in the terminal to enter your preferences and get book recommendations.

Project Structure
books.csv: Dataset containing books and their descriptions

recommender_web.py: Web interface implementation using Gradio

recommender_cli.py: Command-line interface implementation

requirements.txt: Project dependencies

book_cleaned.csv, book_embed.npy, book_faiss.idx: Generated files for cleaned data and search index

Notes
Make sure books.csv is placed in the data/ folder or update the file path accordingly in the scripts.

The first run might take some time to clean data and build the index.

For best results, provide specific topics and genres when searching.

License
MIT License

Contact
For questions or feedback, please contact
[Abdullah Ibrahem Mohammed AL-Mashni].  
[abdullahalmashni2003@gmail.com].

# Book Recommendation System

This project provides personalized book recommendations based on user interests using Natural Language Processing (NLP) and semantic search with sentence embeddings.

---

## Features

- Clean and preprocess book data
- Generate embeddings for book descriptions using Sentence Transformers
- Use FAISS for fast similarity search
- Interactive web interface built with Gradio
- Command-line interface (CLI) for local use

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/book-recommender.git
cd book-recommender
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Usage
Web Interface
Run the web interface:

bash
Copy
Edit
python recommender_web.py
This will start a local web server and open the recommendation tool in your browser.

Command Line Interface (CLI)
Run the CLI version:

bash
Copy
Edit
python recommender_cli.py
You will be asked to enter some keywords, and the script will return similar books.

Project Structure
books.csv: Dataset containing books and their descriptions

recommender_web.py: Web interface built with Gradio

recommender_cli.py: Command-line interface

requirements.txt: List of required Python libraries

book_cleaned.csv, book_embed.npy, book_faiss.idx: Preprocessed data and search index

Notes
Make sure the file books.csv is placed in the data/ folder.

The first run may take time to clean the data and create the index.

Be specific when entering keywords (e.g., "psychology", "adventure", "AI").

License
MIT License

Contact
For questions or feedback, contact:

Abdullah Ibrahem Mohammed AL-Mashni
📧 abdullahalmashni2003@gmail.com

