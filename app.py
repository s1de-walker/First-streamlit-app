import streamlit as st
import pandas as pd
import numpy as np


st.title("Hello, Streamlit!")
st.header("This is a header with a divider", divider="gray")
st.markdown("*:red[Streamlit]* is **really** ***cool***.")

st.subheader("Area chart")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.area_chart(chart_data)
