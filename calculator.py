import streamlit as st

st.title("Student Marks Calculator")

name = st.text_input("Enter Student Name")

m1 = st.number_input("Subject 1 Marks", 0, 100)
m2 = st.number_input("Subject 2 Marks", 0, 100)
m3 = st.number_input("Subject 3 Marks", 0, 100)

if st.button("Calculate"):
    total = m1 + m2 + m3
    percentage = total / 3

    st.write("Name:", name)
    st.write("Total Marks:", total)
    st.write("Percentage:", percentage)

    if percentage >= 40:
        st.success("Pass")
    else:
        st.error("Fail")