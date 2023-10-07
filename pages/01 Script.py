import streamlit as st
import src.load_data as ld

st.set_page_config(page_title="The Script", page_icon=":book:", layout="wide")
# 1. Show the data
st.write("# The full script!")
st.dataframe(ld.load())