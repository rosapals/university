from filter_urls import find_articles
from requesting_urls import get_html

def test_find_articles1():
    html = """
    <a href="#fragment-only">anchor link</a>
    <a id="some-id" href="/relative/path#fragment">relative link</
    a>
    <a href="//other.host/same-protocol">same-protocol link</a>
    <a href="https://example.com">absolute URL</a>
    """
    dir = 'filter_urls/'
    urls = find_articles(html, base="https://en.wikipedia.org", output=dir+"test_find_articles_out.txt")
    assert urls == [
        "https://en.wikipedia.org/relative/path"
    ]

def test_find_articles2(url, output):
    html = get_html(url)  
    dir = 'filter_urls/'
    urls = find_articles(html, base="https://en.wikipedia.org", output=dir+output)

def run_tests():
    # initial test
    test_find_articles1()

    # test the three given urls
    urls = [
            'https://en.wikipedia.org/wiki/Nobel_Prize',
            'https://en.wikipedia.org/wiki/Bundesliga',
            r'https://en.wikipedia.org/wiki/2019%E2%80%9320_FIS_Alpine_Ski_World_Cup'
            ]
    test_find_articles2(urls[0], 'nobel_articles_out.txt')
    test_find_articles2(urls[1], 'bundesliga_articles_out.txt')
    test_find_articles2(urls[2], 'alpine_articles_out.txt')

run_tests()