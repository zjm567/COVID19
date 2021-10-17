def covid19_risk_cal(age, mask, vaccination, geolocation):
    pass
    covid_risk = 1
    print("return from covid19_risk_cal")
    return covid_risk

# calculation of age-related covid-19 risk
def covid19_risk_age_cal(age):
    age = int(input("Please enter the age:"))
    if age <= 18:
        risk_age=0.09
    elif age <= 29:
        risk_age=0.239
    elif age <= 39:
        risk_age=0.165
    elif age <= 49:
        risk_age=0.152
    elif age <= 64:
        risk_age=0.205
    elif age <= 74:
        risk_age=0.076
    elif age <= 84:
        risk_age=0.043
    else:
        risk_age=0.029

    return risk_age

#risk_value = covid19_risk_cal(2,False,True,91108)
#print("the risk is:",risk_value)
risk_value = covid19_risk_age_cal(10)
print("the risk is:", risk_value)

def covid19_risk_mask_cal(mask):
    mask=input("Do you wear mask or not")
    if mask=='yes':
        risk_mask=0.175
    if mask=='no':
        risk_mask=0.825

    return risk_mask

def covid19_risk_vaccination_cal(vaccination):
    vaccination=input("Did you take a vaccine")
    if vaccination=='yes':
        risk_vaccination=0.15
    if vaccination=="no":
        risk_vaccination=0.85
    
    return risk_vaccination

def covid19_risk_geolocation_cal(geolocation):


    

