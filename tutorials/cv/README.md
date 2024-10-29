# Hacker's Guide to Computer Vision (CV)

🚀 Created for the [Duke AI Hackathon 2024](https://dukeaihackathon.com/)

👋 by [Jared Bailey](https://www.linkedin.com/in/jared-l-bailey-mba-cpcu-are/)

# What is Computer Vision?

Computer vision allows a machine to recognize information about an image much like a human would. For example, a computer can learn to recognize the difference between a butterfly and a flower, even when both objects are present within the same image! Computer vision is often accomplished through the training of neural networks.

In this tutorial we demonstrate the training of a YOLOv8 object detection model, and then place this model within a Streamlit web app.

## Instructions - Object Detection

### Train a Model
You can open this notebook in Google Colab directly and run all cells in the notebook. Follow instructions in notebook for setting up environment variables in Google Colab.
- We recommend using an A100 in Google Colab for training.
- Image data can be sourced from multiple locations such as the [Roboflow Universe](https://universe.roboflow.com/).
  - This tutorial used a [rock, paper, scissors dataset](https://universe.roboflow.com/roboflow-58fyf/rock-paper-scissors-sxsw).
  - If you want to use your own images, then you can use a tool like [CVAT](https://www.cvat.ai/) to annotate the data.
- Please note that training a YOLOv8 model using ultralytics requires a [particular folder and data structure](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/uUk1YopS94mytGaCav3ZaQ.png).

### Run the Current Streamlit App

1. Create a python virtual environment
```bash
python -m venv .venv
```

2. Start you virtual environment
Depending on your software installed, one of the following two options will work

```bash
source .venv/Scripts/activate
```

or

```bash
source .venv/bin/activate
```

3. Install the needed python libraries

```bash
pip install -r requirements.txt
```

4. Run the Streamlit web app
```bash
streamlit run app.py
```
