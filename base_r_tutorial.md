# Base R Tutorial

Siqin Shen





## Overview

This is a Base R Cheatsheet/Tutorial, and it includes the most common Base R graphic functions and parameters.

I will use data `SleepStudy` from **Lock5withR** package.

```r
SleepStudy <- Lock5withR::SleepStudy
```


## Section 1 - Functions


### Histogram


```r
hist(SleepStudy$GPA, breaks = 10)
```

<img src="base_r_tutorial_files/figure-html/unnamed-chunk-3-1.png" width="672" style="display: block; margin: auto;" />

### Barplot

**Make sure the data is a matrix or vector before plot barplot.**

**The most easy way is to use the table() function to transform the data.**


```r
LarkOwl <- table(SleepStudy$LarkOwl)
barplot(LarkOwl, names.arg = "Lark-Owl", border = "blue" , col = "grey", horiz = FALSE)
```

<img src="base_r_tutorial_files/figure-html/unnamed-chunk-4-1.png" width="672" style="display: block; margin: auto;" />

### Scatter plot

```r
plot(SleepStudy$StressScore, SleepStudy$GPA)
```

<img src="base_r_tutorial_files/figure-html/unnamed-chunk-5-1.png" width="672" style="display: block; margin: auto;" />

### Dot Plot

**A dot plot is just a bar chart that uses dots to represent individual quanta. **

source: https://www.mvorganizing.org/is-a-dot-plot-the-same-as-a-scatter-plot/#:~:text=A%20dot%20plot%20is%20just,height%20and%20one%20represented%20weight.

```r
table_data <- table(SleepStudy$DepressionStatus, SleepStudy$LarkOwl)
dotchart(table_data)
```

<img src="base_r_tutorial_files/figure-html/unnamed-chunk-6-1.png" width="672" style="display: block; margin: auto;" />

### Box Plot

```r
boxplot(PoorSleepQuality ~ DepressionStatus, data = SleepStudy, horizontal = FALSE, names = c("moderate", "normal", "severe"), col = "gold")
```

<img src="base_r_tutorial_files/figure-html/unnamed-chunk-7-1.png" width="672" style="display: block; margin: auto;" />

### Mosaic Plot

**Make sure the data is a matrix or vector before plot mosaic plot.**

**The most easy way is to use the table() function to transform the data.**


```r
table_data <- table(SleepStudy$ClassYear, SleepStudy$NumEarlyClass)
mosaicplot(table_data, color = TRUE)
```

<img src="base_r_tutorial_files/figure-html/unnamed-chunk-8-1.png" width="672" style="display: block; margin: auto;" />

### Density Plot

**Make sure to transform the data into density before plot density plot.**

**The most easy way is to use the density() function to transform the data.**


```r
density_gpa <- density(SleepStudy$GPA)
plot(density_gpa)
```

<img src="base_r_tutorial_files/figure-html/unnamed-chunk-9-1.png" width="672" style="display: block; margin: auto;" />


## Section 2 - Parameters

### Main

**It adds the title to a graph.**


```r
hist(SleepStudy$GPA, breaks = 10, main = "GPA distribution")
```

<img src="base_r_tutorial_files/figure-html/unnamed-chunk-10-1.png" width="672" style="display: block; margin: auto;" />

### Labels

**It adds the x-axis and y-axis labels to the graph.**


```r
hist(SleepStudy$GPA, breaks = 10, main = "GPA distribution", xlab = "GPA", ylab = "Number of Students")
```

<img src="base_r_tutorial_files/figure-html/unnamed-chunk-11-1.png" width="672" style="display: block; margin: auto;" />

### Add Color


```r
hist(SleepStudy$GPA, breaks = 10, main = "GPA distribution", xlab = "GPA", ylab = "Number of Students",col.lab = "light blue", col = "gold")
```

<img src="base_r_tutorial_files/figure-html/unnamed-chunk-12-1.png" width="672" style="display: block; margin: auto;" />

### Point Shape


```r
plot(SleepStudy$StressScore, SleepStudy$GPA, main = "Stress Score vs GPA", pch = 6, xlab = "StressScore", ylab = "GPA",col.lab = "light blue")
```

