from covid19_risk_vaccination_cal import covid19_risk_vaccination_cal as risk_vaccination
vaccination=input("Are you vaccinated or not?(y/n):")
risk_value = risk_vaccination(vaccination)
print("the risk is: ",risk_value)