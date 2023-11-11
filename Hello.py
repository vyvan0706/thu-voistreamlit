import streamlit as st
st.ballons()
st.header('Bé tập làm toán:smile::exclamation:')
col1,col2,col3=st.columns(3)
with col1:
   number = st.number_input('a',key='num1')
with col2:
   radio = st.radio('Phép toán', ('*+', '*-', 'x',':'),horizontal=True)
with col3:
  number2=st.number_input('b',key='num2')
number3=st.number_input('Nhập kết quả',key='num3')
if st.button('Kiểm tra'):
   if radio=='x':
      if number*number2==number3:
        st.write('True')
      else: 
         st.write('False')
   elif radio==':':
      if number/number2==number3:
        st.write('True')
      else: 
         st.write('False')
   elif radio=='*-':
      if number-number2==number3:
        st.write('True')
      else: 
         st.write('False')
   elif radio=='*+':
      if number + number2==number3:
        st.write('True')
      else: 
         st.write('False')
         
    
