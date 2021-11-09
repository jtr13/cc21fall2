# Tidyverse Cheatsheet

Huaizhi Ge




```r
library(tidyverse)
```

## Introduction

Usually, before we plot the data, we need to preprocess the data first. And we use tidyverse to process data commonly. And I find myself can not remember all the tidyverse functions to deal with the data. So I create a cheat sheet that includes some commonly used functions in tidyverse to process the data. 

reference:
https://www.rdocumentation.org/,
https://dplyr.tidyverse.org/index.html


## select()

To select some columns in the data, we only need to add the names of columns to the Select() function.
(Use dataset "mpg" as an example dataset.)

```r
mpg %>% 
  select(year,manufacturer,model)
```

```
## # A tibble: 234 × 3
##     year manufacturer model     
##    <int> <chr>        <chr>     
##  1  1999 audi         a4        
##  2  1999 audi         a4        
##  3  2008 audi         a4        
##  4  2008 audi         a4        
##  5  1999 audi         a4        
##  6  1999 audi         a4        
##  7  2008 audi         a4        
##  8  1999 audi         a4 quattro
##  9  1999 audi         a4 quattro
## 10  2008 audi         a4 quattro
## # … with 224 more rows
```

Also, we can use start_col:end_col.

```r
mpg %>% 
  select(year:drv)
```

```
## # A tibble: 234 × 4
##     year   cyl trans      drv  
##    <int> <int> <chr>      <chr>
##  1  1999     4 auto(l5)   f    
##  2  1999     4 manual(m5) f    
##  3  2008     4 manual(m6) f    
##  4  2008     4 auto(av)   f    
##  5  1999     6 auto(l5)   f    
##  6  1999     6 manual(m5) f    
##  7  2008     6 auto(av)   f    
##  8  1999     4 manual(m5) 4    
##  9  1999     4 auto(l5)   4    
## 10  2008     4 manual(m6) 4    
## # … with 224 more rows
```

We can select columns that have the same structure using starts_with(),end_with() or contains().


```r
mpg %>% 
  select(starts_with("m"),contains("c"),ends_with("y"))
```

```
## # A tibble: 234 × 6
##    manufacturer model        cyl   cty class     hwy
##    <chr>        <chr>      <int> <int> <chr>   <int>
##  1 audi         a4             4    18 compact    29
##  2 audi         a4             4    21 compact    29
##  3 audi         a4             4    20 compact    31
##  4 audi         a4             4    21 compact    30
##  5 audi         a4             6    16 compact    26
##  6 audi         a4             6    18 compact    26
##  7 audi         a4             6    18 compact    27
##  8 audi         a4 quattro     4    18 compact    26
##  9 audi         a4 quattro     4    16 compact    25
## 10 audi         a4 quattro     4    20 compact    28
## # … with 224 more rows
```

select_if() can be used to select columns that have a specific data type. For example, select_if(is.character) can select all the character type columns. Similarly, we can use is.numeric, is.integer, is.factor and so on.


```r
mpg %>% 
  select_if(is.numeric)
```

```
## # A tibble: 234 × 5
##    displ  year   cyl   cty   hwy
##    <dbl> <int> <int> <int> <int>
##  1   1.8  1999     4    18    29
##  2   1.8  1999     4    21    29
##  3   2    2008     4    20    31
##  4   2    2008     4    21    30
##  5   2.8  1999     6    16    26
##  6   2.8  1999     6    18    26
##  7   3.1  2008     6    18    27
##  8   1.8  1999     4    18    26
##  9   1.8  1999     4    16    25
## 10   2    2008     4    20    28
## # … with 224 more rows
```

select_if() can select the columns that meet some conditions.


```r
mpg %>% select(where(is.numeric)) %>% 
  select(where(~mean(.)<100))
```

```
## # A tibble: 234 × 4
##    displ   cyl   cty   hwy
##    <dbl> <int> <int> <int>
##  1   1.8     4    18    29
##  2   1.8     4    21    29
##  3   2       4    20    31
##  4   2       4    21    30
##  5   2.8     6    16    26
##  6   2.8     6    18    26
##  7   3.1     6    18    27
##  8   1.8     4    18    26
##  9   1.8     4    16    25
## 10   2       4    20    28
## # … with 224 more rows
```

## filter()

We can use filter() to choose certain rows.


```r
mpg %>% 
  filter(year==1999)
```

```
## # A tibble: 117 × 11
##    manufacturer model     displ  year   cyl trans  drv     cty   hwy fl    class
##    <chr>        <chr>     <dbl> <int> <int> <chr>  <chr> <int> <int> <chr> <chr>
##  1 audi         a4          1.8  1999     4 auto(… f        18    29 p     comp…
##  2 audi         a4          1.8  1999     4 manua… f        21    29 p     comp…
##  3 audi         a4          2.8  1999     6 auto(… f        16    26 p     comp…
##  4 audi         a4          2.8  1999     6 manua… f        18    26 p     comp…
##  5 audi         a4 quatt…   1.8  1999     4 manua… 4        18    26 p     comp…
##  6 audi         a4 quatt…   1.8  1999     4 auto(… 4        16    25 p     comp…
##  7 audi         a4 quatt…   2.8  1999     6 auto(… 4        15    25 p     comp…
##  8 audi         a4 quatt…   2.8  1999     6 manua… 4        17    25 p     comp…
##  9 audi         a6 quatt…   2.8  1999     6 auto(… 4        15    24 p     mids…
## 10 chevrolet    c1500 su…   5.7  1999     8 auto(… r        13    17 r     suv  
## # … with 107 more rows
```


