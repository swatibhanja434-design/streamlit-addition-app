import streamlit as st

st.title("Addition App")

num1 = st.number_input("Enter First Number")
num2 = st.number_input("Enter Second Number")

if st.button("Add"):
    st.write("Sum =", num1 + num2)