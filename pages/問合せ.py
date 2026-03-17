import streamlit as st       
# import time


st.subheader('お問い合せ')
# st.write('Display Image')
#st.write('DateFrame')
# st.write('プログレスバーの表示')
# latest_iteration = st.empty()   #空のbarからスタートして100まで0.1秒毎　で100まで終わったら以下が開く
# bar = st.progress(0)            
# for i in range(100):
#     latest_iteration.text(f'Iteration {i+1}')
#     bar.progress(i+1)
#     time.sleep(0.01)







      #インターラクティブとウイジェット
#st.write('Interactive Widgets') 

left_column, right_column = st.columns(2)  #左 ボタン  右 テキスト
button = left_column.button('「右カラムに文字を表示」')
if button:
    right_column.write('「ここは右カラム」')

expander1 = st.expander('streamlit の意味を教えて下さい')
expander1.write('Streamlitは、"stream"（ストリーム 流れ）と"lit"（輝く 点灯する light - lit - lit ）の組み合わせであり、"ストリームを輝かせる"という意味を持ちます。この名前は、Streamlitがデータやモデルの可視化を容易にすることで、データのストリームを鮮やかに表示することを表しています。また、ストリームとは、データや情報が連続的に流れることを意味し、Streamlitがリアルタイムなコードの実行と自動的なアップデートを提供することにも関連しています。そのため、Streamlitという名前は、このフレームワークの目的と特徴を表現するものとなっています。')
expander2 = st.expander('問い合わせ2')
expander2.write('回答')
expander3 = st.expander('問い合わせ3')
expander3.write('回答')


