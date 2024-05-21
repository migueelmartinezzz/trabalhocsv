import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
df=pd.read_csv('songs_normalize.csv')
df['popularity']
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title('Histograma de Popularidade de Músicas')
st.write("Histograma da popularidade das músicas:")
plt.hist(df['popularity'])
st.pyplot()
