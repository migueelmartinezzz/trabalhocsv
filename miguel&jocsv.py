import pandas as pd
df=pd.read_csv('songs_normalize.csv')
df['popularity']
popular = df['popularity'].hist()
st.plot(popular)
