import streamlit as st
import pandas as pd
import numpy as np
from src.recommendation_engine import NutritionRecommender
from src.data_processor import DataProcessor
from src.utils import calculate_bmi, calculate_calorie_needs

def main():
    st.title("Personalized Nutrition Recommendation System")
    
    # Sidebar for user input
    st.sidebar.header("User Profile")
    
    # User inputs
    age = st.sidebar.number_input("Age", 15, 100, 25)
    gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
    weight = st.sidebar.number_input("Weight (kg)", 30.0, 200.0, 70.0)
    height = st.sidebar.number_input("Height (cm)", 100.0, 250.0, 170.0)
    activity_level = st.sidebar.selectbox(
        "Activity Level",
        ["Sedentary", "Lightly Active", "Moderately Active", "Very Active", "Extra Active"]
    )
    
    # Health conditions and dietary preferences
    st.sidebar.subheader("Health Conditions")
    diabetes = st.sidebar.checkbox("Diabetes")
    hypertension = st.sidebar.checkbox("Hypertension")
    heart_disease = st.sidebar.checkbox("Heart Disease")
    
    st.sidebar.subheader("Dietary Preferences")
    vegetarian = st.sidebar.checkbox("Vegetarian")
    vegan = st.sidebar.checkbox("Vegan")
    gluten_free = st.sidebar.checkbox("Gluten Free")
    
    # Calculate BMI and daily calorie needs
    bmi = calculate_bmi(weight, height)
    daily_calories = calculate_calorie_needs(weight, height, age, gender, activity_level)
    
    # Display user metrics
    st.header("Your Health Metrics")
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("BMI", f"{bmi:.1f}")
        st.metric("Daily Calorie Needs", f"{daily_calories:.0f} kcal")
    
    # Initialize recommendation engine
    recommender = NutritionRecommender()
    
    # Get recommendations
    if st.button("Get Personalized Recommendations"):
        user_profile = {
            'age': age,
            'gender': gender,
            'weight': weight,
            'height': height,
            'bmi': bmi,
            'activity_level': activity_level,
            'daily_calories': daily_calories,
            'diabetes': diabetes,
            'hypertension': hypertension,
            'heart_disease': heart_disease,
            'vegetarian': vegetarian,
            'vegan': vegan,
            'gluten_free': gluten_free
        }
        
        recommendations = recommender.get_recommendations(user_profile)
        
        st.header("Your Personalized Nutrition Plan")
        
        # Display meal recommendations
        st.subheader("Daily Meal Plan")
        for meal, items in recommendations['meals'].items():
            st.write(f"**{meal}:**")
            for item in items:
                st.write(f"- {item}")
        
        # Display nutrition tips
        st.subheader("Nutrition Tips")
        for tip in recommendations['tips']:
            st.write(f"- {tip}")
        
        # Display nutrition distribution
        st.subheader("Recommended Macro Distribution")
        st.write(f"- Proteins: {recommendations['macros']['protein']}g")
        st.write(f"- Carbohydrates: {recommendations['macros']['carbs']}g")
        st.write(f"- Healthy Fats: {recommendations['macros']['fats']}g")

if __name__ == "__main__":
    main()
