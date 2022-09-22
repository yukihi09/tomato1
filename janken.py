import streamlit as st
import pandas as pd
import base64
import csv
import os

st.title('トマトの官能評価')
st.header('方法B：多量の２点識別の組合せから順序を導き出す官能評価')
st.subheader('')
st.write('①品質が良いと思う方の選択肢(AorB)を選んでください') # markdown
st.write('②選択肢を選んだら「画像更新」を押して,次の評価を行ってください')
st.write('③エラーが出た場合は「画像更新」を押してください')


from PIL import Image

if st.button("画像更新", key=3):
    import random
    lst_image = ['306.jpg','177.jpg','4.jpg','278.jpg','228.jpg','262.jpg','9.jpg','11.jpg','16.jpg','17.jpg']
    data1 = random.choice(lst_image)
    lst_image.remove(data1)
    data2 = random.choice(lst_image)


if 'key' not in st.session_state:
    st.session_state.key = data1
if 'key2' not in st.session_state:
    st.session_state.key2 = data2
    
    
col1, col2 = st.columns(2)

with col1:
    st.header("A")
    st.image(st.session_state.key, use_column_width=True)

with col2:
    st.header("B")
    st.image(st.session_state.key2, use_column_width=True)



if st.button("A", key=1):
  st.write(st.session_state.key,'>',st.session_state.key2)
  df = pd.read_csv('tomato1.csv',encoding='cp932')
  df.at[ 1000000]  = [st.session_state.key ,st.session_state.key2,1 ,0 ] 
  df.to_csv("tomato1.csv", index=False )
  del st.session_state.key
  del st.session_state.key2


if st.button("B", key=2):
  st.write(st.session_state.key,'<',st.session_state.key2)
  df = pd.read_csv('tomato1.csv',encoding='cp932')
  df.at[ 1000000]  = [st.session_state.key2 ,st.session_state.key,1 ,0 ] 
  df.to_csv("tomato1.csv", index=False )
  del st.session_state.key
  del st.session_state.key2
