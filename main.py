import matplotlib.pyplot as plt
import random

# Data for plotting
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# # Create a plot
# plt.plot(x, y, color='red', linestyle='None', marker='o')  # Red dashed line with circle markers

# # Adding labels and title
# plt.xlabel('Resin used')
# plt.ylabel('Crit Value')
# plt.title('Basic Line Graph')



# Show the plot
#plt.show()


# scatter plot
# plt.scatter(x, y)  # Create a scatter plot
# plt.title('Scatter Plot')
# plt.show()

# bar graph

# make sure the categories and the values have the same number of args
# categories = ['Flower', 'Feather', 'Sands', 'Goblet', 'Circlet'] 
# values = [random.randint(0,55), random.randint(0,55), random.randint(0,55), random.randint(0,55), random.randint(0,55)]

# plt.bar(categories, values)  # Create a bar plot
# plt.title('Bar Plot')
# plt.show()

# histogram
'''

data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6]

plt.hist(data, bins=5)  # Create a histogram with 5 bins
plt.title('Histogram')
plt.show()
'''

# pie chart
# labels = ['A', 'B', 'C', 'D']
# sizes = [20, 30, 25, 25]

# plt.pie(sizes, labels=labels, autopct='%1.1f%%')  # Create a pie chart with percentages
# plt.title('Pie Chart')
# plt.show()

# create mutiple plots at once


# Create a 1x2 grid of subplots
# fig, axs = plt.subplots(1, 2)

# # First subplot
# axs[0].plot([1, 2, 3], [1, 4, 9])
# axs[0].set_title('Line Plot')

# # Second subplot
# axs[1].bar(['A', 'B', 'C'], [5, 7, 3])
# axs[1].set_title('Bar Plot')

# plt.show()



x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [1, 2, 3, 4, 5]

plt.plot(x, y1, label='Quadratic')  # Line with label
plt.plot(x, y2, label='Linear')  # Another line with label
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot with Legend')
plt.legend()  # Show the legend
plt.show()
plt.plot(x, y)
# can save the plot
#plt.savefig('plot.png')  # Save the plot as a PNG file
plt.show()
