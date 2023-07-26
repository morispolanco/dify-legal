import streamlit as st
import requests

headers = {
    'Authorization': 'Bearer app-cGt4ZVQJ94qGNMthIXMPQj1l',
    'Content-Type': 'application/json',
}

def main():
    st.title("LeybotGt")

    user_input = st.text_input("Tu pregunta:")

    if st.button("Enviar"):
        st.write("Tú:", user_input)
        response = send_message(user_input)
        st.write("Chatbot:", response)

if __name__ == "__main__":
    main()
