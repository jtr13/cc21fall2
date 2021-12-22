#!/usr/bin/env python
# coding: utf-8

# Zixiang Tang zt2292 & Chenxi Jiang cj2706

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# ### Tutorial On Commonly Used Plots
# 

# Load Dataset Index Crimes by County and Agency: Beginning 1990

# In[3]:


df = pd.read_csv("https://data.ny.gov/api/views/ca8h-8gjq/rows.csv")
df.head(5) # show first 5 rows 


# ### Useful Functions

# #### Groupby
# Group by a column and apply a function to the rest of columns
# 
# DataFrame.groupby(by=None, axis=0, level=None, as_index=True, sort=True, group_keys=True, squeeze=NoDefault.no_default, observed=False, dropna=True)
# 
# Often uses
# by = label or list of labels
# 
# Follow by a function (such as sum, mean, etc.)
# 
# 
# 
# 
# 

# In[4]:


df_group = df.groupby(by=['Year'],dropna=True).sum() # group by year, sum up number in rest columns
df_group.reset_index(level=0, inplace=True)
df_group


# group_by is very useful in processing data. It is commonly used to group a column and apply a function to the rest column. For example, in this dataset, to find the crime number each year, use group_by to group Year column and apply sum to the rest to find the crime number each year. 

# #### Filter Rows by a specific condition

# In[5]:


df2=df[df['Year']==2000] # filter all crime taken place in 2000
df2.head(5)


# #### Select Columns by names

# In[6]:


df2 = df[['County','Rape','Larceny','Burglary','Murder']]
df2.head(5)


# ### Plot

# #### 1. Line plot
# matplotlib.pyplot.plot(*args, scalex=True, scaley=True, data=None, **kwargs)
# 
# Parameters: y vs x
# 
# x:float or array-like, x coordinates of plot
# 
# y:float or array-like, y coordinates of plot
# 
# Read more on Matplotlib https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html

# In[7]:


plt.plot(df_group['Year'],df_group['Murder'])
plt.title("Murder Number from 1990 to 2020")
plt.xlabel('Year')
plt.ylabel('Count')
plt.show()


# 2. Scatter Plot
# 
# matplotlib.pyplot.scatter(x, y, s=None, c=None, marker=None, cmap=None, norm=None, vmin=None, vmax=None, alpha=None, linewidths=None, *, edgecolors=None, plotnonfinite=False, data=None, **kwargs)
# 
# Parameters: y vs x
# 
# x:float or array-like, x coordinates of plot
# 
# y:float or array-like, y coordinates of plot
# 
# Read more on Matplotlib https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html

# In[8]:


plt.scatter(df_group['Year'],df_group['Murder'])
plt.title("Murder Number from 1990 to 2020")
plt.xlabel('Year')
plt.ylabel('Count')
plt.show()


# We can see the line plot can indicate the amount of the quantity and clearly shows the situation of the increase or decrease of the quantity. 
# Scatter plot reflects the change pattern of the relationship between variables, which is convenient for deciding which mathematical expression to use to simulate the relationship between variables.
# Also, scatter plot can transfer the type of relationship between variables Information and the degree of clarity of the relationship between the reflected variables.
# When we specificly look at the scatter plot for the relationship of year vs. Count. We cannot easily get they are in a linear relationship, but we can conclude they crime count is descending obviously.
# However, when we look at the line plot, we can observe the distinct decreasing murder in around 1993 to 1998 and 2005 to 2008. From this information, we can explain this situation by aspect of change of politics, economy, or culture. 

# 3. Bar plot
# 
# matplotlib.pyplot.plot(*args, scalex=True, scaley=True, data=None, **kwargs)
# 
# Parameters: 
# 
# x:float or array-like, x coordinates of plot
# 
# y:float or array-like, height of the bar
# 
# Read more on Matplotlib https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html

# In[9]:


plt.bar(df_group['Year'],df_group['Murder'])
plt.title("Murder Number from 1990 to 2020")
plt.xlabel('Year')
plt.ylabel('Count')
plt.show()


