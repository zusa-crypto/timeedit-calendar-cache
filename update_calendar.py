import requests
from ics import Calendar
import os

URL = "https://cloud.timeedit.net/ehb_be/web/student/ri6Y2914Q73Z6kQ1dm5tjm035m168Z628Z4y1ZnQQ773908Q470n7F5B01ED5ZEC173FA6AA2Et06F21AE3E8CF86QF.ics"
FILE = "calendar.ics"

r = requests.get(URL)
new = Calendar(r.text)

events = {}

if os.path.exists(FILE):
    with open(FILE) as f:
        old = Calendar(f.read())
        for e in old.events:
            events[e.uid] = e

for e in new.events:
    events[e.uid] = e

merged = Calendar()
merged.events = set(events.values())

with open(FILE,"w") as f:
    f.writelines(merged)
