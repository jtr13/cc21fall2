# R based data organization and visualization

Tengteng Tao


```r
library(tidyverse)
library(ggridges)
library(ggplot2)
library(scales)
```

## Introduction

In this cheat sheet, I conclude all the important functions we have used in the past two graded homeworks. The whole cheat sheet has two sections. In the first section, all functions related to plotting will be listed. In the second section, all functions which are helpful in organizing data will be mentioned.

## Plots and  their corresponding codes

### Box plots
To create box plots, we use the function geom_boxplot() from the ggplot2. The basic function is 

ggplot(dataframe, aes(y = TheColumnForYaxis , x = TheColumnForXaxis ))+
geom_boxplot()

The example used data fastfood from the openintro package. I used the data calories and restaurant to make the box plot. In addition,to make sure the plot is intuitive enough, the plot is ordered by the mean value from high to low. 


```r
df <- openintro::fastfood
ggplot(df, aes(x = reorder(restaurant, calories, median), y = calories))+
geom_boxplot()+
coord_flip()+
xlab("")+
theme_grey(14)
```

<img src="base_r_data_organization_visualization_files/figure-html/unnamed-chunk-2-1.png" width="672" style="display: block; margin: auto;" />

### Histograms
In this section, I will introduce the two ways to make histograms. Examples used data mtl from package openintro
The first way is plotting with base R. We can simply use function hist() like

hist(datafram$TheColumnYouWantToPlot)


```r
df <- openintro::mtl
hist(df$asubic, col = "lightblue",  xlab = "asubic", main = "Histogram of asubic based on R")
```

<img src="base_r_data_organization_visualization_files/figure-html/unnamed-chunk-3-1.png" width="672" style="display: block; margin: auto;" />
The second way is using ggplot2. The thing needed to be noticed is that the bin number is default on 30 for any data set. Acoordingly, for a more intuitive plot, we always need to change the bins' number.
The basic function is:

ggplot(datafram, aes(TheColumnYouWantToPlot))+
geom_hist()


```r
ggplot(df, aes(asubic))+
  geom_histogram()+stat_bin(bins = 9)+
  ggtitle("Histogram of asubic based on ggplot")
```

<img src="base_r_data_organization_visualization_files/figure-html/unnamed-chunk-4-1.png" width="672" style="display: block; margin: auto;" />

### Density curves
To create density curves, we use geom_density from ggplot2. Basic function is:

ggplot(dataframe, aes(x=TheColumnYouWantToPlot))+
geom_density()

The data we used for example here is the astralia soybean from the agridat package.



```r
df <- agridat::australia.soybean
ggplot(df, aes(x = yield))+
  geom_density(alpha = .2, color = "blue")+  
  theme_grey(14)
```

<img src="base_r_data_organization_visualization_files/figure-html/unnamed-chunk-5-1.png" width="672" style="display: block; margin: auto;" />

### Normal curves
To create normal curves, we need use stat_function(fun = dnorm, args = list(mean, sd)). The basic function is:

ggplot(dataframe, aes(x=TheColumnYouWantToPlot))+
stat_function(fun = dnorm, args = list(mean = mean(TheColumnYouWantToPlot), sd = sd(TheColumnYouWantToPlot)))

The data we used for example here is the astralia soybean from the agridat package.


```r
df <- agridat::australia.soybean
ggplot(df, aes(x = yield))+
  stat_function(fun = dnorm, args = list(mean = mean(df$yield), sd = sd(df$yield)), color = "red")
```

<img src="base_r_data_organization_visualization_files/figure-html/unnamed-chunk-6-1.png" width="672" style="display: block; margin: auto;" />

### Ridgeline plot
To create a ridgeline plot, we need to use geom_density_ridges() from the package ggridges. The basic function is:

ggplot(df, aes(y = TheColumnForYaxis , x = TheColumnForXaxis ))+
  geom_density_ridges()+

The example used data loans_full_schema from package openintro. In addition,to make sure the plot is intuitive enough, the plot is ordered by the mean value from high to low.

```r
df <- openintro::loans_full_schema
ggplot(df, aes(y = reorder(loan_purpose, loan_amount, median), 
               x = loan_amount))+
  geom_density_ridges(fill = "blue", alpha = .5, scale = 1)+
  theme_ridges()+
  theme(legend.position = "none")
```

<img src="base_r_data_organization_visualization_files/figure-html/unnamed-chunk-7-1.png" width="672" style="display: block; margin: auto;" />

### Frequency Bar Chart
To create a frequency bar chart, we need to use geom_bar() from ggplot2. Here is the basic function:

ggplot(dataframe, aes(x = TheColumnYouWantToPlot))+
geom_bar(aes(y = ..count..))


Data used here is Roof.Style from ames in the package openintro.  In addition,to make sure the plot is intuitive enough, the plot is ordered in ascending order.