<img src="base_r_tutorial_files/figure-html/unnamed-chunk-13-1.png" width="672" style="display: block; margin: auto;" />

### Legend


```r
plot(SleepStudy$StressScore, SleepStudy$GPA, main = "Stress Score vs GPA", col = SleepStudy$LarkOwl, pch = 6, xlab = "StressScore", ylab = "GPA",col.lab = "light blue")
legend("topleft", legend = levels(SleepStudy$LarkOwl), col = 1:nlevels(SleepStudy$LarkOwl), pch = 6, title = "LarkOwl")
```

<img src="base_r_tutorial_files/figure-html/unnamed-chunk-14-1.png" width="672" style="display: block; margin: auto;" />

### Point/label Size


```r
plot(SleepStudy$StressScore, SleepStudy$GPA, main = "Stress Score vs GPA", col = SleepStudy$LarkOwl, pch = 6, xlab = "StressScore", ylab = "GPA",col.lab = "light blue", cex.lab = 1.5, cex = 0.75)
legend("topleft", legend = levels(SleepStudy$LarkOwl), col = 1:nlevels(SleepStudy$LarkOwl), pch = 6, title = "LarkOwl")
```

<img src="base_r_tutorial_files/figure-html/unnamed-chunk-15-1.png" width="672" style="display: block; margin: auto;" />

### Line Type


```r
plot(density_gpa, main = "GPA Density Distribution", lty = 4, col = "red")
```

<img src="base_r_tutorial_files/figure-html/unnamed-chunk-16-1.png" width="672" style="display: block; margin: auto;" />

### Line Width


```r
plot(density_gpa, main = "GPA Density Distribution", lty = 4, col = "red", lwd = 2)
```

<img src="base_r_tutorial_files/figure-html/unnamed-chunk-17-1.png" width="672" style="display: block; margin: auto;" />

## Section 3 - Others

- Add best fit Lines to a scatter plot

**We need to get the function of line first.**
**We can use Loess smoother loess() to simulate the line.**

source: https://dcgerard.github.io/stat234/base_r_cheatsheet.html


```r
loess_fit <- loess(GPA ~ StressScore, data = SleepStudy)
xnew <- seq(min(SleepStudy$StressScore), max(SleepStudy$StressScore), length = 100)
ynew <- predict(object = loess_fit, newdata = data.frame(StressScore = xnew))

plot(SleepStudy$StressScore, SleepStudy$GPA, main = "Stress Score vs GPA", col = SleepStudy$LarkOwl, pch = 6, xlab = "StressScore", ylab = "GPA",col.lab = "light blue", cex.lab = 1.5, cex = 0.75)
legend("topleft", legend = levels(SleepStudy$LarkOwl), col = 1:nlevels(SleepStudy$LarkOwl), pch = 6, title = "LarkOwl")
lines(xnew, ynew, col = "blue", lty = 1, lwd = 2)
```

<img src="base_r_tutorial_files/figure-html/unnamed-chunk-18-1.png" width="672" style="display: block; margin: auto;" />

### Facet Wrap


```r
wrap <- par(mfrow = c(2, 3))

hist(SleepStudy$GPA, breaks = 10, main = "GPA distribution")
barplot(LarkOwl, names.arg = "Lark-Owl", border = "blue" , col = "grey", horiz = FALSE, main = "Lark Owl Count")
plot(SleepStudy$StressScore, SleepStudy$GPA, main = "Stress Score-GPA Relation")
dotchart(table_data, main = "DepressionStatus-LarkOwl Relation")
boxplot(PoorSleepQuality ~ DepressionStatus, data = SleepStudy, horizontal = FALSE, names = c("moderate", "normal", "severe"), col = "gold", main = "PoorSleepQuality vs DepressionStatus")
mosaicplot(table_data, color = TRUE, main = "ClassYear vs Num Early Class")
```

<img src="base_r_tutorial_files/figure-html/unnamed-chunk-19-1.png" width="960" style="display: block; margin: auto;" />