```r
mpg %>% 
  filter(year!=1999)
```

```
## # A tibble: 117 × 11
##    manufacturer model     displ  year   cyl trans  drv     cty   hwy fl    class
##    <chr>        <chr>     <dbl> <int> <int> <chr>  <chr> <int> <int> <chr> <chr>
##  1 audi         a4          2    2008     4 manua… f        20    31 p     comp…
##  2 audi         a4          2    2008     4 auto(… f        21    30 p     comp…
##  3 audi         a4          3.1  2008     6 auto(… f        18    27 p     comp…
##  4 audi         a4 quatt…   2    2008     4 manua… 4        20    28 p     comp…
##  5 audi         a4 quatt…   2    2008     4 auto(… 4        19    27 p     comp…
##  6 audi         a4 quatt…   3.1  2008     6 auto(… 4        17    25 p     comp…
##  7 audi         a4 quatt…   3.1  2008     6 manua… 4        15    25 p     comp…
##  8 audi         a6 quatt…   3.1  2008     6 auto(… 4        17    25 p     mids…
##  9 audi         a6 quatt…   4.2  2008     8 auto(… 4        16    23 p     mids…
## 10 chevrolet    c1500 su…   5.3  2008     8 auto(… r        14    20 r     suv  
## # … with 107 more rows
```

filter(condition1,condition2) will return the rows that meet the two conditions.


```r
mpg %>% 
  filter(year==1999,cyl==4)
```

```
## # A tibble: 45 × 11
##    manufacturer model   displ  year   cyl trans   drv     cty   hwy fl    class 
##    <chr>        <chr>   <dbl> <int> <int> <chr>   <chr> <int> <int> <chr> <chr> 
##  1 audi         a4        1.8  1999     4 auto(l… f        18    29 p     compa…
##  2 audi         a4        1.8  1999     4 manual… f        21    29 p     compa…
##  3 audi         a4 qua…   1.8  1999     4 manual… 4        18    26 p     compa…
##  4 audi         a4 qua…   1.8  1999     4 auto(l… 4        16    25 p     compa…
##  5 chevrolet    malibu    2.4  1999     4 auto(l… f        19    27 r     midsi…
##  6 dodge        carava…   2.4  1999     4 auto(l… f        18    24 r     miniv…
##  7 honda        civic     1.6  1999     4 manual… f        28    33 r     subco…
##  8 honda        civic     1.6  1999     4 auto(l… f        24    32 r     subco…
##  9 honda        civic     1.6  1999     4 manual… f        25    32 r     subco…
## 10 honda        civic     1.6  1999     4 manual… f        23    29 p     subco…
## # … with 35 more rows
```

filter(condition1|condition2) will return the rows that meet condition1 or condition2.


```r
mpg %>% 
  filter(year==1999|cyl==4)
```

```
## # A tibble: 153 × 11
##    manufacturer model      displ  year   cyl trans drv     cty   hwy fl    class
##    <chr>        <chr>      <dbl> <int> <int> <chr> <chr> <int> <int> <chr> <chr>
##  1 audi         a4           1.8  1999     4 auto… f        18    29 p     comp…
##  2 audi         a4           1.8  1999     4 manu… f        21    29 p     comp…
##  3 audi         a4           2    2008     4 manu… f        20    31 p     comp…
##  4 audi         a4           2    2008     4 auto… f        21    30 p     comp…
##  5 audi         a4           2.8  1999     6 auto… f        16    26 p     comp…
##  6 audi         a4           2.8  1999     6 manu… f        18    26 p     comp…
##  7 audi         a4 quattro   1.8  1999     4 manu… 4        18    26 p     comp…
##  8 audi         a4 quattro   1.8  1999     4 auto… 4        16    25 p     comp…
##  9 audi         a4 quattro   2    2008     4 manu… 4        20    28 p     comp…
## 10 audi         a4 quattro   2    2008     4 auto… 4        19    27 p     comp…
## # … with 143 more rows
```

filter(xor(condition1,condition2)) will return rows that only meet one condition.


```r
mpg %>% 
  filter(xor(year==1999,cyl==4))
```

```
## # A tibble: 108 × 11
##    manufacturer model     displ  year   cyl trans  drv     cty   hwy fl    class
##    <chr>        <chr>     <dbl> <int> <int> <chr>  <chr> <int> <int> <chr> <chr>
##  1 audi         a4          2    2008     4 manua… f        20    31 p     comp…
##  2 audi         a4          2    2008     4 auto(… f        21    30 p     comp…
##  3 audi         a4          2.8  1999     6 auto(… f        16    26 p     comp…
##  4 audi         a4          2.8  1999     6 manua… f        18    26 p     comp…
##  5 audi         a4 quatt…   2    2008     4 manua… 4        20    28 p     comp…
##  6 audi         a4 quatt…   2    2008     4 auto(… 4        19    27 p     comp…
##  7 audi         a4 quatt…   2.8  1999     6 auto(… 4        15    25 p     comp…
##  8 audi         a4 quatt…   2.8  1999     6 manua… 4        17    25 p     comp…
##  9 audi         a6 quatt…   2.8  1999     6 auto(… 4        15    24 p     mids…
## 10 chevrolet    c1500 su…   5.7  1999     8 auto(… r        13    17 r     suv  
## # … with 98 more rows
```

