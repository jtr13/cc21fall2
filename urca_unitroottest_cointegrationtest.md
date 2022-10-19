# Urca: Unit Root Test and Cointegration Test

Zonghan Yue(zy2493), Alvin Pan (qp2134)

**Note (2022-10-19): code not run since data files are no longer available.**




```r
library(urca)
library(ggplot2)
library(RCurl)
```

## Introduction:

Rstudio package urca developed by Bernhard Pfaff, Eric Zivot, Matthieu Stigler in 2016. “urca” is the abbreviation of the Unit Root and Cointegration Tests for Time Series Data. The package provides functions for users to do the cointegration and Unit Root test.

#### Dataset Description:

Data Set scraped from OKEX exchange's API. It is the minute level historical candlesticks of the ETH price. 

Columns:
&emsp; time: the UTC time
&emsp; open: the first trade during that time period
&emsp; high: the highest price trade during that time period
&emsp; low: the lowest price trade during that time period
&emsp; close: the last trade during that time period
&emsp; volume: the quantity trades during that time period




Examples:

```r
eth <- read.csv(url("https://raw.githubusercontent.com/yzh9810/edav_cc/main/eth-usdt.csv"))
eth$time = as.POSIXlt(eth$time)
```

#### What is stationarity ?

 A stationary time series is one whose properties do not depend on the time at which the series is observed. Thus, time series with trends, or with seasonality, are not stationary — the trend and seasonality will affect the value of the time series at different times. On the other hand, a white noise series is stationary — it does not matter when you observe it, it should look much the same at any point in time. 



```r
plot(eth$time, eth$close, type="l", xlab = "Time", ylab = "price", main = "Unstationary: Eth Price")
```

```r
time = eth$time[2:100000]
pre_close = eth$close[1:99999]
next_close = eth$close[2:100000]
close = next_close - pre_close
plot(time, close, type="l", xlab = "Time", ylab = "price", main = "stationary: Eth Return")
```

#### What is Unit Root?
 
 Unit Root: A unit root (also called a unit root process or a different stationary process) is a stochastic trend in a time series, sometimes called a “random walk with drift”; If a time series has a unit root, it shows a systematic pattern that is unpredictable.

A typical simplest time series model is autoregressive model, 
 $$y_{t}=ay_{t-1}+\epsilon_{t}$$
In this equation, the predict variable $y_{t}$ is only predicted by previous time period $y_{t-1}$ and the errors. The preceding model is a first-order autoregression model. If $a < 1$, the model is stationary. If $a = 1$, the model is nonstationary, where $a$ is a stationary test.
 
 Unit Root Tests:
  Unit root tests are tests for stationarity in a time series. The shape of stationarity is if a shift in time doesn’t cause a change in the shape of the distribution. Unit roots are one cause for non-stationarity.


#### What is Cointegration test?

  Cointegration test is used to establish if there is a correlation between several time series in the long term. 


#### Below we have included decumentations and experiments of several popular test methods

## Unit Root Tests methods:

#### The Dickey Fuller Test:

  The Dickey Fuller Test is based on linear regression. 
  
  H0: null hypothes is that a unit root is present in an autoregressive time series model. 
  
  H1: a unit root is not present in an autoregressive time series model. 
  
  The formula for the test is AR(1) with $\alpha = 0$ and $\beta = 0$

$$y_{t} = (\sigma y_{t-1}) + \epsilon_{t}$$
thus, 
$$\Delta y_{t} = (\sigma-1) y_{t-1} + \epsilon_{t} = \gamma y_{t-1} + \epsilon_{t}$$

**urca method: **

  ur.df:    Augmented-Dickey-Fuller Unit Root Test

**Arguments:**
  
&emsp; y:	\ Vector to be tested for a unit root.
      
&emsp; type:	\ Test type, either "none", "drift" or "trend".

For the AR(1) model:
$$y_{t} = \alpha + \beta t +  \sigma y_{t-1} + \epsilon_{t}$$
"none" means $\alpha = 0$ and $\beta = 0$, 
  
"drift" means $\beta = 0$, and $\alpha$ not equal to 0
  
"trend" means both $\alpha$ and $\beta$ are not equal to 0


&emsp; lags:	\ Number of lags for endogenous variables to be included.

Lags in time series is how many previous time period you used to predict target variable. For example, lags n means the equation you use is $$y_{t} = \alpha + \beta t +  (\sigma_{t-1} y_{t-1} + \sigma_{t-2} y_{t-2} + \sigma_{t-3} y_{t-3} +...+ \sigma_{t-n} y_{t-n}) + \epsilon_{t}$$

