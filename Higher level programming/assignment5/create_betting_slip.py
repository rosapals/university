from save_to_file import save_to_file
import os

def create_betting_slip(events, save_as):

    """Saves a markdown format betting slip to the  location datetime_filter/<save_as>.md.
    Inputs
        events (list of tuples): takes a list of 3-tuples containing
                                (date, venue, discipline) in the form of strings.
        save_as (str): filename to save the markdown betting slip as.
    """
    save_as=f"datetime_filter/{save_as}.md"
    savelist=[]
    savelist.append("Betting SLIP")
    savelist.append("")
    savelist.append("Name:")
    savelist.append("")
    edge="+------------+-----------------------------------------+-----------------------+---------------------+"
    savelist.append(edge)
    savelist.append("|    DATE    |                 Venue                   |       Discipline      |       Who wins?     |")
    for event in events:
        date=event[0][0:6]+' '+event[0][-2:]
        date=" " + date + (" "*(11-len(date)))
        venue=" "+ event[1] + (" "*(40-len(event[1])))
        discipline=" "+ event[2] + (" "*(22-len(event[2])))
        savelist.append(edge)
        savelist.append("|"+date+"|"+venue+"|"+discipline+"|                     |")
    savelist.append(edge)
    text = ""
    for s in savelist:
        text += s + "\n"
    # make sure folder exists
    os.makedirs("datetime_filter/", exist_ok=True)
    save_to_file(save_as, text)
    return