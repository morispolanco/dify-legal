# Import necessary libraries
import streamlit as st
import requests
import json

# API configuration
API_ENDPOINT = "https://api.dify.ai/v1/chat-messages"
HEADERS = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer app-OZw6qix4wsjQl4MUTmlpEukZ'
}

# Function to send a message to the API
def send_message(message):
    data = {"message": message}
    response = requests.post(API_ENDPOINT, headers=HEADERS, data=json.dumps(data))
    return response.json()

# Title
st.title("Chatbot")

# User input
user_input = st.text_input("Enter a message")

# When the user clicks the 'Send' button,
# the message is sent to the API and the response is displayed.
if st.button('Send'):
    response = send_message(message=user_input)
    st.write('Chatbot response:', response.get('response', 'No response available'))
