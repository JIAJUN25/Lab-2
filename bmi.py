def calculate_bmi(height, weight):
    print("Height = " + str(height) + " meters")
    print("Weight = " + str(weight) + " kg")
    
    bmi = weight / (height * height)

    print(f"calculated BMI = {bmi:.2f}")

    if bmi < 18.5:
        classification = "under weight"
    elif 18.5 <= bmi <= 25.0:
        classification = "normal weight"
    elif bmi > 25.0:
        classification = "over weight"

    print(f"BMI Classification: {classification}")

calculate_bmi(weight=57, height=1.73)
