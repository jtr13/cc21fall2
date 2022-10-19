#  TidyVerse

Zhisen Cai

Sometimes we may forget the way to use Tidyverse. Therefore, I create this for help. People can finish most of the basic part of tidyverse by using this. I separate it into 4 parts, manipulation between two datasets, manipulation on rows, manipulation on columns and group_by.  With the examples of each function, people can know how to use the function and how the function works.


```r
library(tidyverse)
```
Magrittr use pipeline to convey the data. (%>%) We have to use a dot to represent the thing we convey if it is not used in the first parameter. 

```r
# we can omit '.'
c(1, 3, 4, 5, NA) %>% mean(., na.rm=TRUE)
```

```
## [1] 3.25
```

```r
c(1, 3, 4, 5, NA) %>% mean(na.rm = TRUE)  
```

```
## [1] 3.25
```

```r
# we can not omit '.' in the second parameter
c(1, 3, 4, 5) %>% plot(., main=paste(., collapse=", "))
c(1, 3, 4, 5) %>% plot(main=paste(., collapse=", "))
```

<img src="tidyver_help_files/figure-html/unnamed-chunk-2-1.png" width="672" style="display: block; margin: auto;" />

###  Connection Bewtween two datasets
Efficiently bind multiple data frames by row and column 
bind_rows() and bind_cols() return the same type as the first input, either a data frame, tbl_df, or grouped_df
code:  bind_rows(..., .id = NULL)   bind_cols(...)

```r
bind_rows(
+   sample_n(iris, 10),
+   sample_n(iris, 10),
+   sample_n(iris, 10)) %>% 
  glimpse()
```

```
## Rows: 30
## Columns: 5
## $ Sepal.Length <dbl> 6.0, 4.8, 5.0, 6.4, 4.7, 5.8, 4.4, 7.7, 6.4, 4.5, 4.8, 5.…
## $ Sepal.Width  <dbl> 2.2, 3.4, 3.2, 2.8, 3.2, 2.7, 3.2, 2.6, 3.1, 2.3, 3.0, 2.…
## $ Petal.Length <dbl> 5.0, 1.6, 1.2, 5.6, 1.6, 5.1, 1.3, 6.9, 5.5, 1.3, 1.4, 4.…
## $ Petal.Width  <dbl> 1.5, 0.2, 0.2, 2.1, 0.2, 1.9, 0.2, 2.3, 1.8, 0.3, 0.3, 2.…
## $ Species      <lgl> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, N…
```

```r
bind_cols(
  sample_n(iris, 10),
  sample_n(iris, 10),
  sample_n(iris, 10)
) %>% glimpse()
```

```
## Rows: 10
## Columns: 15
## $ Sepal.Length...1  <dbl> 6.1, 5.0, 7.7, 4.8, 5.1, 6.1, 6.0, 5.5, 5.2, 7.6
## $ Sepal.Width...2   <dbl> 3.0, 3.5, 3.0, 3.0, 3.4, 2.8, 3.4, 2.4, 3.5, 3.0
## $ Petal.Length...3  <dbl> 4.6, 1.6, 6.1, 1.4, 1.5, 4.0, 4.5, 3.7, 1.5, 6.6
## $ Petal.Width...4   <dbl> 1.4, 0.6, 2.3, 0.3, 0.2, 1.3, 1.6, 1.0, 0.2, 2.1
## $ Species...5       <fct> versicolor, setosa, virginica, setosa, setosa, versi…
## $ Sepal.Length...6  <dbl> 6.0, 6.2, 6.3, 5.8, 6.6, 5.2, 6.4, 5.5, 5.6, 6.4
## $ Sepal.Width...7   <dbl> 2.9, 2.9, 2.7, 2.8, 3.0, 2.7, 2.9, 2.4, 2.5, 3.2
## $ Petal.Length...8  <dbl> 4.5, 4.3, 4.9, 5.1, 4.4, 3.9, 4.3, 3.7, 3.9, 4.5
## $ Petal.Width...9   <dbl> 1.5, 1.3, 1.8, 2.4, 1.4, 1.4, 1.3, 1.0, 1.1, 1.5
## $ Species...10      <fct> versicolor, versicolor, virginica, virginica, versic…
## $ Sepal.Length...11 <dbl> 6.1, 6.6, 5.4, 6.5, 5.9, 7.7, 6.1, 5.5, 5.4, 5.1
## $ Sepal.Width...12  <dbl> 3.0, 3.0, 3.4, 3.0, 3.2, 2.8, 2.8, 2.4, 3.4, 3.5
## $ Petal.Length...13 <dbl> 4.6, 4.4, 1.5, 5.8, 4.8, 6.7, 4.7, 3.7, 1.7, 1.4
## $ Petal.Width...14  <dbl> 1.4, 1.4, 0.4, 2.2, 1.8, 2.0, 1.2, 1.0, 0.2, 0.2
## $ Species...15      <fct> versicolor, versicolor, setosa, virginica, versicolo…
```

