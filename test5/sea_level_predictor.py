import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Function to load the dataset
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

# Function to create the scatter plot and lines of best fit
def draw_plot(df):
    # Create the scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Sea Level Data')

    # Line of best fit for the entire dataset
    slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.plot(df['Year'], slope * df['Year'] + intercept, color='red', label='Best Fit Line (1880-Present)')

    # Line of best fit from year 2000 onwards
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    plt.plot(df_recent['Year'], slope_recent * df_recent['Year'] + intercept_recent, color='green', label='Best Fit Line (2000-Present)')

    # Labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.legend()

    # Extend the lines to the year 2050
    plt.xlim([df['Year'].min(), 2050])
    
    # Save the plot
    plt.tight_layout()
    plt.savefig('sea_level_plot.png')
    plt.show()