filter_all() will filter all the columns.


```r
mpg %>% 
  filter_all(any_vars(.==4))
```

```
## # A tibble: 164 × 11
##    manufacturer model      displ  year   cyl trans drv     cty   hwy fl    class
##    <chr>        <chr>      <dbl> <int> <int> <chr> <chr> <int> <int> <chr> <chr>
##  1 audi         a4           1.8  1999     4 auto… f        18    29 p     comp…
##  2 audi         a4           1.8  1999     4 manu… f        21    29 p     comp…
##  3 audi         a4           2    2008     4 manu… f        20    31 p     comp…
##  4 audi         a4           2    2008     4 auto… f        21    30 p     comp…
##  5 audi         a4 quattro   1.8  1999     4 manu… 4        18    26 p     comp…
##  6 audi         a4 quattro   1.8  1999     4 auto… 4        16    25 p     comp…
##  7 audi         a4 quattro   2    2008     4 manu… 4        20    28 p     comp…
##  8 audi         a4 quattro   2    2008     4 auto… 4        19    27 p     comp…
##  9 audi         a4 quattro   2.8  1999     6 auto… 4        15    25 p     comp…
## 10 audi         a4 quattro   2.8  1999     6 manu… 4        17    25 p     comp…
## # … with 154 more rows
```

filter_if() first find the columns that meet some condition then filter.


```r
mpg %>% 
  filter_if(is.character,any_vars(.==4))
```

```
## # A tibble: 103 × 11
##    manufacturer model      displ  year   cyl trans drv     cty   hwy fl    class
##    <chr>        <chr>      <dbl> <int> <int> <chr> <chr> <int> <int> <chr> <chr>
##  1 audi         a4 quattro   1.8  1999     4 manu… 4        18    26 p     comp…
##  2 audi         a4 quattro   1.8  1999     4 auto… 4        16    25 p     comp…
##  3 audi         a4 quattro   2    2008     4 manu… 4        20    28 p     comp…
##  4 audi         a4 quattro   2    2008     4 auto… 4        19    27 p     comp…
##  5 audi         a4 quattro   2.8  1999     6 auto… 4        15    25 p     comp…
##  6 audi         a4 quattro   2.8  1999     6 manu… 4        17    25 p     comp…
##  7 audi         a4 quattro   3.1  2008     6 auto… 4        17    25 p     comp…
##  8 audi         a4 quattro   3.1  2008     6 manu… 4        15    25 p     comp…
##  9 audi         a6 quattro   2.8  1999     6 auto… 4        15    24 p     mids…
## 10 audi         a6 quattro   3.1  2008     6 auto… 4        17    25 p     mids…
## # … with 93 more rows
```

filter_at() need to select columns in vars().


```r
mpg %>% 
  filter_at(vars(displ),all_vars(.>3))
```

```
## # A tibble: 126 × 11
##    manufacturer model     displ  year   cyl trans  drv     cty   hwy fl    class
##    <chr>        <chr>     <dbl> <int> <int> <chr>  <chr> <int> <int> <chr> <chr>
##  1 audi         a4          3.1  2008     6 auto(… f        18    27 p     comp…
##  2 audi         a4 quatt…   3.1  2008     6 auto(… 4        17    25 p     comp…
##  3 audi         a4 quatt…   3.1  2008     6 manua… 4        15    25 p     comp…
##  4 audi         a6 quatt…   3.1  2008     6 auto(… 4        17    25 p     mids…
##  5 audi         a6 quatt…   4.2  2008     8 auto(… 4        16    23 p     mids…
##  6 chevrolet    c1500 su…   5.3  2008     8 auto(… r        14    20 r     suv  
##  7 chevrolet    c1500 su…   5.3  2008     8 auto(… r        11    15 e     suv  
##  8 chevrolet    c1500 su…   5.3  2008     8 auto(… r        14    20 r     suv  
##  9 chevrolet    c1500 su…   5.7  1999     8 auto(… r        13    17 r     suv  
## 10 chevrolet    c1500 su…   6    2008     8 auto(… r        12    17 r     suv  
## # … with 116 more rows
```

## mutate()

mutate() can add a new column based on the existing column.


```r
mpg %>% 
  select(manufacturer,model,year) %>% 
  mutate(year2=year-2000)
```

```
## # A tibble: 234 × 4
##    manufacturer model       year year2
##    <chr>        <chr>      <int> <dbl>
##  1 audi         a4          1999    -1
##  2 audi         a4          1999    -1
##  3 audi         a4          2008     8
##  4 audi         a4          2008     8
##  5 audi         a4          1999    -1
##  6 audi         a4          1999    -1
##  7 audi         a4          2008     8
##  8 audi         a4 quattro  1999    -1
##  9 audi         a4 quattro  1999    -1
## 10 audi         a4 quattro  2008     8
## # … with 224 more rows
```

We can use ifelse() to choose data.


```r
mpg %>% 
  select(manufacturer,model,year) %>% 
  mutate(year2=ifelse(year>2000,0,NA))
```

