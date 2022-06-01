import market_data as md

holding_ports = ['Fidelity Health','Fidelity Potential', 'SA Health, Industrial','SA Technology','SA Industiral, Staples']
sa_top_ports = ['Top Communication Stocks','Top Consumer Discretionary Stocks','Top Consumer Staples Stocks','Top Energy by SA Authors ','Top Energy Stocks','Top Financial Stocks','Top Growth Stocks','Top Healthcare Stocks','Top Industrial Stocks','Top Materials Stocks','Top Quant Dividend Stocks','Top Rated Dividend Stocks','Top Rated Stocks','Top Real Estate Stocks''Top Small Cap Stocks','Top Stocks by Quant','Top Stocks Under $10','Top Technology Stocks','Top Utility Stocks','Top Value Stocks','Top Yield Monsters',
'Top REITs']

def print_old_holding_symbols(resultsdict):
    holding_symbols = set(md.get_symbols('',ports=holding_ports))
    stock_card = md.get_symbols_for_portfolios(['Stock Card'])
    api_symbols = [*resultsdict.values()]
    api_symbols = set([item for sublist in api_symbols for item in sublist])
    old_symbols = holding_symbols - api_symbols
    print('Holding symbols not in api')
    return sorted(old_symbols)

def print_old_sa_symbols(resultsdict):
    sa_directory = md.get_symbols_dir_or_port('Seeking_Alpha',None)
    stock_card = md.get_symbols_for_portfolios(['Stock Card'])
    sa_symbols = set(sa_directory) - set(stock_card)
    api_symbols = [*resultsdict.values()]
    api_symbols = set([item for sublist in api_symbols for item in sublist])
    old_symbols = sa_symbols - api_symbols
    print('Seeking Aplha symbols downgraded in api')
    return sorted(old_symbols)

sa_top_ports = ['Top Communication Stocks','Top Consumer Discretionary Stocks','Top Consumer Staples Stocks','Top Energy by SA Authors ','Top Energy Stocks','Top Financial Stocks','Top Growth Stocks','Top Healthcare Stocks','Top Industrial Stocks','Top Materials Stocks','Top Quant Dividend Stocks','Top Rated Dividend Stocks','Top Rated Stocks','Top Real Estate Stocks''Top Small Cap Stocks','Top Stocks by Quant','Top Stocks Under $10','Top Technology Stocks','Top Utility Stocks','Top Value Stocks','Top Yield Monsters',
'Top REITs']


def holding_not_in_quants():
    holding = md.get_symbols('Holding')
    holding = md.get_symbols('', holding_ports)
    quant = md.get_symbols('Seeking_Alpha')
    xquant = sorted(set(holding).intersection(set(quant)))
    print('Holding ex-long term in quants: ', sorted(xquant))
    xquant = sorted(set(holding).difference(set(quant)))
    print('Holding ex-long term not in quants: ', sorted(xquant))


def stock_card_in_quants():
    sa_top_symbols = md.get_symbols('', sa_top_ports)
    quants_symbols = md.get_symbols('',['Stock Card','Top Stocks by Quant'])
    in_quants = sorted(set(sa_top_symbols).intersection(set(quants_symbols)))
    print('Stock Card in quants: ', sorted(in_quants))

def port_in_top_quants():
    sa_top_symbols = md.get_symbols('', sa_top_ports)
    quants_symbols = md.get_symbols('',['Top Rated Stocks'])
    in_quants = sorted(set(sa_top_symbols).intersection(set(quants_symbols)))
    print('Stock Card in quants: ', sorted(in_quants))



if __name__ == '__main__':
    holding_not_in_quants()
    stock_card_in_quants()