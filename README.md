# Text2Speech Summarization App

## Overview

The Text2Speech Summarization App is an intuitive tool designed to help users distill lengthy pieces of text into concise summaries. This app is built using Streamlit and leverages the power of the T5 model from Hugging Face's Transformers library for text summarization. Additionally, it uses gTTS (Google Text-to-Speech) to convert the generated summaries into audio format.

## Features

- **Text Summarization:** Effortlessly generate concise summaries from lengthy texts.
- **Audio Output:** Listen to the generated summaries using the gTTS engine.
- **Customizable Parameters:** Adjust summarization parameters such as maximum length, length penalty, and number of beams.

## Installation

To run the app locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/text2speech-summarization-app.git
   cd text2speech-summarization-app


2. **Install the required packages:**
   ```bash
   pip install -r requirements.txt

3. **Run the Streamlit app:**
4. ```bash
   streamlit run app.py
***Usage***

##Home Page

The home page provides an overview of the app and instructions on how to use it. Navigate to the home page using the sidebar.

##Summarize Text

Enter Text: Input the text you want to summarize in the provided text area.
Adjust Parameters: Use the sliders in the sidebar to adjust summarization parameters:
Max Length: Set the maximum length of the summary (default is 150).
Length Penalty: Adjust the length penalty to control the length of the summary (default is 2.0).
Number of Beams: Set the number of beams for beam search (default is 4).
Generate Summary: Click the "Summarize" button to generate the summary. The summary will be displayed below the button.
Listen to Summary: Click the "Listen to Summary" button to convert the summary to speech and listen to it.

##Error Handling

The app ensures that the input text contains at least 50 words.
It prompts users to set the maximum length parameter to 4096 for optimal summarization.
##Dependencies
-Streamlit
-Transformers (Hugging Face)
-gTTS (Google Text-to-Speech)
-torch (PyTorch)
##License
This project is licensed under the MIT License. See the LICENSE file for more details.



