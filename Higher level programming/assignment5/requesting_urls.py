import requests
from save_to_file import save_to_file

def get_html(url, params=None, output=None):
    """Takes an url and returns the html text,
    with or without a specific type of data.
    Inputs
        url (str): Required. Website of choice
        params (dict): Optional. To be sent as a query string.
        output (str): Optional. Name of .txt-file to save html text to.
    Returns
        html text (str): The data from website of choice
    """
    html_str = make_str(url, params)
    if output:
        save_to_file(output, html_str)
    return html_str

def make_str(url, params):
    response = requests.get(url, params=params)
    return url + "\n\n" + response.text