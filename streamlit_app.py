import streamlit as st
import requests



def send_message(query):
    url = 'https://api.dify.ai/v1/chat'
    headers = {
        'Authorization': 'Bapp-cGt4ZVQJ94qGNMthIXMPQj1l',
        'Content-Type': 'application/json',
    }
    payload = {
        "inputs": {},
        "query": query,
        "response_mode": "streaming",
        "user": "abc-123"
    }

    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()

def main():
    st.title("CLeybotGt")

    user_input = st.text_input("Enter a message:")

    if st.button("Send"):
        st.write("You:", user_input)
        response = send_message(user_input)
        st.write("Chatbot:", response)

if __name__ == "__main__":
    main()
