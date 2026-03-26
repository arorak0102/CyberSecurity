# Temperature Converter

print("Welcome to the temperature converter!")

userChoice = input(
    "Would you convert Celsius->Fahrenheit (C2F) or Fahrenheit->Celsius (F2C): \n"
).lower()

# Input C2F for Celsius->Fahrenheit or F2C for Fahrenheit->Celsius
if userChoice == "c2f":
    temp = float(input("Enter the temperature: \n"))
    finalTemp = (temp * 1.8) + 32
    print(f"{temp} Celsius -> {finalTemp} Fahrenheit")

elif userChoice == "f2c":
    temp = float(input("Enter the temperature: \n"))
    finalTemp = (temp - 32) / 1.8
    print(f"{temp} Fahrenheit -> {finalTemp} Celsius")

else:
    print("Wrong input!")