### combime two datasets by value: join


```r
# prepare data 
superheroes <- tribble(
  ~name,      ~alignment,  ~gender,   ~publisher,
  "Magneto",  "bad",       "male",    "Marvel",
  "Storm",    "good",      "female",  "Marvel",
  "Mystique", "bad",       "female",  "Marvel",
  "Batman",   "good",      "male",    "DC",
  "Joker",    "bad",       "male",    "DC",
  "Catwoman", "bad",       "female",  "DC",
  "Hellboy",  "good",      "male",    "Dark Horse Comics"
)
publishers <- tribble(
  ~publisher, ~yr_founded,
  "DC",       1934L,
  "Marvel",   1939L,
  "Image",    1992L
)
```

left_join
A left join in R is a merge operation between two data frames where the merge returns all of the rows from one table (the left side) and any matching rows from the second table. A left join in R will NOT return values of the second table which do not already exist in the first table.
left_join(a_tibble, another_tibble, by = ...)

```r
superheroes %>% 
  left_join(publishers, by="publisher")
```

```
## # A tibble: 7 × 5
##   name     alignment gender publisher         yr_founded
##   <chr>    <chr>     <chr>  <chr>                  <int>
## 1 Magneto  bad       male   Marvel                  1939
## 2 Storm    good      female Marvel                  1939
## 3 Mystique bad       female Marvel                  1939
## 4 Batman   good      male   DC                      1934
## 5 Joker    bad       male   DC                      1934
## 6 Catwoman bad       female DC                      1934
## 7 Hellboy  good      male   Dark Horse Comics         NA
```
inner join:
he inner_join keyword selects records that have matching values in both tables.It will not return unmatched rows. Therefore, we do not see the last row shown in the left_join.
code: inner_join(a_tibble, another_tibble, by = ...)

```r
inner_join(superheroes, publishers, by="publisher")
```

```
## # A tibble: 6 × 5
##   name     alignment gender publisher yr_founded
##   <chr>    <chr>     <chr>  <chr>          <int>
## 1 Magneto  bad       male   Marvel          1939
## 2 Storm    good      female Marvel          1939
## 3 Mystique bad       female Marvel          1939
## 4 Batman   good      male   DC              1934
## 5 Joker    bad       male   DC              1934
## 6 Catwoman bad       female DC              1934
```
anti join:
An anti join returns the rows of the first table where it cannot find a match in the second table.

```r
superheroes %>%
  anti_join(publishers, by="publisher")
```

```
## # A tibble: 1 × 4
##   name    alignment gender publisher        
##   <chr>   <chr>     <chr>  <chr>            
## 1 Hellboy good      male   Dark Horse Comics
```

semi join
Semi joins are the opposite of anti joins: an anti-anti join, if you like.
A semi join returns the rows of the first table where it can find a match in the second table. 
code: semi_join(a_tibble, another_tibble, by = ...)

```r
superheroes %>%
  semi_join(publishers, by="publisher")
```

```
## # A tibble: 6 × 4
##   name     alignment gender publisher
##   <chr>    <chr>     <chr>  <chr>    
## 1 Magneto  bad       male   Marvel   
## 2 Storm    good      female Marvel   
## 3 Mystique bad       female Marvel   
## 4 Batman   good      male   DC       
## 5 Joker    bad       male   DC       
## 6 Catwoman bad       female DC
```
### manipulation on column
we use select to choose column.
we can use helper function to choose column
starts_with() : start with a literal string
ends_with() : end with a literal string
matches(): match a regular expression
num_range(): are part of a numercial range
everything(): selects all columns

```r
colnames(iris)
```

```
## [1] "Sepal.Length" "Sepal.Width"  "Petal.Length" "Petal.Width"  "Species"
```

```r
iris <- iris %>% as_tibble() 
iris %>%
  select(starts_with("Petal")) %>%
  head(10)
```

```
## # A tibble: 10 × 2
##    Petal.Length Petal.Width
##           <dbl>       <dbl>
##  1          1.4         0.2
##  2          1.4         0.2
##  3          1.3         0.2
##  4          1.5         0.2
##  5          1.4         0.2
##  6          1.7         0.4
##  7          1.4         0.3
##  8          1.5         0.2
##  9          1.4         0.2
## 10          1.5         0.1
```

