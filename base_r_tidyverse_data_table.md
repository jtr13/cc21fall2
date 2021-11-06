# Comparison among base R, tidyverse, and datatable

Siyue Han


```r
# Load the tidyverse package
library(tidyverse)
# Load the data.table package
library(data.table)
```

## Introduction
There are many ways to read and analyze data in R, the `data.frame` provided in base R can handle most of the situations. Therefore, I have been using it for most of the time so far and occasionally used `tibble` from `tidyverse`. But one time when I was dealing with a large csv, I found it was so slow with `data.frame`. With the help of google, I used `data.table` for the first time, and it was amazing. Therefore, I'd like to share this way of reading and analyzing data to more people.

## Reading Data

First, let's see the performance of reading csv data among these three environments.

### Data.Frame

This is an example of reading csv into a data.frame.


```r
start <- Sys.time()
df <- read.csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv")
end <- Sys.time()
print(end - start)
```

```
## Time difference of 1.295147 secs
```

### Tibble

This is an example of reading csv into a tibble.


```r
start <- Sys.time()
tb <- read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv")
end <- Sys.time()
print(end - start)
```

```
## Time difference of 0.8497355 secs
```

### Data.Table

This is an example of reading csv into a data.table.


```r
start <- Sys.time()
dt <- fread("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv")
end <- Sys.time()
print(end - start)
```

```
## Time difference of 0.1946497 secs
```

As we can see, `data.table` can read a csv file super fast, especially when the file is large. `tibble` in `tidyverse` is slightly faster than `data.frame` in base R, but is still much slower than `data.table`.

## Processing Data

Then, let's see the differences of processing data among these three environments.

### Selecting column(s) and row(s)


```r
start <- Sys.time()
x1 <- df[101:110, c('Lat', 'Long_')]
end <- Sys.time()
print(end - start)
```

```
## Time difference of 0.00269413 secs
```

```r
start <- Sys.time()
x2 <- select(tb, Lat, Long_) %>% slice(101:110)
end <- Sys.time()
print(end - start)
```

```
## Time difference of 0.01958704 secs
```

```r
start <- Sys.time()
x3 <- dt[101:110, .(Lat, Long_)]
end <- Sys.time()
print(end - start)
```

```
## Time difference of 0.01444721 secs
```

### Filtering row(s)


```r
start <- Sys.time()
x1 <- df[df$`X10.31.21` > 500000,]
end <- Sys.time()
print(end - start)
```

```
## Time difference of 0.02132368 secs
```

```r
start <- Sys.time()
x2 <- filter(tb, `10/31/21` > 500000)
end <- Sys.time()
print(end - start)
```

```
## Time difference of 0.01430535 secs
```

```r
start <- Sys.time()
x3 <- dt[`10/31/21` > 500000,]
end <- Sys.time()
print(end - start)
```

```
## Time difference of 0.003150463 secs
```

### Sorting the table

```r
start <- Sys.time()
x1 <- df[order(-df$`X10.31.21`), ]
end <- Sys.time()
print(end - start)
```

```
## Time difference of 0.01976466 secs
```

```r
start <- Sys.time()
x2 <- arrange(tb, -`10/31/21`)
end <- Sys.time()
print(end - start)
```

```
## Time difference of 0.03271651 secs
```

```r
start <- Sys.time()
x3 <- dt[order(-`10/31/21`), ]
end <- Sys.time()
print(end - start)
```

```
## Time difference of 0.1771774 secs
```

### Summarizing columns by group

```r
start <- Sys.time()
x1 <- aggregate(df$`X10.31.21`, list(df$Province_State), sum)
end <- Sys.time()
print(end - start)
```

```
## Time difference of 0.007216692 secs
```

```r
start <- Sys.time()
x2 <- group_by(tb, Province_State) %>% summarise(sum(`10/31/21`))
end <- Sys.time()
print(end - start)
```

```
## Time difference of 0.02284217 secs
```

```r
start <- Sys.time()
x3 <- dt[ , lapply(.(`10/31/21`), sum), by = Province_State] 
end <- Sys.time()
print(end - start)
```

```
## Time difference of 0.004267931 secs
```

### Pivoting longer

```r
start <- Sys.time()
x1 <- reshape(df, 
              varying = 12:dim(df)[2],
              timevar = "Date", v.names="Cases",
              direction = "long")
x1 <- x1[, c('Combined_Key', 'Date', 'Cases')]
end <- Sys.time()
print(end - start)
```

```
## Time difference of 17.64273 secs
```

```r
start <- Sys.time()
x2 <- pivot_longer(tb, 
                   names_to = "Date", 
                   values_to = "Cases", 
                   -(1:11)) %>%
      select(Combined_Key, Date, Cases)
end <- Sys.time()
print(end - start)
```

