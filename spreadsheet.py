from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from operator import itemgetter

# Convert csv lists to dict in O(N * M * M) time.
# Where N is the smallest number of elements in each list
# and M in the number of lists. 
def csv_to_objects(lists):
    keys = lists.pop(0)
    return map(lambda props: dict(zip(keys, props)), lists)

# If the marketcap value is None return 0.
# Otherwise return the string as an int.
def get_marketcap(company):
    marketcap = itemgetter('marketcap')(company)
    try:
        return int(marketcap)
    except ValueError:
        return 0

# Order the array of dicts by marketcap value in descending order.
def marketcap_ordered(companies):
    return sorted(companies, key=lambda company: get_marketcap(company), reverse=True)

# Get the table data from Google Sheets API
# process and return it in market cap sorted order.
def get_companies():
    # Setup the Sheets API
    SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
    store = file.Storage('credentials.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    # Call the Sheets API
    # TODO: - Ignore rows with "None" values.
    SPREADSHEET_ID = '1zla6lHUg--9OZfIdQjA_munKew40lH3z5mFgXHkNHxc'
    RANGE_NAME = 'Database!A1:J'
    result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
    values = result.get('values', [])
    if not values:
        return {}
    else:
        companies = csv_to_objects(values)
        return marketcap_ordered(companies)