&emsp; selectlags: \ Lag selection can be achieved according to the Akaike AIC" or the Bayes "BIC" information criteria. The maximum number of lags considered is set by lags. The default is to use a "fixed" lag length set by lags.


**Usage**

&emsp; ur.df(y, type = c("none", "drift", "trend"), lags = 1, selectlags = c("Fixed", "AIC", "BIC"))


**Example**

```r
urtest = ur.df(eth$close, type="none", lags = 1)
summary(urtest)
```

**Interpretation**

Value of test-statistic is 0.2241 and the Critical values for test statistics are: tau1 -2.58 -1.95 -1.62 for (1%, 5%, 10%). Thus, We reject the null, which means a unit root is present. The "z.lag1" is the $\gamma$ term, the coefficient for the lag term (y(t-1)), which is p=0.823, implies that gamma isn't statistically significant to this model. 

However, the R-square is only 0.00036, which means the time series is not satisfied the non-draft and non-trend model. Thus, the model is not actualy fit the data.

#### The Elliott–Rothenberg–Stock Test:

 The Elliott–Rothenberg–Stock Test have two subtest: P-test takes the error term’s serial correlation into account, the DF-GLS test can be applied to detrended data without intercept.
  
  H0: null hypothes is that a unit root is present in an autoregressive time series model. 
  
  H1: a unit root is not present in an autoregressive time series model. 

**urca method: **

  ur.ers:    Elliott, Rothenberg & Stock Unit Root Test

**Arguments:**
  
&emsp; y:	\ Vector to be tested for a unit root.
      
&emsp; type:	\ Test type, either "DF-GLS" (default), or "P-test".

What Is P-test?

The p-value approach to hypothesis testing uses the calculated probability to determine whether there is evidence to reject the null hypothesis.

What Is DF-GLS?

ADF-GLS test (or DF-GLS test) is a test for a unit root in an economic time series sample. It locally de-trends (de-means) data series to efficiently estimate the deterministic parameters of the series, and use the transformed data to perform a usual ADF unit root test.

&emsp; model:	\ The deterministic model used for detrending.

A detrend involves removing the effects of trend from a data set to show only the differences in values from the trend; it allows cyclical and other patterns to be identified. Detrending can be done using regression analysis and other statistical techniques. Detrending shows a different aspect of time series data by removing deterministic and stochastic trends.

&emsp; lag.max: \ The maximum numbers of lags used for testing of a decent lag truncation for the "P-test" (BIC used), or the maximum number of lagged differences to be included in the test regression for "DF-GLS".


**Usage**

&emsp; ur.ers(y, type = c("DF-GLS", "P-test"), model = c("constant", "trend"), lag.max = 4)

We reject the null hypothesis if the test statistics is greater than 5% confidence value.

**Example**

```r
urtest = ur.ers(eth$close, type="P-test", model="const", lag.max=6)
summary(urtest)
```

**Intepretation**

Test-statistic is: 6.3283, the Critical values of P-test is 1.99, 3.26, 4.48, which for 1%, 5%, 10%, we can not reject the null hypothes. It means that eth is nonstationary.

#### The Schmidt–Phillips Test:

  The Schmidt–Phillips Test includes the coefficients of the deterministic variables in the null and alternate hypotheses. Subtypes are the rho-test and the tau-test. 

  H0: null hypothes is that an observable time series is stationary around a deterministic trend. 
  
  H1: a deterministic trend time series have a unit root 
  
  A process Y is said to be trend-stationary if 

  $$Y(t) = f(t) + e_{t}$$
  f is any function from R to R. The $e_{t}$ is the stationary process.
  
  The Adjusted R-squared: 0.9999 which means the eth time series fit the trend model. 
  
  The p-value for the y.lagged < 0.01, we can reject the null hypothesis. It means that eth is an observable time series is nonstationary around a deterministic trend.

**urca method: **

  ur.sp:    The Schmidt–Phillips Test

**Arguments:**
  
&emsp; y:	\ Vector to be tested for a unit root.
      
&emsp; type:	\ Test type, either 'tau' or 'rho' test.

tau test:

 Kendall’s Tau: usually smaller values than Spearman’s rho correlation. Calculations based on concordant and discordant pairs. Insensitive to error. P values are more accurate with smaller sample sizes

rho test:

 Spearman’s rho usually have larger values than Kendall’s Tau.  Calculations based on deviations.  Much more sensitive to error and discrepancies in data.

&emsp; pol.deg:	\ Degree of polynomial in the test regression.

&emsp; signif: \ Significance level for the critical value of the test statistic.


