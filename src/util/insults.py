import urllib.request

from lxml import html, cssselect


def get_page(page: str) -> bytes:
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers = {'User-Agent': user_agent}

    request = urllib.request.Request(url=page, headers=headers)
    response = urllib.request.urlopen(request)

    return response.read()


def get_xpath_tree(data: [str, bytes]) -> html.HtmlElement:
    if isinstance(data, bytes):
        data = data.decode('utf-8')
    return html.fromstring(data)


def get_selector(tree: html.HtmlElement, selector: str) -> [str]:
    sel = cssselect.CSSSelector(selector)
    output = [e.text for e in sel(tree)]
    return output


def read_insults():
    with open("util/insults.txt", 'r') as fi:
        _insults = fi.read()
    return _insults.split("\n")


if __name__ == "__main__":
    for i in range(1, 19):
        print("processing {0}".format(i))
        if i == 1:
            page = get_page("http://onelinefun.com/insults/")
        else:
            page = get_page("http://onelinefun.com/insults/{0}/".format(i))
        tree = get_xpath_tree(page)
        insults = get_selector(tree, ".oneliner p")
        with open("insults.txt", 'a') as fo:
            fo.write("\n".join(insults))
