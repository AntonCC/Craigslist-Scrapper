import json

with open('./craigslist_scrape/spiders/prices.json') as f:
    data = json.loads(f.read())

interested = []

# all items under $100
idx = 0
while idx < len(data):
    if int(data[idx]['price'].split('$')[1]) < 100:
        interested.append(data[idx])
    idx += 1

with open('./interested.json', 'w') as f:
    json.dump(interested, f)


