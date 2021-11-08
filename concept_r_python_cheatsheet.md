# draw graphs using python and R

Shuyue Xu


## things that need to be done before fitting models
##### check unique of the values
##### check null values, consider to drop values or adding a missing indicator
##### normalize numerical features
##### handle categorical feature using Label encoding or OneHotencoding or other...

<br/> 

## Continuous Variables
we always care about asymmetry, outliers, multimodality, gaps, heaping, errors
<br/> 

### Graphs that usually used for continuous Variables:
#### Histograms: R base code:hist(x, …)
##### different bin boundaries different graphs.
##### shape: 
               skew to left means mean < median < mode
               skew to right means mean > median > mode

#### Boxplot: R base code: boxplot(x, data=),       
##### multiple boxplots usually reorder by median from high to low
##### will show outliers on the graph. outliers are 
               1.5 x hinge or fourth spread above upper-hinge
               1.5 x hinge or fourth spread below lower-hinge<br/> 

### Ways to check normal distribution of the data
<br/> 

#### qqplot: check normal distribution 
             qqnorm(): produces a normal QQ plot of the variable
             qqline(): adds a reference line
##### If the data is normally distributed, the points in the QQ-normal plot lie on a straight diagonal line.
<br/> 

#### density curve line:
##### compare density curve line with normal curve line can also check normal distribution
<br/> 

#### Shapiro Wilk test: code:shapiro.test(x)
##### If the p-value is smaller than alpha level, we should reject the null hypothesis that data is normally distributed and make the conclusion that data is not normally distributed.
<br/> 

## Multivariate categorical data
#### nominal vs. ordinal, ordinal vs. discrete,...
<br/>
### Frequency
#### Bar plot Basic R code: barplot(x)
##### Sort in logical order of the categories (level1, level2, lever3..)(Ordinal data)
##### Sort from highest to lowest count (Nominal data)
<br/>

#### Cleveland dot plot 

#### R codes for factor data
##### don't use" "levels(x) =  ", only use "level(x)"
##### use "fct_reorder()" to assign new factor levels
##### use "fct_inorder()" to set level order to row order
##### use "fct_relevel()" to move levels to beginning to change the level order
##### use "fct_infreq()" to order the levels by decreasing frequency
##### use "fct_rev()" to reverse the order of factor levels 
##### use "fct_explicit_na()" to turn NAs into a real factor level
<br/>
###Proportion / Association 
#### Mosaic plots Code: mosaic(y~x)
##### check association between different variables
##### Chi Square Test: If the p-value is smaller than alpha level, we should reject the null hypothesis that two variables are independent and have the conclusion that they depend on each other.

#### Fluctation diagrams
<br/>

#### Tidy
##### Tidy data means 1 variable per column and 1 observation per row

## Find relations between two variables

#### Scatter Plot: Base R code: plot(x,y)
##### show gaps, clusters, outliers, boundaries, conditional relationships, associations
##### sometimes transform to log scale, square heatmap of bin counts, add density estimate contour lines

## Continuous Categorical Variables
#### parallel coordinates plot
##### df %>% parcoords(rownames = F, brushMode = '1D-axes',reorderable = TRUE,color = list(colorBy = 'Region',colorScale = "scaleOrdinal",colorScheme="schemeCategory10"),withD3 = TRUE,width = 1500,height = 800)

### Heatmaps
#### can be used for continuous or categorical data
#### show frequency counts (2D histogram) or value of a third variable

### Alluvial diagrams
#### shows flow of changes over time
#### color by first variable or color by last variable or 
#### different codes to plot alluvail diagram:
```
ggplot(df, aes(axis1, axis2, y = Freq)) +
  geom_alluvium(color = "blue") +
  geom_stratum() +
  geom_text(stat = "stratum", aes(label = paste(after_stat(stratum)))) 
```
##### or change data to lodes form first
```
dfl <- to_lodes_form(df, axes = 1:2)
ggplot(dfl, aes(alluvium = alluvium, x = x, stratum = stratum, y = Freq)) +
  geom_alluvium(color = "blue") +
  geom_stratum() +
  geom_text(stat = "stratum", aes(label = paste(after_stat(stratum))))
```

### some useful packages to plot in Python
```
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.pyplot import figure
```
### make plot in python
```
##scattler plot
plt.scatter(x,y,marker='o')
plt.ylabel()
plt.xlabel()
```
```
##histogram
plt.hist(x)
```
```
##pie chart
plt.pie(wf["Count"],labels = wf["Weak Foot"])
```
```
##boxplot
sns.boxplot(x=,y=)
```
```
##violin plot
sns.violinplot(x= ,y = )
```

```
##barplot
sns.barplot(x=, y=, data=)
```

```
##small multiple of bar plots
fig,axs = plt.subplots(3,1,figsize = (15,8))
sns.barplot(ax=axs[0],data=s1, x='workclass', hue='target', y='Count')
sns.barplot(ax=axs[1],data=s2, x='education', hue='target', y='Count')
sns.barplot(ax=axs[2],data=s3, x='sex', hue='target', y='Count')
```

```
##another way of small multiple of scatter plots
plt.subplot(3, 1, 1)
plt.scatter(auto_mpg_X['displacement'],auto_mpg_y )

plt.subplot(3,1,2)
plt.scatter(auto_mpg_X['horsepower'],auto_mpg_y )

plt.subplot(3,1,3)
plt.scatter(auto_mpg_X['weight'],auto_mpg_y )
```

```
## some codes to preprocess data
df.groupby()
df.dropna(subset=)
```




For this Cheat sheet, I reviewed all the slides again and collected the most important materials which I think may be used when we do EDA. I think these important materials would help students preparing their final exams and give them hints before they start fitting models on data. This Cheat sheet includes lots of different types of graphs which we can used to see distributions of our data first before future studies like classifications or predictions. Also, I add some explanations for the graphs and what information we can get from each graph. I think this can help students better analyze the graphs.<br/>
I add some basic codes to make plots in Python which gives examples for students who didn’t learn Python before. These codes include examples for basic graphs such as bar chart, pie chart, histograms, scatter plot and so on. <br/>
When making this cheat sheet, I reviewed all the things we learned from class which benefits me to have a deep understanding about this course. This memory consolidation helps me have a deep impression on knowledge. Also, I have another machine learning class which asked us to do data analysis. Before I trying to fit models on the data, we also need to do some preprocessing. I would never forget doing data cleaning after this course. Machine learning course asked us to used Python instead of R codes, so I think this Cheat sheet can save me time in future projects and improve my efficient. <br/>
Next time maybe I will provide more detailed Python codes such as what kind of package in Python can do the same thing as ‘dplyr’. I would add codes that can select rows or columns in a dataframe, change ordering of the rows or other  data manipulations.<br/>