# In[10]:


plt.barh(df_group['Year'],df_group['Murder'])
plt.title("Murder Number from 1990 to 2020")
plt.xlabel('Count')
plt.ylabel('Year')
plt.show()


# Bar plot is generally used to describe categorical variables. Here, the variable of the horizontal axis is the year, and the variable of the vertical axis is the count of Murder number. An interval of the Bar plot represents a categorical variable, and the interval does not need to be next to each other. Because they are parallel to each other, there is no comparison of size. Bar plot displays the relative numbers or proportions of multiple categories and summarize a large data set in visual form.

#   Stacked Bar Plot
#   
#   Stacked Bar Plot is commonly used to compare categories distribution within each type ploted across x coordinates. The plot below shows three crimes distribution each year. 

# In[11]:


df_group.plot.bar(x='Year',y=['Robbery','Murder','Rape'],stacked=True)
plt.show()


# 4. Histogram
# 
# matplotlib.pyplot.hist(x, bins=None, range=None, density=False, weights=None, cumulative=False, bottom=None, histtype='bar', align='mid', orientation='vertical', rwidth=None, log=False, color=None, label=None, stacked=False, *, data=None, **kwargs)
# 
# Parameters: 
# 
# x: array or sequence
# 
# bins: can be assigned or use default
# 
# Read more on Matplotlib https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html

# In[12]:


plt.hist(df['Year'],bins=15, alpha=0.5)
plt.title("Year Distribution")
plt.xlabel('Year')
plt.ylabel('Count')
plt.show()


# Histogram is generally used to describe numerical variables. The horizontal axis of Histogram uses bins to divide the variables into a specific interval. Here, year is used as the variable, separated by a length of five years, so the length of a bin is 5, so each interval in the Histogram is next to each other, and each interval can be compared. Like Bar plot, the vertical axis of Histogram also represents the number of variables.
# Histograms are usually used to present the distribution of variables. Here, the histogram is used to present the year distribution of murder number.
# 

# 5. Box Plot
# 
# matplotlib.pyplot.boxplot(x, notch=None, sym=None, vert=None, whis=None, positions=None, widths=None, patch_artist=None, bootstrap=None, usermedians=None, conf_intervals=None, meanline=None, showmeans=None, showcaps=None, showbox=None, showfliers=None, boxprops=None, labels=None, flierprops=None, medianprops=None, meanprops=None, capprops=None, whiskerprops=None, manage_ticks=True, autorange=False, zorder=None, *, data=None)
# 
# Parameters: 
# 
# x: array or sequence
# 
# Read more on Matplotlib https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.boxplot.html

# In[13]:


plt.boxplot(df_group['Murder'])
plt.xlabel('Murder')
plt.ylabel('Number')
plt.title('Murder each year distribution')
plt.show()


# Using box plots makes it easy for us to investigate multiple continuous variables at the same time, or to investigate a single continuous variable in groups, so it is more flexible in use than histograms and has a wider range of uses. The box plot can tell us the value of: Lower limit, Lower Quartile, Median, Upper Quartile, Upper limit, Mild Outlier and Extreme Outlier. 
# Box plot can summarize variation in large datasets visually, show outliers, compares multiple distributions, Indicate symmetry and skewness to a degree.
# 

# 6. Violin Plot
# 
# Axes.violinplot(dataset, positions=None, vert=True, widths=0.5, showmeans=False, showextrema=True, showmedians=False, quantiles=None, points=100, bw_method=None, *, data=None)
# 
# Parameters: 
# 
# x: array or sequence
# 
# Read more on Matplotlib https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.violinplot.html#matplotlib.axes.Axes.violinplot

# In[14]:


plt.violinplot(df_group['Murder'])
plt.xlabel('Murder')
plt.ylabel('Number')
plt.title('Murder each year distribution')
plt.show()


