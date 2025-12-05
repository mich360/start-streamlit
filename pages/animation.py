import streamlit as st
import json
from urllib.request import Request, urlopen

def load_lottie_url(url: str):
    try:
        # User-Agent を付けてアクセス（403回避）
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

    # 正しい URL を記載（先頭のスペース削除）
    lottie_url = "https://assets8.lottiefiles.com/packages/lf20_OT15QW.json"

    # Lottieファイルを読み込み
    animation_data = load_lottie_url(lottie_url)

    # 表示
    if animation_data:
        from streamlit_lottie import st_lottie
        st_lottie(animation_data, height=300)
    else:
        st.error("Failed to load Lottie animation.")

if __name__ == "__main__":
    main()
