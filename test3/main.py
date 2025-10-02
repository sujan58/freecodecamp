from medical_data_visualizer import load_data, add_overweight_column, normalize_chol_gluc, draw_cat_plot, draw_heat_map

# Load the dataset
df = load_data('medical_examination.csv')

# Add overweight column
df = add_overweight_column(df)

# Normalize cholesterol and gluc
df = normalize_chol_gluc(df)

# Call the functions to visualize the data
draw_cat_plot(df)
draw_heat_map(df)
