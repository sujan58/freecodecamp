import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Function to load the dataset
def load_data(file_path):
    return pd.read_csv(file_path)

# Function to add overweight column
def add_overweight_column(df):
    # Calculate BMI and create an 'overweight' column
    df['bmi'] = df['weight'] / ((df['height'] / 100) ** 2)
    df['overweight'] = df['bmi'].apply(lambda x: 1 if x > 25 else 0)
    return df

# Function to normalize cholesterol and gluc
def normalize_chol_gluc(df):
    df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
    df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)
    return df

# Function to create categorical plot
def draw_cat_plot(df):
    # Melt the dataframe to convert it into long format
    df_cat = pd.melt(df, id_vars=["cardio"], value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"])
    
    # Group and reformat the data
    df_cat = df_cat.groupby(["cardio", "variable", "value"]).size().reset_index(name="total")
    
    # Draw the categorical plot
    fig = sns.catplot(x="variable", hue="value", col="cardio", data=df_cat, kind="count")
    
    # Set axis labels
    fig.set_axis_labels("Feature", "Count")
    
    # Show the plot
    plt.show()

# Function to create a heatmap
def draw_heat_map(df):
    # Clean the data by filtering out incorrect records
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) & 
        (df['height'] >= df['height'].quantile(0.025)) & 
        (df['height'] <= df['height'].quantile(0.975)) & 
        (df['weight'] >= df['weight'].quantile(0.025)) & 
        (df['weight'] <= df['weight'].quantile(0.975))
    ]
    
    # Calculate the correlation matrix
    corr = df_heat.corr()
    
    # Generate a mask for the upper triangle
    mask = np.triu(corr)
    
    # Set up the matplotlib figure
    plt.figure(figsize=(12, 8))
    
    # Plot the heatmap
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", cmap="coolwarm", linewidths=0.5)
    
    # Show the plot
    plt.show()
