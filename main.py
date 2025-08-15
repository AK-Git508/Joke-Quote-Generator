# Joke/Quote Generator - Pure Python Colors Only

import streamlit as st
import requests
import random

# Page configuration
st.set_page_config(page_title="Joke/Quote Generator", page_icon="🎉", layout="centered")

st.title("Joke/Quote Generator")
st.write("---")

# Color functions list
color_funcs = [st.success, st.info, st.warning, st.error]

# Joke button
if st.button("😂 Click for a Joke"):
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    joke_data = response.json()
    color_func = random.choice(color_funcs)  # pick a random color function
    color_func(f"{joke_data['setup']}\n\n{joke_data['punchline']}")
    st.write("---")

# Quote button
if st.button("💡 Click for a Quote"):
    quote_response = requests.get("https://zenquotes.io/api/random")
    quote_data = quote_response.json()[0]
    color_func = random.choice(color_funcs)  # pick a random color function
    color_func(f"\"{quote_data['q']}\"\n\n~ {quote_data['a']}")
    st.write("---")

st.write(" ")
st.write(" ")
st.write("Made by Aariz Khan on 15/Aug/2025")
