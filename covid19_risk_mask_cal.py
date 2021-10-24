
def covid19_risk_mask_cal(mask):
    if mask=='y':
        risk_mask=0.175
    elif mask=='n':
        risk_mask=0.825
    else:
        print("can not identify, please try again")

    return risk_mask

