#from phemex import PhemexConnection, AuthCredentials
from phemex.order import Contract, Side
import math

def order_function(authenticated_conn, my_qty: int, bias, data_dict):
    # set up order helper classes
    order_placer = authenticated_conn.get_order_placer()
    order_factory = order_placer.get_order_factory()
    
    mybid = data_dict['lists_bids'][len(data_dict['lists_bids']) - 1]
    myask = data_dict['lists_asks'][len(data_dict['lists_asks']) - 1]
    avgEntryPriceEp = data_dict['lists_avgEntryPriceEp'][len(data_dict['lists_avgEntryPriceEp']) - 1]
    position_side = data_dict['lists_position_side'][len(data_dict['lists_position_side']) - 1]
    position_size = data_dict['lists_position_size'][len(data_dict['lists_position_size']) - 1]
    #order_orderID = data_dict['lists_orders_orderID'][len(data_dict['lists_orders_orderID']) - 1]
    #order_cumQty = data_dict['lists_cumQty'][len(data_dict['lists_cumQty']) - 1]
    #order_leavesQty = data_dict['lists_leavesQty'][len(data_dict['lists_leavesQty']) - 1]
    order_orderQty = data_dict['lists_orders_orderQty'][len(data_dict['lists_orders_orderQty']) - 1]
    order_side = data_dict['lists_orders_side'][len(data_dict['lists_orders_side']) - 1]
    #order_priceEp = data_dict['lists_orders_priceEp'][len(data_dict['lists_orders_priceEp']) - 1]
    
    if order_orderQty == 0 and position_size == 0 and bias == 'Buy':
        limit = order_factory.create_limit_order(Side.BUY, my_qty, mybid, Contract('BTCUSD'), post_only = True)
        limit_hnd = order_placer.submit(limit)
    elif order_orderQty == 0 and position_size == 0 and bias == 'Sell':
        limit = order_factory.create_limit_order(Side.SELL, my_qty, myask, Contract('BTCUSD'), post_only = True)
        limit_hnd = order_placer.submit(limit)
    elif order_orderQty == 0 and position_size > 0 and position_side == 'Buy':
        myprice = max(myask + 0.5, math.ceil(avgEntryPriceEp))
        limit = order_factory.create_limit_order(Side.SELL, position_size, myprice, Contract('BTCUSD'), post_only = True)
        limit_hnd = order_placer.submit(limit)
    elif order_orderQty == 0 and position_size > 0 and position_side == 'Sell':
        myprice = min(mybid - 0.5, math.floor(avgEntryPriceEp))
        limit = order_factory.create_limit_order(Side.BUY, position_size, myprice, Contract('BTCUSD'), post_only = True)
        limit_hnd = order_placer.submit(limit)
        
    elif order_orderQty != 0 and position_size == 0 and bias == 'Buy':
        authenticated_conn.cancel_all_orders(symbol = "BTCUSD", untriggered = False)
        limit = order_factory.create_limit_order(Side.BUY, my_qty, mybid, Contract('BTCUSD'), post_only = True)
        limit_hnd = order_placer.submit(limit)
    elif order_orderQty != 0 and position_size == 0 and bias == 'Sell':
        authenticated_conn.cancel_all_orders(symbol = "BTCUSD", untriggered = False)
        limit = order_factory.create_limit_order(Side.SELL, my_qty, myask, Contract('BTCUSD'), post_only = True)
        limit_hnd = order_placer.submit(limit)

    elif order_orderQty != 0 and position_size > 0 and position_side == 'Buy' and order_side == 'Buy':
        myorderID = 'Nothing'
    elif order_orderQty != 0 and position_size > 0 and position_side == 'Buy' and order_side == 'Sell':
        myorderID = 'Nothing'    
    elif order_orderQty != 0 and position_size > 0 and position_side == 'Sell' and order_side == 'Buy':
        myorderID = 'Nothing'
    elif order_orderQty != 0 and position_size > 0 and position_side == 'Sell' and order_side == 'Sell':
        myorderID = 'Nothing'
        
    else:
        myorderID = 'Nothing'