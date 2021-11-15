import re
import requests
from bs4 import BeautifulSoup
from requesting_urls import get_html
from collect_dates import find_dates

def extract_events(url):
    """ Extract date , venue and discipline for competitions .
    Your documentation here .
    Args :
        url (str): The url to extract events from .
    Returns :
        table_info ( list of lists ): A nested list where the rows
        represent each
        race date , and the columns are [date, venue, discipline ].
    """
    disciplines = {
            "DH": "Downhill",
            "SL": "Slalom",
            "GS": "Giant Slalom",
            "SG": "Super Giant Slalom",
            "AC": "Alpine Combined",
            "PG": "Parallel Giant Slalom"
    }
    
    # request html
    html = get_html(url)

    # use BeautifulSoup to do something
    soup = BeautifulSoup(html, "html.parser")

    # find table for Men's skiing events
    soup_table = soup.find('table', {'class':'wikitable sortable'})

    # find rows of the table
    rows = soup_table.find_all("tr")

    # remember the previous venue in case successive events use the same venue
    prev_venue = "None"
    # stop flag is when finished=0
    iterate_finals = 1
    
    # iterate rows and parse if possible
    for i in range( len(rows) ):
        # Parse the row
        event_data = rows[i].find_all("td")
        # ignore rows with one column
        if ( len(event_data) > 1 ) and ( iterate_finals != 0 ):
            # the row contains an event
            date = event_data[2].text.strip()
            venue = event_data[3].text.strip()
            if venue[-3:].isnumeric():
                # this is the discipline cell by mistake
                discipline = venue[0:2]
                # the venue is same as in the previous event
                venue = prev_venue
            elif (venue[-2] == '%'):
                # this is the slope cell by mistake
                venue = prev_venue
                discipline = event_data[4].text[0:2]
            else:
                # discipline cell is normally in column 6
                discipline = event_data[5].text[0:2]

            print("(previous venue "+prev_venue+".)")
            prev_venue = venue
            
            print("venue "+venue+".")
            #print()
            print("date "+date+".")
            #print()
            print("discipline "+discipline+".")
            print()
        
        # Ignore if event_data is empty
        if len(event_data) > 0:
            header = event_data[0].text
            if 'Season Final' in header:
                # Final events use the same venue
                venue = event_data[3].text.strip()
                for i in range(len(rows)-i):
                    print ("final venue "+venue)

                # set flag to indicate we are on the rows of the finals
                iterate_finals = 0
    
"""
def find_venue(html):
    regex = r'title=".+title="([a-zA-ZäöüßÄÖÜ]+)'
    return re.findall(regex, html)
"""