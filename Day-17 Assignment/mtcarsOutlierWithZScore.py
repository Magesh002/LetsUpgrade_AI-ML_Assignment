import pandas as pd
import seaborn as sns

mtCars = pd.read_csv('mtcars.csv')

print(mtCars.head())
print("\nThe shape of mtCars:", mtCars.shape)

sns.boxplot(data=mtCars, x=mtCars['hp'])

Q1 = mtCars['hp'].quantile(0.25)
Q3 = mtCars['hp'].quantile(0.75)
IQR = Q3-Q1

print("The Q1 value:", Q1)
print("The Q3 value:", Q3)
print("The IQR value:", IQR)

Lower_Whisker = Q1 - 1.5 * IQR
Upper_Whisker = Q3 + 1.5 * IQR
print("\nLower Whisker:", Lower_Whisker, "and Upper Whisker:", Upper_Whisker)

mtCars = mtCars[mtCars['hp'] < Upper_Whisker]
print(mtCars.head())
print("\nThe shape of mtCars:", mtCars.shape)