# The violin chart is a combination of the box plot and the density distribution. Similar to box plots, expect that they also show the probability density of the data at different values, usually smoothed by a kernel density estimator. The probability density of the data is expressed by the width of the violin. From the figure, the violin plot reflects the dispersion density more clearly than the box plot. We can see the distribution of Murder number in each interval, this figure shows that most of the Murder number is distributed in the interval of 1000-2000 each year, which means that the probability of data distribution in this interval is the greatest.

# 6. Pie chart
# 
# matplotlib.pyplot.pie(x, explode=None, labels=None, colors=None, autopct=None, pctdistance=0.6, shadow=False, labeldistance=1.1, startangle=0, radius=1, counterclock=True, wedgeprops=None, textprops=None, center=(0, 0), frame=False, rotatelabels=False, *, normalize=None, data=None)
# 
# x: an array or sequence
# 
# Read more on Matplotlib https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pie.html

# In[15]:


df_pie = df_group.head(11)
plt.pie(df_pie['Murder'],labels = df_pie['Year'],autopct='%1.1f%%')
plt.axis('equal')
plt.title('Murder Percent from 1990 to 2000 ')
plt.show()


# 
# Pie chart reflects the related parts of different data groups or categories. It shows users what a fraction looks like in a good visual representation of different data sets. It should be used for showing the relationship between partial and overall elements, the pie chart is used here to show the distribution of Murder percent from 1990 to 2000, this allows users to clearly show the percentage of Murder number in each year, allowing users to compare the annual data more easily.
# The advantage of using pie chart is that it can display relative proportions of multiple classes of data, summarize a large data set in visual form and the size of the circle can be made proportional to the total quantity it represents.
# 

# 7. Area plot
# 
# DataFrame.plot.area(x=None, y=None, **kwargs)
# 
# Parameters: 
# 
# x:floats or array-like, x coordinates of plot
# 
# y:floats or array-like, y coordinates of plot
# 
# Read more on pandas https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.area.html

# For this time, we need to compare three different crimes in New York.

# In[16]:


df_group1=df_group[["Murder","Rape","Robbery","Aggravated Assault"]]
df_group1.plot.area()
plt.title('Four different crimes in New York ')
plt.show()


# If you would like to do an overlapping, you can specify (stacked=False)

# In[17]:


df_group1.plot.area(stacked=False);
plt.title('Four different crimes in New York ')
plt.show()


# Even though they looks little similar, to ditinguish them, we create a new random datafram to watch the difference.

# In[18]:


df_new= pd.DataFrame(np.random.rand(20, 4), columns=["a", "b", "c","d"])
df_new.plot.area()
plt.title('Area plot withOUT overlapping ')
plt.show()


# In[19]:


df_new.plot.area(stacked=False)
plt.title('Area plot with overlapping ')
plt.show()


# Area plot represents the distribution of the quantitative data, While the example above only plots a single line with shaded area, an area chart is typically used with multiple lines to make a comparison between groups (aka series) or to show how a whole is divided into component parts. There are two different types of area chart: the stacked area chart and the overlapping area chart.
# The stacked area chart is a part of the area graph where it demonstrates the behavior of multiple groups in a single chart. In the overlapping area chart, each line was shaded from its vertical value to a common baseline. In the stacked area chart, lines are plotted one at a time, with the height of the most recently plotted group serving as a moving baseline. Here, crimes in New York are classified into three categories: Robbery, Rape, Murder and Aggravated Assault, which are represented by green, yellow, blue, and red respectively.
# In the case that we want to compare the values between groups, we end up with an overlapping area chart. We can see most of the space occupied by the green and red areas, and they represent Robbery and Aggravated Assault respectively. This represents that most of the crimes that occurred in New York were classified as Robbery and Aggravated Assault. The blue area is the smallest area in the plot, which means that murder type crimes occur less frequently than other types of crimes.

# 8. Hexagonal bin
# 
# DataFrame.plot.hexbin(x, y, C=None, reduce_C_function=None, gridsize=None, **kwargs)
# 
# Parameters:
# 
# x:floats or array-like, x coordinates of plot
# 
# y:floats or array-like, y coordinates of plot
# 
# Read more on pandas https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.hexbin.html