```r
iris %>%
  select(ends_with("Length"))%>%
  head(10)
```

```
## # A tibble: 10 × 2
##    Sepal.Length Petal.Length
##           <dbl>        <dbl>
##  1          5.1          1.4
##  2          4.9          1.4
##  3          4.7          1.3
##  4          4.6          1.5
##  5          5            1.4
##  6          5.4          1.7
##  7          4.6          1.4
##  8          5            1.5
##  9          4.4          1.4
## 10          4.9          1.5
```


```r
iris %>%
  select(contains(".")) %>%
  head(10)
```

```
## # A tibble: 10 × 4
##    Sepal.Length Sepal.Width Petal.Length Petal.Width
##           <dbl>       <dbl>        <dbl>       <dbl>
##  1          5.1         3.5          1.4         0.2
##  2          4.9         3            1.4         0.2
##  3          4.7         3.2          1.3         0.2
##  4          4.6         3.1          1.5         0.2
##  5          5           3.6          1.4         0.2
##  6          5.4         3.9          1.7         0.4
##  7          4.6         3.4          1.4         0.3
##  8          5           3.4          1.5         0.2
##  9          4.4         2.9          1.4         0.2
## 10          4.9         3.1          1.5         0.1
```

select_if 
we can use select_if to choose column with logical condition or any function return true or false.

```r
starwars %>%
  select_if(is.numeric) %>%
  head(10)
```

```
## # A tibble: 10 × 3
##    height  mass birth_year
##     <int> <dbl>      <dbl>
##  1    172    77       19  
##  2    167    75      112  
##  3     96    32       33  
##  4    202   136       41.9
##  5    150    49       19  
##  6    178   120       52  
##  7    165    75       47  
##  8     97    32       NA  
##  9    183    84       24  
## 10    182    77       57
```


```r
less_than_500 <- function(x) {
  sum(x) < 500
}
iris[1:4] %>%
  select_if(less_than_500)%>%
  head(10)
```

```
## # A tibble: 10 × 2
##    Sepal.Width Petal.Width
##          <dbl>       <dbl>
##  1         3.5         0.2
##  2         3           0.2
##  3         3.2         0.2
##  4         3.1         0.2
##  5         3.6         0.2
##  6         3.9         0.4
##  7         3.4         0.3
##  8         3.4         0.2
##  9         2.9         0.2
## 10         3.1         0.1
```

!!!! we can use ~ to represent anonymous function

```r
iris[1:4] %>%
  select_if(~ sum(.) < 500)%>%
  head(10)
```

```
## # A tibble: 10 × 2
##    Sepal.Width Petal.Width
##          <dbl>       <dbl>
##  1         3.5         0.2
##  2         3           0.2
##  3         3.2         0.2
##  4         3.1         0.2
##  5         3.6         0.2
##  6         3.9         0.4
##  7         3.4         0.3
##  8         3.4         0.2
##  9         2.9         0.2
## 10         3.1         0.1
```

We can select the data by deleting columns using minus sign.

```r
iris %>%
  select(-Species, -Petal.Length) %>%
  head(10)
```

```
## # A tibble: 10 × 3
##    Sepal.Length Sepal.Width Petal.Width
##           <dbl>       <dbl>       <dbl>
##  1          5.1         3.5         0.2
##  2          4.9         3           0.2
##  3          4.7         3.2         0.2
##  4          4.6         3.1         0.2
##  5          5           3.6         0.2
##  6          5.4         3.9         0.4
##  7          4.6         3.4         0.3
##  8          5           3.4         0.2
##  9          4.4         2.9         0.2
## 10          4.9         3.1         0.1
```


```r
iris %>%   
  select(Species, everything(), -ends_with("Length")) %>%
  head(10)
```

```
## # A tibble: 10 × 3
##    Species Sepal.Width Petal.Width
##    <fct>         <dbl>       <dbl>
##  1 setosa          3.5         0.2
##  2 setosa          3           0.2
##  3 setosa          3.2         0.2
##  4 setosa          3.1         0.2
##  5 setosa          3.6         0.2
##  6 setosa          3.9         0.4
##  7 setosa          3.4         0.3
##  8 setosa          3.4         0.2
##  9 setosa          2.9         0.2
## 10 setosa          3.1         0.1
```

rename the column

```r
iris %>%
  rename(sep_len=Sepal.Length, sep_wid=Sepal.Width) %>%
  names()
```

