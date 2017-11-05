from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

import datetime

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'

CATEGORIES = ["Canvass","Community Event","Fundraiser","Meeting","Office","Other","Paid Canvass","Phone Bank","Training","Voter Reg"]
NOW = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def create_calendar(service, category):
    calendar = {}
    calendar['description'] = category;
    calendar['summary'] = "ATX FindABlank " + category
    calendar['timeZone'] = "America/Chicago"
    created_calendar = service.calendars().insert(body=calendar).execute()
    return created_calendar

def get_events(service, calendar, maxResults = 10):
    eventsResult = service.events().list(
        calendarId=calendar['id'], timeMin=NOW, maxResults=maxResults, singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])
    return events

def classify_event(event):
    return "Other"

def already_exists(event, existing_events):
    return False

def add_event(service, calendar, event):
    print(calendar)
    new_event = {}
    new_event['description'] = "test"
    new_event['summary'] = "test"
    new_event['start'] = event['start']
    new_event['end'] = event['end']

    event = service.events().insert(calendarId = calendar['id'], body = new_event).execute()
    return event

def main():
    """Shows basic usage of the Google Calendar API.

    Creates a Google Calendar API service object and outputs a list of the next
    10 events on the user's calendar.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    calendars = service.calendarList().list().execute()['items']
    external_calendars = []
    existing_events = []
    by_category = {}
    primary_calendar = None
    for calendar in calendars:
        if 'primary' in calendar and calendar['primary']:
            # We use primary calendar as a data store
            existing_events = get_events(service, calendar)
            primary_calendar = calendar
        elif calendar['accessRole'] == "owner" and 'description' in calendar:
            by_category[calendar['description']] = calendar
        elif calendar['accessRole'] == "reader":
            external_calendars.append(calendar)

    #Create category calendars that don't exist yet        
    for category in CATEGORIES:
        if not category in by_category:
            by_category[category] = create_calendar(service, category) 

    #Load events from external calendars
    for calendar in external_calendars:
        events = get_events(service, calendar)
        print("Loading", len(events), "events")
        for event in events:
            if already_exists(event, existing_events):
                continue
            category = classify_event(event)
            add_event(service, by_category[category], event)


    # Calendars are separated by ours and theirs and we have events
    #

    #if not events:
    #    print('No upcoming events found.')
    #for event in events:
    #    start = event['start'].get('dateTime', event['start'].get('date'))
    #    print(start, event['summary'])


if __name__ == '__main__':
    main()