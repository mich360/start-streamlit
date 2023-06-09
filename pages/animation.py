import streamlit as st
import json
import sys
sys.path.append('/Users/naomichimasumoto/.pyenv/versions/3.11.2/lib/python3.11/site-packages')
import streamlit_lottie
print(streamlit_lottie.__file__)
from streamlit_lottie import st_lottie
from urllib.request import urlopen

def load_lottie_url(url):
    response = urlopen(url)
    data = response.read()
    return json.loads(data.decode("utf-8"))

def main():
    st.title("Lottie Animation Example")
    
    # LottieファイルのURLを指定します
    lottie_url = " https://assets8.lottiefiles.com/packages/lf20_OT15QW.json"
    
    # Lottieファイルを読み込みます
    animation_data = load_lottie_url(lottie_url)
    
    # Lottieアニメーションを表示します
    st_lottie(animation_data)

if __name__ == "__main__":
    main()
