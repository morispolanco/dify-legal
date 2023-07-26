import requests
import streamlit as st
import json

def send_chat_message(query, conversation_id, user):
    url = 'https://api.dify.ai/v1/chat-messages'
    headers = {
        'Authorization': 'Bearer app-cGt4ZVQJ94qGNMthIXMPQj1l',
        'Content-Type': 'application/json',
    }
    payload = {
        "inputs": {},
        "query": query,
        "response_mode": "streaming",
        "user": user,
        "conversation_id": 
    }

    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()

    return response.json()

# Example usage
query = "es-ES"
user = "Moris"

response = send_chat_message(query, conversation_id, user)
print(response)
