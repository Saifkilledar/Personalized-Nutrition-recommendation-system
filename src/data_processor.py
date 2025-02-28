import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

class DataProcessor:
    def __init__(self):
        self.scaler = StandardScaler()
        
    def load_food_database(self):
        """
        Load and preprocess the food database
        Returns preprocessed DataFrame
        """
        try:
            # Load food database (you'll need to create/provide this)
            df = pd.read_csv('data/food_database.csv')
            return df
        except FileNotFoundError:
            # Create sample food database if not exists
            return self._create_sample_database()
    
    def preprocess_user_data(self, user_profile):
        """
        Preprocess user data for the recommendation engine
        """
        # Convert categorical variables to numerical
        processed_data = {
            'age': user_profile['age'],
            'weight': user_profile['weight'],
            'height': user_profile['height'],
            'bmi': user_profile['bmi'],
            'daily_calories': user_profile['daily_calories'],
            'gender_male': 1 if user_profile['gender'] == 'Male' else 0,
            'diabetes': 1 if user_profile['diabetes'] else 0,
            'hypertension': 1 if user_profile['hypertension'] else 0,
            'heart_disease': 1 if user_profile['heart_disease'] else 0,
            'vegetarian': 1 if user_profile['vegetarian'] else 0,
            'vegan': 1 if user_profile['vegan'] else 0,
            'gluten_free': 1 if user_profile['gluten_free'] else 0
        }
        
        return processed_data
    
    def _create_sample_database(self):
        """
        Create a sample food database for demonstration
        """
        foods = {
            'name': [
                'Grilled Chicken Breast', 'Salmon Fillet', 'Quinoa', 'Brown Rice',
                'Sweet Potato', 'Broccoli', 'Spinach', 'Greek Yogurt',
                'Almonds', 'Banana'
            ],
            'calories': [
                165, 208, 120, 216, 103, 55, 23, 130, 164, 105
            ],
            'protein': [
                31, 22, 4, 5, 2, 3.7, 2.9, 17, 6, 1.3
            ],
            'carbs': [
                0, 0, 21, 45, 24, 11.2, 3.6, 9, 6, 27
            ],
            'fats': [
                3.6, 13, 1.9, 1.6, 0.2, 0.6, 0.4, 0.7, 14, 0.4
            ],
            'category': [
                'protein', 'protein', 'grain', 'grain',
                'vegetable', 'vegetable', 'vegetable', 'dairy',
                'nuts', 'fruit'
            ]
        }
        return pd.DataFrame(foods)
