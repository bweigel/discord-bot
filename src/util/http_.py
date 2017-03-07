import urllib.request


def get_page(page: str, method: str = 'GET', headers=None) -> bytes:
    if headers is None:
        user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
        headers = {'User-Agent': user_agent}

    request = urllib.request.Request(url=page, headers=headers, method=method)
    response = urllib.request.urlopen(request)

    return response.read()


def get_str_page(*args, **kwargs) -> str:
    return get_page(*args, **kwargs).decode('utf-8')
