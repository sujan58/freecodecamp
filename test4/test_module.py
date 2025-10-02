import unittest
import pandas as pd
from time_series_visualizer import clean_data

class TestTimeSeriesVisualizer(unittest.TestCase):

    def setUp(self):
        # Sample data for testing purposes
        data = {
            'date': pd.date_range('2016-05-09', periods=5, freq='D'),
            'page_views': [100, 500, 10000, 150, 1200]
        }
        self.df = pd.DataFrame(data)
        self.df.set_index('date', inplace=True)
        
    def test_clean_data(self):
        # Clean the data
        cleaned_df = clean_data(self.df)
        
        # Check that the data has been cleaned correctly
        self.assertEqual(len(cleaned_df), 3)  # We should have removed the top and bottom 2.5% page views
        
        # Check if the min and max page views are within the 2.5% quantiles
        self.assertGreater(cleaned_df['page_views'].min(), self.df['page_views'].quantile(0.025))
        self.assertLess(cleaned_df['page_views'].max(), self.df['page_views'].quantile(0.975))
    
if __name__ == "__main__":
    unittest.main()
