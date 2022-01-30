import streamlit as st
from covid19_risk_cal import risk_cal

def main():
    # age = int(input("Please enter your age: "))
    # mask = input("Do you wear mask or not? (y/n)")
    # vaccination = input("Are you vaccinated or not?(y/n)")
    # geolocation = input("Please enter your state name: ")
    st.title("Conventage")

    col_l, col_r = st.columns(2)
    with col_l:
        st.write("Risk Calculator")
    with col_r:
        st.write("Tips")
    
    age = st.number_input("Please Enter Your Age:", min_value = 0, max_value = 100, step = 1)
  
    mask = st.selectbox("Do you wear a mask? ",
                            options = ['Yes','No'])

    vaccination = st.selectbox("Are you vaccinated? ",
                            options = ['Yes','No'])

    geolocation = st.text_input("Please Enter Your State:", "The full US state name", max_chars =25)

    #print("The overall risk is :",risk_value,"%")

    calculate_button = st.button("Calculate")
    if calculate_button:
        risk_value = risk_cal(age, mask, vaccination, geolocation)
        st.write("The overall risk is: ",risk_value,"%")

if __name__ == '__main__':
    main()
