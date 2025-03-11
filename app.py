import streamlit as st
import pickle
import pandas as pd

movies_list = pickle.load(open('movies_list.pkl', 'rb'))    
movies_list = movies_list['title'].values

st.title('Movie Recommendation System')

option = st.selectbox('Select a movie:', movies_list)

st.write('You selected:', option)


