<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Text2Speech Summarization App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
        }
        h2 {
            color: #333;
        }
        ul {
            list-style-type: none;
            padding-left: 0;
        }
        code {
            background-color: #f0f0f0;
            padding: 2px 5px;
            border-radius: 3px;
        }
    </style>
</head>
<body>

<h2>Overview</h2>
<p>The Text2Speech Summarization App is an intuitive tool designed to help users distill lengthy pieces of text into concise summaries. This app is built using Streamlit and leverages the power of the T5 model from Hugging Face's Transformers library for text summarization. Additionally, it uses gTTS (Google Text-to-Speech) to convert the generated summaries into audio format.</p>

<h2>Features</h2>
<ul>
    <li><strong>Text Summarization:</strong> Effortlessly generate concise summaries from lengthy texts.</li>
    <li><strong>Audio Output:</strong> Listen to the generated summaries using the gTTS engine.</li>
    <li><strong>Customizable Parameters:</strong> Adjust summarization parameters such as maximum length, length penalty, and number of beams.</li>
</ul>

<h2>Installation</h2>
<p>To run the app locally, follow these steps:</p>
<ol>
    <li><strong>Clone the repository:</strong></li>
    <pre><code>git clone https://github.com/yourusername/text2speech-summarization-app.git<br>cd text2speech-summarization-app</code></pre>
    <li><strong>Install the required packages:</strong></li>
    <pre><code>pip install -r requirements.txt</code></pre>
    <li><strong>Run the Streamlit app:</strong></li>
    <pre><code>streamlit run app.py</code></pre>
</ol>

<h2>Usage</h2>

<h3>Home Page</h3>
<p>The home page provides an overview of the app and instructions on how to use it. Navigate to the home page using the sidebar.</p>

<h3>Summarize Text</h3>
<ul>
    <li><strong>Enter Text:</strong> Input the text you want to summarize in the provided text area.</li>
    <li><strong>Adjust Parameters:</strong> Use the sliders in the sidebar to adjust summarization parameters:
        <ul>
            <li><strong>Max Length:</strong> Set the maximum length of the summary (default is 150).</li>
            <li><strong>Length Penalty:</strong> Adjust the length penalty to control the length of the summary (default is 2.0).</li>
            <li><strong>Number of Beams:</strong> Set the number of beams for beam search (default is 4).</li>
        </ul>
    </li>
    <li><strong>Generate Summary:</strong> Click the "Summarize" button to generate the summary. The summary will be displayed below the button.</li>
    <li><strong>Listen to Summary:</strong> Click the "Listen to Summary" button to convert the summary to speech and listen to it.</li>
</ul>

<h3>Error Handling</h3>
<ul>
    <li>The app ensures that the input text contains at least 50 words.</li>
    <li>It prompts users to set the maximum length parameter to 4096 for optimal summarization.</li>
</ul>

<h2>Code Structure</h2>
<ul>
    <li><strong>app.py:</strong> The main Streamlit app file containing the UI and logic for text summarization and speech output.</li>
    <li><strong>requirements.txt:</strong> A file listing all the dependencies required to run the app.</li>
</ul>

<h2>Dependencies</h2>
<ul>
    <li>Streamlit</li>
    <li>Transformers (Hugging Face)</li>
    <li>gTTS (Google Text-to-Speech)</li>
    <li>torch (PyTorch)</li>
</ul>

<h2>Contributing</h2>
<p>Contributions are welcome! If you have any suggestions or improvements, please create a pull request or open an issue.</p>

<h2>License</h2>
<p>This project is licensed under the MIT License. See the <a href="./LICENSE">LICENSE</a> file for more details.</p>

<h2>Contact</h2>
<p>For any questions or inquiries, please contact <a href="mailto:yourname@example.com">yourname@example.com</a>.</p>

</body>
</html>
