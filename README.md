


### 0. Quandl's data constructs are listed here: https://docs.quandl.com/docs/data-organization

### 1. Get started with an interactive notebook [here](view/Quandl-GettingStarted.ipynb)

### 2. hello world for batch files: 
get a ticker as time series, simply manually run the following: "ticker.py AAPL" or "ticker.py AMZN" or "ticker.py CSCO" et cetera

### 3. Example regression output using quandl and python libs:

![example](raw/latest/results/example.png?inline=true)



```
                          OLS Regression Results                            
==============================================================================
Dep. Variable:                      y   R-squared:                       0.932
Model:                            OLS   Adj. R-squared:                  0.931
Method:                 Least Squares   F-statistic:                     4747.
Date:                Fri, 09 Jun 2017   Prob (F-statistic):          6.93e-205
Time:                        18:46:43   Log-Likelihood:                -458.00
No. Observations:                 350   AIC:                             920.0
Df Residuals:                     348   BIC:                             927.7
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [95.0% Conf. Int.]
------------------------------------------------------------------------------
const          3.5858      0.096     37.269      0.000         3.397     3.775
x1             0.0164      0.000     68.897      0.000         0.016     0.017
x2             0.0164      0.000     68.897      0.000         0.016     0.017
==============================================================================
Omnibus:                        3.826   Durbin-Watson:                   0.129
Prob(Omnibus):                  0.148   Jarque-Bera (JB):                3.628
Skew:                           0.195   Prob(JB):                        0.163
Kurtosis:                       2.689   Cond. No.                     2.13e+16
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The smallest eigenvalue is 6.33e-26. This might indicate that there are
strong multicollinearity problems or that the design matrix is singular.
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                      y   R-squared:                       0.751
Model:                            OLS   Adj. R-squared:                  0.750
Method:                 Least Squares   F-statistic:                     1048.
Date:                Fri, 09 Jun 2017   Prob (F-statistic):          5.45e-107
Time:                        18:46:44   Log-Likelihood:                -1002.5
No. Observations:                 350   AIC:                             2009.
Df Residuals:                     348   BIC:                             2017.
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [95.0% Conf. Int.]
------------------------------------------------------------------------------
const          8.7319      0.456     19.152      0.000         7.835     9.629
x1             0.0364      0.001     32.367      0.000         0.034     0.039
x2             0.0364      0.001     32.367      0.000         0.034     0.039
==============================================================================
Omnibus:                       25.045   Durbin-Watson:                   0.041
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               28.535
Skew:                           0.692   Prob(JB):                     6.36e-07
Kurtosis:                       3.205   Cond. No.                     2.13e+16
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The smallest eigenvalue is 6.33e-26. This might indicate that there are
strong multicollinearity problems or that the design matrix is singular.
```