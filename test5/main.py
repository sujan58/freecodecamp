from sea_level_predictor import load_data, draw_plot

# Load the data from the CSV file
df = load_data('epa-sea-level.csv')

# Call the function to create the plot
draw_plot(df)
