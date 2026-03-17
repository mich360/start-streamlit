import streamlit as st
import pandas as pd
import numpy as np

st.title("表とグラフのデモ")

# --- 静的テーブル ---
st.subheader("静的テーブル")

df_static = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})

st.table(df_static.style.highlight_max(axis=0))


# --- 動的テーブル ---
st.subheader("動的テーブル")

st.dataframe(df_static.style.highlight_max(axis=0))


# --- ランダムデータ ---
st.subheader("ランダムデータ")

df_random = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['A', 'B', 'C']
)

st.write(df_random)


# --- グラフ ---
st.subheader("折れ線グラフ")
st.line_chart(df_random)

st.subheader("エリアグラフ")
st.area_chart(df_random)

st.subheader("棒グラフ")
st.bar_chart(df_random)