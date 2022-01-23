from covid19_risk_cal import risk_cal 

def main():
    age = int(input("Please enter your age: "))
    mask = input("Do you wear mask or not? (y/n): ")
    vaccination = input("Are you vaccinated or not?(y/n): ")
    geolocation = input("Please enter your state name: ")

    risk_value = risk_cal(age, mask, vaccination, geolocation)
    print("The overall risk is : ", risk_value,"%")

if __name__ == '__main__':
    main()
    
