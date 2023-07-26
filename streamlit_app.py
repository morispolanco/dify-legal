import streamlit as st
import requests
from datetime import datetime

secret_key = 'app-OZw6qix4wsjQl4MUTmlpEukZ' # Replace with your actual key

def send_data(user, message):
    url = 'https://api.dify.ai/v1/chat-messages'
    headers = {
        'Authorization': f'Bearer {secret_key}',
        'Content-Type': 'application/json'
    }
    data = {
        "inputs": {},
        "query": message,
        "response_mode": "streaming",
        "user": user
    }
    response = requests.post(url, headers=headers, json=data)
    return response

def run_chat():
    st.title('Streamlit Chat App')
    st.subheader('Enter your username and messages')
    user = st.text_input('Username')
    message = st.text_input('Message')
    if st.button('Send'):
        response = send_data(user, message)
        st.write(response.json())
    st.text('Chat History')

if __name__ == "__main__":
    run_chat()