```
## [1] "sep_len"      "sep_wid"      "Petal.Length" "Petal.Width"  "Species"
```

###  manipulation on row

```r
# prepare data
set.seed(896)
sw_dup <-
  starwars %>%
  select(-(films:starships)) %>%  
  sample_n(100, replace=TRUE)
head(sw_dup,10) 
```

```
## # A tibble: 10 × 11
##    name        height  mass hair_…¹ skin_…² eye_c…³ birth…⁴ sex   gender homew…⁵
##    <chr>        <int> <dbl> <chr>   <chr>   <chr>     <dbl> <chr> <chr>  <chr>  
##  1 Sly Moore      178    48 none    pale    white        NA <NA>  <NA>   Umbara 
##  2 Mon Mothma     150    NA auburn  fair    blue         48 fema… femin… Chandr…
##  3 Finn            NA    NA black   dark    dark         NA male  mascu… <NA>   
##  4 Roos Tarpa…    224    82 none    grey    orange       NA male  mascu… Naboo  
##  5 Arvel Cryn…     NA    NA brown   fair    brown        NA male  mascu… <NA>   
##  6 BB8             NA    NA none    none    black        NA none  mascu… <NA>   
##  7 Saesee Tiin    188    NA none    pale    orange       NA male  mascu… Iktotch
##  8 IG-88          200   140 none    metal   red          15 none  mascu… <NA>   
##  9 Yarael Poof    264    NA none    white   yellow       NA male  mascu… Quermia
## 10 Jek Tono P…    180   110 brown   fair    blue         NA male  mascu… Bestin…
## # … with 1 more variable: species <chr>, and abbreviated variable names
## #   ¹​hair_color, ²​skin_color, ³​eye_color, ⁴​birth_year, ⁵​homeworld
```

Use arrange() to reorder the rows. 

```r
sw_dup %>%
  arrange(name, gender) %>%
  head(10)
```

```
## # A tibble: 10 × 11
##    name        height  mass hair_…¹ skin_…² eye_c…³ birth…⁴ sex   gender homew…⁵
##    <chr>        <int> <dbl> <chr>   <chr>   <chr>     <dbl> <chr> <chr>  <chr>  
##  1 Adi Gallia     184    50 none    dark    blue         NA fema… femin… Corusc…
##  2 Arvel Cryn…     NA    NA brown   fair    brown        NA male  mascu… <NA>   
##  3 Bail Prest…    191    NA black   tan     brown        67 male  mascu… Aldera…
##  4 BB8             NA    NA none    none    black        NA none  mascu… <NA>   
##  5 BB8             NA    NA none    none    black        NA none  mascu… <NA>   
##  6 Ben Quadin…    163    65 none    grey, … orange       NA male  mascu… Tund   
##  7 Ben Quadin…    163    65 none    grey, … orange       NA male  mascu… Tund   
##  8 Beru White…    165    75 brown   light   blue         47 fema… femin… Tatooi…
##  9 Beru White…    165    75 brown   light   blue         47 fema… femin… Tatooi…
## 10 Bossk          190   113 none    green   red          53 male  mascu… Trando…
## # … with 1 more variable: species <chr>, and abbreviated variable names
## #   ¹​hair_color, ²​skin_color, ³​eye_color, ⁴​birth_year, ⁵​homeworld
```

using desc() for decreasing order

```r
sw_dup %>%
  arrange(desc(mass)) %>%
  head(10)
```

```
## # A tibble: 10 × 11
##    name        height  mass hair_…¹ skin_…² eye_c…³ birth…⁴ sex   gender homew…⁵
##    <chr>        <int> <dbl> <chr>   <chr>   <chr>     <dbl> <chr> <chr>  <chr>  
##  1 IG-88          200   140 none    metal   red          15 none  mascu… <NA>   
##  2 Tarfful        234   136 brown   brown   blue         NA male  mascu… Kashyy…
##  3 Bossk          190   113 none    green   red          53 male  mascu… Trando…
##  4 Jek Tono P…    180   110 brown   fair    blue         NA male  mascu… Bestin…
##  5 Jek Tono P…    180   110 brown   fair    blue         NA male  mascu… Bestin…
##  6 Jek Tono P…    180   110 brown   fair    blue         NA male  mascu… Bestin…
##  7 Dexter Jet…    198   102 none    brown   yellow       NA male  mascu… Ojom   
##  8 Dexter Jet…    198   102 none    brown   yellow       NA male  mascu… Ojom   
##  9 Qui-Gon Ji…    193    89 brown   fair    blue         92 male  mascu… <NA>   
## 10 Kit Fisto      196    87 none    green   black        NA male  mascu… Glee A…
## # … with 1 more variable: species <chr>, and abbreviated variable names
## #   ¹​hair_color, ²​skin_color, ³​eye_color, ⁴​birth_year, ⁵​homeworld
```
use distinct() to remove the duplicated rows

