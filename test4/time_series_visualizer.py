import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from the CSV file and set the index to the 'date' column
def load_data(file_path):
    df = pd.read_csv(file_path, parse_dates=['date'], index_col='date')
    return df

# Clean the data by filtering out the top and bottom 2.5% of page views
def clean_data(df):
    lower_percentile = df['page_views'].quantile(0.025)
    upper_percentile = df['page_views'].quantile(0.975)
    df_clean = df[(df['page_views'] > lower_percentile) & (df['page_views'] < upper_percentile)]
    return df_clean

# Create a line plot
def draw_line_plot(df):
    # Plot line chart
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['page_views'], color='b', linewidth=1)
    
    # Add title and labels
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("
