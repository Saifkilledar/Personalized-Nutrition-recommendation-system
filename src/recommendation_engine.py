import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors
from .data_processor import DataProcessor

class NutritionRecommender:
    def __init__(self):
        self.data_processor = DataProcessor()
        self.food_db = self.data_processor.load_food_database()
        
    def get_recommendations(self, user_profile):
        """
        Generate personalized nutrition recommendations based on user profile
        """
        processed_data = self.data_processor.preprocess_user_data(user_profile)
        
        # Calculate macro distributions
        macros = self._calculate_macro_distribution(processed_data)
        
        # Generate meal recommendations
        meals = self._generate_meal_plan(processed_data, macros)
        
        # Generate nutrition tips
        tips = self._generate_nutrition_tips(processed_data)
        
        return {
            'meals': meals,
            'macros': macros,
            'tips': tips
        }
    
    def _calculate_macro_distribution(self, user_data):
        """
        Calculate recommended macro nutrient distribution
        """
        daily_calories = user_data['daily_calories']
        
        # Adjust macro ratios based on user conditions
        if user_data['diabetes']:
            protein_ratio = 0.30
            carbs_ratio = 0.40
            fats_ratio = 0.30
        else:
            protein_ratio = 0.25
            carbs_ratio = 0.50
            fats_ratio = 0.25
        
        return {
            'protein': round((daily_calories * protein_ratio) / 4),  # 4 calories per gram of protein
            'carbs': round((daily_calories * carbs_ratio) / 4),     # 4 calories per gram of carbs
            'fats': round((daily_calories * fats_ratio) / 9)        # 9 calories per gram of fat
        }
    
    def _generate_meal_plan(self, user_data, macros):
        """
        Generate personalized meal recommendations
        """
        meals = {
            'Breakfast': [],
            'Lunch': [],
            'Dinner': [],
            'Snacks': []
        }
        
        # Filter foods based on dietary restrictions
        available_foods = self.food_db.copy()
        if user_data['vegetarian']:
            available_foods = available_foods[~available_foods['category'].isin(['meat'])]
        if user_data['vegan']:
            available_foods = available_foods[~available_foods['category'].isin(['meat', 'dairy', 'eggs'])]
        
        # Simple meal planning logic (can be enhanced with more sophisticated algorithms)
        breakfast_foods = available_foods[available_foods['category'].isin(['grain', 'dairy', 'fruit'])]
        lunch_dinner_foods = available_foods[available_foods['category'].isin(['protein', 'vegetable', 'grain'])]
        snack_foods = available_foods[available_foods['category'].isin(['fruit', 'nuts', 'dairy'])]
        
        # Add sample meals (this is a simplified version)
        meals['Breakfast'] = breakfast_foods['name'].sample(min(3, len(breakfast_foods))).tolist()
        meals['Lunch'] = lunch_dinner_foods['name'].sample(min(4, len(lunch_dinner_foods))).tolist()
        meals['Dinner'] = lunch_dinner_foods['name'].sample(min(4, len(lunch_dinner_foods))).tolist()
        meals['Snacks'] = snack_foods['name'].sample(min(2, len(snack_foods))).tolist()
        
        return meals
    
    def _generate_nutrition_tips(self, user_data):
        """
        Generate personalized nutrition tips based on user profile
        """
        tips = [
            "Stay hydrated by drinking at least 8 glasses of water daily",
            "Try to eat meals at consistent times each day"
        ]
        
        if user_data['bmi'] > 25:
            tips.append("Focus on portion control and include more fiber-rich foods")
        
        if user_data['diabetes']:
            tips.append("Monitor your carbohydrate intake and prefer low glycemic index foods")
        
        if user_data['hypertension']:
            tips.append("Limit sodium intake and increase consumption of potassium-rich foods")
        
        if user_data['heart_disease']:
            tips.append("Choose heart-healthy fats and limit saturated fats")
        
        return tips
