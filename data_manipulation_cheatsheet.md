# Data manipulation in R

Junhao Zhang



### Overview
This cheat sheet is particularly made for people who don't experience with R and it briefly talks about the necessary tools and packages used in our programming assignments that can help manipulate the dataset before doing the visualization. Two packages will be mainly focused here: "dplyr" and "tidyr".

### Environment Set Up
Before using those packages, we need to install them into our computer. To do that, we can simply install the tidyverse package and import it use library() function, which includes dplyr, tidyr and some other useful packages.

### Part One: Data Import 
In this part, three most commonly used ways of importing data will be showed.\
1.<b>Direct Import from R Package</b>\
2.<b>Import Using URL </b>\
3.<b>Import from local computer</b>\

#### Import from Package
One greatest thing about R is that it has a R dataset package which contains a variety of datasets that we can use.
To use those datasets, we just need to import the package into R.
eg If we want to use fastfood dataset from the openintro packaage, we just need to import openintro

```r
library(openintro)
fastfood
```

```
## # A tibble: 515 × 17
##    restaurant item      calories cal_fat total_fat sat_fat trans_fat cholesterol
##    <chr>      <chr>        <dbl>   <dbl>     <dbl>   <dbl>     <dbl>       <dbl>
##  1 Mcdonalds  Artisan …      380      60         7       2       0            95
##  2 Mcdonalds  Single B…      840     410        45      17       1.5         130
##  3 Mcdonalds  Double B…     1130     600        67      27       3           220
##  4 Mcdonalds  Grilled …      750     280        31      10       0.5         155
##  5 Mcdonalds  Crispy B…      920     410        45      12       0.5         120
##  6 Mcdonalds  Big Mac        540     250        28      10       1            80
##  7 Mcdonalds  Cheesebu…      300     100        12       5       0.5          40
##  8 Mcdonalds  Classic …      510     210        24       4       0            65
##  9 Mcdonalds  Double C…      430     190        21      11       1            85
## 10 Mcdonalds  Double Q…      770     400        45      21       2.5         175
## # … with 505 more rows, and 9 more variables: sodium <dbl>, total_carb <dbl>,
## #   fiber <dbl>, sugar <dbl>, protein <dbl>, vit_a <dbl>, vit_c <dbl>,
## #   calcium <dbl>, salad <chr>
```
If there are other dataset called fastfood, to avoid confusion, we can specify it clearly with the package name

```r
openintro::fastfood
```

```
## # A tibble: 515 × 17
##    restaurant item      calories cal_fat total_fat sat_fat trans_fat cholesterol
##    <chr>      <chr>        <dbl>   <dbl>     <dbl>   <dbl>     <dbl>       <dbl>
##  1 Mcdonalds  Artisan …      380      60         7       2       0            95
##  2 Mcdonalds  Single B…      840     410        45      17       1.5         130
##  3 Mcdonalds  Double B…     1130     600        67      27       3           220
##  4 Mcdonalds  Grilled …      750     280        31      10       0.5         155
##  5 Mcdonalds  Crispy B…      920     410        45      12       0.5         120
##  6 Mcdonalds  Big Mac        540     250        28      10       1            80
##  7 Mcdonalds  Cheesebu…      300     100        12       5       0.5          40
##  8 Mcdonalds  Classic …      510     210        24       4       0            65
##  9 Mcdonalds  Double C…      430     190        21      11       1            85
## 10 Mcdonalds  Double Q…      770     400        45      21       2.5         175
## # … with 505 more rows, and 9 more variables: sodium <dbl>, total_carb <dbl>,
## #   fiber <dbl>, sugar <dbl>, protein <dbl>, vit_a <dbl>, vit_c <dbl>,
## #   calcium <dbl>, salad <chr>
```

#### Import Using URL
(a) We can also import dataset direcly from online sources. To achieve that, we will be using the read_csv function.
eg import the crime dataset from government official website.

```r
read_csv("https://data.ny.gov/api/views/ca8h-8gjq/rows.csv")
```

