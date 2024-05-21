import pandas as pd
import streamlit as st
df=pd.read_csv('songs_normalize.csv')
df['popularity']
popular = df['popularity'].hist()
st.pyplot(popular)
