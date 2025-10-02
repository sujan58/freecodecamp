import unittest
import pandas as pd
from sea_level_predictor import load_data

class TestSeaLevelPredictor(unittest.TestCase):

    def setUp(self):
        # Sample data for testing purposes
        data = {
            'Year': [1880, 1881, 1882, 1883, 1884, 1885],
            'CSIRO Adjusted Sea Level': [0.0, 0.1, 0.15, 0.2, 0.25, 0.3]
        }
        self.df = pd.DataFrame(data)

    def test_load_data(self):
        # Check that the data is loaded correctly
        df = load_data('epa-sea-level.csv')
        self.assertIsInstance(df, pd.DataFrame)  # Ensure it's a pandas DataFrame
        self.assertEqual(df.shape[0], 134)  # Check the number of rows in the dataset (there are 134 years of data)
    
if __name__ == "__main__":
    unittest.main()
