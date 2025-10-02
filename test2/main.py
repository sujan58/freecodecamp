import pandas as pd

# Load the dataset
df = pd.read_csv('demographic_data.csv')

# 1. How many people of each race are represented in this dataset?
race_counts = df['race'].value_counts()

# 2. What is the average age of men?
average_age_men = df[df['sex'] == 'Male']['age'].mean()

# 3. What is the percentage of people who have a Bachelor's degree?
percentage_bachelors = (df[df['education'] == 'Bachelors'].shape[0] / df.shape[0]) * 100

# 4. What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
advanced_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
percentage_advanced_education_50k = (advanced_education[advanced_education['salary'] == '>50K'].shape[0] / advanced_education.shape[0]) * 100

# 5. What percentage of people without advanced education make more than 50K?
no_advanced_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
percentage_no_advanced_education_50k = (no_advanced_education[no_advanced_education['salary'] == '>50K'].shape[0] / no_advanced_education.shape[0]) * 100

# 6. What is the minimum number of hours a person works per week?
min_hours_per_week = df['hours-per-week'].min()

# 7. What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
min_hours_50k = df[df['hours-per-week'] == min_hours_per_week]
percentage_min_hours_50k = (min_hours_50k[min_hours_50k['salary'] == '>50K'].shape[0] / min_hours_50k.shape[0]) * 100

# 8. What country has the highest percentage of people that earn >50K and what is that percentage?
country_50k_percentage = df.groupby('native-country').apply(lambda x: (x[x['salary'] == '>50K'].shape[0] / x.shape[0]) * 100)
highest_country_50k = country_50k_percentage.idxmax()
highest_country_percentage = country_50k_percentage.max()

# 9. Identify the most popular occupation for those who earn >50K in India.
india_50k = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
most_popular_occupation_india_50k = india_50k['occupation'].mode()[0]

# Results (you can print these to verify or use for your project requirements)
print("Race Counts:")
print(race_counts)
print(f"\nAverage age of men: {average_age_men:.1f}")
print(f"Percentage of people with a Bachelor's degree: {percentage_bachelors:.1f}%")
print(f"Percentage of people with advanced education earning >50K: {percentage_advanced_education_50k:.1f}%")
print(f"Percentage of people without advanced education earning >50K: {percentage_no_advanced_education_50k:.1f}%")
print(f"Minimum hours per week: {min_hours_per_week}")
print(f"Percentage of people working min hours per week earning >50K: {percentage_min_hours_50k:.1f}%")
print(f"Country with the highest percentage of people earning >50K: {highest_country_50k} ({highest_country_percentage:.1f}%)")
print(f"Most popular occupation for those earning >50K in India: {most_popular_occupation_india_50k}")

