# mb_btc_datascience
Playing with requests and manipulating tabular data
## Pipeline...
### Get Trades -> (a1) Filter-Type -> (a2) Filter-Price 
#### (a1) -> Histogram-Type -> Linear-Regression 
#### (a2) -> Histogram-Price
### get_trades.py -> (a1) filter-buy-sell.py  -> (a2) filter-price.py
#### (a1) -> buy-sell-histogram.py -> histogram-linear_regression.py 
#### (a2) -> histogram-price.py
