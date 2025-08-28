from dotenv import load_dotenv
import streamlit as st
from utils import make_response

load_dotenv()

st.title("한국서부발전")
st.markdown("""
안녕하세요. 저는 서민욱 대리입니다.
좋아하는 과일은
            
+ 바나나
+ 수박
""")

question = st.text_input("질문을 입력하세요.")
if st.button("전송") and question:
    ai_content = make_response(user_content=question)
    st.write(f"AI : {ai_content}")
    