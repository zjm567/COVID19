from covid19_risk_cal import risk_cal as risk_overall

def main():
    age =int(input("Please enter your age: "))

    ratio = float(input("Please enter your test case percentage:"))

    vaccination=input("Are you vaccinated or not?(y/n):")

    mask=input("Do you wear mask or not? (y/n): ")

    risk_value=risk_overall(age, mask, vaccination, ratio)
    print("The overall risk is : ", risk_value)

if __name__ == '__main__':
    main()
    
