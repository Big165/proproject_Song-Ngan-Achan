import streamlit as st
import pandas as pd
import numpy as np

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

st.markdown(html_7, unsafe_allow_html=True)
st.markdown("")

pt_len = st.slider("กรุณาเลือกข้อมูล petal.length")
pt_wd = st.slider("กรุณาเลือกข้อมูล petal.width")

sp_len = st.number_input("กรุณาเลือกข้อมูล sepal.length")
sp_wd = st.number_input("กรุณาเลือกข้อมูล sepal.width")

A1 = st.number_input("ข้อมูล 1")
A2 = st.number_input("ข้อมูล 2")
A3 = st.number_input("ข้อมูล 3")  
A4 = st.number_input("ข้อมูล 4")
A5 = st.number_input("ข้อมูล 5")
A6 = st.number_input("ข้อมูล 6")
A7 = st.number_input("ข้อมูล 7")
A8 = st.number_input("ข้อมูล 8")
A9 = st.number_input("ข้อมูล 9")
A10 = st.number_input("ข้อมูล 10")
A11 = st.number_input("ข้อมูล 11")



if st.button("ทำนายผล"):
    #st.write("ทำนาย")
   dt = pd.read_csv("./data/diabetes-dataset.csv")
   X = dt.drop('Outcome', axis=1)
   y = dt.Outcome


   Knn_model = KNeighborsClassifier(n_neighbors=3)
   Knn_model.fit(X, y)  
    
   x_input = np.array([[A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11]])
   st.write(Knn_model.predict(x_input))
   
   out=Knn_model.predict(x_input)

   if out[0] == 1:
    st.image("./img/One.png")
   elif out[0] == 'Setosa':
    st.image("./img/One.png")
 
else:
    st.write("ไม่ทำนาย")