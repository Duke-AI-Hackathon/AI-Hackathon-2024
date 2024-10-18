# Hacker's Guide to Natural Language Processing (NLP)

🚀 Created for the [Duke AI Hackathon 2024](https://dukeaihackathon.com/)

👋 by [Dr. Brinnae Bent](https://www.linkedin.com/in/brinnaebent/)

## What is NLP?
Natural Language Processing (NLP) is a subfield of AI focused on enabling computers to understand, interpret, and generate language. It combines linguistics, computer science, and machine learning.

NLP includes various tasks such as:
* speech recognition
* language translation
* sentiment analysis
* text summarization.


In this tutorial, we will cover some of the basics, using popular NLP Python libraries `nltk`, `spaCy`, and `transformers`.

## Table of Contents
* Environmental Variables

* Libraries

* NLTK
  * Tokenization
  * Parts-of-speech Tagging
* spaCy
  * Named Entity Recognition
  * Dependency Parsing
* transformers
  * Sentiment Analysis
  * Text Summarization
  * Text Generation

## Instructions
You can open this notebook in Google Colab directly and run all cells in the notebook. Follow instructions in notebook for setting up environment variables in Google Colab.

For **local implementations**, run the following commands in your terminal:

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

For some models in the transformers library, you may need a HuggingFace Token. You can create one following these [instructions](https://huggingface.co/docs/hub/en/security-tokens).

When working on your local machine, it's common to use a .env file to manage environment variables. Always add .env to your .gitignore file to prevent accidental commits!

1. Create a file named .env in your project's root directory
2. Add your environment variables to this file:

`HUGGINGFACE_TOKEN=your_actual_token_here`


3. Install the python-dotenv library:

`pip install python-dotenv`

4. In your Python script, load and use the variables:

```python
from dotenv import load_dotenv
import os

load_dotenv()
huggingface_token = os.getenv('HUGGINGFACE_TOKEN')
```