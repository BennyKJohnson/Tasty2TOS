import json

def count_leading_zeros(s):
    count = 0
    for c in s:
        if c == '0':
            count += 1
        else:
            break
    return count

def load_future_option_symbols():
    with open('resources/future-option-product.json') as file:
        data = file.read()

        items = json.loads(data)['data']['items']
        symbols  = []
        for item in items:
            symbol = item['root-symbol']
            symbols.append(symbol)

        return symbols
    
def find_instrument_for_symbol(symbol):
    with open('resources/future-option-product.json') as file:
        data = file.read()
        symbol_without_product_code = symbol[0:-2]

        items = json.loads(data)['data']['items']
        current_symbol = ''
        current_item = None
        for item in items:
            if symbol_without_product_code.endswith(item['root-symbol']) and len(item['root-symbol']) > len(current_symbol):
                current_item = item
                current_symbol = item['root-symbol']
                

        return current_item

def parse_option_symbol(symbol):
    underlying_symbol = symbol[0:6].strip()
    expiration_date = symbol[6:12]
    option_type = symbol[12]
    strike_price_padded = symbol[13:21]

    leading_padded_zeros = count_leading_zeros(strike_price_padded)
    strike_price_raw = strike_price_padded[leading_padded_zeros:]
    strike_price = int(strike_price_raw) / pow(10, 3)
    
    return {
        'underlying_symbol': underlying_symbol,
        'expiration_date': expiration_date,
        'expiration_date_year': expiration_date[0:2],
        'expiration_date_month': expiration_date[2:4],
        'expiration_date_day': expiration_date[4:6],
        'option_type': option_type,
        'strike_price_padded': strike_price_padded,
        'strike_price': strike_price,
        'is_call': option_type == 'C',
        'is_put': option_type == 'P'
    }

def parse_futures_option_symbol(symbol):
    symbol_components = symbol.split()
    full_symbol = symbol_components[0]

    symbol_without_identifier = full_symbol.replace('./', '')

    instrument = find_instrument_for_symbol(symbol_without_identifier)
    future_symbol = instrument['future-product']['code']

    unparsed_symbol = symbol_without_identifier[len(future_symbol):]
    month_code = unparsed_symbol[0]
    month_identifier = unparsed_symbol[0:2]
    unparsed_symbol = unparsed_symbol[2:]
    second_component = symbol_components[1]

    return {
        'futures_root_symbol': future_symbol,
        'root_symbol': instrument['root-symbol'],
        'underlying_symbol': future_symbol + month_identifier,
        'product_code': month_identifier,
        'option_contract_symbol': unparsed_symbol,
        'expiration_date': second_component[0:6],
        'expiration_date_year': second_component[0:2],
        'expiration_date_month': second_component[2:4],
        'expiration_date_day': second_component[4:6],
        'is_call': second_component[6] == 'C',
        'is_put': second_component[6] == 'P',
        'strike_price': int(second_component[7:]),
        'streamer_exchange_code': instrument['future-product']['streamer-exchange-code'],
        'notional_multiplier': float(instrument['future-product']['notional-multiplier']),
        'month_code': month_code,
        'expiration_type': instrument['expiration-type'],
        'expiration_number': int(symbol_without_identifier[-1]),
        'expiration_code': symbol_without_identifier[-2]
    }