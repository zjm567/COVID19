
import streamlit as st
import datetime

st.title("COVID-19 RISK CALCULATOR")
st.write("Here is the COVID-19 risk calculator for each U.S. state.")

your_name = st.text_input("Your Name:", "Your Full Name", max_chars =20)

your_info = st.text_area("Tell us Something About Yourself: ", "Hobby",
                            help = "You can write anything you want to tell us.")

your_age = st.number_input("Your Age:", min_value = 1, max_value = 100, step = 1)

your_birthday = st.date_input("Your Date of Birth:", min_value = datetime.date(1922, 1, 1), max_value= datetime.date(2050, 1, 1))

health_status = st.checkbox("Are You Healthy?")
your_gender = st.radio("What is Your Gender?",
                            options = ['Male','Female'])

your_weight = st.slider("Choose Your Weight (lb)", min_value = 1., max_value = 300., step = 5.)

health = st.selectbox("Select Level of Your Physical Condition",
                        options = ["Sick","Normal","Good"])

colors = st.multiselect("What are Your Favorite Colors?",
                        options = ["Green","Blue","Red","Yellow","Orange","Purple","Pink","Black","White"])

image = st.file_uploader("Please Upload Your Photo", type=['jpg','png','gif'])

submit_button = st.button("Submit")
if submit_button:
    st.write("Your Form is Successfully Submitted.")

click_button = st.sidebar.button("Click Me!")
if click_button:
    st.sidebar.write("You Clicked Me!")

col1, col2 = st.columns(2)
with col1:
    st.image("https://static.streamlit.io/examples/cat.jpg", width=300)
    st.button("I Clicked Cats!")
with col2:
    st.image("https://static.streamlit.io/examples/dog.jpg",width=300)
    st.button("I Like Dogs!")

st.write("Check Out This [Link](https://ocsef.org)")