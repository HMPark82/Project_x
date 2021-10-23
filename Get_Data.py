def phemex_data(public_conn, authenticated_conn, data_dict):
    ticker = public_conn.get_ticker()
    myorderbook = public_conn.get_orderbook()
    
    mypositions = authenticated_conn.get_account_positions(currency = "BTC")
    myorders = authenticated_conn.get_account_orders(symbol = "BTCUSD")
    
    ticker_close = ticker["result"]["close"]/10000
    ticker_fundingRate = ticker["result"]["fundingRate"]/10000
    ticker_high = ticker["result"]["high"]/10000
    ticker_indexPrice = ticker["result"]["indexPrice"]/10000
    ticker_low = ticker["result"]["low"]/10000
    ticker_markPrice = ticker["result"]["markPrice"]/10000
    ticker_open = ticker["result"]["open"]/10000
    ticker_openInterest = ticker["result"]["openInterest"]
    ticker_predFundingRate = ticker["result"]["predFundingRate"]/10000
    ticker_symbol = ticker["result"]["symbol"]
    ticker_timestamp = ticker["result"]["timestamp"]
    ticker_turnover = ticker["result"]["turnover"]
    ticker_volume = ticker["result"]["volume"]
    
    mybid = myorderbook["result"]["book"]["bids"][0][0]/10000
    myask = myorderbook["result"]["book"]["asks"][0][0]/10000

    avgEntryPriceEp = mypositions["data"]["positions"][0]["avgEntryPriceEp"]/10000
    position_side = mypositions["data"]["positions"][0]["side"]
    position_size = mypositions["data"]["positions"][0]["size"]
    
    if myorders["data"] == None:
        orders_clOrdID = 'None'
        orders_orderID = 'None'
        orders_cumQty = 0
        orders_leavesQty = 0
        orders_orderQTY = 0
        orders_side = 'None'
        orders_priceEp = 0
    else:
        orders_clOrdID = myorders["data"]["rows"][0]["clOrdID"]
        orders_orderID = myorders["data"]["rows"][0]["orderID"]
        orders_cumQty = myorders["data"]["rows"][0]["cumQty"]
        orders_leavesQty = myorders["data"]["rows"][0]["leavesQty"]
        orders_orderQTY = myorders["data"]["rows"][0]["orderQty"]
        orders_side = myorders["data"]["rows"][0]["side"]
        orders_priceEp = myorders["data"]["rows"][0]["priceEp"]/10000

    if len(data_dict['lists_close']) > 239:
        del data_dict['lists_close'][0]
        del data_dict['lists_fundingRate'][0]
        del data_dict['lists_high'][0]
        del data_dict['lists_indexPrice'][0]
        del data_dict['lists_low'][0]
        del data_dict['lists_markPrice'][0]
        del data_dict['lists_open'][0]
        del data_dict['lists_openInterest'][0]
        del data_dict['lists_predFundingRate'][0]
        del data_dict['lists_symbol'][0]
        del data_dict['lists_timestamp'][0]
        del data_dict['lists_turnover'][0]
        del data_dict['lists_volume'][0]
        del data_dict['lists_bids'][0]
        del data_dict['lists_asks'][0]
        del data_dict['lists_avgEntryPriceEp'][0]
        del data_dict['lists_position_side'][0]
        del data_dict['lists_position_size'][0]
        del data_dict['lists_orders_clOrdID'][0]
        del data_dict['lists_orders_orderID'][0]
        del data_dict['lists_orders_cumQty'][0]
        del data_dict['lists_orders_leavesQty'][0]
        del data_dict['lists_orders_orderQty'][0]
        del data_dict['lists_orders_side'][0]
        del data_dict['lists_orders_priceEp'][0]
        
    data_dict['lists_close'].append(ticker_close)
    data_dict['lists_fundingRate'].append(ticker_fundingRate)
    data_dict['lists_high'].append(ticker_high)
    data_dict['lists_indexPrice'].append(ticker_indexPrice)
    data_dict['lists_low'].append(ticker_low)
    data_dict['lists_markPrice'].append(ticker_markPrice)
    data_dict['lists_open'].append(ticker_open)
    data_dict['lists_openInterest'].append(ticker_openInterest)
    data_dict['lists_predFundingRate'].append(ticker_predFundingRate)
    data_dict['lists_symbol'].append(ticker_symbol)
    data_dict['lists_timestamp'].append(ticker_timestamp)
    data_dict['lists_turnover'].append(ticker_turnover)
    data_dict['lists_volume'].append(ticker_volume)
    data_dict['lists_bids'].append(mybid)
    data_dict['lists_asks'].append(myask)
    data_dict['lists_avgEntryPriceEp'].append(avgEntryPriceEp)
    data_dict['lists_position_side'].append(position_side)
    data_dict['lists_position_size'].append(position_size)
    data_dict['lists_orders_clOrdID'].append(orders_clOrdID)
    data_dict['lists_orders_orderID'].append(orders_orderID)
    data_dict['lists_orders_cumQty'].append(orders_cumQty)
    data_dict['lists_orders_leavesQty'].append(orders_leavesQty)
    data_dict['lists_orders_orderQty'].append(orders_orderQTY)
    data_dict['lists_orders_side'].append(orders_side) 
    data_dict['lists_orders_priceEp'].append(orders_priceEp)
    
    return data_dict