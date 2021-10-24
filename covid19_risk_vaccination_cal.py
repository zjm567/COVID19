

def covid19_risk_vaccination_cal(vaccination):
    if vaccination=='y':
        risk_vaccination=0.15
    elif vaccination=='n':
        risk_vaccination=0.85
    else:
        print("can not identify, please try again")
    
    return risk_vaccination


