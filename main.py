'''
basics

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

# histogram - dont need as much


# data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6]

# plt.hist(data, bins=5)  # Create a histogram with 5 bins
# plt.title('Histogram')
# plt.show()


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

'''


##
##

# # creates a real time changing sin graph

# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
# import numpy as np

# # Set up the figure and axis
# fig, ax = plt.subplots()
# '''
# fig: The figure object, which is the overall container for the plot. Think of this as the "canvas" where the plot will be drawn.
# ax: Represents the axes or the plot itself, where the graph is drawn (including the coordinate system, labels, and grid).
# plt.subplots(): Creates both the figure and axes in one call. This is a common way to set up your plotting area.

# '''
# x = np.linspace(0, 2 * np.pi, 100)
# y = np.sin(x)

# '''
# np.linspace(0, 2 * np.pi, 100): Generates 100 equally spaced points between 0 and 2π. This array of values is assigned to x.
# np.sin(x): Takes the sine of each x value, creating an array of corresponding y values. This is used to plot a basic sine wave.
# '''

# line, = ax.plot(x, y)

# '''
# ax.plot(x, y): Plots the x and y data on the axes (ax). Initially, this draws the static sine wave on the figure.
# line, = ...: The plot() function returns a list of Line2D objects, even if there’s only one line. The line, = syntax unpacks the first (and only) line object into the line variable, which we will use to update the plot later. The comma is needed to handle the single object in the returned list.

# '''

# # Function to update the line in real time
# def update(frame):
#     line.set_ydata(np.sin(x + frame / 10.0))  # Update y-data with time shift
#     return line,
# '''
# This is the function that will be called repeatedly to update the plot:

# frame: This is the current "frame" number, provided automatically by the animation framework. It's essentially the time step in the animation.
# np.sin(x + frame / 10.0): The x values remain constant, but the y values (the sine wave) are shifted slightly at each frame. By adding frame / 10.0 to x, the sine wave shifts to the left or right over time, creating the animation effect.
# line.set_ydata(): This method updates the y values of the line on the plot. Here, you update it with the new sine wave values shifted by frame / 10.0.
#  '''

# # Create the animation, updating every 100 ms
# ani = animation.FuncAnimation(fig, update, frames=range(100), interval=100)
# '''
# animation.FuncAnimation: This is the function that handles the animation. It repeatedly calls the update function and redraws the plot with new data at each frame.
# fig: The figure object that holds the plot to animate.
# update: The function that is called on each frame to update the plot.
# frames=range(100): This specifies the number of frames in the animation. Here, it goes from frame 0 to 99 (100 frames in total). The frame number is passed as an argument to the update function.
# interval=100: The delay between frames in milliseconds. In this case, the plot will be updated every 100 milliseconds (10 updates per second).

# just doing frames = 100 also works
# '''

# plt.show()


import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

x_labels = ['flower', 'feather', 'sands', 'goblet', 'circlet']
#x_labels: The labels for the x-axis represent your five artifact types: 'Flower', 'Feather', 'Sands', 'Goblet', and 'Circlet'.


x = np.arange(len(x_labels)) # This will be [0,1,2,3,4]

#x = np.arange(len(x_labels)): This creates an array [0, 1, 2, 3, 4], which is the position of each category on the x-axis.

# Create initial random y values for each category
y = np.random.randint(1,10, size = len(x_labels))

#Initial y values: We create random initial y values (between 1 and 10) for the bar heights.


# Set up the figure and axis
fig,ax = plt.subplots()

# Initialize the bar plot
bars = ax.bar(x,y)

#Initialize the bar plot: This creates the bar chart for the x and y values, and the bars object holds the individual bar patches so that they can be updated later.


# Set the x-axis with artifact names

ax.set_xticks(x)
ax.set_xticklabels(x_labels)

# Set axis labels
ax.set_xlabel('Artifact')
ax.set_ylabel('Random Value')
ax.set_title('Real-Time Bar Graph of Artifacts')

def update(frame):
    new_y = np.random.randint(0,10, size = len(x_labels))

    for bar, height in zip(bars, new_y):
        bar.set_height(height)

    return bars

ani = animation.FuncAnimation(fig, update, frames = range(100), interval = 500)
plt.show()