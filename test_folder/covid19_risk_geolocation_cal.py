import pandas as pd
df = pd.read_csv("RiskCategoryforGeolocation.csv") 

def state_data(state_name):
    for i in range(len(df.name)):
        if state_name == ratio.name[i]:
            value = df.ratio[i]
            return ratio[i]

ratio = float(input("Please enter your state:"))
def state(ratio):
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

risk_value = state(ratio)
print("the risk is: ", risk_value)