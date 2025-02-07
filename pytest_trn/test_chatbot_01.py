import pytest
import test_functions as tf
from transformers import pipeline

# Load the Hugging Face pre-trained model for chatbot functionality
chatbot = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

# Function to get chatbot response
def get_chatbot_response(input_text, context):
    # Call the model to generate a response
    response = chatbot(question=input_text, context=context)
    return f"{response["answer"]}"

# Function to get correct response about weather
def test_weather_request():
    # Write the request, and context for this model
    prompt = "How is the weather today?"
    context = "Let's see...the weather today looks nice, it is sunny"

    # Get response from the model
    response = get_chatbot_response(prompt, context)

    # Check if response is correct
    assert tf.outputResponse("weather") in response, f"Expected response contains {tf.outputResponse("weather")}"

# Test the chatbot with a simple prompt
def test_chatbot_response():
    prompt = "Hello, how are you?"
    context = "Hello to you too! I am doing really good, how about you?"

    # Get the chatbot response
    response = get_chatbot_response(prompt, context)
    
    # Assert that the response contains an appropriate reply
    assert "Hello" in response, f"Expected response to contain 'Hello', got: {response}"

# Test if the chatbot gives a reasonable response to a general question
def test_chatbot_responds_reasonably():
    question = "What is the capital of France?"
    context = "The capital of Romania is Bucharest and for France, Paris."
    
    # Get the chatbot response
    response = get_chatbot_response(question, context)
    
    # Check if the chatbot's answer makes sense
    assert "Paris" in response, f"Expected 'Paris' in response, but got: {response}"

# Test if the chatbot gives a reasonable response to a general question
def test_chatbot_responds_again():
    question = "Can you repeat the question?"
    context = "What?"
    
    # Get the chatbot response
    response = get_chatbot_response(question, context)
    
    # Check if the chatbot's answer makes sense
    assert "What" in response, f"Expected 'what' in response, but got: {response}"