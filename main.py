import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
import codecs

st.set_page_config(
     page_title="Pulp Fiction",
     page_icon=":octopus:",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get help': "https://www.filmaffinity.com/es/film160882.html",
         'About': "*Ezequiel 25:17*. The path of the righteous man is beset on all sides by the inequities of the selfish and the tyranny of evil men. Blessed is he who, in the name of charity and good will, shepherds the weak through the valley of the darkness. For he is truly his brother's keeper and the finder of lost children. And I will strike down upon thee with great vengeance and furious anger those who attempt to poison and destroy my brothers. And you will know I am the Lord when I lay my vengeance upon you."
     }
 )

st.title("Pulp Fiction")

st.header("The Movie Analysis")



cover = Image.open("images/pf.jpg")
st.image(cover, use_column_width=True)

movie_info = {
    "Title": "Pulp Fiction",
    "Director": "Quentin Tarantino",
    "Duration": "154 minutes",
    "Actors": "John Travolta, Samuel L. Jackson, Uma Thurman, Bruce Willis",
}

synopsis = """
"Pulp Fiction" is a 1994 crime film written and directed by Quentin Tarantino. 
The film weaves together multiple interconnected stories involving two hitmen, 
a boxer, a gangster's wife, and a pair of small-time criminals. 
It is known for its non-linear narrative, sharp dialogue, and iconic characters.
"""
col1, col2 = st.columns(2)

# Left Column for the movie information
col1.subheader("**General Information**")
for key, value in movie_info.items():
    col1.write(f"**{key}:** {value}")

# Right column for the movie synopsis
col2.subheader("*Movie Synopsis*")
col2.write(synopsis)

# https://youtubeembedcode.com/es/
f=codecs.open("data/youtube.html", 'r')
pedro = f.read()

components.html(pedro,height=550,scrolling=True)