**Usage**

&emsp; ur.sp(y, type = c("tau", "rho"), pol.deg = c(1, 2, 3, 4),
      signif = c(0.01, 0.05, 0.1))


**Example**

```r
urtest = ur.sp(eth$close, type="tau", pol.deg=1, signif=0.05)
summary(urtest)
```

**Interpretation**
From the t-test, test-statistic is: -1.562, Critical value for a significance level of 0.05 is: -3.02. Thus, we have to reject the null hypothesis. 

#### The Zivot-Andrews test:

  The Zivot-Andrews test allows a break at an unknown point in the intercept or linear trend. 
  
  H0: a null hypothesis of a unit root process with drift that excludes exogenous structural change
  
  H1: the time series is stationary that excludes exogenous structural change
**urca method: **

  ur.za:    Zivot & Andrews Unit Root Test

**Arguments:**
  
&emsp; y:	\ Vector to be tested for a unit root.
      
&emsp; model:	\ Specification if the potential break occured in either the intercept, the linear trend or in both.

&emsp; lag: \ The highest number of lagged endogenous differenced variables to be included in the test regression.


**Usage**

&emsp; ur.za(y, model = c("intercept", "trend", "both"), lag=NULL)


**Example**

```r
urtest = ur.za(eth$close[1:1000], model="intercept", lag=2)
summary(urtest)
```
x, we have sufficient evidence to reject the null that the unit root has a unit root with a single break.

Intepretation:

The test said that Potential break point at 116 position. The break position is the place that the series got structural breaks.  

Since both the p-values of the intercept and y.l1 are < 0.05 and test-statistic -5.6 less than the Critical values of P-test is -4.8. We can can reject the null hypothes with 95 percentage confidence. It means that eth is stationary with drift before the break.


#### The Johansen-Procedure test:

  The Johansen-Procedure test is a procedure for testing cointegration of several time series.

**urca method: **

  ca.jo:    A Unit Root and Cointegration Test for Time Series Data

**Arguments:**
  
&emsp; x:	\ Data frame/matrix to be tested. Given a general VAR model, $$X_t = \Pi_1 X_{t-1} + \dots + \Pi_k X_{t-k} + \mu + {\Phi D}_t + \varepsilon_t , \quad (t = 1, \dots, T),$$
      
&emsp; type:	\ The type of test to be conducted, either "eigen"(eigenvalue) or "trace".

&emsp; ecdet: \ Character, ‘none’ for no intercept in cointegration, ‘const’ for constant term in cointegration and ‘trend’ for trend variable in cointegration.

&emsp; K: \ The lag order of the series (levels) in the Vector autoregression(VAR).

&emsp; spec: \ Determines the specification of the vector error correction model(VECM).

&emsp;&emsp; If spec="longrun", the VECM is estimated by:
$$\Delta X_t = \Gamma_1 \Delta X_{t-1} + \dots + \Gamma_{p-1} \Delta X_{t-p+1} + {\Pi X}_{t-p} + \mu + {\Phi D}_t + \varepsilon_t, \quad (t = 1, \dots , T),$$ 
&emsp;&emsp; where $$\Gamma_i = \Pi_1 + \dots + \Pi_i - I, \quad (i = 1, \dots , p-1),$$
$$\Pi = \Pi_1 + \dots + \Pi_p - I$$ 

&emsp;&emsp; The $\Gamma_i$ matrices contain the cumulative long-run impacts. 

&emsp;&emsp; Else spec="transitory", the VECM is estimated by: 
$$\Delta X_t = \Gamma_1 \Delta X_{t-1} + \dots + \Gamma_{p-1} \Delta X_{t-p+1} + {\Pi X}_{t-1} + \mu + {\Phi D}_t + \varepsilon_t$$ 
&emsp;&emsp; where $$\Gamma_i = \Pi_{i+1} + \dots + \Pi_p - I, \quad(i = 1, \dots , p-1),$$ 

$$\Pi = \Pi_1 + \dots + \Pi_p - I.$$ 
&emsp;&emsp; The $\Pi$ matrix is the same as in the longrun VECM. 

&emsp;&emsp; Both inferences drawn on $\Pi$ and the explanatory power will be the same, but the $\Gamma_i$ matrices are no longer the same in terms of measuring transitory effects.

&emsp; season: \ If seasonal dummies should be included, the data frequency must be set accordingly, i.e ‘4’ for quarterly data. If "season" is not NULL, centered seasonal dummy variables are included.

