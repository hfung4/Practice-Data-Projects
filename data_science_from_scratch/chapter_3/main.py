''' Chapter 3: Data visualization
- Tutorial on data exploration using data visualization (matplotlib)
'''
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
'''
Pycharm has a shortkey:  ALT-SHFIT-E that allows you to copy and paste selected lines to the Python Console

Use CTRL-R to run the entire project
Use CRTL-D to run the entire project in debug mode

Use CRTL-SHIFT-R to run ONLY main.py
Use CRTL-SHIFT-D to run ONLY main.py in debug mode
'''

from matplotlib import pyplot as plt
from collections import Counter

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # line plot using matplotlib
    years=[1950,1960,1970,1980,1990,2000,2010]
    gdp=[300.2,543.3,1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

    # create a line chart: years on the x-axis, and gdp on y-axis
    plt.plot(years,gdp,
             color='green',
             marker='o',
             linestyle='solid')
    # add a title
    plt.title("Nominal GDP")
    # add y-axis label
    plt.ylabel('Billions of $')
    plt.show()

    # bar charts ----------------------------------------------
    # useful to show how some quantity varies among some discrete set of tiems
    # For example, let's say we want to visualize the number of academy awards won by a
    # set of movies

    movies=["Annie Hall","Ben-Hur","Casablanca","Gandhi","West Side Story"]
    num_oscars=[5,11,3,8,10]

    # bar plots with movies as x-axis and number of oscars as y-axis
    plt.bar(range(len(movies)), num_oscars)  #range(len(movies)) is range(0,5)
    plt.title("My Favorite Movies") # add a title
    plt.ylabel("# of Academy Awards") # add y-axis labels
    # instead of 1,2,3...5, label x-ticks with movie names
    plt.xticks(range(len(movies)),movies)
    plt.show()


    # Histogram ------------------------------------------------------------------

    # A bar chart can be useful in visualizing the probability distribution of a discrete RV
    marks = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
    # bucket grades by decile (count frequency of observations with 0-9, 10-19, 20-29,...
    # but inlcude 100 in the 90-99 category
    # note: // operator is called "floor division".  I divide x by y and then remove all
    # decimal numbers.  For example, 10//3=3
    temp=[mark//10 * 10 for mark in marks] # this operation floors each mark
    min(90,100) # 90
    # This operation floors each mark to the nearest 10, 20, ....90.  If the mark is 100, then
    # it is floored to 90 (that's what the min(...,90) does.
    temp=[min(mark//10*10,90) for mark in marks]
    temp

    d_mark=Counter(temp) # count the number of values that are 80, that are 90, that are 70 ...
    d_mark

    # I can condense the code to the following to get d_mark
    d_mark=Counter(min(mark//10*10,90)for mark in marks)

    # create bar plot from the d_mark dictionary.  The key is the levels and
    # the value is the frequency of the level.

    lvls=[x for x in d_mark.keys()] # [80,90,70,0,60]
    lvls

    # shift bars to the right by 5
    lvls=[x+5 for x in d_mark.keys()] # [85,95,75,5,65]
    lvls

    plt.bar(lvls, # lvls in the x axis. For 80-89 level, I center the bar at 85
            d_mark.values(), # frequency of each level
            10, # set width of bar
            edgecolor='black') # black edges for each bar

    # set x-axis range from -5 to 105, and y axis range from 0 to 5
    plt.axis([-5,105,0,5])

    # set x-ticks
    plt.xticks([10*i for i in range(11)]) # 0,10,20,...100
    # set xlabel
    plt.xlabel("Decile")
    # set ylabel
    plt.ylabel("# of Students")
    # set plot title
    plt.title("Distribution of Exam 1 Grades")
    plt.show()

    # histogram condense code ------------------------------------------

    plt.bar([x+5 for x in d_mark.keys()],  # lvls in the x axis. For 80-89 level, I center the bar at 85
            d_mark.values(),  # frequency of each level
            10,  # set width of bar
            edgecolor='black')  # black edges for each bar

    # set x-axis range from -5 to 105, and y axis range from 0 to 5
    plt.axis([-5, 105, 0, 5])
    # set x-ticks
    plt.xticks([10 * i for i in range(11)])  # 0,10,20,...100
    # set xlabel
    plt.xlabel("Decile")
    # set ylabel
    plt.ylabel("# of Students")
    # set plot title
    plt.title("Distribution of Exam 1 Grades")
    plt.show()