```
## # A tibble: 234 × 4
##    manufacturer model       year year2
##    <chr>        <chr>      <int> <dbl>
##  1 audi         a4          1999    NA
##  2 audi         a4          1999    NA
##  3 audi         a4          2008     0
##  4 audi         a4          2008     0
##  5 audi         a4          1999    NA
##  6 audi         a4          1999    NA
##  7 audi         a4          2008     0
##  8 audi         a4 quattro  1999    NA
##  9 audi         a4 quattro  1999    NA
## 10 audi         a4 quattro  2008     0
## # … with 224 more rows
```

mutate_all() can change all the columns.


```r
mpg %>% 
  mutate_all(toupper)
```

```
## # A tibble: 234 × 11
##    manufacturer model      displ year  cyl   trans drv   cty   hwy   fl    class
##    <chr>        <chr>      <chr> <chr> <chr> <chr> <chr> <chr> <chr> <chr> <chr>
##  1 AUDI         A4         1.8   1999  4     AUTO… F     18    29    P     COMP…
##  2 AUDI         A4         1.8   1999  4     MANU… F     21    29    P     COMP…
##  3 AUDI         A4         2     2008  4     MANU… F     20    31    P     COMP…
##  4 AUDI         A4         2     2008  4     AUTO… F     21    30    P     COMP…
##  5 AUDI         A4         2.8   1999  6     AUTO… F     16    26    P     COMP…
##  6 AUDI         A4         2.8   1999  6     MANU… F     18    26    P     COMP…
##  7 AUDI         A4         3.1   2008  6     AUTO… F     18    27    P     COMP…
##  8 AUDI         A4 QUATTRO 1.8   1999  4     MANU… 4     18    26    P     COMP…
##  9 AUDI         A4 QUATTRO 1.8   1999  4     AUTO… 4     16    25    P     COMP…
## 10 AUDI         A4 QUATTRO 2     2008  4     MANU… 4     20    28    P     COMP…
## # … with 224 more rows
```

mutate_if() can select certain columns and mutate.


```r
mpg %>% 
  mutate_if(is.numeric,round)
```

```
## # A tibble: 234 × 11
##    manufacturer model      displ  year   cyl trans drv     cty   hwy fl    class
##    <chr>        <chr>      <dbl> <dbl> <dbl> <chr> <chr> <dbl> <dbl> <chr> <chr>
##  1 audi         a4             2  1999     4 auto… f        18    29 p     comp…
##  2 audi         a4             2  1999     4 manu… f        21    29 p     comp…
##  3 audi         a4             2  2008     4 manu… f        20    31 p     comp…
##  4 audi         a4             2  2008     4 auto… f        21    30 p     comp…
##  5 audi         a4             3  1999     6 auto… f        16    26 p     comp…
##  6 audi         a4             3  1999     6 manu… f        18    26 p     comp…
##  7 audi         a4             3  2008     6 auto… f        18    27 p     comp…
##  8 audi         a4 quattro     2  1999     4 manu… 4        18    26 p     comp…
##  9 audi         a4 quattro     2  1999     4 auto… 4        16    25 p     comp…
## 10 audi         a4 quattro     2  2008     4 manu… 4        20    28 p     comp…
## # … with 224 more rows
```

mutate_at() need to select columns in vars().


```r
mpg %>% 
  select(manufacturer,model,displ,cyl) %>% 
  mutate_at(vars(displ,cyl),~(.*2))
```

```
## # A tibble: 234 × 4
##    manufacturer model      displ   cyl
##    <chr>        <chr>      <dbl> <dbl>
##  1 audi         a4           3.6     8
##  2 audi         a4           3.6     8
##  3 audi         a4           4       8
##  4 audi         a4           4       8
##  5 audi         a4           5.6    12
##  6 audi         a4           5.6    12
##  7 audi         a4           6.2    12
##  8 audi         a4 quattro   3.6     8
##  9 audi         a4 quattro   3.6     8
## 10 audi         a4 quattro   4       8
## # … with 224 more rows
```

case_when() can create categorical data.


```r
mpg %>% 
  select(manufacturer,model,year) %>% 
  mutate(year2=case_when(
    year<2000~"very old",
    year<2005~"old",
    TRUE~"new"
  ))
```

```
## # A tibble: 234 × 4
##    manufacturer model       year year2   
##    <chr>        <chr>      <int> <chr>   
##  1 audi         a4          1999 very old
##  2 audi         a4          1999 very old
##  3 audi         a4          2008 new     
##  4 audi         a4          2008 new     
##  5 audi         a4          1999 very old
##  6 audi         a4          1999 very old
##  7 audi         a4          2008 new     
##  8 audi         a4 quattro  1999 very old
##  9 audi         a4 quattro  1999 very old
## 10 audi         a4 quattro  2008 new     
## # … with 224 more rows
```

## rowwise()

rowwise() can process data by row.


```r
mpg %>% 
  select_if(is.numeric) %>% 
  rowwise() %>% 
  mutate(mean = mean(c_across(displ:hwy)))
```

```
## # A tibble: 234 × 6
## # Rowwise: 
##    displ  year   cyl   cty   hwy  mean
##    <dbl> <int> <int> <int> <int> <dbl>
##  1   1.8  1999     4    18    29  410.
##  2   1.8  1999     4    21    29  411.
##  3   2    2008     4    20    31  413 
##  4   2    2008     4    21    30  413 
##  5   2.8  1999     6    16    26  410.
##  6   2.8  1999     6    18    26  410.
##  7   3.1  2008     6    18    27  412.
##  8   1.8  1999     4    18    26  410.
##  9   1.8  1999     4    16    25  409.
## 10   2    2008     4    20    28  412.
## # … with 224 more rows
```

