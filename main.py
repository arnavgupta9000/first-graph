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
'''
Why this is necessary:
Bar plots expect numeric positions** on the x-axis (e.g., 0, 1, 2, etc.), but your actual labels (like 'Flower', 'Feather') are categorical (non-numeric).
So, x = np.arange(len(x_labels)) provides the numeric positions [0, 1, 2, 3, 4] that correspond to each category in x_labels. This array x is used to determine where to place each bar.

'''
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
'''
ax.set_xticks(x)
Purpose: This sets the positions of the ticks on the x-axis.
How it works:
x = [0, 1, 2, 3, 4] are the numeric positions where we want the ticks (i.e., where the bars are drawn).
ax.set_xticks(x) tells Matplotlib, "Put the tick marks at these positions on the x-axis."
Without set_xticks(x), the bars may be drawn, but the x-axis wouldn't know where to place the tick marks for each bar.
ie it would mess up where the artifacts are supposed to be on the x-axis
'''
ax.set_xticklabels(x_labels)
'''
ax.set_xticklabels(x_labels)
Purpose: This replaces the numeric ticks with category names (your artifact types).
How it works:
x_labels = ['Flower', 'Feather', 'Sands', 'Goblet', 'Circlet'] are your categorical names.
ax.set_xticklabels(x_labels) tells Matplotlib, "Replace the tick numbers (0, 1, 2, etc.) with these labels."
without this no x-values will show up (this just replaced the [0,1,2,3,4] with acc values)
'''

#set_xticks() and set_xticklabels(): These two lines make sure that the x-axis has the proper labels (Flower, Feather, etc.).



# Set axis labels
ax.set_xlabel('Artifact')
ax.set_ylabel('Random Value')
ax.set_title('Real-Time Bar Graph of Artifacts')

def update(frame): # frame must be a parameter
    # bars holds the references to all the bars
    new_y = np.random.randint(0,10, size = len(x_labels)) 
    # print(bars[0] -> Rectangle(xy=(-0.4, 0), width=0.8, height=7, angle=0)
    for bar, height in zip(bars, new_y): #->(bar1, height1), (bar2, height2), (bar3, height3), (bar4, height4), (bar5, height5)
        bar.set_height(height) # bar.set_height is a method from matlib that well sets the height of a single bar

    return bars # with FuncAnimation the thing we updated must be returned

#The update() function: This is called on each frame by FuncAnimation to update the bar heights.

# new_y: Generates new random y values for each of the five artifact types.
# bar.set_height(): Updates the height of each individual bar with the new y value

ani = animation.FuncAnimation(fig, update, frames = range(100), interval = 500)
plt.show()

# why was the code so diff between these 2?
'''
1.type of plots are different
2. Line Plot (line.set_ydata()) vs. Bar Plot (bar.set_height())
Sine Graph:

The line plot updates by changing the y values for all x positions at once. This is done with the method line.set_ydata() in the update() function.
Since it's one continuous line, we only need to change the y-values across the entire x-axis.

Bar Graph:

The bar plot updates by changing the height of each bar individually. This is done with bar.set_height() for each bar in the update() function.
Bars are individual elements, and each one needs to be updated separately. Therefore, a for loop is used to iterate over the bars and update each bar's height based on the new y values.

3. Initialization Differences
Sine Graph:

For a sine wave, you define the x and y arrays (np.linspace and np.sin). These arrays represent the continuous line plot, and the ax.plot() creates a line object that can be updated.
Bar Graph:

For a bar plot, you define categorical x values (like 'Flower', 'Feather', etc.) and assign random y values initially. The ax.bar() function creates the bars on the plot. You need to handle each bar individually, as bars are not continuous like a line plot.

4.
Sine Graph:

Since we are updating a continuous line, you just change the y-values using a mathematical function (in this case, the sine function). You don't need to iterate over multiple objects because the line is treated as one object.

Bar Graph:

You need to update each bar's height individually. Since the bars are individual elements, you loop through the bars and apply new heights to each one.

5. X-Axis Setup
Sine Graph:

The x-axis is continuous and numerical (from 0 to 2π), and Matplotlib automatically handles the axis ticks and labels.

Bar Graph:

The x-axis uses categorical labels (artifacts like 'Flower', 'Feather', etc.), so you need to manually set the tick positions and labels using ax.set_xticks() and ax.set_xticklabels().

6. Initial Plotting
Sine Graph:
You create a single Line2D object (the line plot) and store it in a variable (line, = ax.plot(x, y)).
Bar Graph:
You create multiple Rectangle objects (bars) and store them as a list in the bars variable (bars = ax.bar(x, y)).

Summary of Key Differences:
Sine Graph: Simple line plot that updates by shifting the y values of a single line.
Bar Graph: Requires updating the height of each bar individually, which means looping over multiple objects (the bars).
Categorical vs. Numerical X-Axis: The sine wave uses a continuous numerical x-axis, while the bar chart uses categorical labels, requiring different setup for the x-axis.

'''
