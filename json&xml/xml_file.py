import xml.etree.ElementTree as ET
from collections import Counter
parser = ET.XMLParser(encoding="utf-8")
tree = ET.parse("newsafr.xml", parser)
news_description = []
root = tree.getroot()
xml_items = root.findall("channel/item")

for item in xml_items:
    description = item.find("description").text.split(" ")
    news_description.extend(description)

news_description = list(filter(lambda del_len: len(del_len) < 7, news_description))
news_description.sort(key=len, reverse=True)
occurence_count = Counter(news_description)
ten_count = occurence_count.most_common(10)
print(ten_count)
