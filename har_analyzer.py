import json
from haralyzer import HarParser

with open('try_har.json', 'r', encoding='utf8') as f:
    har_parser = HarParser(json.loads(f.read()))
total_weight = 0
count=0
for page in har_parser.pages:
    for entry in page.entries:
        total_weight += entry['response']['content']['size']


print("Total time: {0}(seconds)".format(har_parser.har_data['pages'][0]['pageTimings']['onLoad']/1000))
print("Total requests: ", len(har_parser.har_data['entries']))
print("Total weight: {0}(MB)".format(total_weight/1000000))
