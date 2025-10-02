from time_series_visualizer import load_data, clean_data, draw_line_plot, draw_bar_plot, draw_box_plot

# Load data
df = load_data('fcc-forum-pageviews.csv')

# Clean the data
df_clean = clean_data(df)

# Call the functions to create the visualizations
draw_line_plot(df_clean)
draw_bar_plot(df_clean)
draw_box_plot(df_clean)