# In[20]:


df_group2=df_group[["Murder","Aggravated Assault"]]
df_group2.plot.hexbin(x="Murder", y="Aggravated Assault", gridsize=25);
plt.show()


# 9. Parallel Coordinates
# 
# pandas.plotting.parallel_coordinates(frame, class_column, cols=None, ax=None, color=None, use_columns=False, xticks=None, colormap=None, axvlines=True, axvlines_kwds=None, sort_labels=False, **kwargs)
# 
# Parameters:
# 
# frame: Data Frame for plotting
# class_column: Column name, one line for each class
# 
# Read more on pandas https://pandas.pydata.org/docs/reference/api/pandas.plotting.parallel_coordinates.html

# Parallel Coordinates plot is used to observe trend among the classes plotted. It is especially useful for observing relationship and outliers. 

# In[21]:


df2= df2.groupby(by=['County']).sum() # group by county sum the rest
df2.reset_index(level=0, inplace=True)
plt.figure(figsize=(18,20))
pd.plotting.parallel_coordinates(df2, 'County')
plt.show()


# 10. Scatter Matrix
# 
# pandas.plotting.scatter_matrix(frame, alpha=0.5, figsize=None, ax=None, grid=False, diagonal='hist', marker='.', density_kwds=None, hist_kwds=None, range_padding=0.05, **kwargs)
# 
# Parameters:
# 
# frame: data frame
# 
# Read more on pandas https://pandas.pydata.org/docs/reference/api/pandas.plotting.scatter_matrix.html

# Scatter Matrix is a plot that is good at comparing each pair of column features in the dataframe. This plots show a pairwise relationship in a matrix.

# In[22]:


from pandas.plotting import scatter_matrix
scatter_matrix(df2,alpha=0.8,figsize=(10,10))
plt.show()


# 11. Mosaic Plot
# 
# statsmodels.graphics.mosaicplot.mosaic(data, index=None, ax=None, horizontal=True, gap=0.005, properties=<function <lambda>>, labelizer=None, title='', statistic=False, axes_label=True, label_rotation=0.0)
#     
# Parameters:
#     
# frame: Data Frame
#  
# Columns: an array, columns for splitting
#     
# Read more on https://www.statsmodels.org/dev/generated/statsmodels.graphics.mosaicplot.mosaic.html

# Mosaic plot is a tool to visualize whether there's a relationship among the target variables. 

# In[23]:


from statsmodels.graphics.mosaicplot import mosaic
dfm=df[df['Year']==2000] #select year 2000 data
dfmo = dfm.head(50) # choose first 50 rows
mosaic(dfmo,['Region','County'])
plt.show()


# #### Multiple plots in one figure
# 
# Sometimes multiple plots side by side may provide a better visualization
# 

# 1. Using Subplot
# 
# Subplot can be used for plots arranged in a matrix

# In[24]:


plt.figure(figsize=(18,12))
for i in range(6):
    plt.subplot(2,3,i+1)
    plt.scatter(df_group['Year'],df_group['Murder'])
    plt.title("Murder Number from 1990 to 2020")
    plt.xlabel('Year')
    plt.ylabel('Count')


# 2. Multiple plots storing in a dictionary
# 
# Same kind of plot using a common x and y axis plot in one figure. This type of plot can be done by storing data in a dictionary. The plot below is a multiple boxplots in one figure, other types of plots can also be plotted in this way, for example violin plot. 

# In[25]:


box = {}
box['Murder'] = df_group['Murder']
box['Rape'] = df_group['Rape']
box['Robbery'] = df_group['Robbery'] 
fig, ax = plt.subplots(figsize=(12,4))
ax.boxplot(box.values())
ax.set_xticklabels(box.keys())
ax.set_xlabel('Crime Type')
ax.set_ylabel('Count')
ax.set_title('3 Types Crime Number Per Year Distribution')
plt.show()

