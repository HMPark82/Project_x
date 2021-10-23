def bias_function(data_dict, bias_dict):
    w1 = 1
    w2 = 1
    iprice_spread = 15
    
    iprice = data_dict['lists_indexPrice'][len(data_dict['lists_indexPrice']) - 1]
    
    high = data_dict['lists_high'][len(data_dict['lists_high']) - 1]
    low = data_dict['lists_low'][len(data_dict['lists_low']) - 1]
    
    mybid = data_dict['lists_bids'][len(data_dict['lists_bids']) - 1]
    myask = data_dict['lists_asks'][len(data_dict['lists_asks']) - 1]
    
    hl_position_factor = max(-1, min(1, ((high + low) / 2 - mybid) / (high - low)))
    iprice_factor = max(-1, min(1, (iprice - mybid)/iprice_spread))
    
    final_factor = w1 * hl_position_factor + w2 * iprice_factor
    
    if final_factor < 0:
        bias = 'Sell'
    else:
        bias = 'Buy'

    if len(bias_dict['lists_w1']) > 239:
        del bias_dict['lists_w2'][0]
        del bias_dict['lists_iprice_spread'][0]
        del bias_dict['lists_indexPrice'][0]
        del bias_dict['lists_high'][0]
        del bias_dict['lists_low'][0]
        del bias_dict['lists_mybid'][0]
        del bias_dict['lists_myask'][0]
        del bias_dict['lists_hl_position_factor'][0]
        del bias_dict['lists_iprice_factor'][0]
        del bias_dict['lists_final_factor'][0]
        del bias_dict['lists_bias'][0]
        
    bias_dict['lists_w1'].append(w1)
    bias_dict['lists_w2'].append(w2)
    bias_dict['lists_iprice_spread'].append(iprice_spread)
    bias_dict['lists_indexPrice'].append(iprice)
    bias_dict['lists_high'].append(high)
    bias_dict['lists_low'].append(low)
    bias_dict['lists_mybid'].append(mybid)
    bias_dict['lists_myask'].append(myask)
    bias_dict['lists_hl_position_factor'].append(hl_position_factor)
    bias_dict['lists_iprice_factor'].append(iprice_factor)
    bias_dict['lists_final_factor'].append(final_factor)
    bias_dict['lists_bias'].append(bias)
        
    return bias, bias_dict