from time_planner import extract_events

def test_time_planner():
    url = "https://en.wikipedia.org/wiki/2021-22_FIS_Alpine_Ski_World_Cup"
    extract_events(url)

test_time_planner()