```r
df <- openintro::ames

ggplot(df,  aes(x = fct_rev(fct_infreq(Roof.Style)))) + 
  geom_bar( aes(y = ..count..), color = "blue", fill = "lightblue") +
  xlab("") +
  ylab("Frequency") +
  ggtitle("Frequency bar chart for the roof styles of the properties")
```

<img src="base_r_data_organization_visualization_files/figure-html/unnamed-chunk-8-1.png" width="672" style="display: block; margin: auto;" />

### Cleveland dot plots
To create a cleveland dot plots, we need to geom_point from ggplot2. The basic function is

ggplot(dataframe, aes(y =reorder(TheColumnForYaxis, TheColumnForXaxis) , x = TheColumnForXaxis))+
geom_point()


Data used here is seattlepets from package openintro. I plotted the most popular 30 names. 

```r
df <- openintro::seattlepets %>% dplyr::count(animal_name, sort = TRUE) %>% drop_na()

ggplot(df[1:30,], aes(x = n, y = reorder(animal_name, n)))+
  geom_point()
```

<img src="base_r_data_organization_visualization_files/figure-html/unnamed-chunk-9-1.png" width="672" style="display: block; margin: auto;" />




### Scatter plot
To create a scatter plot, we also use geom_point(). The basic function is 

ggplot(dataframe, aes(y = TheColumnForYaxis , x = TheColumnForXaxis))+
geom_point()

Data used here is ames from the package openintro

```r
df <- openintro::ames
ggplot(df, aes(area, price))+
  geom_point( alpha = .15, stroke = 0,size = 1.5)+
  ggtitle("Scatter plot of price vs. area")
```

<img src="base_r_data_organization_visualization_files/figure-html/unnamed-chunk-10-1.png" width="672" style="display: block; margin: auto;" />

### Density contour lines
To create density contour lines, we need to use geom_density_2d(). Here is the basic function:

ggplot(dataframe, aes(y = TheColumnForYaxis , x = TheColumnForXaxis))+
geom_density_2d()

Data used here is ames from the package openintro.

```r
ggplot(df,aes(area, price)) + 
  geom_density_2d(aes(colour=..level..)) + 
  scale_colour_gradient(low="green",high="red") +
  ggtitle("Density contour lines of price vs. area")
```

<img src="base_r_data_organization_visualization_files/figure-html/unnamed-chunk-11-1.png" width="672" style="display: block; margin: auto;" />

### Hexagonal heatmap
To create hexagonal heatmap, we need to use geom_hex(). Here is the basic function:

ggplot(dataframe, aes(y = TheColumnForYaxis , x = TheColumnForXaxis))+
geom_hex()

Data used here is ames from the package openintro.


```r
ggplot(df,aes(area, price)) + 
  geom_hex(bins = 30) +
  scale_fill_gradient(low = "#F2F0F7", high = "#08519C" ) +
  theme_bw() +
  ggtitle("Hexagonal heatmap of price vs. area")
```

<img src="base_r_data_organization_visualization_files/figure-html/unnamed-chunk-12-1.png" width="672" style="display: block; margin: auto;" />

### Square heatmap
To create hexagonal heatmap, we need to use geom_bin_2d(). Here is the basic function:

ggplot(dataframe, aes(y = TheColumnForYaxis , x = TheColumnForXaxis))+
geom_bin_2d()

Data used here is ames from the package openintro.


```r
ggplot(df, aes(area, price)) +
 geom_bin_2d(bins = 20) +
  scale_fill_gradient(low = "#F2F0F7", high = "#08519C" ) +
  theme_bw() +
  ggtitle("Square heatmap of price vs. area") 
```

<img src="base_r_data_organization_visualization_files/figure-html/unnamed-chunk-13-1.png" width="672" style="display: block; margin: auto;" />

## Data organization functions

### Pipe(%>%) Operator
Pipe operator can be used to simplified your code. It can be simple interpreted as "and then" For example:
filter(data, variable == numeric_value) and
data %>% filter(variable == numeric_value) will yield same result.

By using this operator properly, we can make our code clean and brief.
### facet_warp()
facet_warp() allow us to combine multiple plots, which can give us a more directly view of comparison between those type of plots.

The data we used for example here is the astralia soybean from the agridat package.

```r
df <- agridat::australia.soybean
ggplot(df, aes(x = yield, color = loc, fill = loc))+
  geom_histogram(aes(y = ..density..),  fill = NA) + 
  facet_wrap(~loc, nrow = 2, strip.position = "right")+
  theme_grey(14)
```

<img src="base_r_data_organization_visualization_files/figure-html/unnamed-chunk-14-1.png" width="672" style="display: block; margin: auto;" />

### filter()
filter() function allows us to select those variable with specific values. For example, in the data seattlepets from the package openintro, we can use filter to find all dogs' name:


```r
df <- openintro::seattlepets %>% filter(species == "Dog")
df
```

