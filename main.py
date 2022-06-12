import pandas as pd
import matplotlib.pyplot as plt

# PART 1
titanic_data = pd.read_csv("titanic.csv")

# PART 2
shortened_data = titanic_data.dropna()

removed_observations = len(shortened_data) - len(titanic_data)
print("Step 2 total removed observations: ", removed_observations)

# PART 3
shortened_titanic_data = titanic_data.drop(columns=['deck'])
shortened_titanic_data = shortened_titanic_data.dropna()

removed_observations_2 = len(shortened_titanic_data) - len(titanic_data)
print("Step 3 total removed observations: ", removed_observations_2)

#For the following steps, we will use the updated dataset produced in this step.
titanic_data = shortened_titanic_data
#print(titanic_data)

# PART 4
#Standard deviation, MEAN of "fare"
#print(titanic_data['fare'])

print("Step 4 mean: ", titanic_data['fare'].mean())
print("Step 4 Std: ", titanic_data['fare'].std())

standard_deviation = titanic_data['fare'].std()
mean = titanic_data['fare'].mean()

#GRAPH BEFORE
plt.hist(titanic_data['fare'], density=True, bins=30)
plt.ylabel('Probability')
plt.xlabel('Fare')
plt.show()

titanic_data.boxplot(column=['fare'])
plt.show()

#print(titanic_data['fare'])

#Filters
filtered_titanic_data = titanic_data.loc[~(titanic_data['fare'] > mean + 2*standard_deviation)]
filtered_titanic_data = filtered_titanic_data.loc[~(filtered_titanic_data['fare'] < mean - 2*standard_deviation)]

#print("Step 4 end filter ",filtered_titanic_data['fare'])
#GRAPH AFTER
plt.hist(filtered_titanic_data['fare'], density=True, bins=30)
plt.ylabel('Probability')
plt.xlabel('Fare')
plt.show()

filtered_titanic_data.boxplot(column=['fare'])
plt.show()

# PART 5

#FINDS QUARTILES
Q1 = titanic_data['fare'].quantile(0.25)
Q3 = titanic_data['fare'].quantile(0.75)
IQR = Q3 - Q1

print("FARE IQR: ", IQR)
age_Q1 = titanic_data['age'].quantile(0.25)
age_Q3 = titanic_data['age'].quantile(0.75)
age_IQR = age_Q3 - age_Q1
print("age IQR: ", age_IQR)

#print("Q3: ", Q3)
#print("Q1: ", Q1)
#print("IQR: ", IQR)

#FINDS BOUNDS
lower_bound = Q1 - (1.5 * IQR)
upper_bound = Q3 + (1.5 * IQR)

age_lower_bound = age_Q1 - (1.5 * age_IQR)
age_upper_bound = age_Q1 + (1.5 * age_IQR)

#FILTERS
#STEP 4 FILTERS RE-APPLIED
removed_outliers_titanic_data = titanic_data.loc[~(titanic_data['fare'] > mean + 2*standard_deviation)]
removed_outliers_titanic_data = removed_outliers_titanic_data.loc[~(removed_outliers_titanic_data['fare'] < mean - 2*standard_deviation)]

# REMOVE OUTLIERS for "fare" and "age"
removed_outliers_titanic_data = removed_outliers_titanic_data.loc[~(removed_outliers_titanic_data['fare'] > upper_bound)]
removed_outliers_titanic_data = removed_outliers_titanic_data.loc[~(removed_outliers_titanic_data['fare'] < lower_bound)]

removed_outliers_titanic_data = removed_outliers_titanic_data.loc[~(removed_outliers_titanic_data['age'] > age_upper_bound)]
removed_outliers_titanic_data = removed_outliers_titanic_data.loc[~(removed_outliers_titanic_data['age'] < age_lower_bound)]

# print("upper_bound: ", upper_bound, " lower: ", lower_bound)
#print("step 5: ", removed_outliers_titanic_data['fare'])

# GRAPHS
plt.hist(removed_outliers_titanic_data ['fare'], density=True, bins=30)
plt.ylabel('Probability')
plt.xlabel('Fare')
plt.show()

removed_outliers_titanic_data.boxplot(column=['fare'])
plt.show()

plt.hist(removed_outliers_titanic_data ['age'], density=True, bins=30)
plt.ylabel('Probability')
plt.xlabel('Age')
plt.show()

removed_outliers_titanic_data.boxplot(column=['age'])
plt.show()