from sklearn.neighbors import KNeighborsClassifier
import streamlit as st
import pandas as pd
import numpy as np

st.title("🐷🐷🐷Website Developing using Python🐷🐷")
st.header("🍖🍖Website Developing using Python🍖🍖")

st.image("./img/One.png")
st.subheader("นายวงศกร สุขขันติราษฎร์")

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


A1 = st.number_input("เคยตั้งครรภ์มาแล้วกี่รอบ")
A2 = st.number_input("ค่าน้ำตาลในเลือด")
A3 = st.number_input("ความดันโลหิต")  
A4 = st.number_input("ไขมันในผิวหนัง")
A5 = st.number_input("อินซูลิน")
A6 = st.number_input("BMI")
A7 = st.number_input("โรคเบาหวานสายเลือด")
A8 = st.number_input("อายุ")



if st.button("ทำนายผล"):
    #st.write("ทำนาย")
   dt = pd.read_csv("./data/diabetes-dataset.csv")
   X = dt.drop('Outcome', axis=1)
   y = dt.Outcome


   Knn_model = KNeighborsClassifier(n_neighbors=3)
   Knn_model.fit(X, y)  
    
   x_input = np.array([[A1,A2,A3,A4,A5,A6,A7,A8]])
   st.write(Knn_model.predict(x_input))
   
   out=Knn_model.predict(x_input)

   if out[0] == 1:
    st.image("./img/One.png")
    st.write("คุณเป็นโรคเบาหวาน")
   elif out[0] == 0:
    st.image("./img/One.png")
    st.write("คุณไม่เป็นโรคเบาหวาน")
 
else:
    st.write("ไม่ทำนาย")