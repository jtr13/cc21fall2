# Downloading files

Aaron Aknin and Ashkan Bozorgzad





So this Section is about how do you use r to download files. It is important to use the right method when importing a dataset in order to optimize its use. 

## Get/set your working directory

* A basic component of working with data is knowing your working directory
* The two main commands are ```getwd()``` and ```setwd()```. 
* Be aware of relative versus absolute paths

## Checking for and creating directories

`file.exists ("directoryName")` will check to see if the directory exists and `dir.create ("directoryName")` will create a directory if it doesn't exist. Here is an example checking for a "data" directory and creating it if it doesn't exist.


```r
if (!file.exists("data")){
        dir.create("data")
        }
```


## Download a file from the web

* Download a file from the internet
* Even if you could do this by hand, helps with reproducibility
* Important parameters are _url_, _destfile_, _method_
* Useful for downloading tab-delimited, csv, and other files



The method that we're going to use is `curl`. This is necessary because this website is an https, secure website, and so if you're doing this from a Mac, you need to specify the method is curl in order for it to work. If you list the files in this data directory, You see that we now have one file in that directory, and it's the cameras.csv file.


```r
list.files( "./data" )
```

```
## [1] "output.csv"
```

An important component of downloading files from the internet is that those files might change. So you want to keep track of the date that you downloaded the data, and you can do that with the date function. So you just assign to dateDownloaded the command date and that will give you the date that those data were downloaded.


```r
dateDownloaded <- date()
dateDownloaded
```

```
## [1] "Sat Nov  6 04:04:20 2021"
```

## Reading Local Files

* Loading flat files - read.table().
* This is the main function for reading data into R. 
* Flexible and robust but requires more parameters. 
* Reads the data into RAM so big data can cause problems.


```r
df <- read.table( "resources/downloading_files/output.csv" , sep = ",",header= TRUE )
head(df)
```

```
##   year industry_code_ANZSIC              industry_name_ANZSIC rme_size_grp
## 1 2011                    A Agriculture, Forestry and Fishing          a_0
## 2 2011                    A Agriculture, Forestry and Fishing          a_0
## 3 2011                    A Agriculture, Forestry and Fishing          a_0
## 4 2011                    A Agriculture, Forestry and Fishing          a_0
## 5 2011                    A Agriculture, Forestry and Fishing          a_0
## 6 2011                    A Agriculture, Forestry and Fishing          a_0
##                                          variable value              unit
## 1                                   Activity unit 46134             COUNT
## 2                          Rolling mean employees     0             COUNT
## 3                         Salaries and wages paid   279 DOLLARS(millions)
## 4 Sales, government funding, grants and subsidies  8187 DOLLARS(millions)
## 5                                    Total income  8866 DOLLARS(millions)
## 6                               Total expenditure  7618 DOLLARS(millions)
```

You can also use read.csv in the case that you have a csv file, it automatically sets sep equal to the quote comma and it automatically sets header = TRUE. 


```r
df <- read.csv( "resources/downloading_files/output.csv")
head(df)
```

```
##   year industry_code_ANZSIC              industry_name_ANZSIC rme_size_grp
## 1 2011                    A Agriculture, Forestry and Fishing          a_0
## 2 2011                    A Agriculture, Forestry and Fishing          a_0
## 3 2011                    A Agriculture, Forestry and Fishing          a_0
## 4 2011                    A Agriculture, Forestry and Fishing          a_0
## 5 2011                    A Agriculture, Forestry and Fishing          a_0
## 6 2011                    A Agriculture, Forestry and Fishing          a_0
##                                          variable value              unit
## 1                                   Activity unit 46134             COUNT
## 2                          Rolling mean employees     0             COUNT
## 3                         Salaries and wages paid   279 DOLLARS(millions)
## 4 Sales, government funding, grants and subsidies  8187 DOLLARS(millions)
## 5                                    Total income  8866 DOLLARS(millions)
## 6                               Total expenditure  7618 DOLLARS(millions)
```

### Some more important parameters

* quote - you can tell R whether there are any quoted values quote="" means no quotes.
* na.strings - set the character that represents a missing value.
* nrows - how many rows to read of the file (e.g. nrows=10 reads 10 lines).
* skip- number of lines to skip before starting to read


## Reading XML

* Extensible markup language
* Frequently used to store structured data
* Particularly widely used in internet applications
* Extracting XML is the basis for most web scraping
* Components
   * Markup - labels that give the text structure
   * Content - the actual text of the document