```r
sw_dup %>%
  distinct() %>%
  glimpse() %>%
  anyDuplicated()  
```

```
## Rows: 57
## Columns: 11
## $ name       <chr> "Sly Moore", "Mon Mothma", "Finn", "Roos Tarpals", "Arvel C…
## $ height     <int> 178, 150, NA, 224, NA, NA, 188, 200, 264, 180, 163, 183, 18…
## $ mass       <dbl> 48, NA, NA, 82, NA, NA, NA, 140, NA, 110, 65, 80, 84, 75, 4…
## $ hair_color <chr> "none", "auburn", "black", "none", "brown", "none", "none",…
## $ skin_color <chr> "pale", "fair", "dark", "grey", "fair", "none", "pale", "me…
## $ eye_color  <chr> "white", "blue", "dark", "orange", "brown", "black", "orang…
## $ birth_year <dbl> NA, 48, NA, NA, NA, NA, NA, 15, NA, NA, NA, NA, 72, 47, 46,…
## $ sex        <chr> NA, "female", "male", "male", "male", "none", "male", "none…
## $ gender     <chr> NA, "feminine", "masculine", "masculine", "masculine", "mas…
## $ homeworld  <chr> "Umbara", "Chandrila", NA, "Naboo", NA, NA, "Iktotch", NA, …
## $ species    <chr> NA, "Human", "Human", "Gungan", "Human", "Droid", "Iktotchi…
```

```
## [1] 0
```

use drop_na() to remove all the rows including NA

```r
sw_dup %>%
  drop_na() %>%
  glimpse() %>%
  anyNA()
```

```
## Rows: 30
## Columns: 11
## $ name       <chr> "Mace Windu", "Beru Whitesun lars", "Padmé Amidala", "Mace …
## $ height     <int> 188, 165, 165, 188, 175, 175, 165, 198, 196, 198, 188, 175,…
## $ mass       <dbl> 84.0, 75.0, 45.0, 84.0, 79.0, 80.0, 45.0, 82.0, 66.0, 82.0,…
## $ hair_color <chr> "none", "brown", "brown", "none", "none", "none", "brown", …
## $ skin_color <chr> "dark", "light", "light", "dark", "light", "red", "light", …
## $ eye_color  <chr> "brown", "blue", "brown", "brown", "blue", "yellow", "brown…
## $ birth_year <dbl> 72, 47, 46, 72, 37, 54, 46, 92, 52, 92, 22, 54, 92, 8, 72, …
## $ sex        <chr> "male", "female", "female", "male", "male", "male", "female…
## $ gender     <chr> "masculine", "feminine", "feminine", "masculine", "masculin…
## $ homeworld  <chr> "Haruun Kal", "Tatooine", "Naboo", "Haruun Kal", "Bespin", …
## $ species    <chr> "Human", "Human", "Human", "Human", "Human", "Zabrak", "Hum…
```

```
## [1] FALSE
```
or can only drop na with specific rows

```r
sw_dup %>%
  drop_na(gender:species) %>%
  glimpse() %>%
  anyNA()
```

```
## Rows: 83
## Columns: 11
## $ name       <chr> "Mon Mothma", "Roos Tarpals", "Saesee Tiin", "Yarael Poof",…
## $ height     <int> 150, 224, 188, 264, 180, 163, 183, 188, 165, 165, 188, 175,…
## $ mass       <dbl> NA, 82, NA, NA, 110, 65, 80, 84, 75, 45, 84, 79, 48, NA, 80…
## $ hair_color <chr> "auburn", "none", "none", "none", "brown", "none", "none", …
## $ skin_color <chr> "fair", "grey", "pale", "white", "fair", "grey, green, yell…
## $ eye_color  <chr> "blue", "orange", "orange", "yellow", "blue", "orange", "ye…
## $ birth_year <dbl> 48, NA, NA, NA, NA, NA, NA, 72, 47, 46, 72, 37, NA, 82, 54,…
## $ sex        <chr> "female", "male", "male", "male", "male", "male", "male", "…
## $ gender     <chr> "feminine", "masculine", "masculine", "masculine", "masculi…
## $ homeworld  <chr> "Chandrila", "Naboo", "Iktotch", "Quermia", "Bestine IV", "…
## $ species    <chr> "Human", "Gungan", "Iktotchi", "Quermian", "Human", "Toong"…
```

