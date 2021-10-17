w0, w1, w2, w3 = (0.1,0.20,0.30,0.20)
def risk_cal(age, mask, vaccination, geolocation):
    risk = w0*age+w1+mask+w2+vaccination+w3*geolocation
    return risk
