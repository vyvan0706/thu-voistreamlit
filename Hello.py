import streamlit as st
from streamlit_chat import message
import requests
tab1, tab2, tab3,tab4 = st.tabs(["Math", "Video", "Lời kết",'test'])
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
 st.set_page_config(
    page_title="Streamlit Chat - Demo",
    page_icon=":robot:"
 )

 API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
 headers = {"Authorization": st.secrets['api_key']}
 st.header("Streamlit Chat - Demo")
 st.markdown("[Github](https://github.com/ai-yash/st-chat)")

 if 'generated' not in st.session_state:
    st.session_state['generated'] = []
 if 'past' not in st.session_state:
    st.session_state['past'] = []
 def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()
 def get_text():
    input_text = st.text_input("You: ","Hello, how are you?", key="input")
    return input_text 
 user_input = get_text()
 if user_input:
    output = query({
        "inputs": {
            "past_user_inputs": st.session_state.past,
            "generated_responses": st.session_state.generated,
            "text": user_input,
        },"parameters": {"repetition_penalty": 1.33},
    })

    st.session_state.past.append(user_input)
    st.session_state.generated.append(output["generated_text"])
  if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
