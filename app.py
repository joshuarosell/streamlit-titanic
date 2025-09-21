import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("Titanic Dashboard")

df = pd.read_csv("titani_data.csv")

df['Embarked'] = df['Embarked'].fillna('Unknown')

# get unique values for embarked port
embarked_options = df['Embarked'].unique().tolist()
gender_options = df['Sex'].unique().tolist()

col1, col2 = st.columns([1, 1])
selected_embarked = col1.selectbox("Select Embarked Port", options=embarked_options, index=0)
selected_gender = col2.selectbox("Select Gender", options=gender_options, index=0)