```
## [1] TRUE
```

use filter to select rows

```r
sw_dup %>%
  filter(species == "Human", (is.na(mass) | height > 180)) %>%
  head(10)
```

```
## # A tibble: 10 × 11
##    name        height  mass hair_…¹ skin_…² eye_c…³ birth…⁴ sex   gender homew…⁵
##    <chr>        <int> <dbl> <chr>   <chr>   <chr>     <dbl> <chr> <chr>  <chr>  
##  1 Mon Mothma     150    NA auburn  fair    blue         48 fema… femin… Chandr…
##  2 Finn            NA    NA black   dark    dark         NA male  mascu… <NA>   
##  3 Arvel Cryn…     NA    NA brown   fair    brown        NA male  mascu… <NA>   
##  4 Mace Windu     188    84 none    dark    brown        72 male  mascu… Haruun…
##  5 Mace Windu     188    84 none    dark    brown        72 male  mascu… Haruun…
##  6 Qui-Gon Ji…    193    89 brown   fair    blue         92 male  mascu… <NA>   
##  7 Cliegg Lars    183    NA brown   fair    blue         82 male  mascu… Tatooi…
##  8 Cliegg Lars    183    NA brown   fair    blue         82 male  mascu… Tatooi…
##  9 Mon Mothma     150    NA auburn  fair    blue         48 fema… femin… Chandr…
## 10 Cliegg Lars    183    NA brown   fair    blue         82 male  mascu… Tatooi…
## # … with 1 more variable: species <chr>, and abbreviated variable names
## #   ¹​hair_color, ²​skin_color, ³​eye_color, ⁴​birth_year, ⁵​homeworld
```

use filter_all() to choose rows in all the columns

```r
iris[,1:4] %>%
  as_tibble() %>%  
  filter_all(any_vars(. > 7.5))
```

```
## # A tibble: 6 × 4
##   Sepal.Length Sepal.Width Petal.Length Petal.Width
##          <dbl>       <dbl>        <dbl>       <dbl>
## 1          7.6         3            6.6         2.1
## 2          7.7         3.8          6.7         2.2
## 3          7.7         2.6          6.9         2.3
## 4          7.7         2.8          6.7         2  
## 5          7.9         3.8          6.4         2  
## 6          7.7         3            6.1         2.3
```

use filter_if() to choose rows 

```r
sw_dup %>% 
  filter_if(is.character, any_vars(is.na(.)))
```

```
## # A tibble: 19 × 11
##    name        height  mass hair_…¹ skin_…² eye_c…³ birth…⁴ sex   gender homew…⁵
##    <chr>        <int> <dbl> <chr>   <chr>   <chr>     <dbl> <chr> <chr>  <chr>  
##  1 Sly Moore      178    48 none    pale    white        NA <NA>  <NA>   Umbara 
##  2 Finn            NA    NA black   dark    dark         NA male  mascu… <NA>   
##  3 Arvel Cryn…     NA    NA brown   fair    brown        NA male  mascu… <NA>   
##  4 BB8             NA    NA none    none    black        NA none  mascu… <NA>   
##  5 IG-88          200   140 none    metal   red          15 none  mascu… <NA>   
##  6 Qui-Gon Ji…    193    89 brown   fair    blue         92 male  mascu… <NA>   
##  7 R2-D2           96    32 <NA>    white,… red          33 none  mascu… Naboo  
##  8 R5-D4           97    32 <NA>    white,… red          NA none  mascu… Tatooi…
##  9 Captain Ph…     NA    NA unknown unknown unknown      NA <NA>  <NA>   <NA>   
## 10 Ric Olié       183    NA brown   fair    blue         NA <NA>  <NA>   Naboo  
## 11 Poe Dameron     NA    NA brown   light   brown        NA male  mascu… <NA>   
## 12 BB8             NA    NA none    none    black        NA none  mascu… <NA>   
## 13 Yoda            66    17 white   green   brown       896 male  mascu… <NA>   
## 14 Yoda            66    17 white   green   brown       896 male  mascu… <NA>   
## 15 Ric Olié       183    NA brown   fair    blue         NA <NA>  <NA>   Naboo  
## 16 Finn            NA    NA black   dark    dark         NA male  mascu… <NA>   
## 17 Rey             NA    NA brown   light   hazel        NA fema… femin… <NA>   
## 18 Finn            NA    NA black   dark    dark         NA male  mascu… <NA>   
## 19 Rey             NA    NA brown   light   hazel        NA fema… femin… <NA>   
## # … with 1 more variable: species <chr>, and abbreviated variable names
## #   ¹​hair_color, ²​skin_color, ³​eye_color, ⁴​birth_year, ⁵​homeworld
```