```r
fileURL<-"https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2Frestaurants.xml"
doc <- xmlTreeParse(sub("s", "", fileURL), useInternal = TRUE)
rootNode <- xmlRoot(doc)

xmlName(rootNode)
```

```
## [1] "response"
```

```r
rootNode[[1]][[1]]
```

```
## <row _id="1" _uuid="93CACF6F-C8C2-4B87-95A8-8177806D5A6F" _position="1" _address="http://data.baltimorecity.gov/resource/k5ry-ef3g/1">
##   <name>410</name>
##   <zipcode>21206</zipcode>
##   <neighborhood>Frankford</neighborhood>
##   <councildistrict>2</councildistrict>
##   <policedistrict>NORTHEASTERN</policedistrict>
##   <location_1 human_address="{&quot;address&quot;:&quot;4509 BELAIR ROAD&quot;,&quot;city&quot;:&quot;Baltimore&quot;,&quot;state&quot;:&quot;MD&quot;,&quot;zip&quot;:&quot;&quot;}" needs_recoding="true"/>
## </row>
```

## Reading JSON

* Javascript Object Notation
* Lightweight data storage
* Common format for data from application programming interfaces (APIs)
* Similar structure to XML but different syntax/format
* Data stored as
  * Numbers (double)
  * Strings (double quoted)
  * Boolean (_true_ or _false_)
  * Array (ordered, comma separated enclosed in square brackets _[]_)
  * Object (unorderd, comma separated collection of key:value pairs in curley brackets _{}_)


```r
# extracting data from the website
jsonData <- fromJSON("https://data.ny.gov/api/views/9a8c-vfzj/rows.json?accessType=DOWNLOAD")
# extract the data node
food_market <- jsonData[['data']]
# assembling the data into data frames

food_market[1,19]
```

```
## [1] "GREENVILLE"
```

The `httr` package allows to connect to websites and to connect to APIs. It allows, when a `GET` request is made (a request to access the result of a search), to retrieve the result in the form of a text to be reworked. In general, a call to an API via `httr` is made as follows:


```r
url <- "https://world.openfoodfacts.org/api/v0/product/3017620425400.json"

results <- 
  httr::content(
    httr::GET(url),             # url to query
    as="text",                  # type of the output
    httr::content_type_json(),  # type of the answer
    encoding= "UTF-8"           # encoding of the answer
  )

jsonData <-fromJSON(results)
```

## Webscraping

* It can be a great way to get data 
* Many websites have information you may want to programaticaly read
* In some cases this is against the terms of service for the website
* Attempting to read too many pages too quickly can get your IP address blocked

In order to retrieve data from a web page we can use the `rvest` package. 

In order to begin parsing a web page, we must first request this data from the computer server that contains it. In `rvest`, the function that does this is the `read_html()` function. For this tutorial we will use a weather website, the National Weather Service website.


```r
page <- read_html("https://forecast.weather.gov/MapClick.php?lat=37.7771&lon=-122.4196#.Xl0j6BNKhTY")
page
```

```
## {html_document}
## <html class="no-js">
## [1] <head>\n<meta http-equiv="Content-Type" content="text/html; charset=UTF-8 ...
## [2] <body>\n        <main class="container"><header class="row clearfix" id=" ...
```

The goal being to recover the temperatures, we will search via the developer mode of Google Chrome the identifier of the Html tags where the information is located. Exemple : <p class="temp temp-high">High: 63 °F</p>


```r
results = page  %>% html_nodes(".temp") %>% html_text()
results
```

```
## [1] "Low: 55 °F"  "High: 64 °F" "Low: 50 °F"  "High: 62 °F" "Low: 48 °F" 
## [6] "High: 60 °F" "Low: 52 °F"  "High: 64 °F" "Low: 54 °F"
```

It is hard to read, One way to deal with that is to, as we've seen before is to use the XML package. So again, we could use this same URL. Use the XML package, and parse the HTML again, using the InternalNodes to get the complete structure out. 

## dplyr Pachage

This section is about the dplyr package in R, which is a package specifically designed to help you work with data frames. So in this lecture we will just cover the basics to introduce the package and we'll talk about the verbs arrange, filter, select, mutate and rename.

### Load the dplyr package

The dataset we are going to work is a data set on  air pollution and weather variables in the city of Chicago for the years 1987 to 2005, and it's kind of daily data.


```r
chicago <- readRDS("resources/downloading_files/chicago.rds")
dim(chicago)
```

```
## [1] 6940    8
```

```r
str(chicago)
```