```
## # A tibble: 35,181 × 7
##    license_issue_date license_number animal_name species primary_breed          
##    <date>             <chr>          <chr>       <chr>   <chr>                  
##  1 2018-11-16         8002756        Wall-E      Dog     Mixed Breed, Medium (u…
##  2 2018-11-11         S124529        Andre       Dog     Terrier, Jack Russell  
##  3 2018-11-21         903793         Mac         Dog     Retriever, Labrador    
##  4 2018-12-16         S138529        Cody        Dog     Retriever, Labrador    
##  5 2017-10-04         580652         Millie      Dog     Terrier, Boston        
##  6 2018-12-23         961052         Sabre       Dog     Terrier                
##  7 2018-12-07         S125461        Thomas      Dog     Chihuahua, Short Coat  
##  8 2018-11-07         8002543        Lulu        Dog     Vizsla, Smooth Haired  
##  9 2018-12-15         S138838        Milo        Dog     Boxer                  
## 10 2018-11-27         S123980        Anubis      Dog     Poodle, Standard       
## # … with 35,171 more rows, and 2 more variables: secondary_breed <chr>,
## #   zip_code <chr>
```
### group_by()
group_by()function allow us to group the data by some variables.

For example, we want to group the data that crimes in 2020 by county and region, we can do this

```r
df <- read.csv("https://data.ny.gov/api/views/ca8h-8gjq/rows.csv")
df %>% filter(Year == 2020) %>% group_by(County, Region)
```

```
## # A tibble: 624 × 15
## # Groups:   County, Region [62]
##    County Agency     Year Months.Reported Index.Total Violent.Total Murder  Rape
##    <chr>  <chr>     <int>           <int>       <int>         <int>  <int> <int>
##  1 Albany Albany C…  2020              12        3547           875     18    61
##  2 Albany Albany C…  2020              12           2             0      0     0
##  3 Albany Albany C…  2020              12         127            12      0     4
##  4 Albany Albany C…  2020              12         103            26      0    18
##  5 Albany Altamont…  2020              12           6             2      0     0
##  6 Albany Bethlehe…  2020              12         407            25      1     7
##  7 Albany Coeymans…  2020              12          49             8      0     0
##  8 Albany Cohoes C…  2020              12         134            23      0     3
##  9 Albany Colonie …  2020              12        1936            83      0     4
## 10 Albany County T…  2020              NA        7412          1115     19   109
## # … with 614 more rows, and 7 more variables: Robbery <int>,
## #   Aggravated.Assault <int>, Property.Total <int>, Burglary <int>,
## #   Larceny <int>, Motor.Vehicle.Theft <int>, Region <chr>
```
### summarise()
We can use summarise() to measure some value for a certain group. For example, in data set ames from openintro, we want to know the average price and area for each Neighborhood, we can do this:

```r
df <-openintro::ames %>%
  group_by(Neighborhood) %>%
  summarise(price = mean(price), area = mean(area))

df
```

```
## # A tibble: 28 × 3
##    Neighborhood   price  area
##    <fct>          <dbl> <dbl>
##  1 Blmngtn      196662. 1405.
##  2 Blueste      143590  1160.
##  3 BrDale       105608. 1115.
##  4 BrkSide      124756. 1235.
##  5 ClearCr      208662. 1744.
##  6 CollgCr      201803. 1496.
##  7 Crawfor      207551. 1723.
##  8 Edwards      130843. 1338.
##  9 Gilbert      190647. 1621.
## 10 Greens       193531. 1157.
## # … with 18 more rows
```
### summarise_at()
For some specific situation, we need to summaries many variables. Writing them one by one will be time comsuming and we can do this by using summarise_at().

For Example, we want to know for year 2020, the total number of each type of crime happened in every county. We can write something like this:

```r
df2020 <- read.csv("https://data.ny.gov/api/views/ca8h-8gjq/rows.csv") %>% 
  filter(Year == 2020)
df2020$Property.Total = NULL
df2020 %>%
  group_by(County) %>%
  summarise_at(.vars = names(.)[7:13], .funs = c(sum = "sum"))
```

```
## # A tibble: 62 × 8
##    County      Murder_sum Rape_sum Robbery_sum Aggravated.Assault_… Burglary_sum
##    <chr>            <int>    <int>       <int>                <int>        <int>
##  1 Albany              38      218         426                 1548         1416
##  2 Allegany             6       76           6                   58          172
##  3 Bronx              111      523        3519                 8976         2230
##  4 Broome              10      252         156                  902         1336
##  5 Cattaraugus          2       74          12                  162          274
##  6 Cayuga               4      126          32                  236          290
##  7 Chautauqua           2      164          66                  552         1080
##  8 Chemung              4       64          56                  220          262
##  9 Chenango             2      104          14                  106          292
## 10 Clinton              2      118           6                  130          246
## # … with 52 more rows, and 2 more variables: Larceny_sum <int>,
## #   Motor.Vehicle.Theft_sum <int>
```
