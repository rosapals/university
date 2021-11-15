from requesting_urls import get_html

def test_requesting_urls():
    """Tests get_html(url, params=None, output=None) in requesting_urls.py
    with three given url's. Testing with and without parameters.
    The three runs output the .txt-files studio_ghibli_out.txt, 
    star_wars_out.txt and with_params_out.txt.
    """
    url =   [
            'https://en.wikipedia.org/wiki/Studio_Ghibli',
            'https://en.wikipedia.org/wiki/Star_Wars',
            'https://en.wikipedia.org/w/index.php' ]
    dir = 'requesting_urls/'
    output =    [
                dir + 'studio_ghibli_out.txt',
                dir + 'star_wars_out.txt',
                dir + 'with_params_out.txt' ]

    def test_studio_ghibli():
        get_html(url[0], None, output[0])

    def test_star_wars():
        get_html(url[1], None, output[1])

    def test_with_params():
        params = {'title':'Main_page', 'action':'info'}
        get_html(url[2], params, output[2])

    test_studio_ghibli()
    test_star_wars()
    test_with_params()

test_requesting_urls()