```
## 'data.frame':	6940 obs. of  8 variables:
##  $ city      : chr  "chic" "chic" "chic" "chic" ...
##  $ tmpd      : num  31.5 33 33 29 32 40 34.5 29 26.5 32.5 ...
##  $ dptp      : num  31.5 29.9 27.4 28.6 28.9 ...
##  $ date      : Date, format: "1987-01-01" "1987-01-02" ...
##  $ pm25tmean2: num  NA NA NA NA NA NA NA NA NA NA ...
##  $ pm10tmean2: num  34 NA 34.2 47 NA ...
##  $ o3tmean2  : num  4.25 3.3 3.33 4.38 4.75 ...
##  $ no2tmean2 : num  20 23.2 23.8 30.4 30.3 ...
```

### Select

Show the dataframe with the first 5 columns

```r
head(select(chicago, 1:5))
```

```
##   city tmpd   dptp       date pm25tmean2
## 1 chic 31.5 31.500 1987-01-01         NA
## 2 chic 33.0 29.875 1987-01-02         NA
## 3 chic 33.0 27.375 1987-01-03         NA
## 4 chic 29.0 28.625 1987-01-04         NA
## 5 chic 32.0 28.875 1987-01-05         NA
## 6 chic 40.0 35.125 1987-01-06         NA
```


```r
names(chicago)[1:3]
```

```
## [1] "city" "tmpd" "dptp"
```
 if we want to look at the columns starting with city and ending with D DPTP, which is the dew point column. I, and I want to include all the columns in between.


```r
head(select(chicago, city:dptp))
```

```
##   city tmpd   dptp
## 1 chic 31.5 31.500
## 2 chic 33.0 29.875
## 3 chic 33.0 27.375
## 4 chic 29.0 28.625
## 5 chic 32.0 28.875
## 6 chic 40.0 35.125
```

you can use the minus sign to say, I want to look at all the columns except for these. The columns indicated by this range. And you can use the select function to just say minus on that city colon dew point sequence. And you'll get all of the columns, except those few columns. 

```r
head(select(chicago, -(city:dptp)))
```

```
##         date pm25tmean2 pm10tmean2 o3tmean2 no2tmean2
## 1 1987-01-01         NA   34.00000 4.250000  19.98810
## 2 1987-01-02         NA         NA 3.304348  23.19099
## 3 1987-01-03         NA   34.16667 3.333333  23.81548
## 4 1987-01-04         NA   47.00000 4.375000  30.43452
## 5 1987-01-05         NA         NA 4.750000  30.33333
## 6 1987-01-06         NA   48.00000 5.833333  25.77233
```

the equivalent code to do this in kind of regular R, without using the deplyr package is a little bit tricky


```r
i <- match("city", names(chicago))
j <- match("dptp", names(chicago))
head(chicago[, -(i:j)])
```

```
##         date pm25tmean2 pm10tmean2 o3tmean2 no2tmean2
## 1 1987-01-01         NA   34.00000 4.250000  19.98810
## 2 1987-01-02         NA         NA 3.304348  23.19099
## 3 1987-01-03         NA   34.16667 3.333333  23.81548
## 4 1987-01-04         NA   47.00000 4.375000  30.43452
## 5 1987-01-05         NA         NA 4.750000  30.33333
## 6 1987-01-06         NA   48.00000 5.833333  25.77233
```

### Verbs
#### filter

The filter function is the next function in deplyr that we'll talk about and it's basically used subset rows based on conditions. So, for example, you might want to take all the rows in the Chicago data set where pm 2.5 is greater than 30


```r
chic.f <- filter(chicago, pm25tmean2 > 30)
head(select(chic.f, 1:3, pm25tmean2), 10)
```

```
##    city tmpd dptp pm25tmean2
## 1  chic   23 21.9      38.10
## 2  chic   28 25.8      33.95
## 3  chic   55 51.3      39.40
## 4  chic   59 53.7      35.40
## 5  chic   57 52.0      33.30
## 6  chic   57 56.0      32.10
## 7  chic   75 65.8      56.50
## 8  chic   61 59.0      33.80
## 9  chic   73 60.3      30.30
## 10 chic   78 67.1      41.40
```

you don't have to just subset rows based on values in one column. You can take multiple columns and create a more complicated logical sequence. here we are looking at pm2.5 greater than 30. As well as temperature greater than 80. 


```r
chic.f <- filter(chicago, pm25tmean2 > 30 & tmpd > 80)
head(select(chic.f, 1:3, pm25tmean2, tmpd), 10)
```

