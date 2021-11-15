import re
from save_to_file import save_to_file

##MAKE REMOVE_DUPLICATES()
##MAKE REMOVE_UNVALID_URLS()

def find_articles(html_str, base=None, output=None):
    """Returns only wikipedia urls
    """
    urls = find_urls(html_str, base)
    urls_str = ' '.join(urls)
    regex = r'https:\/\/[^\.]+\.wikip[^ ]+' # does not include wikimedia urls
    wiki_urls = re.findall(regex, urls_str)
    wiki_urls = remove_unvalid_urls(wiki_urls)
    if output:
        wiki_str = list_to_str(wiki_urls)
        save_to_file(output, wiki_str)
    return wiki_urls

def find_urls(html_str, base=None, output=None):
    """Receives a string of html and returns a list of all urls found in
    the text.
    Input
        html_str (str): String of text
        base (str): Optional. Base of url
    Returns
        urls (list): list of urls found
    """
    regex = r'href=\"([^#\"]+)[^\>]*'
    urls = re.findall(regex, html_str)
    if base:
        urls = find_relative_links(urls, base)
    if output:
        filename = output
        urls_str = list_to_str(urls)
        save_to_file(filename, urls_str)
    return urls



# Below are helper functions

def find_relative_links(urls, base):
    """Makes absolute urls of all links not starting with https
    Input
        urls (list of str): list of relative and absolute urls
        base (str): base url
    Returns
        urls (list of str): list of same urls as input, but as absolute links
    """
    for i in range(len(urls)):
        url = urls[i]
        if url[0] != 'h':
            urls[i] = make_absolute_url(url, base)
    return urls

def remove_duplicates(list_with_duplicates):
    """
    Input
        list with duplicates
    Returns
        same list without duplicates (set)
    """

    no_duplicates = {}
    return no_duplicates

def make_absolute_url(relative_link, base):
    """Handles cases of urls starting with "//" or "/"
    Input
        relative_link (str): Link that need a base url
        base (str): base to be added to relatie link
    Returns
        Absolute link of the relative link
    """
    if relative_link[0:2] == '//':
        return 'https:' + relative_link
    return base + relative_link

def list_to_str(list):
    text = ''
    for streng in list:
        text += streng + '\n'
    return text