###  build new column or mutate column
use mutate to create rows or columns

```r
iris %>%
  as_tibble(iris) %>%
  mutate(add_all = Sepal.Length + Sepal.Width + Petal.Length + Petal.Width) %>%
  head(10)
```

```
## # A tibble: 10 × 6
##    Sepal.Length Sepal.Width Petal.Length Petal.Width Species add_all
##           <dbl>       <dbl>        <dbl>       <dbl> <fct>     <dbl>
##  1          5.1         3.5          1.4         0.2 setosa     10.2
##  2          4.9         3            1.4         0.2 setosa      9.5
##  3          4.7         3.2          1.3         0.2 setosa      9.4
##  4          4.6         3.1          1.5         0.2 setosa      9.4
##  5          5           3.6          1.4         0.2 setosa     10.2
##  6          5.4         3.9          1.7         0.4 setosa     11.4
##  7          4.6         3.4          1.4         0.3 setosa      9.7
##  8          5           3.4          1.5         0.2 setosa     10.1
##  9          4.4         2.9          1.4         0.2 setosa      8.9
## 10          4.9         3.1          1.5         0.1 setosa      9.6
```


```r
iris %>%
  as_tibble() %>%
  mutate(median_petal_length = median(Petal.Length),
         has_long_petals = Petal.Length > median_petal_length,
         has_long_petals = as.numeric(has_long_petals)) %>%  
  select(Petal.Length, median_petal_length, has_long_petals)
```

```
## # A tibble: 150 × 3
##    Petal.Length median_petal_length has_long_petals
##           <dbl>               <dbl>           <dbl>
##  1          1.4                4.35               0
##  2          1.4                4.35               0
##  3          1.3                4.35               0
##  4          1.5                4.35               0
##  5          1.4                4.35               0
##  6          1.7                4.35               0
##  7          1.4                4.35               0
##  8          1.5                4.35               0
##  9          1.4                4.35               0
## 10          1.5                4.35               0
## # … with 140 more rows
```

use mutate_all to apply function to all the rows and columns

```r
msleep %>%
  mutate_all(tolower)
```

```
## # A tibble: 83 × 11
##    name   genus vore  order conse…¹ sleep…² sleep…³ sleep…⁴ awake brainwt bodywt
##    <chr>  <chr> <chr> <chr> <chr>   <chr>   <chr>   <chr>   <chr> <chr>   <chr> 
##  1 cheet… acin… carni carn… lc      12.1    <NA>    <NA>    11.9  <NA>    50    
##  2 owl m… aotus omni  prim… <NA>    17      1.8     <NA>    7     0.0155  0.48  
##  3 mount… aplo… herbi rode… nt      14.4    2.4     <NA>    9.6   <NA>    1.35  
##  4 great… blar… omni  sori… lc      14.9    2.3     0.1333… 9.1   0.00029 0.019 
##  5 cow    bos   herbi arti… domest… 4       0.7     0.6666… 20    0.423   600   
##  6 three… brad… herbi pilo… <NA>    14.4    2.2     0.7666… 9.6   <NA>    3.85  
##  7 north… call… carni carn… vu      8.7     1.4     0.3833… 15.3  <NA>    20.49 
##  8 vespe… calo… <NA>  rode… <NA>    7       <NA>    <NA>    17    <NA>    0.045 
##  9 dog    canis carni carn… domest… 10.1    2.9     0.3333… 13.9  0.07    14    
## 10 roe d… capr… herbi arti… lc      3       <NA>    <NA>    21    0.0982  14.8  
## # … with 73 more rows, and abbreviated variable names ¹​conservation,
## #   ²​sleep_total, ³​sleep_rem, ⁴​sleep_cycle
```

use mutate_if to apply function to specific row and column which satisfied some conditions

```r
iris %>%
  mutate_if(is.double, as.integer) %>%
  head(10)
```

```
## # A tibble: 10 × 5
##    Sepal.Length Sepal.Width Petal.Length Petal.Width Species
##           <int>       <int>        <int>       <int> <fct>  
##  1            5           3            1           0 setosa 
##  2            4           3            1           0 setosa 
##  3            4           3            1           0 setosa 
##  4            4           3            1           0 setosa 
##  5            5           3            1           0 setosa 
##  6            5           3            1           0 setosa 
##  7            4           3            1           0 setosa 
##  8            5           3            1           0 setosa 
##  9            4           2            1           0 setosa 
## 10            4           3            1           0 setosa
```

