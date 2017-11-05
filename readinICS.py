from icalendar import Calendar, Event
import sys
import json
import npm
sys.getdefaultencoding()
# package installed from https://icalendar.readthedocs.io/en/latest/index.html

def display(cal):
    for event in cal.walk("vevent"):
        summary = str(event.get("summary").to_ical())
        print("summary: " + summary[2:-1])
        date = str(event.get("dtstart").to_ical())
        print("date: " + date[2:-1])
        end = str(event.get("dtend").to_ical())
        print("ends at: " + end[2:-1])
        location = str(event.get("location").to_ical())
        print("location: " + location[2:-1])
        descr = str(event.get("http").to_ical())
        print("description: " + descr[-2:-1])
        contact = str(event.get("contact").to_ical())
        if contact != " ":
            print("contact: " + contact[2:-1])
        geo = str(event.get("geo").to_ical())
        print("geo: " + geo[2:-1])

        print()


file = open("search_results.ics", "r") # reads in ics file downloaded from battleground texas website
cal = Calendar.from_ical(file.read())
print(display(cal))