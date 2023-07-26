import streamlit as st
import requests

secret_key = 'app-OZw6qix4wsjQl4MUTmlpEukZ'

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
        "conversation_id"
        "user"
    }
    response = requests.post(url, headers=headers, json=data)
    try:
        response = response.json()
    except ValueError:
        st.write('Server response might not contain JSON content.')
        st.write(f'Response status code: {response.status_code}')
        st.write(f'Response content: {response.content}')
    return response

def run_chat():
    st.title('Streamlit Chat App')
    st.subheader('Enter your username and messages')
    user = st.text_input('Username')
    message = st.text_input('Message')
    if st.button('Send'):
        response = send_data(user, message)
        st.write(response)
    st.text('Chat History')

if __name__ == "__main__":
    run_chat()