Or, we can do this by another way.


```r
mpg %>% 
  rowwise() %>% 
  mutate(mean=rowMeans(across(where(is.numeric))))
```

```
## # A tibble: 234 × 12
## # Rowwise: 
##    manufacturer model      displ  year   cyl trans drv     cty   hwy fl    class
##    <chr>        <chr>      <dbl> <int> <int> <chr> <chr> <int> <int> <chr> <chr>
##  1 audi         a4           1.8  1999     4 auto… f        18    29 p     comp…
##  2 audi         a4           1.8  1999     4 manu… f        21    29 p     comp…
##  3 audi         a4           2    2008     4 manu… f        20    31 p     comp…
##  4 audi         a4           2    2008     4 auto… f        21    30 p     comp…
##  5 audi         a4           2.8  1999     6 auto… f        16    26 p     comp…
##  6 audi         a4           2.8  1999     6 manu… f        18    26 p     comp…
##  7 audi         a4           3.1  2008     6 auto… f        18    27 p     comp…
##  8 audi         a4 quattro   1.8  1999     4 manu… 4        18    26 p     comp…
##  9 audi         a4 quattro   1.8  1999     4 auto… 4        16    25 p     comp…
## 10 audi         a4 quattro   2    2008     4 manu… 4        20    28 p     comp…
## # … with 224 more rows, and 1 more variable: mean <dbl>
```

We can use rowwise() to get the max/min/sum/sd too.


```r
mpg %>% 
  rowwise() %>% 
  mutate(sum=sum(across(where(is.numeric))))
```

```
## # A tibble: 234 × 12
## # Rowwise: 
##    manufacturer model      displ  year   cyl trans drv     cty   hwy fl    class
##    <chr>        <chr>      <dbl> <int> <int> <chr> <chr> <int> <int> <chr> <chr>
##  1 audi         a4           1.8  1999     4 auto… f        18    29 p     comp…
##  2 audi         a4           1.8  1999     4 manu… f        21    29 p     comp…
##  3 audi         a4           2    2008     4 manu… f        20    31 p     comp…
##  4 audi         a4           2    2008     4 auto… f        21    30 p     comp…
##  5 audi         a4           2.8  1999     6 auto… f        16    26 p     comp…
##  6 audi         a4           2.8  1999     6 manu… f        18    26 p     comp…
##  7 audi         a4           3.1  2008     6 auto… f        18    27 p     comp…
##  8 audi         a4 quattro   1.8  1999     4 manu… 4        18    26 p     comp…
##  9 audi         a4 quattro   1.8  1999     4 auto… 4        16    25 p     comp…
## 10 audi         a4 quattro   2    2008     4 manu… 4        20    28 p     comp…
## # … with 224 more rows, and 1 more variable: sum <dbl>
```

## arrange()

arrange() can sort the data.


```r
mpg %>% 
  arrange(displ)
```

```
## # A tibble: 234 × 11
##    manufacturer model      displ  year   cyl trans drv     cty   hwy fl    class
##    <chr>        <chr>      <dbl> <int> <int> <chr> <chr> <int> <int> <chr> <chr>
##  1 honda        civic        1.6  1999     4 manu… f        28    33 r     subc…
##  2 honda        civic        1.6  1999     4 auto… f        24    32 r     subc…
##  3 honda        civic        1.6  1999     4 manu… f        25    32 r     subc…
##  4 honda        civic        1.6  1999     4 manu… f        23    29 p     subc…
##  5 honda        civic        1.6  1999     4 auto… f        24    32 r     subc…
##  6 audi         a4           1.8  1999     4 auto… f        18    29 p     comp…
##  7 audi         a4           1.8  1999     4 manu… f        21    29 p     comp…
##  8 audi         a4 quattro   1.8  1999     4 manu… 4        18    26 p     comp…
##  9 audi         a4 quattro   1.8  1999     4 auto… 4        16    25 p     comp…
## 10 honda        civic        1.8  2008     4 manu… f        26    34 r     subc…
## # … with 224 more rows
```

desc() can help sort data by descending order.


```r
mpg %>% 
  arrange(desc(displ))
```

```
## # A tibble: 234 × 11
##    manufacturer model     displ  year   cyl trans  drv     cty   hwy fl    class
##    <chr>        <chr>     <dbl> <int> <int> <chr>  <chr> <int> <int> <chr> <chr>
##  1 chevrolet    corvette    7    2008     8 manua… r        15    24 p     2sea…
##  2 chevrolet    k1500 ta…   6.5  1999     8 auto(… 4        14    17 d     suv  
##  3 chevrolet    corvette    6.2  2008     8 manua… r        16    26 p     2sea…
##  4 chevrolet    corvette    6.2  2008     8 auto(… r        15    25 p     2sea…
##  5 jeep         grand ch…   6.1  2008     8 auto(… 4        11    14 p     suv  
##  6 chevrolet    c1500 su…   6    2008     8 auto(… r        12    17 r     suv  
##  7 dodge        durango …   5.9  1999     8 auto(… 4        11    15 r     suv  
##  8 dodge        ram 1500…   5.9  1999     8 auto(… 4        11    15 r     pick…
##  9 chevrolet    c1500 su…   5.7  1999     8 auto(… r        13    17 r     suv  
## 10 chevrolet    corvette    5.7  1999     8 manua… r        16    26 p     2sea…
## # … with 224 more rows
```

