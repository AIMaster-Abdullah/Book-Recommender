📚 Book Recommendation System
This project offers a personalized book recommendation system leveraging Natural Language Processing (NLP) and semantic search with sentence embeddings. Discover new books tailored to your interests!

✨ Features
Data Preprocessing: Cleans and prepares raw book data for analysis.

Semantic Search: Generates powerful sentence embeddings for book descriptions using Sentence Transformers to understand their meaning.

Fast Similarity Search: Utilizes FAISS (Facebook AI Similarity Search) for efficient and rapid retrieval of similar books.

Interactive Web Interface: A user-friendly web application built with Gradio for seamless recommendations.

Command-Line Interface (CLI): For quick recommendations directly from your terminal.

🚀 Installation
Follow these steps to get the project up and running on your local machine:

Clone the repository:

Bash

git clone https://github.com/yourusername/book-recommender.git
cd book-recommender
Install dependencies:

Bash

pip install -r requirements.txt
🖥️ Usage
Choose your preferred way to interact with the recommender system:

Web Interface
Run the web application:

Bash

python recommender_web.py
This command will launch a local web server and automatically open the recommendation interface in your default browser.

Command Line Interface (CLI)
For terminal-based recommendations:

Bash

python recommender_cli.py
You'll be prompted to enter keywords or preferences, and the system will then suggest relevant books.

📂 Project Structure
Here's an overview of the key files and directories in this project:

books.csv: The primary dataset containing book titles and their descriptions.

recommender_web.py: Contains the code for the Gradio web interface.

recommender_cli.py: Implements the command-line interface logic.

requirements.txt: Lists all necessary Python libraries for the project.

book_cleaned.csv: Cleaned version of books.csv after preprocessing.

book_embed.npy: Numerical embeddings generated from book descriptions.

book_faiss.idx: The FAISS index for fast similarity lookups.

💡 Important Notes
Ensure that the books.csv file is located in a data/ directory relative to your project root, or update the file path in the scripts accordingly.

The first run of the application may take some time as it needs to clean the data and build the FAISS index. Subsequent runs will be much faster.

For the best recommendation results, try to be specific with your keywords (e.g., "science fiction space opera," "historical romance 18th century," "self-help productivity").

📄 License
This project is licensed under the MIT License. See the LICENSE file for more details.

✉️ Contact
For any questions, feedback, or collaborations, feel free to reach out:

Abdullah Ibrahem Mohammed AL-Mashni

📧 abdullahalmashni2003@gmail.com
