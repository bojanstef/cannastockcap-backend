from operator import itemgetter

csv = [["marketcap", "name", "price"], ["None", "Bojan", "2",], ["8000", "Jenny", "2.5"], ["3000", "Lord", "25"]]

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

companies = csv_to_objects(csv)
ordered = marketcap_ordered(companies)
print(ordered)
