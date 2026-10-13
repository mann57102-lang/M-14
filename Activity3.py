# ================================
#  INTRODUCTION TO MATPLOTLIB
# ================================

# ================================================
#  ACTIVITY - MY MONTHLY EXERCISE TRACKER
#  File: exercise-tracker.py
# ================================================

# PART 1 - IMPORT MATPLOTLIB
import matplotlib.pyplot as plt

# PART 2 - YOUR DATA
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
hours = [10, 15, 8, 20, 25]

# PART 3 - PLOT YOUR FIRST LINE GRAPH
plt.plot(months, hours)
plt.show()

# PART 4 - ADD LABELS AND A TITLE
plt.plot(months, hours)
plt.title('My Monthly Exercise Tracker')
plt.xlabel('Month')
plt.ylabel('Exercise Hours')
plt.grid(True)
plt.ylim(0, 30)
plt.show()

# PART 5 - STYLE YOUR LINE CHART
plt.plot(
    months,
    hours,
    color='green',
    marker='o',
    linestyle='dashed',
    linewidth=2
)
plt.title('My Monthly Exercise Tracker')
plt.xlabel('Month')
plt.ylabel('Exercise Hours')
plt.grid(True)
plt.ylim(0, 30)
plt.show()

# PART 6 - DRAW A BAR CHART
plt.bar(months, hours, color='purple')
plt.title('My Monthly Exercise Bar Chart')
plt.xlabel('Month')
plt.ylabel('Exercise Hours')
plt.ylim(0, 30)
plt.show()
