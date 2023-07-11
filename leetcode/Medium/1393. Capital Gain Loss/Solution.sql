select stock_name, sum(IF(operation='Buy', -price, price)) as capital_gain_loss
from Stocks
group by stock_name;