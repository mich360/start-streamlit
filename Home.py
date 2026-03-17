import streamlit as st
from pathlib import Path
import time

st.title("初めてのStreamlitを試す")
st.write("[前のページに戻る >](https://canape2020.stars.ne.jp/python/)")
st.write("他のページ目次が見えない場合には左上 > をクリックして開いて下さい。")
st.write("pythonのフレームstreamlitテストアプリです。")
st.caption("プログレスバー表示されます、終わったら下が開きます。")

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i + 1)
    time.sleep(0.01)

video_path = Path("data/sho.mov")

if video_path.exists():
    try:
        with open(video_path, "rb") as video_file:
            video_bytes = video_file.read()
        st.video(video_bytes)
    except Exception as e:
        st.error(f"動画の読み込みでエラー: {e}")
else:
    st.warning("動画ファイル data/sho.mov が見つかりません。")