## distinct()

distinct() can help delete the duplicate rows.


```r
df <- tibble(
  x=sample(5,20,rep=TRUE),
  y=sample(5,20,rep=TRUE)
)
df %>% 
  distinct()
```

```
## # A tibble: 12 × 2
##        x     y
##    <int> <int>
##  1     1     2
##  2     5     2
##  3     1     5
##  4     4     3
##  5     4     4
##  6     4     2
##  7     2     1
##  8     5     3
##  9     2     3
## 10     2     4
## 11     1     3
## 12     1     1
```

## rename()

rename() can change the column name.


```r
mpg %>% 
  rename(YEAR=year)
```

```
## # A tibble: 234 × 11
##    manufacturer model      displ  YEAR   cyl trans drv     cty   hwy fl    class
##    <chr>        <chr>      <dbl> <int> <int> <chr> <chr> <int> <int> <chr> <chr>
##  1 audi         a4           1.8  1999     4 auto… f        18    29 p     comp…
##  2 audi         a4           1.8  1999     4 manu… f        21    29 p     comp…
##  3 audi         a4           2    2008     4 manu… f        20    31 p     comp…
##  4 audi         a4           2    2008     4 auto… f        21    30 p     comp…
##  5 audi         a4           2.8  1999     6 auto… f        16    26 p     comp…
##  6 audi         a4           2.8  1999     6 manu… f        18    26 p     comp…
##  7 audi         a4           3.1  2008     6 auto… f        18    27 p     comp…
##  8 audi         a4 quattro   1.8  1999     4 manu… 4        18    26 p     comp…
##  9 audi         a4 quattro   1.8  1999     4 auto… 4        16    25 p     comp…
## 10 audi         a4 quattro   2    2008     4 manu… 4        20    28 p     comp…
## # … with 224 more rows
```

## relocate()

relocate() can help change the order of the columns.


```r
mpg %>% 
  relocate(year)
```

```
## # A tibble: 234 × 11
##     year manufacturer model      displ   cyl trans drv     cty   hwy fl    class
##    <int> <chr>        <chr>      <dbl> <int> <chr> <chr> <int> <int> <chr> <chr>
##  1  1999 audi         a4           1.8     4 auto… f        18    29 p     comp…
##  2  1999 audi         a4           1.8     4 manu… f        21    29 p     comp…
##  3  2008 audi         a4           2       4 manu… f        20    31 p     comp…
##  4  2008 audi         a4           2       4 auto… f        21    30 p     comp…
##  5  1999 audi         a4           2.8     6 auto… f        16    26 p     comp…
##  6  1999 audi         a4           2.8     6 manu… f        18    26 p     comp…
##  7  2008 audi         a4           3.1     6 auto… f        18    27 p     comp…
##  8  1999 audi         a4 quattro   1.8     4 manu… 4        18    26 p     comp…
##  9  1999 audi         a4 quattro   1.8     4 auto… 4        16    25 p     comp…
## 10  2008 audi         a4 quattro   2       4 manu… 4        20    28 p     comp…
## # … with 224 more rows
```


```r
mpg %>% 
  relocate(year,.after = manufacturer)
```

```
## # A tibble: 234 × 11
##    manufacturer  year model      displ   cyl trans drv     cty   hwy fl    class
##    <chr>        <int> <chr>      <dbl> <int> <chr> <chr> <int> <int> <chr> <chr>
##  1 audi          1999 a4           1.8     4 auto… f        18    29 p     comp…
##  2 audi          1999 a4           1.8     4 manu… f        21    29 p     comp…
##  3 audi          2008 a4           2       4 manu… f        20    31 p     comp…
##  4 audi          2008 a4           2       4 auto… f        21    30 p     comp…
##  5 audi          1999 a4           2.8     6 auto… f        16    26 p     comp…
##  6 audi          1999 a4           2.8     6 manu… f        18    26 p     comp…
##  7 audi          2008 a4           3.1     6 auto… f        18    27 p     comp…
##  8 audi          1999 a4 quattro   1.8     4 manu… 4        18    26 p     comp…
##  9 audi          1999 a4 quattro   1.8     4 auto… 4        16    25 p     comp…
## 10 audi          2008 a4 quattro   2       4 manu… 4        20    28 p     comp…
## # … with 224 more rows
```


```r
mpg %>% 
  relocate(year,.before = displ)
```

```
## # A tibble: 234 × 11
##    manufacturer model       year displ   cyl trans drv     cty   hwy fl    class
##    <chr>        <chr>      <int> <dbl> <int> <chr> <chr> <int> <int> <chr> <chr>
##  1 audi         a4          1999   1.8     4 auto… f        18    29 p     comp…
##  2 audi         a4          1999   1.8     4 manu… f        21    29 p     comp…
##  3 audi         a4          2008   2       4 manu… f        20    31 p     comp…
##  4 audi         a4          2008   2       4 auto… f        21    30 p     comp…
##  5 audi         a4          1999   2.8     6 auto… f        16    26 p     comp…
##  6 audi         a4          1999   2.8     6 manu… f        18    26 p     comp…
##  7 audi         a4          2008   3.1     6 auto… f        18    27 p     comp…
##  8 audi         a4 quattro  1999   1.8     4 manu… 4        18    26 p     comp…
##  9 audi         a4 quattro  1999   1.8     4 auto… 4        16    25 p     comp…
## 10 audi         a4 quattro  2008   2       4 manu… 4        20    28 p     comp…
## # … with 224 more rows
```