```
## Time difference of 1.070366 secs
```

```r
start <- Sys.time()
x3 <- melt(dt, 
           id.vars = 1:11, 
           variable.name = "Date", 
           value.name = "Cases")[
             , .(Combined_Key, Date, Cases)]
end <- Sys.time()
print(end - start)
```

```
## Time difference of 1.012232 secs
```

### Joining tables

```r
start <- Sys.time()
x1 <- merge(df[, 1:11], x1)
end <- Sys.time()
print(end - start)
```

```
## Time difference of 25.52823 secs
```

```r
start <- Sys.time()
x2 <- left_join(select(tb, 1:11), x2, by = "Combined_Key")
end <- Sys.time()
print(end - start)
```

```
## Time difference of 1.356773 secs
```

```r
start <- Sys.time()
x3 <- dt[, 1:11][x3, on = "Combined_Key"]
end <- Sys.time()
print(end - start)
```

```
## Time difference of 1.044259 secs
```

### Chaining structures
Base R does not have chaining structure like the `tidyverse` or `data.table`. Here we compare chaining structures in `tidyverse` and `data.table`.
The `tidyverse` uses `%>%` to connect operations together.
The `data.table` uses bracketed operations back to back as `[...][...]`. 

```r
start <- Sys.time()
x2 <- tb %>% 
      mutate(year = `10/31/21` - `10/31/20`) %>% 
      group_by(Province_State) %>% 
      summarise(year = sum(year)) %>% 
      arrange(-year)

end <- Sys.time()
print(end - start)
```

```
## Time difference of 0.03047562 secs
```

```r
start <- Sys.time()
x3 <- dt[, year := `10/31/21` - `10/31/20`, ][
         order(-year), .(year = sum(year)), by = Province_State]
end <- Sys.time()
print(end - start)
```

```
## Time difference of 0.006450891 secs
```

From all the above, we can see that when doing simple operations such as selecting, filtering and sorting, Base R can finish very fast. However, when doing complex operations such as pivoting and joining, Base R will cost huge amount of time. Comparing `tidyverse` and `data.table`, we can see that `data.table` have slightly faster speed than `tidyverse` in almost every task. Especially, when using chaining structure, `data.table` finishes much faster than `tidyverse`. This is probably because `data.table` includes many different operations together in one bracketed operation. In the above example, it use one bracketed operation to do the `group_by`, `summarise` and `arrange` task in `tidyverse`. On the other hand, since `tidyverse` does only one task in each function, and what task a function will do is easy to understand through its name, the code in `tidyverse` is more readable than in `data.table`.

## Summary of key functions

|Environment	| base	      | tidyverse	  | data.table  | 
| ----------- | ----------- | ----------- | ----------- |
|Supported data class	| data.frame	| tibble	| data.table|
|Reading data	        | read.csv	| read_csv	| fread|
|Subset by column	    | [ , ...]	| select()	| [ ,... , ]|
|Subset by rows	      | [... , ]	| filter()	| [... , , ]|
|Create new column	  | df\$y = ...	| mutate(tb, y = ...)	| [ , y := ..., ]|
|Delete a column	    | df\$y = NULL	| select(tb, -y)	| [ , y := NULL, ]|
|Summarize	          | apply(df[ , y], 2, ...)	| summarise()	| [ , ...(y), ]|
|Grouping	            | aggregate()	| group_by()	| [ , , by = ...]|
|Pivot to long	      | reshape()	| pivot_longer()	| melt()|
|Pivot to wide	      | reshape()	| pivot_wider()	| dcast()|
|Joining tables	      | merge()	| left_join()	| dt1[dt2, on = ...]|

## Conclusion
The motivation for this project is that one day when I was dealing with a large csv, I found it was so slow with `data.frame`. With the help of google, I used `data.table` for the first time, and it was amazing. Therefore, I'd like to compare its performance with that of `base R` and `tidyverse` when reading and analyzing data.

From this project, I learned how to use `data.table` to analyze data. Also I learned the advantage of using each of the three ways. `data.frame` in base R is the most convenient and easy way to deal with data analytics tasks, but it takes too much time when the data is large or the operation is complex. Therefore, in such cases, it would be better to use `data.table` and `tidyverse`. In cases when we are handling very large dataset, `data.table` would be a good choice since it runs extremely fast. In cases when we are not requiring the speed so much, especially when collaborating with others, we can choose `tidyverse` since its code is more readable.

## Reference
[1] https://cran.r-project.org/web/packages/data.table/vignettes/datatable-intro.html

[2] https://megapteraphile.wordpress.com/2020/03/25/data-frame-vs-data-table-vs-tibble-in-r/

[3] https://mgimond.github.io/rug_2019_12/Index.html
