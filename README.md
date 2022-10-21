# mb_btc_datascience
Playing with requests and manipulating tabular data
## Pipeline...
### Get Trades -> (a1) Filter-Type -> (a2) Filter-Price -> (a3) Modify-Table
#### (a1) -> Histogram-Type -> Linear-Regression 
#### (a2) -> Histogram-Price -> Linear-Regression
### get_trades.py -> (a1) filter-buy-sell.py  -> (a2) filter-price.py
#### (a1) -> buy-sell-histogram.py -> histogram-linear_regression.py 
#### (a2) -> histogram-price.py -> histogram-price-linear-reg.py
#### (a3) -> new_historical.py