```
## # A tibble: 21,228 × 15
##    County Agency      Year `Months Reporte… `Index Total` `Violent Total` Murder
##    <chr>  <chr>      <dbl>            <dbl>         <dbl>           <dbl>  <dbl>
##  1 Albany Albany Ci…  1990               NA          6635            1052      9
##  2 Albany Albany Ci…  1991               NA          7569            1201     11
##  3 Albany Albany Ci…  1992               NA          7791            1150      8
##  4 Albany Albany Ci…  1993               NA          7802            1238      6
##  5 Albany Albany Ci…  1994               NA          8648            1380     13
##  6 Albany Albany Ci…  1995               NA          8329            1227      7
##  7 Albany Albany Ci…  1996               NA          8130            1132     11
##  8 Albany Albany Ci…  1997               NA          7354            1035      7
##  9 Albany Albany Ci…  1998               NA          7320             995      2
## 10 Albany Albany Ci…  1999               NA          7475             897     12
## # … with 21,218 more rows, and 8 more variables: Rape <dbl>, Robbery <dbl>,
## #   Aggravated Assault <dbl>, Property Total <dbl>, Burglary <dbl>,
## #   Larceny <dbl>, Motor Vehicle Theft <dbl>, Region <chr>
```
(b) We can alsp import dataset direcly from the github.\
1.Go to the github repository link where you have the CSV file\
2.Click on the raw option present on the top right of the data\
3.Copy the URL and put into the read_csv function\
eg read dataset from the github

```r
read_csv("https://raw.githubusercontent.com/curran/data/gh-pages/dataSoup/datasets.csv")
```

```
## # A tibble: 57 × 12
##    `Dataset Name`  `Person Adding` `Date Added` `Dataset Link`  `Most Recent Ye…
##    <chr>           <chr>           <chr>        <chr>           <chr>           
##  1 2008 Election … EJ              11/7/2012    https://docs.g… 2008            
##  2 Occupy Oakland… EJ              11/7/2012    https://docs.g… 2012            
##  3 NYPD Stop-and-… EJ              11/7/2012    http://api.occ… 2011            
##  4 Presidential S… Kai             11/7/2012    http://millerc… 2012            
##  5 USDA National … Kai             11/7/2012    http://www.ars… 2012            
##  6 US Foreign Aid  Kai             11/7/2012    https://explor… 2010            
##  7 US Potato Stat… Kai             11/7/2012    https://explor… 2007            
##  8 Livestock and … Kai             11/7/2012    https://explor… 2011            
##  9 Mine Accidents… Kai             11/7/2012    http://www.msh… 2012            
## 10 Sloan Digital … Kai             11/7/2012    http://www.sds… 2011            
## # … with 47 more rows, and 7 more variables: Earliest Year In Data <dbl>,
## #   Status <chr>, Dataset Type <chr>, Documentation <chr>, Existing Work <chr>,
## #   Tags <chr>, Active <chr>
```

#### Import from the local computer
If the file is already in you computer, then you can simple import it by finding its path and read it.\
eg read the state_wl.csv file from the computer.\
1. Find the location of state_wl.csv in your computer.\
2. Use read_csv to read it: read_csv(file path).\

### Missing Values
Before we talk about data transformation packages, I want to first address the missing values problem. In reality, most data set will not be tidy, especially data set from online sources.The most common issue in any given data set is the missing value. Sometimes missing values are just meaningless errors, but sometimes they are important. It's up to you to decide whether to include those missing values or not. This part will show how to detect, recode and exclude missing values.\

#### Detecting missing values
The is.na() function will help test whether missing values exist or not by returning a logical vector with either TRUE or FALSE

```r
x <- c(1:4, NA, 6:7, NA)
x
```

```
## [1]  1  2  3  4 NA  6  7 NA
```

```r
is.na(x)
```

```
## [1] FALSE FALSE FALSE FALSE  TRUE FALSE FALSE  TRUE
```
To identify the location or the number of NAs in a vector, we can use which() and sum()

```r
# identify the location of NA
which(is.na(x))
```

```
## [1] 5 8
```

```r
# coun the number of NA
sum(is.na(x))
```

```
## [1] 2
```
#### Recode missing values
Not all missing values are meaningless. Some missing values are caused by human error and thus we can correct them by recoding missing values.

```r
# original x
x
```

```
## [1]  1  2  3  4 NA  6  7 NA
```

```r
# replace NA in x by other numbers
x[is.na(x)] <- mean(x, na.rm = TRUE) 
round(x,2)
```

```
## [1] 1.00 2.00 3.00 4.00 3.83 6.00 7.00 3.83
```

#### Exclude missing values
If we are sure that missing values are meaningless, then we can remove it from the dataset because any arithmetic calculation involving NA results in NA.

```r
y <- c(1,2,NA,3)
mean(y) 
```

```
## [1] NA
```

```r
mean(y, na.rm=TRUE) 
```

```
## [1] 2
```
Another way to remove all NA from a dataframe is by using na.omit().

```r
df <- data.frame(col1 = c(1:3, NA),
                 col2 = c("this", NA,"is", "text"), 
                 col3 = c(TRUE, FALSE, TRUE, TRUE), 
                 col4 = c(2.5, 4.2, 3.2, NA),
                 stringsAsFactors = FALSE)
