import streamlit as st
from transformers import T5ForConditionalGeneration, T5Tokenizer
from gtts import gTTS

# Load the T5 model and tokenizer
model_name = "t5-small"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

# Function to display the home page
def display_home():
    st.title("Welcome to the Text2Speech Summarization app")
    st.markdown(
       """
    ### ABOUT

    This intuitive tool empowers you to distill lengthy pieces of text into concise summaries effortlessly. Whether you're grappling with extensive articles, research papers, or even verbose emails, this app streamlines the process, allowing you to extract key information swiftly. Delve into the nuances of your content without the noise, saving time and enhancing productivity.

    **Instructions:**
    - **Enter the text you want to summarize in the text area.**
    - **Click control + enter to submit the input.**
    - **Adjust summarization parameters using the sliders in the sidebar.**
    - **Click the "Listen to Summary" button to listen to the summary in audio format.**
    """
    )

# Streamlit app
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Summarize Text"])

    if page == "Home":
        display_home()
    elif page == "Summarize Text":
        st.title("Text2Speech Summarizer")

        # User input text
        text = st.text_area("Enter text to summarize")

        # Message to inform users about adjusting parameters and viewing the summary
        st.info("After inputting text, you can adjust parameters in the sidebar and click 'Summarize' to view the generated summary.")

        # Options for adjusting summarization parameters
        max_length = st.sidebar.slider("Max Length", min_value=50, max_value=4096, value=150)  # Adjust max_value for T5
        length_penalty = st.sidebar.slider("Length Penalty", min_value=0.5, max_value=2.5, step=0.1, value=2.0)
        num_beams = st.sidebar.slider("Number of Beams", min_value=1, max_value=8, value=4)

        # Button to generate summary
        if text:
            if len(text.split()) < 50:
                st.error("Input text must contain at least 50 words.")
            elif max_length != 4096:
                st.error("Please set the max length to the maximum value (4096) for optimal summarization.")
            else:
                # Summarize the input text
                summary = summarize_text(text, max_length, length_penalty, num_beams)
                # Display success message
                st.success("Summary generated successfully.")
                # Display the summary
                st.subheader("Summary:")
                st.write(summary)

                # Button for speech output
                if st.button("Listen to Summary"):
                    # Convert summary text to speech using gTTS
                    tts = gTTS(summary, lang='en')
                    # Save speech as audio file
                    tts.save("summary.mp3")
                    # Play audio file
                    st.audio("summary.mp3", format="audio/mp3")
                    # Display success message for speech output
                    st.success("Speech generated successfully.")
        else:
            st.warning("Please enter some text to summarize.")

# Function to generate summary
def summarize_text(text, max_length, length_penalty, num_beams):
    # Tokenize the input text
    inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=512, truncation=True)
    # Generate summary
    summary_ids = model.generate(inputs, max_length=max_length, min_length=40, length_penalty=length_penalty, num_beams=num_beams, early_stopping=True)
    # Decode the generated summary
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

# Function to tokenize text
def tokenize(text):
    # Tokenize the input text
    tokens = tokenizer.tokenize(text)
    # Remove '▁' character from the beginning of each token
    tokens = [token.lstrip('▁') for token in tokens]
    return tokens
# Function for text summarization
def summarize_text(input_text, max_length=150, length_penalty=2.0, num_beams=4):
    # Tokenize the input text
    input_ids = tokenizer.encode("summarize: " + input_text, return_tensors="pt", max_length=512, truncation=True)
    # Generate summary
    summary_ids = model.generate(input_ids, max_length=max_length, min_length=40, length_penalty=length_penalty, num_beams=num_beams, early_stopping=True)
    # Decode the generated summary
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary



if __name__ == "__main__":
    main()
