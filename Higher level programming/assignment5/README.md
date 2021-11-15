# IN3110 Assignment 5 README

This code ran with Python version 3.8.2 on MacOS and Linux.

Task 5.1 uses module requests. To install write:
```sh
$  python3 -m pip install requests
```
Task 5.4 uses the Python tool Beautiful Soup. To install write:
```sh
$  python3 -m pip install beautifulsoup4
```
Task 5.5 uses matplotlib. To install write:
```sh
$  python3 -m pip install matplotlib
```

## Task 5.1 - Send HTTP requests

A directory `requesting_urls` which contains:
- Three output files `studio_ghibli_out.txt`, `star_wars_out.txt` and `with_params_out.txt`. The output files from the test runs

## Task 5.3 - Regex for finding dates
Explaining a regex for defining a month name:

`[jJ](?:anuary|an\.?)` (line 15)

`jJ`: matches a single character in the list jJ

`anuary|an`: anuary or an are matched

`\.?`: matches the character . between zero and one times, as many times as possible

Explaining a regex for dmy format:

`(?:(\d{1,2})\s)?` and `\s(\d{4})` (line 30)

`\d{1,2}`: match digit between 1 and 2 times
`\s`: match whitespace

## Task 5.4 - Soup for finding dates
The code in time_planner.py does not use regex to find the event venues,
becuase it seemed as a good idea at the time. It ended with a bit messy code,
but works fine.

## Task 5.5 - NBA Player stats
from `extract_top_players(all_players)`:
The following code was found on https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value,
in the third answer on the website.

It takes a dictionary and returns it sorted by value, biggest value first
```python
sorted(d.items(), key=lambda x: x[1], reverse=True)
```
The task has a fault in sorting top three players,
or in extracting values from the respective player´s wiki site. I did not have time to fix this.
But the plots looks nice. 

## Task 5.6 - Wiki Race
Task not done due to lack of time and being stupid

## How to run tests

For all tests navigate to assignment5 folder.
For testing `requesting_urls.py` write in terminal:
```sh
$ python3 test_requesting_urls.py
```
This will create a folder `requesting_urls` containing three .txt-files.


For testing `filter_urls.py` we use the two testfiles test_find_urls.py and test_find_articles.py.
Write for example:
```
$ python3 test_find_articles.py
```
This will create a folder `filter_urls` containing four .txt-files.
Do the same with `test_find_urls.py`, which will put additionally
four files in the `filter_urls` folder.

For testing `collect_dates.py` write in terminal:
```
$ python3 collect_dates.py
```
This will run main function in the file. 
A folder `collect_dates_regex` will be created, containing three 
.txt-files with sorted dates.

For testing `time_planner.py` write in terminal:
```
$ python3 test_time_planner.py
```
Which saves the files `betting_slip_empty.md` and `extract_events_out.txt`
to the folder `datetime_filter`.
__When viewing the betting slip in github, view as Raw or Blame__

For testing `fetch_player_statistics.py` and all its
subfunctions, write in terminal:
```
$ python3 test_fetch_player_stats.py
```
This may take up to a minute, and will put three plots in a folder `NBA_player_statistics`.
__Plots differ from time to time so something is wrong, look section Task 5.5 above__
