import streamlit as st
from transformers import pipeline

# Load the LLaMA LLM model
@st.cache_resource
def load_model():
    # Here, we're using a placeholder for the LLaMA model.
    # Replace 'your_model_name' with the actual model name you are using.
    model_name = "llama-v3p1-405b-instruct"  # Placeholder, use the actual model name
    recipe_generator = pipeline("text-generation", model=model_name)
    return recipe_generator

model = load_model()

# Streamlit app layout
st.title("Recipe Chatbot")
st.write("Ask me how to make a recipe, and I'll provide detailed instructions!")

# User input
user_input = st.text_input("You:", "")

# Process user input and generate a response
if user_input:
    with st.spinner("Thinking..."):
        # Query the LLM model
        response = model(user_input, max_length=200, num_return_sequences=1)
        # Display the model's response
        st.write("Recipe Bot:", response[0]['generated_text'])

# Adding an example prompt for users to get started
if st.button("Need an idea?"):
    example_prompt = "How do I make chocolate chip cookies?"
    st.text_input("You:", value=example_prompt, key="example_prompt")
    response = model(example_prompt, max_length=200, num_return_sequences=1)
    st.write("Recipe Bot:", response[0]['generated_text'])

# Disclaimer
st.write("Note: This is an AI-generated recipe guide. Please ensure to follow food safety guidelines.")
