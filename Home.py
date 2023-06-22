import streamlit as st       
from PIL import Image
import requests
#from streamlit_lottie import st_lottie

import time
st.title('初めてのStreamlitを試す')
st.write("[前のページに戻る >](https://canape2020.stars.ne.jp/python/)")
st.write('pythonのフレームstreamlitテストアプリです。')
st.caption('プログレスバー表示されます、100まで終わった開く。')
latest_iteration = st.empty()   #空のbarからスタートして100まで0.1秒毎　で100まで終わったら以下が開く
bar = st.progress(0)             

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.05)

# 動画　　
video_file = open('./data/sho.mov','rb')
video_bytes = video_file.read()
st.video(video_bytes)



# video_file = open('./data/sho.mov','rb')
# video_bytes = video_file.read()
# st.video(video_bytes)



# image = Image.open('./data/e.png')
# st.image(image, width=600)
# st.caption('## Shoonan')
