import streamlit as st
import pandas as pd
import numpy as np

# st.line_chart(df)   #折れ線グラフでフでプロットする。
# st.area_chart(df)    #エリアチャート
#st.bar_chart(df)    #棒グラフ
st.write('静的テーブル')
df = pd.DataFrame({

    '1列目': [1 ,2 ,3 ,4],
    '2列目': [10 ,20 ,30 ,40]

})

st.table(df.style.highlight_max(axis=0))
st.warning('動的テーブル')
df = pd.DataFrame({

    '1列目': [1 ,2 ,3 ,4],
    '2列目': [10 ,20 ,30 ,40]

})
st.dataframe(df.style.highlight_max(axis=0))
st.warning('ランダムな表')
df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)
df
st.warning('折れ線グラフ')
st.line_chart(df)   #折れ線グラフでフでプロットする。
st.warning('エリアグラフ')
st.area_chart(df)    #エリアチャート
st.warning('棒グラフ')
st.bar_chart(df)    #棒グラフ





