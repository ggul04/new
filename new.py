import matplotlib.pyplot as plt
import streamlit as st

fig,ax= plt.subplots()

x=[]

for i in range(-29,30,3):
    x.append(i)

a= st.number_input('a의 값을 입력하시오',value=2.0,step=1.0)
b= st.number_input('b의 값을 입력하시오',value=-1.0,step=1.0)
c= st.number_input('c의 값을 입력하시오',value=15.0,step=1.0)
d= st.number_input('d의 값을 입력하시오',value=2000.0,step=100.0)

c1= st.sidebar.radio('선의 색 선택',['red','blue','green'])
c2= st.sidebar.radio('선의 스타일 선택',[':','--','solid'])
c3= st.sidebar.radio('마커의 스타일 선택',['p','s','x'])

plt.plot(a,b,c,d,x,color=c1, linestyle= c2, marker=c3)
st.pyplot(fig)
import sys
sys.exit()