import streamlit as st
import gtts
from ftlangdetect import detect as lang_detector
from deep_translator import GoogleTranslator
tab1, tab2, tab3 , tab4 = st.tabs(["Math", "Video", "Lời kết",'thu'])
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
   st.write('Cuộc sống này không có điều gì đơn giản, quan trọng nhất là')  
   st.write(':rainbow[bản thân mình đã đạt được thành tựu to lớn nào hay ho]')
   st.write('hihi iu bn')
with tab4:
   st.title(':blue[Lồng tiếng với chị Google]')
   user_input= st.text_area('Nhập văn bản muốn lồng tiếng')
   language_code_mapping={
     'Tiếng Việt':'vi',
     'Tiếng Anh':'en',
     'Tiếng Hàn':'ko',
     'Tiếng Nhật':'ja'} 
   translate = st.toggle('Dịch văn bản')
   if translate:
     target_language= st.selectbox( 'Chọn ngôn ngữ của bản dịch', ('Tiếng Việt','Tiếng Anh','Tiếng Hàn','Tiếng Nhật'))
     target_language_code=language_code_mapping[target_language]
     submitbut=st.button('Xác nhận')
   if user_input and submitbut:
     language_code=lang_detector(user_input)['lang']
     result= gtts.gTTS(text=user_input, lang=language_code)
     result.save('result.mp3')
     col41,col42=st.columns(2)
     with col41:
       st.subheader('Văn bản gốc')
       st.audio('result.mp3')
     if translate:
          translated_input = GoogleTranslator(source='auto', target=target_language_code).translate(user_input)  
          trans_result= gtts.gTTS(text=translated_input, lang=target_language_code)
          trans_result.save('tts_result/trans_result.mp3')
      with col42:
        st.subheader('Văn bản dịch')
        st.audio('trans_result.mp3')
