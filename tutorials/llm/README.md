# Hacker's Guide to Large Language Models (LLMs)

🚀 Created for the [Duke AI Hackathon 2024](https://dukeaihackathon.com/)

👋 by [Suneel Nadipalli](https://www.linkedin.com/in/suneel-n/)

# What are LLMs?

A large language model is a type of computational model designed for natural language processing tasks such as language generation. LLMs work by using a massive amount of text data to train a transformer.

In this tutorial, we will cover some of the basics, using popular LLM Python libraries `openai`, `langchain`, `google-generativeai`

## Table of Contents
* Environmental Variables

* Libraries

* LLM Tutorials
  * OpenAI - Examples
  * Gemini - Examples
  * HuggingFace - Examples
* Prompting Principles
  * Principle 1 - Clear Instructions
    * Strategy 1 - Delimiters
    * Strategy 2 - Structured output
    * Strategy 3 - Condition Check
    * Strategy 4 - Few-Shot Prompting
  * Principle 2 - Let the model think
    * Strategy 1 - Provide Step-by-Step instructions for task
    * Strategy 2 - Instruct the model to work out its own solution first
* LLM Limitations
  * Hallucinations
  * Hedging
  * Refusals
* NLP Tasks with LLMs
  * Text Summarization
  * Extractive Summarization
  * Sentiment Analysis
  * Translation

## Instructions
You can open this notebook in Google Colab directly and run all cells in the notebook. Follow instructions in notebook for setting up environment variables in Google Colab.

For **local implementations**, run the following commands in your terminal:

```bash
pip install -r requirements.txt
```

1. Create a file named .env in your project's root directory
2. Add your environment variables to this file:

`OPENAI_KEY=your_actual_token_here`
`HF_KEY=your_actual_token_here`
`GEMINI_KEY=your_actual_token_here`

3. Install the python-dotenv library:

`pip install python-dotenv`

4. In your Python script, load and use the variables:

```python
from dotenv import load_dotenv
import os

load_dotenv()
huggingface_token = os.getenv('HF_KEY')
```
