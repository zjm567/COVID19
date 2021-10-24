def covid19_risk_cal(age, mask, vaccination, geolocation):
    pass
    covid_risk = 1
    print("return from covid19_risk_cal")
    return covid_risk

age = int(input("Please enter the age:"))
# calculation of age-related covid-19 risk
def covid19_risk_age_cal(age):
    risk_age=0
    if age >= 0 and age <= 17:
        risk_age=0.09
    elif age >=18 and age <= 29:
        risk_age=0.239
    elif age >=30 and age <= 39:
        risk_age=0.165
    elif age >=40 and age <= 49:
        risk_age=0.152
    elif age >=50 and age <= 64:
        risk_age=0.205
    elif age >=65 and age <= 74:
        risk_age=0.076
    elif age >=75 and age <= 84:
        risk_age=0.043
    elif age >=85:
        risk_age=0.029
    else:
        print("not acceptable value, please try again")

    return risk_age

#risk_value = covid19_risk_cal(2,False,True,91108)
#print("the risk is:",risk_value)
risk_value = covid19_risk_age_cal(age)
print("the risk is:", risk_value)