## drop_na()

drop_na can help drop the missing value.


```r
df <- tibble(
  x=c(1,NA,2,3),
  y=c(4,5,NA,6)
)
df %>% 
  drop_na()
```

```
## # A tibble: 2 × 2
##       x     y
##   <dbl> <dbl>
## 1     1     4
## 2     3     6
```

## pull()

pull() can help get a single column.


```r
mpg %>% 
  pull(year)
```

```
##   [1] 1999 1999 2008 2008 1999 1999 2008 1999 1999 2008 2008 1999 1999 2008 2008
##  [16] 1999 2008 2008 2008 2008 2008 1999 2008 1999 1999 2008 2008 2008 2008 2008
##  [31] 1999 1999 1999 2008 1999 2008 2008 1999 1999 1999 1999 2008 2008 2008 1999
##  [46] 1999 2008 2008 2008 2008 1999 1999 2008 2008 2008 1999 1999 1999 2008 2008
##  [61] 2008 1999 2008 1999 2008 2008 2008 2008 2008 2008 1999 1999 2008 1999 1999
##  [76] 1999 2008 1999 1999 1999 2008 2008 1999 1999 1999 1999 1999 2008 1999 2008
##  [91] 1999 1999 2008 2008 1999 1999 2008 2008 2008 1999 1999 1999 1999 1999 2008
## [106] 2008 2008 2008 1999 1999 2008 2008 1999 1999 2008 1999 1999 2008 2008 2008
## [121] 2008 2008 2008 2008 1999 1999 2008 2008 2008 2008 1999 2008 2008 1999 1999
## [136] 1999 2008 1999 2008 2008 1999 1999 1999 2008 2008 2008 2008 1999 1999 2008
## [151] 1999 1999 2008 2008 1999 1999 1999 2008 2008 1999 1999 2008 2008 2008 2008
## [166] 1999 1999 1999 1999 2008 2008 2008 2008 1999 1999 1999 1999 2008 2008 1999
## [181] 1999 2008 2008 1999 1999 2008 1999 1999 2008 2008 1999 1999 2008 1999 1999
## [196] 1999 2008 2008 1999 2008 1999 1999 2008 1999 1999 2008 2008 1999 1999 2008
## [211] 2008 1999 1999 1999 1999 2008 2008 2008 2008 1999 1999 1999 1999 1999 1999
## [226] 2008 2008 1999 1999 2008 2008 1999 1999 2008
```

## unite()

unite() can help unite the columns.


```r
mpg %>% 
  unite(col="newcolumn",manufacturer:model,sep=",")->newdf

newdf
```

```
## # A tibble: 234 × 10
##    newcolumn       displ  year   cyl trans      drv     cty   hwy fl    class  
##    <chr>           <dbl> <int> <int> <chr>      <chr> <int> <int> <chr> <chr>  
##  1 audi,a4           1.8  1999     4 auto(l5)   f        18    29 p     compact
##  2 audi,a4           1.8  1999     4 manual(m5) f        21    29 p     compact
##  3 audi,a4           2    2008     4 manual(m6) f        20    31 p     compact
##  4 audi,a4           2    2008     4 auto(av)   f        21    30 p     compact
##  5 audi,a4           2.8  1999     6 auto(l5)   f        16    26 p     compact
##  6 audi,a4           2.8  1999     6 manual(m5) f        18    26 p     compact
##  7 audi,a4           3.1  2008     6 auto(av)   f        18    27 p     compact
##  8 audi,a4 quattro   1.8  1999     4 manual(m5) 4        18    26 p     compact
##  9 audi,a4 quattro   1.8  1999     4 auto(l5)   4        16    25 p     compact
## 10 audi,a4 quattro   2    2008     4 manual(m6) 4        20    28 p     compact
## # … with 224 more rows
```

## separate()

separate() can help separate one column to several columns.


```r
newdf %>% 
  separate("newcolumn",into=c("manufacturer","model"),sep=",")
```

```
## # A tibble: 234 × 11
##    manufacturer model      displ  year   cyl trans drv     cty   hwy fl    class
##    <chr>        <chr>      <dbl> <int> <int> <chr> <chr> <int> <int> <chr> <chr>
##  1 audi         a4           1.8  1999     4 auto… f        18    29 p     comp…
##  2 audi         a4           1.8  1999     4 manu… f        21    29 p     comp…
##  3 audi         a4           2    2008     4 manu… f        20    31 p     comp…
##  4 audi         a4           2    2008     4 auto… f        21    30 p     comp…
##  5 audi         a4           2.8  1999     6 auto… f        16    26 p     comp…
##  6 audi         a4           2.8  1999     6 manu… f        18    26 p     comp…
##  7 audi         a4           3.1  2008     6 auto… f        18    27 p     comp…
##  8 audi         a4 quattro   1.8  1999     4 manu… 4        18    26 p     comp…
##  9 audi         a4 quattro   1.8  1999     4 auto… 4        16    25 p     comp…
## 10 audi         a4 quattro   2    2008     4 manu… 4        20    28 p     comp…
## # … with 224 more rows
```

## pivot_longer()

pivot_longer() "lengthens" data, increasing the number of rows and decreasing the number of columns.


```r
df <- tibble(index=c(1,2),x=c('a','b'),y=c('c','d'),z=c('e','f'))
df
```

