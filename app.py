import streamlit as st
import pandas as pd

st.set_page_config(page_title="Welcome to this TIME TRAVEL PORTAL!",layout="wide")

with st.sidebar:

    choice = st.selectbox("pick one",("Prehistory","Classical Era","Middle Ages","Early Modern Era","Modern Era","Future"),)
    st.write("You selected:", choice)

    API_LINKS = {
        "Prehistory":'https://maddie11.pythonanywhere.com/api/era/prehistory',
        "Classical Era":'https://maddie11.pythonanywhere.com/api/era/classical_era',
        "Middle Ages":'https://maddie11.pythonanywhere.com/api/era/middle_ages',
        "Early Modern Era":'https://maddie11.pythonanywhere.com/api/era/early_modern_era',
        "Modern Era":'https://maddie11.pythonanywhere.com/api/era/modern_era',
        "Future":'https://maddie11.pythonanywhere.com/api/era/future'
    }


if choice =="Prehistory":
    st.title("Pre-Historical Era")
    col1, col2 = st.columns([1,3])
    col1.metric("Average Life Span", 20)
    col2.metric("Child morality rate", "Extreamly High")
    #col3.metric("Gender Ratio", "Unknown")
    table = pd.DataFrame({
        "dominant species":["Homo Habilis","Homo Neanderthals","Mamoths"]
            })
    st.table(table) 
    st.image("https://media.slidesgo.com/storage/30914139/the-prehistory1675674167.jpg")