```
##    city tmpd dptp pm25tmean2
## 1  chic   81 71.2    39.6000
## 2  chic   81 70.4    31.5000
## 3  chic   82 72.2    32.3000
## 4  chic   84 72.9    43.7000
## 5  chic   85 72.6    38.8375
## 6  chic   84 72.6    38.2000
## 7  chic   82 67.4    33.0000
## 8  chic   82 63.5    42.5000
## 9  chic   81 70.4    33.1000
## 10 chic   82 66.2    38.8500
```

#### arrange

The next function of range has a simple purpose. It's basically used to reorder the rows of a data frame based on the values of a column. 



```r
chicago <- arrange(chicago, date)
head(select(chicago, date, pm25tmean2), 3)
```

```
##         date pm25tmean2
## 1 1987-01-01         NA
## 2 1987-01-02         NA
## 3 1987-01-03         NA
```

use the tail function to look at the last couple rows

```r
tail(select(chicago, date, pm25tmean2), 3)
```

```
##            date pm25tmean2
## 6938 2005-12-29    7.45000
## 6939 2005-12-30   15.05714
## 6940 2005-12-31   15.00000
```

To  arrange the rows in descending order, the desc function can be used


```r
chicago <- arrange(chicago, desc(date))
head(select(chicago, date, pm25tmean2), 3)
```

```
##         date pm25tmean2
## 1 2005-12-31   15.00000
## 2 2005-12-30   15.05714
## 3 2005-12-29    7.45000
```
use the tail function to look at the last couple rows

```r
tail(select(chicago, date, pm25tmean2), 3)
```

```
##            date pm25tmean2
## 6938 1987-01-03         NA
## 6939 1987-01-02         NA
## 6940 1987-01-01         NA
```

#### rename

The rename function is very simple. it can be used to rename a variable in R.


```r
head(chicago[, 1:5], 3)
```

```
##   city tmpd dptp       date pm25tmean2
## 1 chic   35 30.1 2005-12-31   15.00000
## 2 chic   36 31.0 2005-12-30   15.05714
## 3 chic   35 29.4 2005-12-29    7.45000
```

```r
chicago <- rename(chicago, dewpoint = dptp, pm25 = pm25tmean2)
head(chicago[, 1:5], 3)
```

```
##   city tmpd dewpoint       date     pm25
## 1 chic   35     30.1 2005-12-31 15.00000
## 2 chic   36     31.0 2005-12-30 15.05714
## 3 chic   35     29.4 2005-12-29  7.45000
```

#### mutate

The mutate function is used to simply transform existing variables or to create new variables. So here in this example we want to create a new variable called pm25detrend. And this is the pm25 variable with the mean subtracted off.


```r
chicago <- mutate(chicago, pm25detrend=pm25-mean(pm25, na.rm=TRUE))
head(select(chicago, pm25, pm25detrend))
```

```
##       pm25 pm25detrend
## 1 15.00000   -1.230958
## 2 15.05714   -1.173815
## 3  7.45000   -8.780958
## 4 17.75000    1.519042
## 5 23.56000    7.329042
## 6  8.40000   -7.830958
```


#### group_by

Finally the group by function allows you to split a data frame according to Certain categorical variables.  in this example, we are going to create a temperature category variable which will indicate whether a given day was hot or cold, depending on whether the temperature was over 80 degrees or not.
 

```r
chicago <- mutate(chicago, tempcat = factor(1 * (tmpd > 80), labels = c("cold", "hot")))
hotcold <- group_by(chicago, tempcat)
summarize(hotcold, pm25 = mean(pm25, na.rm = TRUE),
o3 = max(o3tmean2),
no2 = median(no2tmean2))
```

```
## # A tibble: 3 × 4
##   tempcat  pm25    o3   no2
##   <fct>   <dbl> <dbl> <dbl>
## 1 cold     16.0 66.6   24.5
## 2 hot      26.5 63.0   24.9
## 3 <NA>     47.7  9.42  37.4
```

We can also categorize the data set on on other variables. For example we might want to do a summary for each year in the data set. We can create I can use the mutate function to create a year variable.


```r
chicago <- mutate(chicago, year = as.POSIXlt(date)$year + 1900)
years <- group_by(chicago, year)
summarize(years, pm25 = mean(pm25, na.rm = TRUE),
o3 = max(o3tmean2, na.rm = TRUE),
no2 = median(no2tmean2, na.rm = TRUE))
```