```
## # A tibble: 2 × 4
##   index x     y     z    
##   <dbl> <chr> <chr> <chr>
## 1     1 a     c     e    
## 2     2 b     d     f
```


```r
df2 <- df %>% 
  pivot_longer(cols=!index,names_to="key",values_to="val")
df2
```

```
## # A tibble: 6 × 3
##   index key   val  
##   <dbl> <chr> <chr>
## 1     1 x     a    
## 2     1 y     c    
## 3     1 z     e    
## 4     2 x     b    
## 5     2 y     d    
## 6     2 z     f
```

## pivot_wider()

pivot_wider() "widens" data, increasing the number of columns and decreasing the number of rows.


```r
df2 %>% 
  pivot_wider(names_from=key,values_from=val)
```

```
## # A tibble: 2 × 4
##   index x     y     z    
##   <dbl> <chr> <chr> <chr>
## 1     1 a     c     e    
## 2     2 b     d     f
```

## count()

count() can count the number of occurences.


```r
mpg %>% 
  count(model,sort=TRUE)
```

```
## # A tibble: 38 × 2
##    model                   n
##    <chr>               <int>
##  1 caravan 2wd            11
##  2 ram 1500 pickup 4wd    10
##  3 civic                   9
##  4 dakota pickup 4wd       9
##  5 jetta                   9
##  6 mustang                 9
##  7 a4 quattro              8
##  8 grand cherokee 4wd      8
##  9 impreza awd             8
## 10 a4                      7
## # … with 28 more rows
```

## summarize()

summarise() is typically used on grouped data created by group_by(). The output will have one row for each group.


```r
mpg %>% 
  group_by(model) %>% 
  summarise(count=n(),averagedispl=mean(displ),maxdispl=max(displ))
```

```
## # A tibble: 38 × 4
##    model              count averagedispl maxdispl
##    <chr>              <int>        <dbl>    <dbl>
##  1 4runner 4wd            6         3.48      4.7
##  2 a4                     7         2.33      3.1
##  3 a4 quattro             8         2.42      3.1
##  4 a6 quattro             3         3.37      4.2
##  5 altima                 6         2.8       3.5
##  6 c1500 suburban 2wd     5         5.52      6  
##  7 camry                  7         2.67      3.5
##  8 camry solara           7         2.64      3.3
##  9 caravan 2wd           11         3.39      4  
## 10 civic                  9         1.71      2  
## # … with 28 more rows
```

summarise_all() applies the functions to all (non-grouping) columns.


```r
mpg %>% 
  group_by(model) %>% 
  select_if(is.numeric) %>% 
  summarise_all(mean)
```

```
## # A tibble: 38 × 6
##    model              displ  year   cyl   cty   hwy
##    <chr>              <dbl> <dbl> <dbl> <dbl> <dbl>
##  1 4runner 4wd         3.48 2002   5.67  15.2  18.8
##  2 a4                  2.33 2003.  4.86  18.9  28.3
##  3 a4 quattro          2.42 2004.  5     17.1  25.8
##  4 a6 quattro          3.37 2005   6.67  16    24  
##  5 altima              2.8  2005   4.67  20.7  28.7
##  6 c1500 suburban 2wd  5.52 2006.  8     12.8  17.8
##  7 camry               2.67 2003.  4.86  19.9  28.3
##  8 camry solara        2.64 2003.  4.86  19.9  28.1
##  9 caravan 2wd         3.39 2003.  5.82  15.8  22.4
## 10 civic               1.71 2003   4     24.4  32.6
## # … with 28 more rows
```

summarise_if() operate on columns for which a predicate returns TRUE.


```r
mpg %>% 
  group_by(model) %>% 
  summarise_if(is.numeric,mean)
```

```
## # A tibble: 38 × 6
##    model              displ  year   cyl   cty   hwy
##    <chr>              <dbl> <dbl> <dbl> <dbl> <dbl>
##  1 4runner 4wd         3.48 2002   5.67  15.2  18.8
##  2 a4                  2.33 2003.  4.86  18.9  28.3
##  3 a4 quattro          2.42 2004.  5     17.1  25.8
##  4 a6 quattro          3.37 2005   6.67  16    24  
##  5 altima              2.8  2005   4.67  20.7  28.7
##  6 c1500 suburban 2wd  5.52 2006.  8     12.8  17.8
##  7 camry               2.67 2003.  4.86  19.9  28.3
##  8 camry solara        2.64 2003.  4.86  19.9  28.1
##  9 caravan 2wd         3.39 2003.  5.82  15.8  22.4
## 10 civic               1.71 2003   4     24.4  32.6
## # … with 28 more rows
```

summarise_at() allow you to select columns.


```r
mpg %>% 
  group_by(model) %>% 
  summarise_at(vars(displ,cyl),mean)
```

```
## # A tibble: 38 × 3
##    model              displ   cyl
##    <chr>              <dbl> <dbl>
##  1 4runner 4wd         3.48  5.67
##  2 a4                  2.33  4.86
##  3 a4 quattro          2.42  5   
##  4 a6 quattro          3.37  6.67
##  5 altima              2.8   4.67
##  6 c1500 suburban 2wd  5.52  8   
##  7 camry               2.67  4.86
##  8 camry solara        2.64  4.86
##  9 caravan 2wd         3.39  5.82
## 10 civic               1.71  4   
## # … with 28 more rows
```

