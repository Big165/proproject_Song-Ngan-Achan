import streamlit as st
import pandas as pd

st.title("🐷🐷🐷Website Developing using Python🐷🐷")
st.header("🍖🍖Website Developing using Python🍖🍖")

st.image("./img/One.png")
st.subheader("นายวงศกร สุขขันติราษฎร์")

col1, col2, col3 = st.columns(3)

with col1:
        st.header("black")
        st.image("./img/One.png")

with col2:
        st.header("white")
        st.image("./img/One.png")

with col3:
        st.header("yellow")
        st.image("./img/One.png")

html_7 = """
<div style="background-color:#EC7063;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>ชนเผ่ามนุษย์</h5></center>
</div>
"""
st.markdown(html_7, unsafe_allow_html=True)
st.markdown("")
st.markdown("")
st.subheader("ข้อมูลส่วนแรก 10 แถว")
dt = pd.read_csv("./data/diabetes-dataset.csv")
st.write(dt.head(10))
st.subheader("ข้อมูลส่วนแรก 10 แถว")
dt = pd.read_csv("./data/diabetes-dataset.csv")
st.write(dt.head(10))