use mutate_at to apply function to specific row and column

```r
iris %>%
  as_tibble() %>%
  mutate_at(vars(contains("Length"), contains("Width")), ~ .*10) %>%
  head(10)
```

```
## # A tibble: 10 × 5
##    Sepal.Length Sepal.Width Petal.Length Petal.Width Species
##           <dbl>       <dbl>        <dbl>       <dbl> <fct>  
##  1           51          35           14           2 setosa 
##  2           49          30           14           2 setosa 
##  3           47          32           13           2 setosa 
##  4           46          31           15           2 setosa 
##  5           50          36           14           2 setosa 
##  6           54          39           17           4 setosa 
##  7           46          34           14           3 setosa 
##  8           50          34           15           2 setosa 
##  9           44          29           14           2 setosa 
## 10           49          31           15           1 setosa
```

We can use if_else() and case_when() to decide how to change the value
if_else(condition, if true:---, if false: ----)

```r
warpbreaks %>%
  mutate(breed = if_else(wool == "A",
                         true = "Merino",
                         false = "Corriedale")) %>%
  sample_frac(size = 0.15)
```

```
##   breaks wool tension      breed
## 1     41    B       L Corriedale
## 2     54    A       L     Merino
## 3     51    A       L     Merino
## 4     15    B       H Corriedale
## 5     13    B       H Corriedale
## 6     30    A       M     Merino
## 7     35    A       M     Merino
## 8     21    A       H     Merino
```
case_when (condition1 ~ class1,
           condition2 ~ class2,
           condition3 ~ class3,
           ......
  )

```r
warpbreaks %>%
  mutate(tension=case_when(tension == "H" ~ "High",
                           tension == "M" ~ "Medium",
                           tension == "L" ~ "Low",
                           TRUE ~ NA_character_)) %>%
  sample_frac(size = 0.15)
```

```
##   breaks wool tension
## 1     29    B  Medium
## 2     28    B    High
## 3     30    A  Medium
## 4     16    B    High
## 5     25    A     Low
## 6     29    B     Low
## 7     70    A     Low
## 8     15    B    High
```

###  Group
use group_by() to create groups and use ungroup to separate group
use summarize() to find out the properties of the group
n() :count the frequency
sum(var),max(var),min(var),mean(var),median(var),sd(var)

```r
iris %>%
  group_by(Species) %>%
  summarise(n = n(),
            avg_len = mean(Petal.Length, na.rm=TRUE),
            med_len = median(Petal.Length))
```

```
## # A tibble: 3 × 4
##   Species        n avg_len med_len
##   <fct>      <int>   <dbl>   <dbl>
## 1 setosa        50    1.46    1.5 
## 2 versicolor    50    4.26    4.35
## 3 virginica     50    5.55    5.55
```

We can also use summarize_if,summarize_all

```r
dat <- iris %>%
  group_by(Species) %>%
  summarise_if(is.numeric, list(~mean(.), ~median(.), ~min(.), ~max(.)))
dat
```

```
## # A tibble: 3 × 17
##   Species    Sepal.Len…¹ Sepal…² Petal…³ Petal…⁴ Sepal…⁵ Sepal…⁶ Petal…⁷ Petal…⁸
##   <fct>            <dbl>   <dbl>   <dbl>   <dbl>   <dbl>   <dbl>   <dbl>   <dbl>
## 1 setosa            5.01    3.43    1.46   0.246     5       3.4    1.5      0.2
## 2 versicolor        5.94    2.77    4.26   1.33      5.9     2.8    4.35     1.3
## 3 virginica         6.59    2.97    5.55   2.03      6.5     3      5.55     2  
## # … with 8 more variables: Sepal.Length_min <dbl>, Sepal.Width_min <dbl>,
## #   Petal.Length_min <dbl>, Petal.Width_min <dbl>, Sepal.Length_max <dbl>,
## #   Sepal.Width_max <dbl>, Petal.Length_max <dbl>, Petal.Width_max <dbl>, and
## #   abbreviated variable names ¹​Sepal.Length_mean, ²​Sepal.Width_mean,
## #   ³​Petal.Length_mean, ⁴​Petal.Width_mean, ⁵​Sepal.Length_median,
## #   ⁶​Sepal.Width_median, ⁷​Petal.Length_median, ⁸​Petal.Width_median
```
