import streamlit as st
import numpy as np
import time

progress_bar = st.sidebar.progress(0)
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)

for i in range(100):
    new_row = np.random.randn(1,1)
    chart.add_rows(new_row) 
    progress_bar.progress(i)
    time.sleep(0.05)