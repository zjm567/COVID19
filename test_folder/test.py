import pandas as pd

df = pd.read_csv("RiskCategoryforGeolocation.csv") 

geolocation = input("Please enter your state name:")

def state_data(state_name):
    for i in range(len(df.State)):
        if state_name == df.State[i]:
           ratio = df.Ratio[i]
           return ratio


def covid19_risk_ratio_cal(ratio):
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

def covid19_risk_geolocation_cal(geolocation):
    x = state_data(geolocation)
    risk_level=covid19_risk_ratio_cal(x)
    return risk_level

risk_value = covid19_risk_geolocation_cal(geolocation)
print(risk_value)