df
```

```
##   col1 col2  col3 col4
## 1    1 this  TRUE  2.5
## 2    2 <NA> FALSE  4.2
## 3    3   is  TRUE  3.2
## 4   NA text  TRUE   NA
```

```r
na.omit(df)
```

```
##   col1 col2 col3 col4
## 1    1 this TRUE  2.5
## 3    3   is TRUE  3.2
```

### Part Two: dylyr
There are 7 key functions that help transform dataset.\
1.<b>filter</b>: subset a data frame where all columns in the subset satisfy certain conditions.\
2.<b>select</b>: select columns by their names.\
3.<b>mutate</b>: adds news columns at the end of dataset and preserves the existing ones.\
4.<b>arrange</b>: change the order of rows in a data frame.\
5.<b>summarise/summarize</b>: reduces multiple values down to a single value and usually used on grouped data.\
6.<b>group_by</b>: group the whole dataset by one or more variables \
7.<b>rename</b>: rename column names.\

We will be using mtcars dataset in r to illustrate the above key functions.\

#### filter() 
We can use this function to get columns based on their values.\
eg find all cars that has 6 cylinders 

```r
filter(mtcars,cyl==6)
```

```
##                 mpg cyl  disp  hp drat    wt  qsec vs am gear carb
## Mazda RX4      21.0   6 160.0 110 3.90 2.620 16.46  0  1    4    4
## Mazda RX4 Wag  21.0   6 160.0 110 3.90 2.875 17.02  0  1    4    4
## Hornet 4 Drive 21.4   6 258.0 110 3.08 3.215 19.44  1  0    3    1
## Valiant        18.1   6 225.0 105 2.76 3.460 20.22  1  0    3    1
## Merc 280       19.2   6 167.6 123 3.92 3.440 18.30  1  0    4    4
## Merc 280C      17.8   6 167.6 123 3.92 3.440 18.90  1  0    4    4
## Ferrari Dino   19.7   6 145.0 175 3.62 2.770 15.50  0  1    5    6
```
We can also use c() to filter more than more columns\
eg find all information of cars that have number of foward gears is 3 or 5

```r
filter(mtcars,gear %in% c(3,5))
```

```
##                      mpg cyl  disp  hp drat    wt  qsec vs am gear carb
## Hornet 4 Drive      21.4   6 258.0 110 3.08 3.215 19.44  1  0    3    1
## Hornet Sportabout   18.7   8 360.0 175 3.15 3.440 17.02  0  0    3    2
## Valiant             18.1   6 225.0 105 2.76 3.460 20.22  1  0    3    1
## Duster 360          14.3   8 360.0 245 3.21 3.570 15.84  0  0    3    4
## Merc 450SE          16.4   8 275.8 180 3.07 4.070 17.40  0  0    3    3
## Merc 450SL          17.3   8 275.8 180 3.07 3.730 17.60  0  0    3    3
## Merc 450SLC         15.2   8 275.8 180 3.07 3.780 18.00  0  0    3    3
## Cadillac Fleetwood  10.4   8 472.0 205 2.93 5.250 17.98  0  0    3    4
## Lincoln Continental 10.4   8 460.0 215 3.00 5.424 17.82  0  0    3    4
## Chrysler Imperial   14.7   8 440.0 230 3.23 5.345 17.42  0  0    3    4
## Toyota Corona       21.5   4 120.1  97 3.70 2.465 20.01  1  0    3    1
## Dodge Challenger    15.5   8 318.0 150 2.76 3.520 16.87  0  0    3    2
## AMC Javelin         15.2   8 304.0 150 3.15 3.435 17.30  0  0    3    2
## Camaro Z28          13.3   8 350.0 245 3.73 3.840 15.41  0  0    3    4
## Pontiac Firebird    19.2   8 400.0 175 3.08 3.845 17.05  0  0    3    2
## Porsche 914-2       26.0   4 120.3  91 4.43 2.140 16.70  0  1    5    2
## Lotus Europa        30.4   4  95.1 113 3.77 1.513 16.90  1  1    5    2
## Ford Pantera L      15.8   8 351.0 264 4.22 3.170 14.50  0  1    5    4
## Ferrari Dino        19.7   6 145.0 175 3.62 2.770 15.50  0  1    5    6
## Maserati Bora       15.0   8 301.0 335 3.54 3.570 14.60  0  1    5    8
```
We can also put complex conditions 
eg find all cars have more than 6 cylinders and fuel consumption less than 20 mpg.

```r
filter(mtcars,cyl>6 & mpg<20)
```

```
##                      mpg cyl  disp  hp drat    wt  qsec vs am gear carb
## Hornet Sportabout   18.7   8 360.0 175 3.15 3.440 17.02  0  0    3    2
## Duster 360          14.3   8 360.0 245 3.21 3.570 15.84  0  0    3    4
## Merc 450SE          16.4   8 275.8 180 3.07 4.070 17.40  0  0    3    3
## Merc 450SL          17.3   8 275.8 180 3.07 3.730 17.60  0  0    3    3
## Merc 450SLC         15.2   8 275.8 180 3.07 3.780 18.00  0  0    3    3
## Cadillac Fleetwood  10.4   8 472.0 205 2.93 5.250 17.98  0  0    3    4
## Lincoln Continental 10.4   8 460.0 215 3.00 5.424 17.82  0  0    3    4
## Chrysler Imperial   14.7   8 440.0 230 3.23 5.345 17.42  0  0    3    4
## Dodge Challenger    15.5   8 318.0 150 2.76 3.520 16.87  0  0    3    2
## AMC Javelin         15.2   8 304.0 150 3.15 3.435 17.30  0  0    3    2
## Camaro Z28          13.3   8 350.0 245 3.73 3.840 15.41  0  0    3    4
## Pontiac Firebird    19.2   8 400.0 175 3.08 3.845 17.05  0  0    3    2
## Ford Pantera L      15.8   8 351.0 264 4.22 3.170 14.50  0  1    5    4
## Maserati Bora       15.0   8 301.0 335 3.54 3.570 14.60  0  1    5    8
```

#### select()
we can use select to pick up certain columns by their names, especially when you have a really long dataframe, select allows you to select only columns you need.\

eg select car information containing information of miles per gallon and number of cylinders

```r
select(mtcars,mpg,cyl)
```

```
##                      mpg cyl
## Mazda RX4           21.0   6
## Mazda RX4 Wag       21.0   6
## Datsun 710          22.8   4
## Hornet 4 Drive      21.4   6
## Hornet Sportabout   18.7   8
## Valiant             18.1   6
## Duster 360          14.3   8
## Merc 240D           24.4   4
## Merc 230            22.8   4
## Merc 280            19.2   6
## Merc 280C           17.8   6
## Merc 450SE          16.4   8
## Merc 450SL          17.3   8
## Merc 450SLC         15.2   8
## Cadillac Fleetwood  10.4   8
## Lincoln Continental 10.4   8
## Chrysler Imperial   14.7   8
## Fiat 128            32.4   4
## Honda Civic         30.4   4
## Toyota Corolla      33.9   4
## Toyota Corona       21.5   4
## Dodge Challenger    15.5   8
## AMC Javelin         15.2   8
## Camaro Z28          13.3   8
## Pontiac Firebird    19.2   8
## Fiat X1-9           27.3   4
## Porsche 914-2       26.0   4
## Lotus Europa        30.4   4
## Ford Pantera L      15.8   8
## Ferrari Dino        19.7   6
## Maserati Bora       15.0   8
## Volvo 142E          21.4   4
```

We can select several columns using index ":"
eg select car information from displacement to weight

```r
select(mtcars,disp:wt)
```

```
##                      disp  hp drat    wt
## Mazda RX4           160.0 110 3.90 2.620
## Mazda RX4 Wag       160.0 110 3.90 2.875
## Datsun 710          108.0  93 3.85 2.320
## Hornet 4 Drive      258.0 110 3.08 3.215
## Hornet Sportabout   360.0 175 3.15 3.440
## Valiant             225.0 105 2.76 3.460
## Duster 360          360.0 245 3.21 3.570
## Merc 240D           146.7  62 3.69 3.190
## Merc 230            140.8  95 3.92 3.150
## Merc 280            167.6 123 3.92 3.440
## Merc 280C           167.6 123 3.92 3.440
## Merc 450SE          275.8 180 3.07 4.070
## Merc 450SL          275.8 180 3.07 3.730
## Merc 450SLC         275.8 180 3.07 3.780
## Cadillac Fleetwood  472.0 205 2.93 5.250
## Lincoln Continental 460.0 215 3.00 5.424
## Chrysler Imperial   440.0 230 3.23 5.345
## Fiat 128             78.7  66 4.08 2.200
## Honda Civic          75.7  52 4.93 1.615
## Toyota Corolla       71.1  65 4.22 1.835
## Toyota Corona       120.1  97 3.70 2.465
## Dodge Challenger    318.0 150 2.76 3.520
## AMC Javelin         304.0 150 3.15 3.435
## Camaro Z28          350.0 245 3.73 3.840
## Pontiac Firebird    400.0 175 3.08 3.845
## Fiat X1-9            79.0  66 4.08 1.935
## Porsche 914-2       120.3  91 4.43 2.140
## Lotus Europa         95.1 113 3.77 1.513
## Ford Pantera L      351.0 264 4.22 3.170
## Ferrari Dino        145.0 175 3.62 2.770
## Maserati Bora       301.0 335 3.54 3.570
## Volvo 142E          121.0 109 4.11 2.780
```

We could add a minus sign in front of the column name to not select them.
eg select all information of car except Rear axle ration and number of carburetors

```r
select(mtcars,-drat,-carb)
```

```
##                      mpg cyl  disp  hp    wt  qsec vs am gear
## Mazda RX4           21.0   6 160.0 110 2.620 16.46  0  1    4
## Mazda RX4 Wag       21.0   6 160.0 110 2.875 17.02  0  1    4
## Datsun 710          22.8   4 108.0  93 2.320 18.61  1  1    4
## Hornet 4 Drive      21.4   6 258.0 110 3.215 19.44  1  0    3
## Hornet Sportabout   18.7   8 360.0 175 3.440 17.02  0  0    3
## Valiant             18.1   6 225.0 105 3.460 20.22  1  0    3
## Duster 360          14.3   8 360.0 245 3.570 15.84  0  0    3
## Merc 240D           24.4   4 146.7  62 3.190 20.00  1  0    4
## Merc 230            22.8   4 140.8  95 3.150 22.90  1  0    4
## Merc 280            19.2   6 167.6 123 3.440 18.30  1  0    4
## Merc 280C           17.8   6 167.6 123 3.440 18.90  1  0    4
## Merc 450SE          16.4   8 275.8 180 4.070 17.40  0  0    3
## Merc 450SL          17.3   8 275.8 180 3.730 17.60  0  0    3
## Merc 450SLC         15.2   8 275.8 180 3.780 18.00  0  0    3
## Cadillac Fleetwood  10.4   8 472.0 205 5.250 17.98  0  0    3
## Lincoln Continental 10.4   8 460.0 215 5.424 17.82  0  0    3
## Chrysler Imperial   14.7   8 440.0 230 5.345 17.42  0  0    3
## Fiat 128            32.4   4  78.7  66 2.200 19.47  1  1    4
## Honda Civic         30.4   4  75.7  52 1.615 18.52  1  1    4
## Toyota Corolla      33.9   4  71.1  65 1.835 19.90  1  1    4
## Toyota Corona       21.5   4 120.1  97 2.465 20.01  1  0    3
## Dodge Challenger    15.5   8 318.0 150 3.520 16.87  0  0    3
## AMC Javelin         15.2   8 304.0 150 3.435 17.30  0  0    3
## Camaro Z28          13.3   8 350.0 245 3.840 15.41  0  0    3
## Pontiac Firebird    19.2   8 400.0 175 3.845 17.05  0  0    3
## Fiat X1-9           27.3   4  79.0  66 1.935 18.90  1  1    4
## Porsche 914-2       26.0   4 120.3  91 2.140 16.70  0  1    5
## Lotus Europa        30.4   4  95.1 113 1.513 16.90  1  1    5
## Ford Pantera L      15.8   8 351.0 264 3.170 14.50  0  1    5
## Ferrari Dino        19.7   6 145.0 175 2.770 15.50  0  1    5
## Maserati Bora       15.0   8 301.0 335 3.570 14.60  0  1    5
## Volvo 142E          21.4   4 121.0 109 2.780 18.60  1  1    4
```

eg Don't select information between displacement and weight

```r
select(mtcars,-(disp:wt))
```

```
##                      mpg cyl  qsec vs am gear carb
## Mazda RX4           21.0   6 16.46  0  1    4    4
## Mazda RX4 Wag       21.0   6 17.02  0  1    4    4
## Datsun 710          22.8   4 18.61  1  1    4    1
## Hornet 4 Drive      21.4   6 19.44  1  0    3    1
## Hornet Sportabout   18.7   8 17.02  0  0    3    2
## Valiant             18.1   6 20.22  1  0    3    1
## Duster 360          14.3   8 15.84  0  0    3    4
## Merc 240D           24.4   4 20.00  1  0    4    2
## Merc 230            22.8   4 22.90  1  0    4    2
## Merc 280            19.2   6 18.30  1  0    4    4
## Merc 280C           17.8   6 18.90  1  0    4    4
## Merc 450SE          16.4   8 17.40  0  0    3    3
## Merc 450SL          17.3   8 17.60  0  0    3    3
## Merc 450SLC         15.2   8 18.00  0  0    3    3
## Cadillac Fleetwood  10.4   8 17.98  0  0    3    4
## Lincoln Continental 10.4   8 17.82  0  0    3    4
## Chrysler Imperial   14.7   8 17.42  0  0    3    4
## Fiat 128            32.4   4 19.47  1  1    4    1
## Honda Civic         30.4   4 18.52  1  1    4    2
## Toyota Corolla      33.9   4 19.90  1  1    4    1
## Toyota Corona       21.5   4 20.01  1  0    3    1
## Dodge Challenger    15.5   8 16.87  0  0    3    2
## AMC Javelin         15.2   8 17.30  0  0    3    2
## Camaro Z28          13.3   8 15.41  0  0    3    4
## Pontiac Firebird    19.2   8 17.05  0  0    3    2
## Fiat X1-9           27.3   4 18.90  1  1    4    1
## Porsche 914-2       26.0   4 16.70  0  1    5    2
## Lotus Europa        30.4   4 16.90  1  1    5    2
## Ford Pantera L      15.8   8 14.50  0  1    5    4
## Ferrari Dino        19.7   6 15.50  0  1    5    6
## Maserati Bora       15.0   8 14.60  0  1    5    8
## Volvo 142E          21.4   4 18.60  1  1    4    2
```

#### mutate()
We can use this function to add new variables and adding it at the end of dataset and preserves the existing columns.\

eg we can calculate the displacement per cylinder for each car with mpg greater than 20 by using mutate

```r
mtcars %>%
  filter(mpg>20) %>%
  mutate(capacity=disp/cyl)
