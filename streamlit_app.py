import streamlit as st
import requests

headers = {
    'Authorization': 'Bearer app-cGt4ZVQJ94qGNMthIXMPQj1l',
    'Content-Type': 'application/json',
}

def send_message(message):
    data = {
        'inputs': {},
        'messages': [
            {
                'role': "user",
                'content': message,
            }
        ]
    }

    response = requests.post('https://api.dify.ai/v1/chat-messages', headers=headers, json=data)

    if response.status_code == 200:
        return response.json()['content']
    else:
        return f'Error (Código {response.status_code}): {response.text}'

def main():
    st.title("LeybotGt")

    user_input = st.text_input("Tu pregunta:")

    if st.button("Enviar"):
        st.write("Tú:", user_input)
        response = send_message(user_input)
        st.write("Chatbot:", response)

if __name__ == "__main__":
    main()
