import json
from collections import Counter
with open("newsafr.json", encoding="utf-8") as datafile:
    json_data = json.load(datafile)
news = json_data['rss']['channel']['items']
news_description = []
for item in news:
    description = item['description'].split(' ')
    news_description.extend(description)
news_description_lower = []
for low in news_description:
    news_description_lower.append(low.lower())
news_description_lower_filter = list(filter(lambda del_len: len(del_len) >= 6, news_description_lower))
news_description_lower_filter.sort(key = len, reverse=True)
occurence_count = Counter(news_description_lower_filter)
ten_count = occurence_count.most_common(10)
print(ten_count)

