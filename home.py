from sklearn.neighbors import KNeighborsClassifier
import streamlit as st
import pandas as pd
import numpy as np

st.title("คาดการณ์ว่าคุณเป็นโรคเบาหวานหรือไม่")
st.image('./img/One.png', width=1000)



html_7 = """
<div style="background-color:#EC7063;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>กรอกข้อมูลของคุณ</h5></center>
</div>
"""
st.markdown(html_7, unsafe_allow_html=True)


A1 = st.number_input("เคยตั้งครรภ์มาแล้วกี่รอบ")
A2 = st.number_input("ค่าน้ำตาลในเลือด")
A3 = st.number_input("ความดันโลหิต")  
A4 = st.number_input("ไขมันในผิวหนัง")
A5 = st.number_input("ค่าอินซูลิน")
A6 = st.number_input("ค่า BMI")
A7 = st.number_input("โรคเบาหวานสายเลือด")
A8 = st.number_input("อายุของคุณ")



if st.button("กดตรงนี้เพื่อดูผล"):
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
    st.image('./img/THREE.jpg', width=1000)
    st.subheader("เสียใจด้วย คุณเป็นโรคเบาหวาน")
   elif out[0] == 0:
    st.image('./img/TWO.jpg', width=1000)
    st.subheader("ยินดีด้วย คุณไม่เป็นโรคเบาหวาน")
 
else:
    st.write("ไม่ทำนาย")



st.write("By นายวงศกร สุขขันติราษฎร์")