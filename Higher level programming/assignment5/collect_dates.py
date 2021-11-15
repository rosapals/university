import re
import sys

def find_dates(html_str, output=None):
    """Searches for dates in the given html string using regex

    Args
        html_str (str): String containing html code to search for dates
        output (str): name of output file

    Returns
        Str: A string containing all the extracted dates
    """

    # First define separate groups for month names
    jan = r"[jJ](?:anuary|an\.?)"
    feb = r"[fF](?:ebruary|eb\.?)"
    mar = r"[mM](?:arch|ar\.?)"
    apr = r"[aA](?:pril|pr\.?)"
    may = r"[mM]ay"
    jun = r"[jJ](?:une|un\.?)"
    jul = r"[jJ](?:uly|ul\.?)"
    aug = r"[aA](?:ugust|ug\.?)"
    sep = r"[sS](?:eptember|ept\.?)"
    octo = r"[oO](?:ctober|ct\.?)"
    nov = r"[nN](?:ovember|ov\.?)"
    dec = r"[dD](?:ecember|ec\.?)"
    any_month = rf"({jan}|{feb}|{mar}|{apr}|{may}|{jun}|{jul}|{aug}|{sep}|{octo}|{nov}|{dec})"

    #then define one regex for each format
    dmy_format = r"(?:(\d{1,2})\s)?" + any_month + r"\s(\d{4})"
    mdy_format = any_month + r"(?:\s(\d{1,2}))?" + r",\s(\d{4})"
    ymd_format = r"(\d{4})\s" + any_month + r"(?:\s(\d{1,2}))"
    iso_format = r"\b(\d{4})-(\d{1,2})-(\d{1,2})\b"
    #Combine everything into  the final regex
    regex = rf"(?:{dmy_format}|{mdy_format}|{ymd_format}|{iso_format})"

    result_list = re.findall(regex, html_str)

    result_list_formatted = []
    for line in result_list:
        line_formatted = line[2]+line[5]+line[6]+line[9]+'/'+line[1]+line[3]+line[7]+line[10]+'/'+line[0]+line[4]+line[8]+line[11]
        months = [jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec]

        for i in range(len(months)):
            #replace months with corresponding number
            line_formatted = re.sub(rf"{months[i]}", rf"{i+1}", line_formatted)
        #padding one- digit months with a zero
        line_formatted = re.sub(r"/(\d)/", r"/0\1/", line_formatted)
        #padding one- digit days with a zero
        line_formatted = re.sub(r"/(\d)$", r"/0\1", line_formatted)
        #removing any extra /'s on the right side
        line_formatted = re.sub(r"/$", r"", line_formatted)
        result_list_formatted.append(line_formatted)
    #callback function used for sorting the list of the dates by year, month, day
    def sorting(date):
        split = date.split('/')
        return split[0], split[1], '00' if len(split) == 2 else split[2]

    sorted_res = sorted(result_list_formatted, key=sorting)


    result_text = '\n'.join(sorted_res)
    if output:
        out_file = open(output, "w")
        out_file.write(result_text)
        out_file.close()
    else:
        return result_text

if __name__ == '__main__':
    import requesting_urls as ru
    folder = 'collect_dates_regex'
    rowling = "http://en.wikipedia.org/wiki/J._K._Rowling"
    richard = "https://en.wikipedia.org/wiki/Richard_Feynman"
    hans = "https://en.wikipedia.org/wiki/Hans_Rosling"
    find_dates(ru.get_html(rowling), folder + "/j_k_rowling_dates.txt")
    find_dates(ru.get_html(richard), folder + "/richard_feynman_dates.txt")
    find_dates(ru.get_html(hans), folder + "/hans_rosling_dates.txt")
