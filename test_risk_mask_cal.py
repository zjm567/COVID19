from covid19_risk_mask_cal import covid19_risk_mask_cal as risk_mask
mask=input("Do you wear mask or not? (y/n): ")
risk_value=risk_mask(mask)
print("The risk is: ",risk_value)