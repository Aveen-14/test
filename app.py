import streamlit as st
# import pandas


history = st.sidebar.selectbox(
    "when do you want to go",
    ("future","middle ages","prehistory","classical eara","early modern eara"),
)
# st.image
# if history == "future":
#     st.image("")



st.write("You selected:", history)

st.write("Hi,today NASA had invented a crazy looking time machine" \
" It is also LEVITETING!!!!!!!!!!!!!")



st.image("https://assets.isu.pub/document-structure/230410225044-e1fc316b1d34ed1275beb8178f89a526/v1/68fe689b851084f53f1519d5b12558ee.jpeg")


st.button("reset", type="primary")
if st.button("past (ninjago danger!!)"):
    st.image("https://www.lego.com/cdn/cs/set/assets/blte9d0e23489f7d487/71742_alt2.png")
    st.write("danger the overlord with the overlord !!!!!!")
else:
    st.write("Goodbye")

# if st.button("future")