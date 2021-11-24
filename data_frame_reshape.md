# Data Frame Reshape

Jingwen Bai




### Introduction

In this tutorial we will focusing on the reshape of a data frame in R using pacakges `reshape2` and `tidyr`.
First, we need to know what are wide-format data or long-format data. Wide data has a column for each variable. While long data using all variable as values.

#### Build a simple data frame

We created a simple wide data `df`, where it has a column for each variable. 


```r
df <- data.frame(
  #x = c(1, 2, 3), 
 player=c('A', 'B', 'C', 'D'),
 #gender=c('F', 'M', 'F', 'M'),
 classYear=c(2, 4, 3, 3),
 year1=c(12, 15, 19, 19),
 year2=c(22, 29, 18, 12),
 year3=c(17, 17, 22, 25),check.names = FALSE)
head(df)
```

### Convert wide-format data to long-format data

#### Method 1: Use melt() in package `reshape2` 

Melt takes wide-format data and melts it into long-format data.
Default parameter:


```r
library(reshape2)
df_melt <- reshape2::melt(df)
df_melt
```
ID variables are the variables that. By default, melt has assumed that all columns with numeric values are variables with values. So here we have `player`   as id variables.



```r
# assign variable and value's column name 
library(reshape2)
df_melt_name <- reshape2::melt(df,id.vars = c("player"), variable.name = "year",value.name = "value")
df_melt_name
```
Now lets try combined ID variables

```r
df_melt_multi <- reshape2::melt(df,id.vars = c("player" , 'classYear'), 
                               variable.name = "year")
df_melt_multi
```

#### Method 2: Use gather() in tidyr 

The gather() function from the tidyr package can be used to “gather” a key-value pair across multiple columns.


```r
#gather data from columns except player column
df_gather <- tidyr::gather(data = df,key = 'year', value = 'value', -player) 

df_gather
```


Now, let's try gather values from more than two columns


```r
df_gather_multi <- tidyr::gather(data = df,key = 'year', value = 'value', 3:5)
# df_gather <- tidyr::gather(data = df,key = 'year', value = 'value', -x) <- same 

df_gather_multi
```

### Convert long-format data to wide-format data
Now we have learned how to convert from wide-format data to long-format data. Now let's try the inverse
#### Method 1: Use dcast() in package `reshape2` 
The dcast formula takes the form LHS ~ RHS.


```r
df_cast <- reshape2::dcast(df_melt, player~variable,value.var = 'value')
head(df_cast)
```

Now let's revert the `df_melt_multi`

```r
df_cast_muli <- reshape2::dcast(df_melt_multi, player + classYear ~ year,value.var = 'value')
head(df_cast)
```

#### Method 2: Use spread() in package `tidyr`


```r
df_spread <- tidyr::spread(df_gather,year,value)
head(df_spread)
```

Revert the `df_gather_multi` using `spread()`:

`spread()` doesn't like `dcast()`, we don't have to consider which columns are used in gathering and what columns are the ID variables , we only need to specidy the columns name of key and value. 



```r
df_spread <- tidyr::spread(df_gather_multi, year,value)
head(df_spread)
```
