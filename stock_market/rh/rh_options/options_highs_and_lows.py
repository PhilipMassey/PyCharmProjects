import pandas as pd
import robin_stocks as r


def diffMaxHighLow(df, dfstrike_prices):
    print('Strike\tVolume\tOpen\tHigh\tLow\tClose\tOCDiff\tOCP\tHLDiff\tHLPercent')
    for idx, row in dfstrike_prices.iterrows():
        strike_price: object = row.strike_price
        volume = row.volume
        df_stpr = df[(df.strike_price == strike_price)]
        if df_stpr.empty: continue
        high_price = max(df_stpr.high_price, default=0)
        low_price = min(df_stpr.high_price, default=0)
        hldiff = round(high_price - low_price, 2)
        hlpercent = 0 if low_price == 0 else round(hldiff / low_price, 2)
        open_price = df_stpr.iloc[0].open_price
        close_price = df_stpr.iloc[-1].close_price
        ocdiff = round(close_price - open_price, 2)
        ocpercent = 0 if high_price == 0 else round(ocdiff / open_price, 2)
        print(
            '${sp:.2f}\t{vol:,.0f}\t{op:.2f}\t{hp:.2f}\t{lp:.2f}\t{cp:.2f}\t{ocd:.2f}\t{ocp:,.0%}\t{hld}\t{hlp:,.0%}'.format(sp=strike_price, vol=volume,
                                                                    op=open_price,hp=high_price, lp=low_price, cp=close_price,ocd=ocdiff,ocp=ocpercent,hld=hldiff, hlp=hlpercent))


def getStrikesOHLCChangesExpiration(symbol, expiration_dates, optionType, span, volume_limit=0):
    df_expirationDates = pd.DataFrame()
    for expirationDate in expiration_dates[0:5]:
        print('{}\t'.format(expirationDate), end='')
        #options = r.find_options_for_list_of_stocks_by_expiration_date([symbol], expirationDate, optionType)
        options = r.find_options_by_expiration([symbol], expirationDate, optionType)
        dfoptions = pd.DataFrame((filter(lambda x: x['volume'] > volume_limit, options)))
        if dfoptions.empty:
            print('Volume is 0 for options')
        else:
            dfoptions[['strike_price', 'high_price', 'low_price']] = dfoptions[
                ['strike_price', 'high_price', 'low_price']].apply(pd.to_numeric)
            dfstrike_prices = dfoptions.sort_values(by='volume', ascending=False)[0:5][['strike_price', 'volume']]
            dfstrike_prices.sort_values(by='strike_price', inplace=True)
            # dfstrike_prices
            df_all = pd.DataFrame()
            for idx, row in dfstrike_prices.iterrows():
                strike_price = row.strike_price
                # print('Strike price: {}'.format(strike_price))
#                df = pd.DataFrame(
#                    r.get_option_historicals(symbol, expirationDate, strike_price, optionType, span)['data_points'])
                df = pd.DataFrame(
                    r.get_option_historicals(symbol, expirationDate, strike_price, optionType, span))
                df['strike_price'] = strike_price
                df_all = pd.concat([df_all, df[
                    ['begins_at', 'strike_price', 'open_price', 'high_price', 'low_price', 'close_price', 'volume']]])

            df_all[['strike_price','open_price', 'high_price', 'low_price','close_price']] = df_all[
                ['strike_price', 'open_price','high_price', 'low_price','close_price']].apply(pd.to_numeric)
            df_all = df_all[df_all.high_price != 0.01]
            df_all['expiration_date'] = expirationDate
            print()
            diffMaxHighLow(df_all, dfstrike_prices)
            df_expirationDates = pd.concat([df_expirationDates, df_all])
    return df_expirationDates
