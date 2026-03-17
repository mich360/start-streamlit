import streamlit as st
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

st.success("アプリは正常に起動しました。")

st.page_link("pages/1始めに.py", label="1始めに")
st.page_link("pages/animation.py", label="animation")
st.page_link("pages/サンプル.py", label="サンプル")
st.page_link("pages/地図.py", label="地図")
st.page_link("pages/表とグラフ.py", label="表とグラフ")
st.page_link("pages/問合せ.py", label="問合せ")