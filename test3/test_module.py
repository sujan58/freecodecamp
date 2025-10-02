import unittest
import pandas as pd
from medical_data_visualizer import add_overweight_column, normalize_chol_gluc

class TestMedicalDataVisualizer(unittest.TestCase):

    def setUp(self):
        # Sample data for testing purposes
        self.df = pd.DataFrame({
            'height': [170, 160, 180],
            'weight': [70, 60, 80],
            'cholesterol': [1, 2, 3],
            'gluc': [1, 2, 3],
            'cardio': [1, 0, 1],
            'smoke': [0, 1, 0],
            'alco': [0, 1, 0],
            'active': [1, 0, 1],
            'ap_lo': [80, 75, 70],
            'ap_hi': [120, 115, 110]
        })

    def test_add_overweight_column(self):
        # Add overweight column
        df = add_overweight_column(self.df)
        # Test if overweight column is added and has correct values
        self.assertIn('overweight', df.columns)
        self.assertEqual(df['overweight'].iloc[0], 0)  # First person is not overweight

    def test_normalize_chol_gluc(self):
        # Normalize cholesterol and gluc columns
        df = normalize_chol_gluc(self.df)
        # Test if cholesterol and gluc columns are normalized
        self.assertEqual(df['cholesterol'].iloc[0], 0)  # Normal cholesterol value should be 0
        self.assertEqual(df['gluc'].iloc[1], 1)  # Elevated glucose should be 1

if __name__ == "__main__":
    unittest.main()