```
## # A tibble: 19 × 4
##     year  pm25    o3   no2
##    <dbl> <dbl> <dbl> <dbl>
##  1  1987 NaN    63.0  23.5
##  2  1988 NaN    61.7  24.5
##  3  1989 NaN    59.7  26.1
##  4  1990 NaN    52.2  22.6
##  5  1991 NaN    63.1  21.4
##  6  1992 NaN    50.8  24.8
##  7  1993 NaN    44.3  25.8
##  8  1994 NaN    52.2  28.5
##  9  1995 NaN    66.6  27.3
## 10  1996 NaN    58.4  26.4
## 11  1997 NaN    56.5  25.5
## 12  1998  18.3  50.7  24.6
## 13  1999  18.5  57.5  24.7
## 14  2000  16.9  55.8  23.5
## 15  2001  16.9  51.8  25.1
## 16  2002  15.3  54.9  22.7
## 17  2003  15.2  56.2  24.6
## 18  2004  14.6  44.5  23.4
## 19  2005  16.2  58.8  22.6
```

#### %>%

The dplyr package implements a special operator. That allows you to chain different operations. It allows you to see what operations are happening in a readable way. it's indicated by a percent symbol and then the greater than symbol and then the percent symbol. We will call it the pipeline operator. The idea it that you take a data set and you feed through a pipeline of operations to create a new data set. We have the Chicago data set and we want to mutate to create a month variable because we want to create a summary of each of the pollutant variables by month. Then we want to take the output of mutate. Then group by it use according to this month variable. finally we want to take the output of group by and then run it through summarize.



```r
chicago %>% mutate(month = as.POSIXlt(date)$mon + 1) %>% group_by(month) %>%  summarize(pm25 = mean(pm25, na.rm = TRUE),
    o3 = max(o3tmean2, na.rm = TRUE),
    no2 = median(no2tmean2, na.rm = TRUE))
```

```
## # A tibble: 12 × 4
##    month  pm25    o3   no2
##    <dbl> <dbl> <dbl> <dbl>
##  1     1  17.8  28.2  25.4
##  2     2  20.4  37.4  26.8
##  3     3  17.4  39.0  26.8
##  4     4  13.9  47.9  25.0
##  5     5  14.1  52.8  24.2
##  6     6  15.9  66.6  25.0
##  7     7  16.6  59.5  22.4
##  8     8  16.9  54.0  23.0
##  9     9  15.9  57.5  24.5
## 10    10  14.2  47.1  24.2
## 11    11  15.2  29.5  23.6
## 12    12  17.5  27.7  24.5
```

### Connecting to SQL DataBase 

This part will teach us how to connect a SQL database with R and submit queries to it. For this we need `dbplyr` and `RSQLite` packages. 

Retrieve the SQL file the way you want. In our case we will retrieve it from a url and stock it in the data folder.


```r
download.file(url = "https://ndownloader.figshare.com/files/2292171", destfile = "data/db_sql.sqlite", mode = "wb")
```

We then connect the R terminal with the SQL database. 


```r
db <- DBI::dbConnect(RSQLite::SQLite(), "resources/downloading_files/db_sql.sqlite")
```

#### Querying the database with the SQL syntax

The `sql` function allows us to submit queries to the database using the SQL language. 


```r
tbl(db, sql("SELECT year, species_id, plot_id FROM surveys"))
```

```
## # Source:   SQL [?? x 3]
## # Database: sqlite 3.36.0
## #   [/home/runner/work/cc21fall2/cc21fall2/resources/downloading_files/db_sql.sqlite]
##     year species_id plot_id
##    <int> <chr>        <int>
##  1  1977 NL               2
##  2  1977 NL               3
##  3  1977 DM               2
##  4  1977 DM               7
##  5  1977 DM               3
##  6  1977 PF               1
##  7  1977 PE               2
##  8  1977 DM               1
##  9  1977 DM               1
## 10  1977 PF               6
## # … with more rows
```

#### Querying the database with the dplyr syntax

The same result can be achieved by using the dplyr syntax.


```r
surveys <- tbl(db, "surveys")
surveys %>% select(year, species_id, plot_id)
```

```
## # Source:   lazy query [?? x 3]
## # Database: sqlite 3.36.0
## #   [/home/runner/work/cc21fall2/cc21fall2/resources/downloading_files/db_sql.sqlite]
##     year species_id plot_id
##    <int> <chr>        <int>
##  1  1977 NL               2
##  2  1977 NL               3
##  3  1977 DM               2
##  4  1977 DM               7
##  5  1977 DM               3
##  6  1977 PF               1
##  7  1977 PE               2
##  8  1977 DM               1
##  9  1977 DM               1
## 10  1977 PF               6
## # … with more rows
```

### Other benefit of dplyr

* dplyr can work with other data frame “backends” 
* data.table for large fast tables
* SQL interface for relational databases via the DBI package
