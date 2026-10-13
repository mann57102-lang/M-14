# ============================================================
# Advanced Visualizations in Python
# Activity: Student Performance Explorer
# ============================================================

import seaborn as sns
import matplotlib.pyplot as plt

# ---- PART 1: Bar Plot and Count Plot ----

df = sns.load_dataset('titanic')
df = df.dropna(subset=['age', 'fare', 'sex', 'class', 'survived'])

print(df.head())
print(df.info())

sns.barplot(x='class', y='fare', hue='sex', data=df)
plt.title('Average Fare per Passenger Class by Gender')
plt.xlabel('Passenger Class')
plt.ylabel('Average Fare')
plt.show()

sns.countplot(x='class', hue='sex', data=df)
plt.title('Number of Passengers per Class by Gender')
plt.xlabel('Passenger Class')
plt.ylabel('Count')
plt.show()


# ---- PART 2: Box Plot, Strip Plot and Swarm Plot ----

sns.boxplot(x='class', y='age', data=df)
plt.title('Distribution of Passenger Age per Class')
plt.xlabel('Passenger Class')
plt.ylabel('Age')
plt.show()

sns.stripplot(x='class', y='age', data=df, jitter=True)
plt.title('Every Passenger Age per Class (Strip Plot)')
plt.xlabel('Passenger Class')
plt.ylabel('Age')
plt.show()

sns.swarmplot(x='class', y='age', data=df)
plt.title('Every Passenger Age per Class (Swarm Plot)')
plt.xlabel('Passenger Class')
plt.ylabel('Age')
plt.show()


# ---- PART 3: Joint Plot ----

sns.jointplot(x='age', y='fare', data=df)
plt.suptitle('Passenger Age vs Fare', y=1.02)
plt.show()

sns.jointplot(x='age', y='fare', data=df, kind='kde')
plt.suptitle('Passenger Age vs Fare — KDE Joint Plot', y=1.02)
plt.show()


# ---- PART 4: Pair Plot ----

sns.pairplot(df[['age', 'fare', 'survived']])
plt.suptitle('Pair Plot — Age, Fare and Survival', y=1.02)
plt.show()


# ---- PART 5: Point Plot and lmplot ----

sns.pointplot(x='class', y='fare', hue='sex', data=df)
plt.title('Average Fare per Passenger Class by Gender')
plt.xlabel('Passenger Class')
plt.ylabel('Average Fare')
plt.show()

sns.lmplot(x='age', y='fare', data=df)
plt.title('Passenger Age vs Fare — Trend Line')
plt.show()
