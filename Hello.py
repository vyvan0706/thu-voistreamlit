import streamlit as st
tab1, tab2, tab3 = st.tabs(["Math", "Video", "Lời kết"])
with tab1:
   st.header('Bé tập làm toán:smile::exclamation:')
   st.image('https://www.unicef.org/montenegro/sites/unicef.org.montenegro/files/styles/hero_tablet/public/his_sofija-05-19-235_0.jpg?itok=YJQLrCrq')
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
        st.balloons()
        st.snow()
      else: 
         st.write('False')
     elif radio==':':
       if number/number2==number3:
        st.write('True')
        st.balloons()
        st.snow()
       else: 
         st.write('False')
     elif radio=='*-':
      if number-number2==number3:
        st.write('True')
        st.balloons()
        st.snow()
      else: 
         st.write('False')
     elif radio=='*+':
      if number + number2==number3:
        st.write('True')
        st.balloons()
        st.snow()      
      else: 
         st.write('False')
with tab2:
   st.title('Đây là một video đặc sắc')
   st.video('https://youtu.be/qOih8EjXnx4?si=VW79yWbFEbiUl5Mo')
with tab3:
   st.title('Lời đề bạt')
   st.text('Cuộc sống này không có điều gì đơn giản, quan trọng nhất là')  
   st.text(:rainbow['bản thân mình đã đạt được thành tựu to lớn nào hay ho'])
   st.write('hihi iu bn')
   
    
