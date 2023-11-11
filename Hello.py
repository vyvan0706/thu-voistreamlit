import streamlit as st

tab1, tab2, tab3 = st.tabs(["Math", "Video", "Lời kết"])

with tab1:
    st.header('Bé tập làm toán:smile::exclamation:')
    st.image('https://www.unicef.org/montenegro/sites/unicef.org.montenegro/files/styles/hero_tablet/public/his_sofija-05-19-235_0.jpg?itok=YJQLrCrq')
    col1, col2, col3 = st.columns(3)
    
    with col1:
        number = st.number_input('a', key='num1')

    with col2:
        radio = st.radio('Phép toán', ('*+', '*-', 'x', ':'), horizontal=True)

    with col3:
        number2 = st.number_input('b', key='num2')
        number3 = st.number_input('Nhập kết quả', key='num3')

    if st.button('Kiểm tra'):
        result = 0
        if radio == 'x':
            result = number * number2
        elif radio == ':':
            result = number / number2
        elif radio == '*-':
            result = number - number2
        elif radio == '*+':
            result = number + number2

        if result == number3:
            st.write('True')
            st.balloons()
            st.snow()
        else:
            st.write('False')

with tab2:
    st.title('Đây là một video đặc sắc')
    st.video('https://www.youtube.com/watch?v=U1NalirmJjg')

with tab3:
    st.title('Lời đề bạt')
    st.write('Cuộc sống này không có điều gì đơn giản, quan trọng nhất là')
    st.write(':rainbow[bản thân mình đã đạt được thành tựu to lớn nào hay ho]')
    st.write('hihi iu bn')
