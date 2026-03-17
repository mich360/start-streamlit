import streamlit as st
import json
from urllib.request import Request, urlopen
from streamlit_lottie import st_lottie  # ← ここに移動

def load_lottie_url(url: str):
    try:
        req = Request(
            url,
            headers={"User-Agent": "Mozilla/5.0"}
        )
        with urlopen(req) as response:
            data = response.read().decode("utf-8")
            return json.loads(data)
    except Exception as e:
        st.error(f"Error loading Lottie animation: {e}")
        return None

def main():
    st.title("Lottie Animation Example")

    lottie_url = "https://assets8.lottiefiles.com/packages/lf20_OT15QW.json"
    animation_data = load_lottie_url(lottie_url)

    if animation_data:
        st_lottie(animation_data, height=300)
    else:
        st.error("Failed to load Lottie animation.")

if __name__ == "__main__":
    main()