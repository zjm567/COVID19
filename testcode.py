mask=input("Do you wear mask or not? (y/n): ")
print (mask)
def covid19_risk_mask_cal(mask):
    if mask=='y':
        risk_mask=0.175
    elif mask=='n':
        risk_mask=0.825
    else:
        print("can not identify, please try again")

    return risk_mask

risk_value = covid19_risk_mask_cal(mask)
print("the risk is:", risk_value)