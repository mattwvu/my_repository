import pandas as pd

# Read the dataset
df = pd.read_csv('data/dice_rolls.csv')

# Display the dataset
print(df)

# Example: Calculate the average total roll for each dice type
avg_total_by_dice_type = df.groupby('Dice_Type')['Total'].mean()
print("\nAverage Total by Dice Type:")
print(avg_total_by_dice_type)

# Example: Count the number of rolls per dice type
count_by_dice_type = df['Dice_Type'].value_counts()
print("\nCount of Rolls by Dice Type:")
print(count_by_dice_type)