```

```
##                 mpg cyl  disp  hp drat    wt  qsec vs am gear carb capacity
## Mazda RX4      21.0   6 160.0 110 3.90 2.620 16.46  0  1    4    4 26.66667
## Mazda RX4 Wag  21.0   6 160.0 110 3.90 2.875 17.02  0  1    4    4 26.66667
## Datsun 710     22.8   4 108.0  93 3.85 2.320 18.61  1  1    4    1 27.00000
## Hornet 4 Drive 21.4   6 258.0 110 3.08 3.215 19.44  1  0    3    1 43.00000
## Merc 240D      24.4   4 146.7  62 3.69 3.190 20.00  1  0    4    2 36.67500
## Merc 230       22.8   4 140.8  95 3.92 3.150 22.90  1  0    4    2 35.20000
## Fiat 128       32.4   4  78.7  66 4.08 2.200 19.47  1  1    4    1 19.67500
## Honda Civic    30.4   4  75.7  52 4.93 1.615 18.52  1  1    4    2 18.92500
## Toyota Corolla 33.9   4  71.1  65 4.22 1.835 19.90  1  1    4    1 17.77500
## Toyota Corona  21.5   4 120.1  97 3.70 2.465 20.01  1  0    3    1 30.02500
## Fiat X1-9      27.3   4  79.0  66 4.08 1.935 18.90  1  1    4    1 19.75000
## Porsche 914-2  26.0   4 120.3  91 4.43 2.140 16.70  0  1    5    2 30.07500
## Lotus Europa   30.4   4  95.1 113 3.77 1.513 16.90  1  1    5    2 23.77500
## Volvo 142E     21.4   4 121.0 109 4.11 2.780 18.60  1  1    4    2 30.25000
```
#### arrange()
We can use this function to sort all rows by the value of columns. The default order is ascending. Use desc() to sort it in descending order.\

eg we sort all the cars by the fuel consumption (mpg) in acending and decending order

```r
arrange(mtcars,mpg)
```

```
##                      mpg cyl  disp  hp drat    wt  qsec vs am gear carb
## Cadillac Fleetwood  10.4   8 472.0 205 2.93 5.250 17.98  0  0    3    4
## Lincoln Continental 10.4   8 460.0 215 3.00 5.424 17.82  0  0    3    4
## Camaro Z28          13.3   8 350.0 245 3.73 3.840 15.41  0  0    3    4
## Duster 360          14.3   8 360.0 245 3.21 3.570 15.84  0  0    3    4
## Chrysler Imperial   14.7   8 440.0 230 3.23 5.345 17.42  0  0    3    4
## Maserati Bora       15.0   8 301.0 335 3.54 3.570 14.60  0  1    5    8
## Merc 450SLC         15.2   8 275.8 180 3.07 3.780 18.00  0  0    3    3
## AMC Javelin         15.2   8 304.0 150 3.15 3.435 17.30  0  0    3    2
## Dodge Challenger    15.5   8 318.0 150 2.76 3.520 16.87  0  0    3    2
## Ford Pantera L      15.8   8 351.0 264 4.22 3.170 14.50  0  1    5    4
## Merc 450SE          16.4   8 275.8 180 3.07 4.070 17.40  0  0    3    3
## Merc 450SL          17.3   8 275.8 180 3.07 3.730 17.60  0  0    3    3
## Merc 280C           17.8   6 167.6 123 3.92 3.440 18.90  1  0    4    4
## Valiant             18.1   6 225.0 105 2.76 3.460 20.22  1  0    3    1
## Hornet Sportabout   18.7   8 360.0 175 3.15 3.440 17.02  0  0    3    2
## Merc 280            19.2   6 167.6 123 3.92 3.440 18.30  1  0    4    4
## Pontiac Firebird    19.2   8 400.0 175 3.08 3.845 17.05  0  0    3    2
## Ferrari Dino        19.7   6 145.0 175 3.62 2.770 15.50  0  1    5    6
## Mazda RX4           21.0   6 160.0 110 3.90 2.620 16.46  0  1    4    4
## Mazda RX4 Wag       21.0   6 160.0 110 3.90 2.875 17.02  0  1    4    4
## Hornet 4 Drive      21.4   6 258.0 110 3.08 3.215 19.44  1  0    3    1
## Volvo 142E          21.4   4 121.0 109 4.11 2.780 18.60  1  1    4    2
## Toyota Corona       21.5   4 120.1  97 3.70 2.465 20.01  1  0    3    1
## Datsun 710          22.8   4 108.0  93 3.85 2.320 18.61  1  1    4    1
## Merc 230            22.8   4 140.8  95 3.92 3.150 22.90  1  0    4    2
## Merc 240D           24.4   4 146.7  62 3.69 3.190 20.00  1  0    4    2
## Porsche 914-2       26.0   4 120.3  91 4.43 2.140 16.70  0  1    5    2
## Fiat X1-9           27.3   4  79.0  66 4.08 1.935 18.90  1  1    4    1
## Honda Civic         30.4   4  75.7  52 4.93 1.615 18.52  1  1    4    2
## Lotus Europa        30.4   4  95.1 113 3.77 1.513 16.90  1  1    5    2
## Fiat 128            32.4   4  78.7  66 4.08 2.200 19.47  1  1    4    1
## Toyota Corolla      33.9   4  71.1  65 4.22 1.835 19.90  1  1    4    1
```

```r
arrange(mtcars,desc(mpg))
```

```
##                      mpg cyl  disp  hp drat    wt  qsec vs am gear carb
## Toyota Corolla      33.9   4  71.1  65 4.22 1.835 19.90  1  1    4    1
## Fiat 128            32.4   4  78.7  66 4.08 2.200 19.47  1  1    4    1
## Honda Civic         30.4   4  75.7  52 4.93 1.615 18.52  1  1    4    2
## Lotus Europa        30.4   4  95.1 113 3.77 1.513 16.90  1  1    5    2
## Fiat X1-9           27.3   4  79.0  66 4.08 1.935 18.90  1  1    4    1
## Porsche 914-2       26.0   4 120.3  91 4.43 2.140 16.70  0  1    5    2
## Merc 240D           24.4   4 146.7  62 3.69 3.190 20.00  1  0    4    2
## Datsun 710          22.8   4 108.0  93 3.85 2.320 18.61  1  1    4    1
## Merc 230            22.8   4 140.8  95 3.92 3.150 22.90  1  0    4    2
## Toyota Corona       21.5   4 120.1  97 3.70 2.465 20.01  1  0    3    1
## Hornet 4 Drive      21.4   6 258.0 110 3.08 3.215 19.44  1  0    3    1
## Volvo 142E          21.4   4 121.0 109 4.11 2.780 18.60  1  1    4    2
## Mazda RX4           21.0   6 160.0 110 3.90 2.620 16.46  0  1    4    4
## Mazda RX4 Wag       21.0   6 160.0 110 3.90 2.875 17.02  0  1    4    4
## Ferrari Dino        19.7   6 145.0 175 3.62 2.770 15.50  0  1    5    6
## Merc 280            19.2   6 167.6 123 3.92 3.440 18.30  1  0    4    4
## Pontiac Firebird    19.2   8 400.0 175 3.08 3.845 17.05  0  0    3    2
## Hornet Sportabout   18.7   8 360.0 175 3.15 3.440 17.02  0  0    3    2
## Valiant             18.1   6 225.0 105 2.76 3.460 20.22  1  0    3    1
## Merc 280C           17.8   6 167.6 123 3.92 3.440 18.90  1  0    4    4
## Merc 450SL          17.3   8 275.8 180 3.07 3.730 17.60  0  0    3    3
## Merc 450SE          16.4   8 275.8 180 3.07 4.070 17.40  0  0    3    3
## Ford Pantera L      15.8   8 351.0 264 4.22 3.170 14.50  0  1    5    4
## Dodge Challenger    15.5   8 318.0 150 2.76 3.520 16.87  0  0    3    2
## Merc 450SLC         15.2   8 275.8 180 3.07 3.780 18.00  0  0    3    3
## AMC Javelin         15.2   8 304.0 150 3.15 3.435 17.30  0  0    3    2
## Maserati Bora       15.0   8 301.0 335 3.54 3.570 14.60  0  1    5    8
## Chrysler Imperial   14.7   8 440.0 230 3.23 5.345 17.42  0  0    3    4
## Duster 360          14.3   8 360.0 245 3.21 3.570 15.84  0  0    3    4
## Camaro Z28          13.3   8 350.0 245 3.73 3.840 15.41  0  0    3    4
## Cadillac Fleetwood  10.4   8 472.0 205 2.93 5.250 17.98  0  0    3    4
## Lincoln Continental 10.4   8 460.0 215 3.00 5.424 17.82  0  0    3    4
```

We can also sort the dataframe using more than one column values 
eg sort all the cars by cylinder number in descending order and if cars have the same culinder number then sort by weight in ascending order

```r
arrange(mtcars,desc(cyl),wt)
```

```
##                      mpg cyl  disp  hp drat    wt  qsec vs am gear carb
## Ford Pantera L      15.8   8 351.0 264 4.22 3.170 14.50  0  1    5    4
## AMC Javelin         15.2   8 304.0 150 3.15 3.435 17.30  0  0    3    2
## Hornet Sportabout   18.7   8 360.0 175 3.15 3.440 17.02  0  0    3    2
## Dodge Challenger    15.5   8 318.0 150 2.76 3.520 16.87  0  0    3    2
## Duster 360          14.3   8 360.0 245 3.21 3.570 15.84  0  0    3    4
## Maserati Bora       15.0   8 301.0 335 3.54 3.570 14.60  0  1    5    8
## Merc 450SL          17.3   8 275.8 180 3.07 3.730 17.60  0  0    3    3
## Merc 450SLC         15.2   8 275.8 180 3.07 3.780 18.00  0  0    3    3
## Camaro Z28          13.3   8 350.0 245 3.73 3.840 15.41  0  0    3    4
## Pontiac Firebird    19.2   8 400.0 175 3.08 3.845 17.05  0  0    3    2
## Merc 450SE          16.4   8 275.8 180 3.07 4.070 17.40  0  0    3    3
## Cadillac Fleetwood  10.4   8 472.0 205 2.93 5.250 17.98  0  0    3    4
## Chrysler Imperial   14.7   8 440.0 230 3.23 5.345 17.42  0  0    3    4
## Lincoln Continental 10.4   8 460.0 215 3.00 5.424 17.82  0  0    3    4
## Mazda RX4           21.0   6 160.0 110 3.90 2.620 16.46  0  1    4    4
## Ferrari Dino        19.7   6 145.0 175 3.62 2.770 15.50  0  1    5    6
## Mazda RX4 Wag       21.0   6 160.0 110 3.90 2.875 17.02  0  1    4    4
## Hornet 4 Drive      21.4   6 258.0 110 3.08 3.215 19.44  1  0    3    1
## Merc 280            19.2   6 167.6 123 3.92 3.440 18.30  1  0    4    4
## Merc 280C           17.8   6 167.6 123 3.92 3.440 18.90  1  0    4    4
## Valiant             18.1   6 225.0 105 2.76 3.460 20.22  1  0    3    1
## Lotus Europa        30.4   4  95.1 113 3.77 1.513 16.90  1  1    5    2
## Honda Civic         30.4   4  75.7  52 4.93 1.615 18.52  1  1    4    2
## Toyota Corolla      33.9   4  71.1  65 4.22 1.835 19.90  1  1    4    1
## Fiat X1-9           27.3   4  79.0  66 4.08 1.935 18.90  1  1    4    1
## Porsche 914-2       26.0   4 120.3  91 4.43 2.140 16.70  0  1    5    2
## Fiat 128            32.4   4  78.7  66 4.08 2.200 19.47  1  1    4    1
## Datsun 710          22.8   4 108.0  93 3.85 2.320 18.61  1  1    4    1
## Toyota Corona       21.5   4 120.1  97 3.70 2.465 20.01  1  0    3    1
## Volvo 142E          21.4   4 121.0 109 4.11 2.780 18.60  1  1    4    2
## Merc 230            22.8   4 140.8  95 3.92 3.150 22.90  1  0    4    2
## Merc 240D           24.4   4 146.7  62 3.69 3.190 20.00  1  0    4    2
```

#### summarise()/summarize()
#### group_by()
In most cases, summarise() and group_by() functions are used together when transforming the data. Summarise() creates a new dataframe which contains one column for each grouping variable and one column for each summary statistics.\

eg summarize the mean and count statistics of fuel consumption for cars without grouping

```r
summarise(mtcars,mean=mean(mpg),count=n())
```

```
##       mean count
## 1 20.09062    32
```

eg first group by the number of cylinders then summarize the mean and count statistics of fuel consumption for cars

```r
mtcars %>%
  group_by(cyl) %>%
  summarise(mean=mean(mpg),count=n())
