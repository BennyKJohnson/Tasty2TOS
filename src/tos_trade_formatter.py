import calendar

def format_price(price):
    formatted_price = '{:.2f}'.format(price)
    if formatted_price.startswith('0'):
        return formatted_price[1:]
    return formatted_price

def convert_option_to_tos(option, option_series, quantity, price):
    is_buy = quantity > 0
    quantity_str = f'+{quantity}' if is_buy else f'{quantity}'
    action = 'BUY' if quantity > 0 else 'SELL'
    underlying_symbol = option['underlying_symbol']
    expiration_date_month = calendar.month_abbr[int(option['expiration_date_month'])].upper()

    expiration_date_day = option['expiration_date_day']
    expiration_date_year = option['expiration_date_year']
    strike_price = option['strike_price']
    option_type = 'CALL' if option['is_call'] else 'PUT'
    weekly_str = ' (Weeklys)' if option_series['is_weekly'] else ''

    return f'{action} {quantity_str} {underlying_symbol} 100{weekly_str} {expiration_date_day} {expiration_date_month} {expiration_date_year} {strike_price:.0f} {option_type} @{format_price(price)} LMT FIXED'

def get_product_code(option_details):
    if option_details['expiration_type'] == 'End-Of-Month':
        return '/{}{}{}{}'.format(option_details['root_symbol'], option_details['expiration_number'], option_details['expiration_code'], option_details['expiration_date_year'])
    return '/{}{}{}'.format(option_details['root_symbol'], option_details['expiration_code'], option_details['expiration_date_year'])

def get_future_product_code(option_details):
    return '/{}{}{}'.format(option_details['futures_root_symbol'], option_details['month_code'], option_details['expiration_date_year'])

def format_quantity(quantity):
    is_buy = quantity > 0
    quantity_str = f'+{quantity}' if is_buy else f'{quantity}'
    action = 'BUY' if quantity > 0 else 'SELL'

    return f'{action} {quantity_str}'

def convert_futures_option_to_tos(option_details, option_series, quantity, price):
    quantity_str = format_quantity(quantity)

    expiration_date_month = calendar.month_abbr[int(option_details['expiration_date_month'])].upper()
    expiration_date_year = option_details['expiration_date_year']
    strike_price = option_details['strike_price']
    option_type = 'CALL' if option_details['is_call'] else 'PUT'
    settlement_type = option_series['settlement_type']
    streamer_exchange_code = option_details['streamer_exchange_code']
    multiplier = '1/{:.0f}'.format(option_details['notional_multiplier'])
    am_settled = ' (AM Settled)' if settlement_type == 'AM' else ''

    another_symbol = '{}:{}'.format(get_product_code(option_details), option_details['streamer_exchange_code'])
    contract_symbol = get_future_product_code(option_details)
    show_weekly_period = option_details['expiration_type'] == 'End-Of-Month' or option_details['expiration_type'] == 'Weekly'
    expiration_period = '(Wk{}) {}'.format(option_details['expiration_number'], another_symbol) if show_weekly_period else f'{contract_symbol}:{streamer_exchange_code}'
    return f'{quantity_str} {contract_symbol}:{streamer_exchange_code} {multiplier} {expiration_date_month} {expiration_date_year}{am_settled} {expiration_period} {strike_price:.0f} {option_type} @{format_price(price)} LMT FIXED'