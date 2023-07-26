import requests
import streamlit as st
import json

# Streamlit Configuration
st.set_page_config(page_title='Chat Application')

# Variables
secret_key = "app-cGt4ZVQJ94qGNMthIXMPQj1l"  # Replace with your actual key
url = 'https://api.dify.ai/v1/chat-messages'

# Headers
headers = {
    'Authorization': 'Bearer '+secret_key,
    'Content-Type': 'application/json'
}

# Input Field
user_input = st.text_input("Say something")

if st.button('Send'):
    if user_input:

        # Data
        data = json.dumps({
            "inputs": {},
            "query": user_input,
            "response_mode": "streaming",
            "conversation":
            "user": "abc-123"
        })

        # Request
        response = requests.request("POST", url, headers=headers, data=data)

        # Response
        st.write(response.json())
    else:
        st.write('Input field is empty')
