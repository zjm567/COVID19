from covid19_risk_age_cal import covid19_risk_age_cal as risk_age
age=int(input("Please enter your age: "))
risk_value=risk_age(age)
print("The risk is: ",risk_value)