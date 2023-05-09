import json

def get_wmt_equity_option_chain_response_body():
    return {'context': '/option-chains/WMT/nested',
 'data': {'items': [{'deliverables': [{'amount': '100.0',
                                       'deliverable-type': 'Shares',
                                       'description': '100 shares of WMT',
                                       'id': 1566,
                                       'instrument-type': 'Equity',
                                       'percent': '100',
                                       'root-symbol': 'WMT',
                                       'symbol': 'WMT'}],
                     'expirations': [{'days-to-expiration': 53,
                                      'expiration-date': '2023-06-16',
                                      'expiration-type': 'Regular',
                                      'settlement-type': 'PM',
                                      'strikes': [{'call': 'WMT   '
                                                           '230616C00060000',
                                                   'put': 'WMT   '
                                                          '230616P00060000',
                                                   'strike-price': '60.0'},
                                                  {'call': 'WMT   '
                                                           '230616C00065000',
                                                   'put': 'WMT   '
                                                          '230616P00065000',
                                                   'strike-price': '65.0'},
                                                  {'call': 'WMT   '
                                                           '230616C00070000',
                                                   'put': 'WMT   '
                                                          '230616P00070000',
                                                   'strike-price': '70.0'},
                                                  {'call': 'WMT   '
                                                           '230616C00075000',
                                                   'put': 'WMT   '
                                                          '230616P00075000',
                                                   'strike-price': '75.0'},
                                                  {'call': 'WMT   '
                                                           '230616C00080000',
                                                   'put': 'WMT   '
                                                          '230616P00080000',
                                                   'strike-price': '80.0'},
                                                  {'call': 'WMT   '
                                                           '230616C00085000',
                                                   'put': 'WMT   '
                                                          '230616P00085000',
                                                   'strike-price': '85.0'},
                                                  {'call': 'WMT   '
                                                           '230616C00090000',
                                                   'put': 'WMT   '
                                                          '230616P00090000',
                                                   'strike-price': '90.0'},
                                                  {'call': 'WMT   '
                                                           '230616C00095000',
                                                   'put': 'WMT   '
                                                          '230616P00095000',
                                                   'strike-price': '95.0'},
                                                  {'call': 'WMT   '
                                                           '230616C00100000',
                                                   'put': 'WMT   '
                                                          '230616P00100000',
                                                   'strike-price': '100.0'},
                                                  {'call': 'WMT   '
                                                           '230616C00105000',
                                                   'put': 'WMT   '
                                                          '230616P00105000',
                                                   'strike-price': '105.0'},
                                                  {'call': 'WMT   '
                                                           '230616C00110000',
                                                   'put': 'WMT   '
                                                          '230616P00110000',
                                                   'strike-price': '110.0'},
                                                  {'call': 'WMT   '
                                                           '230616C00115000',
                                                   'put': 'WMT   '
                                                          '230616P00115000',
                                                   'strike-price': '115.0'},
                                                  {'call': 'WMT   '
                                                           '230616C00120000',
                                                   'put': 'WMT   '
                                                          '230616P00120000',
                                                   'strike-price': '120.0'},
                                                  {'call': 'WMT   '
                                                           '230616C00125000',
                                                   'put': 'WMT   '
                                                          '230616P00125000',
                                                   'strike-price': '125.0'},
                                                  {'call': 'WMT   '
                                                           '230616C00130000',
                                                   'put': 'WMT   '
                                                          '230616P00130000',
                                                   'strike-price': '130.0'},
                                                  {'call': 'WMT   '
                                                           '230616C00135000',
                                                   'put': 'WMT   '
                                                          '230616P00135000',
                                                   'strike-price': '135.0'},
                                                  {'call': 'WMT   '
                                                           '230616C00140000',
                                                   'put': 'WMT   '
                                                          '230616P00140000',
                                                   'strike-price': '140.0'},
                                                  {'call': 'WMT   '
                                                           '230616C00145000',
                                                   'put': 'WMT   '
                                                          '230616P00145000',
                                                   'strike-price': '145.0'},
                                                  {'call': 'WMT   '
                                                           '230616C00150000',
                                                   'put': 'WMT   '
                                                          '230616P00150000',
                                                   'strike-price': '150.0'},
                                                  {'call': 'WMT   '
                                                           '230616C00155000',
                                                   'put': 'WMT   '
                                                          '230616P00155000',
                                                   'strike-price': '155.0'},
                                                  {'call': 'WMT   '
                                                           '230616C00160000',
                                                   'put': 'WMT   '
                                                          '230616P00160000',
                                                   'strike-price': '160.0'},
                                                  {'call': 'WMT   '
                                                           '230616C00165000',
                                                   'put': 'WMT   '
                                                          '230616P00165000',
                                                   'strike-price': '165.0'},
                                                  {'call': 'WMT   '
                                                           '230616C00170000',
                                                   'put': 'WMT   '
                                                          '230616P00170000',
                                                   'strike-price': '170.0'},
                                                  {'call': 'WMT   '
                                                           '230616C00175000',
                                                   'put': 'WMT   '
                                                          '230616P00175000',
                                                   'strike-price': '175.0'},
                                                  {'call': 'WMT   '
                                                           '230616C00180000',
                                                   'put': 'WMT   '
                                                          '230616P00180000',
                                                   'strike-price': '180.0'},
                                                  {'call': 'WMT   '
                                                           '230616C00185000',
                                                   'put': 'WMT   '
                                                          '230616P00185000',
                                                   'strike-price': '185.0'},
                                                  {'call': 'WMT   '
                                                           '230616C00190000',
                                                   'put': 'WMT   '
                                                          '230616P00190000',
                                                   'strike-price': '190.0'},
                                                  {'call': 'WMT   '
                                                           '230616C00195000',
                                                   'put': 'WMT   '
                                                          '230616P00195000',
                                                   'strike-price': '195.0'},
                                                  {'call': 'WMT   '
                                                           '230616C00200000',
                                                   'put': 'WMT   '
                                                          '230616P00200000',
                                                   'strike-price': '200.0'},
                                                  {'call': 'WMT   '
                                                           '230616C00210000',
                                                   'put': 'WMT   '
                                                          '230616P00210000',
                                                   'strike-price': '210.0'},
                                                  {'call': 'WMT   '
                                                           '230616C00220000',
                                                   'put': 'WMT   '
                                                          '230616P00220000',
                                                   'strike-price': '220.0'},
                                                  {'call': 'WMT   '
                                                           '230616C00230000',
                                                   'put': 'WMT   '
                                                          '230616P00230000',
                                                   'strike-price': '230.0'}]},
                                     {'days-to-expiration': 144,
                                      'expiration-date': '2023-09-15',
                                      'expiration-type': 'Regular',
                                      'settlement-type': 'PM',
                                      'strikes': [{'call': 'WMT   '
                                                           '230915C00070000',
                                                   'put': 'WMT   '
                                                          '230915P00070000',
                                                   'strike-price': '70.0'},
                                                  {'call': 'WMT   '
                                                           '230915C00075000',
                                                   'put': 'WMT   '
                                                          '230915P00075000',
                                                   'strike-price': '75.0'},
                                                  {'call': 'WMT   '
                                                           '230915C00080000',
                                                   'put': 'WMT   '
                                                          '230915P00080000',
                                                   'strike-price': '80.0'},
                                                  {'call': 'WMT   '
                                                           '230915C00085000',
                                                   'put': 'WMT   '
                                                          '230915P00085000',
                                                   'strike-price': '85.0'},
                                                  {'call': 'WMT   '
                                                           '230915C00090000',
                                                   'put': 'WMT   '
                                                          '230915P00090000',
                                                   'strike-price': '90.0'},
                                                  {'call': 'WMT   '
                                                           '230915C00095000',
                                                   'put': 'WMT   '
                                                          '230915P00095000',
                                                   'strike-price': '95.0'},
                                                  {'call': 'WMT   '
                                                           '230915C00100000',
                                                   'put': 'WMT   '
                                                          '230915P00100000',
                                                   'strike-price': '100.0'},
                                                  {'call': 'WMT   '
                                                           '230915C00105000',
                                                   'put': 'WMT   '
                                                          '230915P00105000',
                                                   'strike-price': '105.0'},
                                                  {'call': 'WMT   '
                                                           '230915C00110000',
                                                   'put': 'WMT   '
                                                          '230915P00110000',
                                                   'strike-price': '110.0'},
                                                  {'call': 'WMT   '
                                                           '230915C00115000',
                                                   'put': 'WMT   '
                                                          '230915P00115000',
                                                   'strike-price': '115.0'},
                                                  {'call': 'WMT   '
                                                           '230915C00120000',
                                                   'put': 'WMT   '
                                                          '230915P00120000',
                                                   'strike-price': '120.0'},
                                                  {'call': 'WMT   '
                                                           '230915C00125000',
                                                   'put': 'WMT   '
                                                          '230915P00125000',
                                                   'strike-price': '125.0'},
                                                  {'call': 'WMT   '
                                                           '230915C00130000',
                                                   'put': 'WMT   '
                                                          '230915P00130000',
                                                   'strike-price': '130.0'},
                                                  {'call': 'WMT   '
                                                           '230915C00135000',
                                                   'put': 'WMT   '
                                                          '230915P00135000',
                                                   'strike-price': '135.0'},
                                                  {'call': 'WMT   '
                                                           '230915C00140000',
                                                   'put': 'WMT   '
                                                          '230915P00140000',
                                                   'strike-price': '140.0'},
                                                  {'call': 'WMT   '
                                                           '230915C00145000',
                                                   'put': 'WMT   '
                                                          '230915P00145000',
                                                   'strike-price': '145.0'},
                                                  {'call': 'WMT   '
                                                           '230915C00150000',
                                                   'put': 'WMT   '
                                                          '230915P00150000',
                                                   'strike-price': '150.0'},
                                                  {'call': 'WMT   '
                                                           '230915C00155000',
                                                   'put': 'WMT   '
                                                          '230915P00155000',
                                                   'strike-price': '155.0'},
                                                  {'call': 'WMT   '
                                                           '230915C00160000',
                                                   'put': 'WMT   '
                                                          '230915P00160000',
                                                   'strike-price': '160.0'},
                                                  {'call': 'WMT   '
                                                           '230915C00165000',
                                                   'put': 'WMT   '
                                                          '230915P00165000',
                                                   'strike-price': '165.0'},
                                                  {'call': 'WMT   '
                                                           '230915C00170000',
                                                   'put': 'WMT   '
                                                          '230915P00170000',
                                                   'strike-price': '170.0'},
                                                  {'call': 'WMT   '
                                                           '230915C00175000',
                                                   'put': 'WMT   '
                                                          '230915P00175000',
                                                   'strike-price': '175.0'},
                                                  {'call': 'WMT   '
                                                           '230915C00180000',
                                                   'put': 'WMT   '
                                                          '230915P00180000',
                                                   'strike-price': '180.0'},
                                                  {'call': 'WMT   '
                                                           '230915C00185000',
                                                   'put': 'WMT   '
                                                          '230915P00185000',
                                                   'strike-price': '185.0'},
                                                  {'call': 'WMT   '
                                                           '230915C00190000',
                                                   'put': 'WMT   '
                                                          '230915P00190000',
                                                   'strike-price': '190.0'},
                                                  {'call': 'WMT   '
                                                           '230915C00195000',
                                                   'put': 'WMT   '
                                                          '230915P00195000',
                                                   'strike-price': '195.0'},
                                                  {'call': 'WMT   '
                                                           '230915C00200000',
                                                   'put': 'WMT   '
                                                          '230915P00200000',
                                                   'strike-price': '200.0'},
                                                  {'call': 'WMT   '
                                                           '230915C00210000',
                                                   'put': 'WMT   '
                                                          '230915P00210000',
                                                   'strike-price': '210.0'},
                                                  {'call': 'WMT   '
                                                           '230915C00220000',
                                                   'put': 'WMT   '
                                                          '230915P00220000',
                                                   'strike-price': '220.0'}]},
                                     {'days-to-expiration': 270,
                                      'expiration-date': '2024-01-19',
                                      'expiration-type': 'Regular',
                                      'settlement-type': 'PM',
                                      'strikes': [{'call': 'WMT   '
                                                           '240119C00060000',
                                                   'put': 'WMT   '
                                                          '240119P00060000',
                                                   'strike-price': '60.0'},
                                                  {'call': 'WMT   '
                                                           '240119C00065000',
                                                   'put': 'WMT   '
                                                          '240119P00065000',
                                                   'strike-price': '65.0'},
                                                  {'call': 'WMT   '
                                                           '240119C00070000',
                                                   'put': 'WMT   '
                                                          '240119P00070000',
                                                   'strike-price': '70.0'},
                                                  {'call': 'WMT   '
                                                           '240119C00075000',
                                                   'put': 'WMT   '
                                                          '240119P00075000',
                                                   'strike-price': '75.0'},
                                                  {'call': 'WMT   '
                                                           '240119C00080000',
                                                   'put': 'WMT   '
                                                          '240119P00080000',
                                                   'strike-price': '80.0'},
                                                  {'call': 'WMT   '
                                                           '240119C00085000',
                                                   'put': 'WMT   '
                                                          '240119P00085000',
                                                   'strike-price': '85.0'},
                                                  {'call': 'WMT   '
                                                           '240119C00090000',
                                                   'put': 'WMT   '
                                                          '240119P00090000',
                                                   'strike-price': '90.0'},
                                                  {'call': 'WMT   '
                                                           '240119C00095000',
                                                   'put': 'WMT   '
                                                          '240119P00095000',
                                                   'strike-price': '95.0'},
                                                  {'call': 'WMT   '
                                                           '240119C00100000',
                                                   'put': 'WMT   '
                                                          '240119P00100000',
                                                   'strike-price': '100.0'},
                                                  {'call': 'WMT   '
                                                           '240119C00105000',
                                                   'put': 'WMT   '
                                                          '240119P00105000',
                                                   'strike-price': '105.0'},
                                                  {'call': 'WMT   '
                                                           '240119C00110000',
                                                   'put': 'WMT   '
                                                          '240119P00110000',
                                                   'strike-price': '110.0'},
                                                  {'call': 'WMT   '
                                                           '240119C00115000',
                                                   'put': 'WMT   '
                                                          '240119P00115000',
                                                   'strike-price': '115.0'},
                                                  {'call': 'WMT   '
                                                           '240119C00120000',
                                                   'put': 'WMT   '
                                                          '240119P00120000',
                                                   'strike-price': '120.0'},
                                                  {'call': 'WMT   '
                                                           '240119C00125000',
                                                   'put': 'WMT   '
                                                          '240119P00125000',
                                                   'strike-price': '125.0'},
                                                  {'call': 'WMT   '
                                                           '240119C00130000',
                                                   'put': 'WMT   '
                                                          '240119P00130000',
                                                   'strike-price': '130.0'},
                                                  {'call': 'WMT   '
                                                           '240119C00135000',
                                                   'put': 'WMT   '
                                                          '240119P00135000',
                                                   'strike-price': '135.0'},
                                                  {'call': 'WMT   '
                                                           '240119C00140000',
                                                   'put': 'WMT   '
                                                          '240119P00140000',
                                                   'strike-price': '140.0'},
                                                  {'call': 'WMT   '
                                                           '240119C00145000',
                                                   'put': 'WMT   '
                                                          '240119P00145000',
                                                   'strike-price': '145.0'},
                                                  {'call': 'WMT   '
                                                           '240119C00150000',
                                                   'put': 'WMT   '
                                                          '240119P00150000',
                                                   'strike-price': '150.0'},
                                                  {'call': 'WMT   '
                                                           '240119C00155000',
                                                   'put': 'WMT   '
                                                          '240119P00155000',
                                                   'strike-price': '155.0'},
                                                  {'call': 'WMT   '
                                                           '240119C00160000',
                                                   'put': 'WMT   '
                                                          '240119P00160000',
                                                   'strike-price': '160.0'},
                                                  {'call': 'WMT   '
                                                           '240119C00165000',
                                                   'put': 'WMT   '
                                                          '240119P00165000',
                                                   'strike-price': '165.0'},
                                                  {'call': 'WMT   '
                                                           '240119C00170000',
                                                   'put': 'WMT   '
                                                          '240119P00170000',
                                                   'strike-price': '170.0'},
                                                  {'call': 'WMT   '
                                                           '240119C00175000',
                                                   'put': 'WMT   '
                                                          '240119P00175000',
                                                   'strike-price': '175.0'},
                                                  {'call': 'WMT   '
                                                           '240119C00180000',
                                                   'put': 'WMT   '
                                                          '240119P00180000',
                                                   'strike-price': '180.0'},
                                                  {'call': 'WMT   '
                                                           '240119C00185000',
                                                   'put': 'WMT   '
                                                          '240119P00185000',
                                                   'strike-price': '185.0'},
                                                  {'call': 'WMT   '
                                                           '240119C00190000',
                                                   'put': 'WMT   '
                                                          '240119P00190000',
                                                   'strike-price': '190.0'},
                                                  {'call': 'WMT   '
                                                           '240119C00195000',
                                                   'put': 'WMT   '
                                                          '240119P00195000',
                                                   'strike-price': '195.0'},
                                                  {'call': 'WMT   '
                                                           '240119C00200000',
                                                   'put': 'WMT   '
                                                          '240119P00200000',
                                                   'strike-price': '200.0'},
                                                  {'call': 'WMT   '
                                                           '240119C00210000',
                                                   'put': 'WMT   '
                                                          '240119P00210000',
                                                   'strike-price': '210.0'},
                                                  {'call': 'WMT   '
                                                           '240119C00220000',
                                                   'put': 'WMT   '
                                                          '240119P00220000',
                                                   'strike-price': '220.0'},
                                                  {'call': 'WMT   '
                                                           '240119C00230000',
                                                   'put': 'WMT   '
                                                          '240119P00230000',
                                                   'strike-price': '230.0'}]},
                                     {'days-to-expiration': 424,
                                      'expiration-date': '2024-06-21',
                                      'expiration-type': 'Regular',
                                      'settlement-type': 'PM',
                                      'strikes': [{'call': 'WMT   '
                                                           '240621C00075000',
                                                   'put': 'WMT   '
                                                          '240621P00075000',
                                                   'strike-price': '75.0'},
                                                  {'call': 'WMT   '
                                                           '240621C00080000',
                                                   'put': 'WMT   '
                                                          '240621P00080000',
                                                   'strike-price': '80.0'},
                                                  {'call': 'WMT   '
                                                           '240621C00085000',
                                                   'put': 'WMT   '
                                                          '240621P00085000',
                                                   'strike-price': '85.0'},
                                                  {'call': 'WMT   '
                                                           '240621C00090000',
                                                   'put': 'WMT   '
                                                          '240621P00090000',
                                                   'strike-price': '90.0'},
                                                  {'call': 'WMT   '
                                                           '240621C00095000',
                                                   'put': 'WMT   '
                                                          '240621P00095000',
                                                   'strike-price': '95.0'},
                                                  {'call': 'WMT   '
                                                           '240621C00100000',
                                                   'put': 'WMT   '
                                                          '240621P00100000',
                                                   'strike-price': '100.0'},
                                                  {'call': 'WMT   '
                                                           '240621C00105000',
                                                   'put': 'WMT   '
                                                          '240621P00105000',
                                                   'strike-price': '105.0'},
                                                  {'call': 'WMT   '
                                                           '240621C00110000',
                                                   'put': 'WMT   '
                                                          '240621P00110000',
                                                   'strike-price': '110.0'},
                                                  {'call': 'WMT   '
                                                           '240621C00115000',
                                                   'put': 'WMT   '
                                                          '240621P00115000',
                                                   'strike-price': '115.0'},
                                                  {'call': 'WMT   '
                                                           '240621C00120000',
                                                   'put': 'WMT   '
                                                          '240621P00120000',
                                                   'strike-price': '120.0'},
                                                  {'call': 'WMT   '
                                                           '240621C00125000',
                                                   'put': 'WMT   '
                                                          '240621P00125000',
                                                   'strike-price': '125.0'},
                                                  {'call': 'WMT   '
                                                           '240621C00130000',
                                                   'put': 'WMT   '
                                                          '240621P00130000',
                                                   'strike-price': '130.0'},
                                                  {'call': 'WMT   '
                                                           '240621C00135000',
                                                   'put': 'WMT   '
                                                          '240621P00135000',
                                                   'strike-price': '135.0'},
                                                  {'call': 'WMT   '
                                                           '240621C00140000',
                                                   'put': 'WMT   '
                                                          '240621P00140000',
                                                   'strike-price': '140.0'},
                                                  {'call': 'WMT   '
                                                           '240621C00145000',
                                                   'put': 'WMT   '
                                                          '240621P00145000',
                                                   'strike-price': '145.0'},
                                                  {'call': 'WMT   '
                                                           '240621C00150000',
                                                   'put': 'WMT   '
                                                          '240621P00150000',
                                                   'strike-price': '150.0'},
                                                  {'call': 'WMT   '
                                                           '240621C00155000',
                                                   'put': 'WMT   '
                                                          '240621P00155000',
                                                   'strike-price': '155.0'},
                                                  {'call': 'WMT   '
                                                           '240621C00160000',
                                                   'put': 'WMT   '
                                                          '240621P00160000',
                                                   'strike-price': '160.0'},
                                                  {'call': 'WMT   '
                                                           '240621C00165000',
                                                   'put': 'WMT   '
                                                          '240621P00165000',
                                                   'strike-price': '165.0'},
                                                  {'call': 'WMT   '
                                                           '240621C00170000',
                                                   'put': 'WMT   '
                                                          '240621P00170000',
                                                   'strike-price': '170.0'},
                                                  {'call': 'WMT   '
                                                           '240621C00175000',
                                                   'put': 'WMT   '
                                                          '240621P00175000',
                                                   'strike-price': '175.0'},
                                                  {'call': 'WMT   '
                                                           '240621C00180000',
                                                   'put': 'WMT   '
                                                          '240621P00180000',
                                                   'strike-price': '180.0'},
                                                  {'call': 'WMT   '
                                                           '240621C00185000',
                                                   'put': 'WMT   '
                                                          '240621P00185000',
                                                   'strike-price': '185.0'},
                                                  {'call': 'WMT   '
                                                           '240621C00190000',
                                                   'put': 'WMT   '
                                                          '240621P00190000',
                                                   'strike-price': '190.0'},
                                                  {'call': 'WMT   '
                                                           '240621C00195000',
                                                   'put': 'WMT   '
                                                          '240621P00195000',
                                                   'strike-price': '195.0'},
                                                  {'call': 'WMT   '
                                                           '240621C00200000',
                                                   'put': 'WMT   '
                                                          '240621P00200000',
                                                   'strike-price': '200.0'},
                                                  {'call': 'WMT   '
                                                           '240621C00210000',
                                                   'put': 'WMT   '
                                                          '240621P00210000',
                                                   'strike-price': '210.0'}]},
                                     {'days-to-expiration': 634,
                                      'expiration-date': '2025-01-17',
                                      'expiration-type': 'Regular',
                                      'settlement-type': 'PM',
                                      'strikes': [{'call': 'WMT   '
                                                           '250117C00065000',
                                                   'put': 'WMT   '
                                                          '250117P00065000',
                                                   'strike-price': '65.0'},
                                                  {'call': 'WMT   '
                                                           '250117C00070000',
                                                   'put': 'WMT   '
                                                          '250117P00070000',
                                                   'strike-price': '70.0'},
                                                  {'call': 'WMT   '
                                                           '250117C00075000',
                                                   'put': 'WMT   '
                                                          '250117P00075000',
                                                   'strike-price': '75.0'},
                                                  {'call': 'WMT   '
                                                           '250117C00080000',
                                                   'put': 'WMT   '
                                                          '250117P00080000',
                                                   'strike-price': '80.0'},
                                                  {'call': 'WMT   '
                                                           '250117C00085000',
                                                   'put': 'WMT   '
                                                          '250117P00085000',
                                                   'strike-price': '85.0'},
                                                  {'call': 'WMT   '
                                                           '250117C00090000',
                                                   'put': 'WMT   '
                                                          '250117P00090000',
                                                   'strike-price': '90.0'},
                                                  {'call': 'WMT   '
                                                           '250117C00095000',
                                                   'put': 'WMT   '
                                                          '250117P00095000',
                                                   'strike-price': '95.0'},
                                                  {'call': 'WMT   '
                                                           '250117C00100000',
                                                   'put': 'WMT   '
                                                          '250117P00100000',
                                                   'strike-price': '100.0'},
                                                  {'call': 'WMT   '
                                                           '250117C00105000',
                                                   'put': 'WMT   '
                                                          '250117P00105000',
                                                   'strike-price': '105.0'},
                                                  {'call': 'WMT   '
                                                           '250117C00110000',
                                                   'put': 'WMT   '
                                                          '250117P00110000',
                                                   'strike-price': '110.0'},
                                                  {'call': 'WMT   '
                                                           '250117C00115000',
                                                   'put': 'WMT   '
                                                          '250117P00115000',
                                                   'strike-price': '115.0'},
                                                  {'call': 'WMT   '
                                                           '250117C00120000',
                                                   'put': 'WMT   '
                                                          '250117P00120000',
                                                   'strike-price': '120.0'},
                                                  {'call': 'WMT   '
                                                           '250117C00125000',
                                                   'put': 'WMT   '
                                                          '250117P00125000',
                                                   'strike-price': '125.0'},
                                                  {'call': 'WMT   '
                                                           '250117C00130000',
                                                   'put': 'WMT   '
                                                          '250117P00130000',
                                                   'strike-price': '130.0'},
                                                  {'call': 'WMT   '
                                                           '250117C00135000',
                                                   'put': 'WMT   '
                                                          '250117P00135000',
                                                   'strike-price': '135.0'},
                                                  {'call': 'WMT   '
                                                           '250117C00140000',
                                                   'put': 'WMT   '
                                                          '250117P00140000',
                                                   'strike-price': '140.0'},
                                                  {'call': 'WMT   '
                                                           '250117C00145000',
                                                   'put': 'WMT   '
                                                          '250117P00145000',
                                                   'strike-price': '145.0'},
                                                  {'call': 'WMT   '
                                                           '250117C00150000',
                                                   'put': 'WMT   '
                                                          '250117P00150000',
                                                   'strike-price': '150.0'},
                                                  {'call': 'WMT   '
                                                           '250117C00155000',
                                                   'put': 'WMT   '
                                                          '250117P00155000',
                                                   'strike-price': '155.0'},
                                                  {'call': 'WMT   '
                                                           '250117C00160000',
                                                   'put': 'WMT   '
                                                          '250117P00160000',
                                                   'strike-price': '160.0'},
                                                  {'call': 'WMT   '
                                                           '250117C00165000',
                                                   'put': 'WMT   '
                                                          '250117P00165000',
                                                   'strike-price': '165.0'},
                                                  {'call': 'WMT   '
                                                           '250117C00170000',
                                                   'put': 'WMT   '
                                                          '250117P00170000',
                                                   'strike-price': '170.0'},
                                                  {'call': 'WMT   '
                                                           '250117C00175000',
                                                   'put': 'WMT   '
                                                          '250117P00175000',
                                                   'strike-price': '175.0'},
                                                  {'call': 'WMT   '
                                                           '250117C00180000',
                                                   'put': 'WMT   '
                                                          '250117P00180000',
                                                   'strike-price': '180.0'},
                                                  {'call': 'WMT   '
                                                           '250117C00185000',
                                                   'put': 'WMT   '
                                                          '250117P00185000',
                                                   'strike-price': '185.0'},
                                                  {'call': 'WMT   '
                                                           '250117C00190000',
                                                   'put': 'WMT   '
                                                          '250117P00190000',
                                                   'strike-price': '190.0'},
                                                  {'call': 'WMT   '
                                                           '250117C00195000',
                                                   'put': 'WMT   '
                                                          '250117P00195000',
                                                   'strike-price': '195.0'},
                                                  {'call': 'WMT   '
                                                           '250117C00200000',
                                                   'put': 'WMT   '
                                                          '250117P00200000',
                                                   'strike-price': '200.0'},
                                                  {'call': 'WMT   '
                                                           '250117C00210000',
                                                   'put': 'WMT   '
                                                          '250117P00210000',
                                                   'strike-price': '210.0'},
                                                  {'call': 'WMT   '
                                                           '250117C00220000',
                                                   'put': 'WMT   '
                                                          '250117P00220000',
                                                   'strike-price': '220.0'}]}],
                     'option-chain-type': 'Standard',
                     'root-symbol': 'WMT',
                     'shares-per-contract': 100,
                     'tick-sizes': [{'threshold': '3.0', 'value': '0.01'},
                                    {'value': '0.05'}],
                     'underlying-symbol': 'WMT'}]}}

def get_es_futures_option_chain_response_body():
    with open('test/resources/es_futures_option_chain_response_body.json') as f:
        return json.load(f)
    
def get_mes_futures_option_chain_response_body():
    with open('test/resources/mes_futures_option_chain_response_body.json') as f:
        return json.load(f)
    