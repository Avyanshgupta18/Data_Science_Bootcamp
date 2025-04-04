import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "Brooklyn_Bridge_Automated_Pedestrian_Counts_Demonstration_Project.csv"
df = pd.read_csv(file_path)

# Convert 'hour_beginning' to datetime format
df['hour_beginning'] = pd.to_datetime(df['hour_beginning'])

# --- Question 1: Weekday Analysis ---
df['DayOfWeek'] = df['hour_beginning'].dt.day_name()
weekday_df = df[df['DayOfWeek'].isin(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])]

weekday_counts = weekday_df.groupby('DayOfWeek')['Pedestrians'].sum().reindex(
    ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
)

plt.figure(figsize=(10, 5))
plt.plot(weekday_counts.index, weekday_counts.values, marker='o')
plt.title('Pedestrian Counts on Brooklyn Bridge (Weekdays)')
plt.xlabel('Day of the Week')
plt.ylabel('Total Pedestrian Count')
plt.grid(True)
plt.tight_layout()
plt.show()

df['year'] = df['hour_beginning'].dt.year
df_2019 = df[df['year'] == 2019]

weather_df = df_2019[['Pedestrians', 'weather_summary']].dropna()

# One-hot encode weather summary
weather_encoded = pd.get_dummies(weather_df['weather_summary'])
encoded_df = pd.concat([weather_df[['Pedestrians']], weather_encoded], axis=1)

# Correlation matrix
correlation_matrix = encoded_df.corr()

plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix: Weather Conditions and Pedestrian Counts (2019)')
plt.tight_layout()
plt.show()

def categorize_time_of_day(hour):
    if 5 <= hour < 12:
        return 'Morning'
    elif 12 <= hour < 17:
        return 'Afternoon'
    elif 17 <= hour < 21:
        return 'Evening'
    else:
        return 'Night'

# Extract hour and apply function
df['Hour'] = df['hour_beginning'].dt.hour
df['TimeOfDay'] = df['Hour'].apply(categorize_time_of_day)

# Group and plot
time_of_day_activity = df.groupby('TimeOfDay')['Pedestrians'].mean().reindex(
    ['Morning', 'Afternoon', 'Evening', 'Night']
)

plt.figure(figsize=(8, 5))
plt.bar(time_of_day_activity.index, time_of_day_activity.values)
plt.title('Average Pedestrian Activity by Time of Day')
plt.xlabel('Time of Day')
plt.ylabel('Average Pedestrian Count')
plt.tight_layout()
plt.show()