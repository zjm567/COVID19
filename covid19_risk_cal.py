#age = int(input("Please enter the age:"))
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

#risk_value = covid19_risk_age_cal(age)
#print("the risk is: ", risk_value)

#mask=input("Do you wear mask or not? (y/n): ")
def covid19_risk_mask_cal(mask):
    if mask=='y':
        risk_mask=0.175
    elif mask=='n':
        risk_mask=0.825
    else:
        print("can not identify, please try again")

    return risk_mask

#risk_value = covid19_risk_mask_cal(mask)
#print("the risk is: ", risk_value)

#vaccination=input("Are you vaccinated or not?(y/n):")
def covid19_risk_vaccination_cal(vaccination):

    if vaccination=='y':
        risk_vaccination=0.15
    elif vaccination=='n':
        risk_vaccination=0.85
    else:
        print("can not identify, please try again")
    
    return risk_vaccination

#risk_value = covid19_risk_vaccination_cal(vaccination)
#print("the risk is: ", risk_value)

#def covid19_risk_geolocation_cal(geolocation):
# Note: geolocation is equal to percentage
#ratio = float(input("Please enter your test case percentage:"))

def test_case_ratio(ratio):
    if ratio >= 0 and ratio <= 10:
        risk_ratio=0.015
    elif ratio >=11 and ratio <= 20:
        risk_ratio=0.035
    elif ratio >=21 and ratio <= 35:
        risk_ratio=0.1
    elif ratio >=36 and ratio <= 50:
        risk_ratio=0.15
    elif ratio >=51 and ratio <= 100:
        risk_ratio=0.7
    else:
        print("invalid input value, please try again")
    return risk_ratio

#risk_value = test_case_ratio(ratio)
#print("the risk is: ", risk_value)

w0, w1, w2, w3 = (0.1,0.20,0.30,0.20)
def risk_cal(age, mask, vaccination, geolocation):
    risk = w0*age+w1+mask+w2+vaccination+w3*geolocation
    return risk

