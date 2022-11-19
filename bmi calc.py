#this is the bmi calculator part
weight = int(input("Enter your weight in Kg : "))
height = float(input("Enter your height in m : "))
bmi = weight / height**2 
print("Your bmi is",bmi)
if bmi < 20:
    print("You are underweight.\nYou should gain some weight by modifying your diet to include more ???")
elif bmi < 25:
    print("You are perfectly healthy")
elif bmi < 30:
    print("You are overweight.\nYou should lose some weight by modifying your diet and doing some exercise. Gaining more weight will put you in serious health problems.")
elif bmi < 40:
    print("You are obese.\nYou should definitely reconsider your diet and do a lot of exercise to lose weight because you are vaulnrable to a series of health problems, including : heart disease, diabetes, high blood pressure, gall bladder disease, circulation problems, and some cancers.")
else:
    print("You are obese but at a very dangerous level : YOUR LIFE IS AT RISK!!\nYou should definitely reconsider your diet and do a lot of exercise to lose weight because you are extremely vaulnrable to a series of health problems, including : heart disease, diabetes, high blood pressure, gall bladder disease, circulation problems, and some cancers.")

