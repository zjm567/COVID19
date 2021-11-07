from covid19_risk_cal import covid19_risk_age_cal as risk_age

if __name__ == '__main__':
 age =int(input("Please enter your age: "))
risk_value=risk_age(age)
print("The risk is: ",risk_value)


from covid19_risk_cal import test_case_ratio as risk_ratio

ratio = float(input("Please enter your test case percentage:"))
risk_value = risk_ratio(ratio)
print("the risk is: ", risk_value)

from covid19_risk_cal import covid19_risk_vaccination_cal as risk_vaccination

vaccination=input("Are you vaccinated or not?(y/n):")
risk_value = risk_vaccination(vaccination)
print("the risk is: ", risk_value)

from covid19_risk_cal import covid19_risk_mask_cal as risk_mask

mask=input("Do you wear mask or not? (y/n): ")
risk_value=risk_mask(mask)
print("The risk is: ",risk_value)

