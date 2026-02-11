import streamlit as st
import g4f

st.set_page_config(page_title="X Assistant", page_icon="🤖")
st.title("🤖 X Assistant")
st.markdown("مبرمج بواسطة الحريف: **أحمد الحريف**")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "أهلاً بك! أنا X Assistant، مبرمجي هو أحمد الحريف. تؤمرني بإيه يا بطل؟"}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("اسأل X Assistant..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        try:
            response = g4f.ChatCompletion.create(
                model=g4f.models.gpt_4,
                messages=[{"role": "system", "content": "أنت مساعد ذكي ومرح اسمك X Assistant. مبرمجك هو أحمد الحريف. اتكلم بالعامية المصرية بأسلوب ممتع."},
                          {"role": "user", "content": prompt}]
            )
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
        except:
            st.error("السيرفر مريح شوية، جرب كمان ثواني!")
          
