# ============================================================
# Seaborn Library in Python
# Activity: World Sports Explorer
# ============================================================

import seaborn as sns
import matplotlib.pyplot as plt

# ---- PART 1: Import and Load Data ----

df = sns.load_dataset('exercise')
df = df.dropna()

print("First 5 rows:")
print(df.head())
print()
print(df.info())
print()
print(df.describe())
print()
print("Exercises:", df['kind'].unique())
print("Diet types:", df['diet'].unique())


# ---- PART 2: Histogram ----

sns.histplot(data=df, x='pulse', bins=20, color='steelblue')
plt.title('Distribution of Pulse Rates')
plt.xlabel('Pulse Rate')
plt.ylabel('Count')
plt.show()


# ---- PART 3: KDE Plot and Fitting Distribution ----

sns.kdeplot(data=df, x='pulse', hue='kind', fill=True)
plt.title('Pulse Rate Distribution by Exercise Type (KDE)')
plt.xlabel('Pulse Rate')
plt.show()

sns.histplot(data=df, x='pulse', kde=True, color='coral')
plt.title('Pulse Rate — Histogram with KDE Curve')
plt.xlabel('Pulse Rate')
plt.ylabel('Count')
plt.show()


# ---- PART 4: Scatter Plot ----

sns.scatterplot(data=df, x='pulse', y='time', hue='kind')
plt.title('Pulse Rate vs Exercise Time')
plt.xlabel('Pulse Rate')
plt.ylabel('Exercise Time')
plt.show()


# ---- PART 5: Heatmap ----

corr = df.corr(numeric_only=True)
print("Correlation table:")
print(corr)
print()

sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap — Exercise Data')
plt.show()
