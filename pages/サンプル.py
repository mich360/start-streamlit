import streamlit as st
import json
from streamlit_lottie import st_lottie
from urllib.request import urlopen

def load_lottie_url(url):
    response = urlopen(url)
    data = response.read()
    return json.loads(data.decode("utf-8"))

st.title("Lottie Animation Example")

url = "https://assets8.lottiefiles.com/packages/lf20_OT15QW.json"
data = load_lottie_url(url)

st_lottie(data)