# Curve Fitting of Commodity Future Prices

## Summary

This notebook demostrates how to use Python **curves** library to build commodity futures curves.  Once the prices are generated, one can estimate the volatility of a futures contract with a specific number of days to expiry.  From the volatility, one can calculate other analytics like VaR and Expected Shortfall of the position.

## Notebook
1. https://github.com/edgetrader/commodity-curve-fitting/blob/master/notebook/curve-fitting.ipynb

## Reference

1. https://www.quandl.com/
2. http://www.shfe.com.cn/en/
3. https://github.com/cmdty/curves
4. https://pypi.org/project/curves/
5. https://github.com/jonemo/pythonnet-docker

## Special notes

The **curves** library runs in an environment with **pythonnet** installed.  I ran the notebook in the a docker container with **pythonnet** installed.


