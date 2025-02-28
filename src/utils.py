def calculate_bmi(weight, height):
    """
    Calculate BMI given weight in kg and height in cm
    """
    height_m = height / 100  # convert cm to m
    bmi = weight / (height_m * height_m)
    return round(bmi, 2)

def calculate_calorie_needs(weight, height, age, gender, activity_level):
    """
    Calculate daily calorie needs using the Mifflin-St Jeor equation
    """
    # Calculate BMR (Basal Metabolic Rate)
    height_cm = height
    if gender == "Male":
        bmr = 10 * weight + 6.25 * height_cm - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height_cm - 5 * age - 161
    
    # Activity multipliers
    activity_multipliers = {
        "Sedentary": 1.2,
        "Lightly Active": 1.375,
        "Moderately Active": 1.55,
        "Very Active": 1.725,
        "Extra Active": 1.9
    }
    
    # Calculate total daily calorie needs
    daily_calories = bmr * activity_multipliers[activity_level]
    
    return round(daily_calories)
