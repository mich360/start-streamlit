import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(8, 2) / [50, 50] + [35.32, 139.41],
    columns=['lat', 'lon'])

st.map(df)