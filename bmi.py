def calculate_bmi(height, weight):
    
    bmi = weight / (height * height)

    
    if bmi < 18.5:
        classification = -1  # Underweight
    elif 18.5 <= bmi <= 25.0:
        classification = 0   # Normal weight
    else:
        classification = 1   # Overweight

    print("Height = " + str(height) + " meters")
    print("Weight = " + str(weight) + " kg")
    print(f"calculated BMI = {bmi:.2f}")
    print(f"BMI Classification: {classification}")

    return bmi, classification

if __name__ == "__main__":
    height = 1.73
    weight = 57
    calculate_bmi(height, weight)