```

```
## # A tibble: 3 × 3
##     cyl  mean count
##   <dbl> <dbl> <int>
## 1     4  26.7    11
## 2     6  19.7     7
## 3     8  15.1    14
```

we can also group by more than one variables\
eg gourp by number of cylinders and weight and then summarize the mean and count statistics of fuel consumption for cars.

```r
mtcars %>%
  group_by(cyl,wt) %>%
  summarise(mean=mean(mpg),count=n())
```

```
## # A tibble: 30 × 4
## # Groups:   cyl [3]
##      cyl    wt  mean count
##    <dbl> <dbl> <dbl> <int>
##  1     4  1.51  30.4     1
##  2     4  1.62  30.4     1
##  3     4  1.84  33.9     1
##  4     4  1.94  27.3     1
##  5     4  2.14  26       1
##  6     4  2.2   32.4     1
##  7     4  2.32  22.8     1
##  8     4  2.46  21.5     1
##  9     4  2.78  21.4     1
## 10     4  3.15  22.8     1
## # … with 20 more rows
```
If we want to perform operations on ungrouped data, use ungroup()

#### rename()
we can use this function to change the column names.\
eg change the qsec to acceleration

```r
rename(mtcars,acceleration=qsec)
```

```
##                      mpg cyl  disp  hp drat    wt acceleration vs am gear carb
## Mazda RX4           21.0   6 160.0 110 3.90 2.620        16.46  0  1    4    4
## Mazda RX4 Wag       21.0   6 160.0 110 3.90 2.875        17.02  0  1    4    4
## Datsun 710          22.8   4 108.0  93 3.85 2.320        18.61  1  1    4    1
## Hornet 4 Drive      21.4   6 258.0 110 3.08 3.215        19.44  1  0    3    1
## Hornet Sportabout   18.7   8 360.0 175 3.15 3.440        17.02  0  0    3    2
## Valiant             18.1   6 225.0 105 2.76 3.460        20.22  1  0    3    1
## Duster 360          14.3   8 360.0 245 3.21 3.570        15.84  0  0    3    4
## Merc 240D           24.4   4 146.7  62 3.69 3.190        20.00  1  0    4    2
## Merc 230            22.8   4 140.8  95 3.92 3.150        22.90  1  0    4    2
## Merc 280            19.2   6 167.6 123 3.92 3.440        18.30  1  0    4    4
## Merc 280C           17.8   6 167.6 123 3.92 3.440        18.90  1  0    4    4
## Merc 450SE          16.4   8 275.8 180 3.07 4.070        17.40  0  0    3    3
## Merc 450SL          17.3   8 275.8 180 3.07 3.730        17.60  0  0    3    3
## Merc 450SLC         15.2   8 275.8 180 3.07 3.780        18.00  0  0    3    3
## Cadillac Fleetwood  10.4   8 472.0 205 2.93 5.250        17.98  0  0    3    4
## Lincoln Continental 10.4   8 460.0 215 3.00 5.424        17.82  0  0    3    4
## Chrysler Imperial   14.7   8 440.0 230 3.23 5.345        17.42  0  0    3    4
## Fiat 128            32.4   4  78.7  66 4.08 2.200        19.47  1  1    4    1
## Honda Civic         30.4   4  75.7  52 4.93 1.615        18.52  1  1    4    2
## Toyota Corolla      33.9   4  71.1  65 4.22 1.835        19.90  1  1    4    1
## Toyota Corona       21.5   4 120.1  97 3.70 2.465        20.01  1  0    3    1
## Dodge Challenger    15.5   8 318.0 150 2.76 3.520        16.87  0  0    3    2
## AMC Javelin         15.2   8 304.0 150 3.15 3.435        17.30  0  0    3    2
## Camaro Z28          13.3   8 350.0 245 3.73 3.840        15.41  0  0    3    4
## Pontiac Firebird    19.2   8 400.0 175 3.08 3.845        17.05  0  0    3    2
## Fiat X1-9           27.3   4  79.0  66 4.08 1.935        18.90  1  1    4    1
## Porsche 914-2       26.0   4 120.3  91 4.43 2.140        16.70  0  1    5    2
## Lotus Europa        30.4   4  95.1 113 3.77 1.513        16.90  1  1    5    2
## Ford Pantera L      15.8   8 351.0 264 4.22 3.170        14.50  0  1    5    4
## Ferrari Dino        19.7   6 145.0 175 3.62 2.770        15.50  0  1    5    6
## Maserati Bora       15.0   8 301.0 335 3.54 3.570        14.60  0  1    5    8
## Volvo 142E          21.4   4 121.0 109 4.11 2.780        18.60  1  1    4    2
```

### Part Three: tidyr
There are 2 key functions that help transform dataset.\
1.<b>pivot_longer</b>: Increase the number of rows and decrease the number of columns\
2.<b>pivot_wider</b>: The opposite of pivot_longer.\

#### pivot_longer()
One of the most commom problem with dataset is that the some column names are not the variable names, but values of a variable. To deal with this case, we use pivot_longer to transform the dataset.\
eg in table4a, the column "1999" and "2000" are not variables but they are values of variable "year, so we use pivot_longer to change it.

```r
table4a
```

```
## # A tibble: 3 × 3
##   country     `1999` `2000`
## * <chr>        <int>  <int>
## 1 Afghanistan    745   2666
## 2 Brazil       37737  80488
## 3 China       212258 213766
```

```r
pivot_longer(table4a,c(`1999`, `2000`), names_to = "year", values_to = "cases")
```

```
## # A tibble: 6 × 3
##   country     year   cases
##   <chr>       <chr>  <int>
## 1 Afghanistan 1999     745
## 2 Afghanistan 2000    2666
## 3 Brazil      1999   37737
## 4 Brazil      2000   80488
## 5 China       1999  212258
## 6 China       2000  213766
```

#### Pivot_wider()
This function is the opposite of pivot_longer. Instead of increasing the number of rows, it decreases the number of rows but increases the number of columns. We normally use it when an observation is scattered across multiple rows.\
eg in table2, an observation is a county in a year, but each observation across two row,and we want to transform it such at each county in a year only has one row.

```r
table2
```

```
## # A tibble: 12 × 4
##    country      year type            count
##    <chr>       <int> <chr>           <int>
##  1 Afghanistan  1999 cases             745
##  2 Afghanistan  1999 population   19987071
##  3 Afghanistan  2000 cases            2666
##  4 Afghanistan  2000 population   20595360
##  5 Brazil       1999 cases           37737
##  6 Brazil       1999 population  172006362
##  7 Brazil       2000 cases           80488
##  8 Brazil       2000 population  174504898
##  9 China        1999 cases          212258
## 10 China        1999 population 1272915272
## 11 China        2000 cases          213766
## 12 China        2000 population 1280428583
```

```r
pivot_wider(table2,names_from = type,values_from = count)
```

```
## # A tibble: 6 × 4
##   country      year  cases population
##   <chr>       <int>  <int>      <int>
## 1 Afghanistan  1999    745   19987071
## 2 Afghanistan  2000   2666   20595360
## 3 Brazil       1999  37737  172006362
## 4 Brazil       2000  80488  174504898
## 5 China        1999 212258 1272915272
## 6 China        2000 213766 1280428583
```
#### Note: 
pivot_longer makes dataframe narrower and longer, while pivot_wider makes dataframe wider and shorter, so they are actually complements.

### Part Four: Example
In this part, we will use an example to show how those functions really work in transforming the dataset.\
The dataset we will be using is seattlepets in the openintro package.\
The goal is to find the dog names and cat names and decide which names are more popular for dogs and for cats.

```r
dogcat <- seattlepets %>%
  filter(species %in% c("Dog","Cat")) %>%
  count(animal_name,species,name='total') %>%
  pivot_wider(id_cols=animal_name,names_from = species,values_from = total) %>%
  rowwise() %>%
  mutate(total=sum(Cat,Dog,na.rm = TRUE),proportion=Dog/total,ratio=Dog/Cat) %>%
  ungroup() %>%
  arrange(desc(total))
