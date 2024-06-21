import streamlit as st
from langmodel import analyse_sentiment

def main():
    st.title("Simple Sentiment Analysis Tools")

    # Display a text input field
    user_input = st.text_input("Enter your text here")

    # Display the input back to the user
    if st.button("Analyse"):
        if user_input:
            st.write("You entered:", user_input)
            response = analyse_sentiment(user_input)
            st.write("Anysed sentiment:", response)
        else:
            st.write("Please enter some text.")

if __name__ == "__main__":
    main()
