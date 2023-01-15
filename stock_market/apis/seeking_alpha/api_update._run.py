import requests
import pandas as pd
import json
import os
from os.path import join
import market_data as md
import apis

exclude_screeners = ["Earnings Season's Strong Sells",
"Earnings Season's Top Stocks",
"Top Energy by SA Authors ",
"Most Shorted Stocks",
"Strong Buy Stocks With Short Squeeze Potential",
"Earnings Season's Top Stocks"]


def build_dict_count(screeners, default_count = 15):
    screener_names = [screener[0] for screener in screeners]
    dict_count ={}
    for name in screener_names:
        dict_count[name] = default_count
    dict_count['Top Rated Stocks'] = 45
    dict_count['Top Stocks by Quant'] = 45
    return dict_count

screeners = apis.get_sa_screener_details_list()
resultsdict = apis.adict_screener_details(screeners, perpage=45)
apis.change_value_to_list(resultsdict)
apis.replacedot((resultsdict))
print('\nNo of portfolios: ',len(resultsdict.keys()))
dict_count = build_dict_count(screeners)
apis.trim_to_count(resultsdict, dict_count)
subdir = md.sa
path = os.path.join(md.data_dir, subdir)
apis.file_api_symbols(resultsdict, path)




