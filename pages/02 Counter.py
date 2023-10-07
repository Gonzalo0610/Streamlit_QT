import streamlit as st
import pandas as pd
import src.load_data as ld

df = ld.load()

st.title("Word Frequency Counter")

st.header("And its Script information")
word_to_search = st.text_input("Enter a word:")

# Count the number of times the word appears in the "Line" column. That is the script!

if word_to_search: #That is a TRUE. In the case there is no word, a GIF will appear
    word_to_search_lower = word_to_search.lower()  # LOWERCASE!
    word_count = df["Line"].str.lower().str.count(word_to_search_lower).sum()
    st.write(f'The word "{word_to_search}" appears {word_count} times in the Script.')

    #I also want to know exactly in which part of the script the word is
    filtered_df = df[df["Line"].str.lower().str.contains(word_to_search_lower)]
    st.write(filtered_df)
else: 
    st.image("images/dancegif.gif")