import streamlit as st
import requests
import json

def send_message(query):
    url = 'https://api.dify.ai/v1/chat-messages'
    headers = {
        'Authorization': 'Bearer app-OZw6qix4wsjQl4MUTmlpEukZ',
        'Content-Type': 'application/json',
    }
    payload = {
        "inputs": {},
        "query": query,
        "response_mode": "streaming",
        "user": "abc-123"
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        
        response_json = response.json()
        return response_json
    except requests.exceptions.HTTPError as e:
        return f'Error (Code {e.response.status_code}): {e.response.text}'
    except json.JSONDecodeError as e:
        return f'Error decoding JSON response: {response.text}'

def main():
    st.title("Chat Application")

    user_input = st.text_input("Enter a message:")

    if st.button("Send"):
        st.write("You:", user_input)
        response = send_message(user_input)
        st.write("Chatbot:", response)

if __name__ == "__main__":
    main()
