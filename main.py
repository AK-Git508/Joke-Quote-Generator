# Joke/Quote Generator

import streamlit as st
import requests

st.title("Joke/Quote Generator")
st.write(" ")

# Joke button
if st.button("Click for a Joke"):
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    joke_data = response.json()
    st.write(joke_data["setup"])
    st.write(" ")
    st.write(joke_data["punchline"])

# Quote button
if st.button("Click for a Quote"):
    quote_response = requests.get("https://zenquotes.io/api/random")
    quote_data = quote_response.json()[0]  # ZenQuotes returns a list with one dictionary
    st.write(quote_data["q"])
    st.write(" ")
    st.write("~" + quote_data["a"])

st.write("Made by Aariz Khan on 15/Aug/2025")
