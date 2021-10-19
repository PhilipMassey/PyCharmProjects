#!/usr/bin/env bash
echo 'running mdb missing'
python3 /Users/philipmassey/PycharmProjects/stock_market/market_data/scripts/mdb_missing_five.py
echo 'starting plot all'
echo 'running steady increase'
python3 /Users/philipmassey/PycharmProjects/stock_market/performance/scripts/steady_increase.py
echo 'starting plot all'
nohup python3 /Users/philipmassey/PycharmProjects/stock_market/plots/scripts/plot_all_today.py &
