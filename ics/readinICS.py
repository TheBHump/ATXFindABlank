from icalendar import Calendar, Event
import sys
from urllib.request import urlopen
import pytz
import json
import npm
sys.getdefaultencoding()
# package installed from https://icalendar.readthedocs.io/en/latest/index.html

def importCalendar(link): # insert url to ics file download
    url = link
    sock = urlopen(url)
    icsSource = sock.read()
    return Calendar.from_ical(icsSource)


def display(cal):
    for event in cal.walk("vevent"):
        uid = str(event.get("uid").to_ical())
        print("uid: " + uid[2:-1])
        date = str(event.get("dtstart").to_ical())
        print("date: " + date[2:-1])
        end = str(event.get("dtend").to_ical())
        print("ends at: " + end[2:-1])
        created = str(event.get("created").to_ical())
        print("created: " + created[2:-1])
        dtsamp = str(event.get("dtstamp").to_ical())
        print("dtstamp: " + dtsamp[2:-1])
        lastmod = str(event.get("last-modified").to_ical())
        print("last-modified: " + lastmod[2:-1])
        summary = str(event.get("summary").to_ical())
        print("summary: " + summary[2:-1])
        descr = str(event.get("http").to_ical())
        print("description: " + "http" + descr[2:])
        location = str(event.get("location").to_ical())
        print("location: " + location[2:-1])
        geo = str(event.get("geo").to_ical())
        print("geo: " + geo[2:-1])
        contact = str(event.get("contact").to_ical())
        if contact != " ":
            print("contact: " + contact[2:-1])
        categ = str(event.get("categories").to_ical())
        print("categories: " + categ[2:-1])

        print()

#make battleground texas calendar
bgtxCalendar = importCalendar("https://secure.battlegroundtexas.com/page/event/search_results?orderby=zip_radius&zip_radius%5b0%5d=78704&zip_radius%5b1%5d=100&country=US&limit=100&radius_unit=mi&format=ical&wrap=no")
print(display(bgtxCalendar))

