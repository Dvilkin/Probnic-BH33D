# Лимиты QIWI Кошелька


def limits(login, api_access_token):
    types = ['TURNOVER', 'REFILL', 'PAYMENTS_P2P', 'PAYMENTS_PROVIDER_INTERNATIONALS', 'PAYMENTS_PROVIDER_PAYOUT',
             'WITHDRAW_CASH']
    s = requests.Session()
    s.headers['Accept'] = 'application/json'
    s.headers['Content-Type'] = 'application/json'
    s.headers['authorization'] = 'Bearer ' + api_access_token
    parameters = {}
    for i, type in enumerate(types):
        parameters['types[' + str(i) + ']'] = type
    b = s.get('https://edge.qiwi.com/qw-limits/v1/persons/' + login + '/actual-limits', params=parameters)
    return b.json()
