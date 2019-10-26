def show():
    url = input('Url: ')

    headers = []
    header = input('Header: ')
    while header != '':
        headers.append(header)
        header = input('Next header: ')

    method = input('Method: ')
    body = input('Body: ')
    print(url, headers, method, body)