&emsp; dumvar: \ If dummy variables should be included, a matrix with row dimension equal to x can be provided. If "dumvar" is not NULL, a matrix of dummy variables is included in the VECM. Furthermore, the number of rows of the matrix containing the dummy variables must be equal to the row number of x

Note: Critical values are only reported for systems with less than 11 variables and are taken from Osterwald-Lenum.

**Usage**

&emsp; ca.jo(x, type = c("eigen", "trace"), ecdet = c("none", "const", "trend"), K = 2,
spec=c("longrun", "transitory"), season = NULL, dumvar = NULL)

&emsp; We denote $r$ as the rank of the matrix $\Pi$ and it's upper bounded by the number of time series vectors under test(Denoted as $n$), where $r = 0$ represents the test for presence of cointegration. It sequentially tests whether $r \leq k$, where $k \in [0, n-1]$. We normally reject a null hypothesis if the test statistics is larger than 5% confidence level estimate, where the best estimate of the rank represents the number time series that the linear combinations requires to form a stationary series. Then we can use the eigenvector that corresponds to the largest eigenvalue to compute the linear combinations w.r.t $r$.

**Example**

We first extract the target time series stock vectors from the 2 datasets

```r
xrp <- read.csv(url("https://raw.githubusercontent.com/yzh9810/edav_cc/main/xrp-usdt.csv"))
eth <- read.csv(url("https://raw.githubusercontent.com/yzh9810/edav_cc/main/eth-usdt.csv"))
xrp$time = as.POSIXlt(xrp$time)
eth$time = as.POSIXlt(eth$time)
```

We first visualize the 2 time series data:

```r
plot(xrp$time, xrp$close, type="l", xlab = "Time", ylab = "close", col="red", main = "Stock timeseries", ylim = c(0,10))
#apply logorithm to eth data since the magnitudes are significantly higher.
lines(eth$time, log(eth$close), col="blue")
```

Now we do the modelling:

```r
stock = data.frame(y = xrp$close, x = log(eth$close))
coint = ca.jo(stock, type="trace", ecdet="trend", K=2, spec="longrun")
summary(coint)
```

**Interpretation** 

There are 3 generated eigenvalues and the largest one is 1.03e-4. In the next section, there are 2 hypotheses of $r\leq 1$ and $r = 0$, where $r$ is the rank of the matrix $\Pi$ and it's upper bounded by the number of time series vectors under test(In this case $r \leq 2$). column 1,2,3,4 contain test statistics, 10%, 5% and 1% confidence level values respectively. 

The test statistics 31.34 is greater 30.45, which is the 1% confidence level value. Hence we have sufficient evidence to reject the null hypothesis that there is no cointegration. But since for $r \leq 1$ the 10% confidence level value is 10.49, which is higher than the test statistics, we don't have sufficient evidence to reject that $r \leq 1$. Thus the test tells us we only need one of the two time series vectors to form a stationary series. The eigenvector that has the largest eigenvalue is column y.12 of the matrix in section 3, where we only need one of y.12 and x.12 to form a stationary series. We plot the 2 series weighted by their corresponding eigenvalues below.


```r
plot(xrp$time, stock$y, type="l", col = "red", xlab = "Time", ylab = "close", ylim = c(-10,2), main = "Stationary series")
lines(xrp$time, -1.210520*stock$x, col = "blue")
```

References:

Bernhard Pfaff. Package ‘urca’. September 6, 2016, from https://cran.r-project.org/web/packages/urca/urca.pdf

ur.sp: Schmidt & Phillips Unit Root Test.(2020) https://rdrr.io/cran/urca/

YUGESH VERMA. Dickey-Fuller Test In Time-Series Analysis. Aug 18, 2021, from https://analyticsindiamag.com/complete-guide-to-dickey-fuller-test-in-time-series-analysis/ 

aptech, A Guide to Conducting Cointegration Tests, JANUARY 28, 2020 https://www.aptech.com/blog/a-guide-to-conducting-cointegration-tests/

Peter Schmidt, Peter C.B. Phillips, Cowles Foundation for Research in Economics at Yale University October, 1989
https://cowles.yale.edu/sites/default/files/files/pub/d09/d0933.pdf

Schmidt, P. and Phillips, P.C.B. (1992), LM Test for a Unit Root in the Presence of Deterministic Trends, Oxford Bulletin of Economics and Statistics, 54(3), 257--287.

Zivot, E. and Andrews, Donald W.K. (1992), Further Evidence on the Great Crash, the Oil-Price Shock, and the Unit-Root Hypothesis, Journal of Business & Economic Statistics, 10(3), 251–270.

Johansen test
https://en.wikipedia.org/wiki/Johansen_test