dogcat
```

```
## # A tibble: 13,920 × 6
##    animal_name   Cat   Dog total proportion ratio
##    <chr>       <int> <int> <int>      <dbl> <dbl>
##  1 <NA>          406    76   482      0.158 0.187
##  2 Lucy          102   337   439      0.768 3.30 
##  3 Charlie        81   306   387      0.791 3.78 
##  4 Luna          111   244   355      0.687 2.20 
##  5 Bella          82   249   331      0.752 3.04 
##  6 Max            83   186   269      0.691 2.24 
##  7 Daisy          40   221   261      0.847 5.52 
##  8 Molly          54   186   240      0.775 3.44 
##  9 Jack           65   167   232      0.720 2.57 
## 10 Lily           86   146   232      0.629 1.70 
## # … with 13,910 more rows
```
#### Explanation:
1. use the filter function to find all animal names whose species are dog or cat.\
2. find the total number for each animal name using the count function.\
3. use pivot_wider to expand the dataframe to get the count of each name for dog and cat.\
4. add new columns total,proportion and raio using mutate().\
5. reorder the datafram by total in descending order using arrange().\
6. notice that there are some NAs in dog and cat columns. We can use na.rm to avoid it.

### Summary
The motivation of this project is to create a guide to future 5702 students who don't have much experience with R. I personally don't have much experience with R before taking this class, so when I was doing the problem sets, I kind struggled a little bit. I want to create this cheat sheet so it can help future students get familiar with R. In this project, I mainly talk about three parts. The first part is about importing data. I discussed three most common ways that people use to import data: package, online website, github. The second part is dplyr package. This is one of the most useful packages in R. It contains a variety of functions that help transform the data. I illustrate 7 key functions in the package by giving some simple examples. I'm not giving complicated examples because this cheat sheet is for students who don't have much experience with R. The last part is another package "tidyr", also one of the most important packages in R. It allows to create tidy data. Two functions are mainly talked about in this part. Finally, I give an example step by step using the previous functions to show how to use them in analyzing a real problem. Apparently, this cheat sheet is only for R beginners because the stuff it covers is really simple. I only talk about packages and functions I used before. Of course, there are more useful functions and packages not covered in this cheat sheet. For people who want to know more information, please refer to the following links in the preferences. If I will do it again next time, I will add more details and more advanced uses of the previous stuff.

### References 
https://r4ds.had.co.nz/transform.html \
https://dplyr.tidyverse.org/ \
https://r4ds.had.co.nz/tidy-data.html#tidy-data-1 \
https://tidyr.tidyverse.org/

