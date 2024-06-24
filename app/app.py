from lxml import html
import requests

# headers = {
#     'User-Agent': 'HarvesterRobot'
# }
# page_content = requests.get('https://fiis.com.br/lista-de-fundos-imobiliarios/', headers=headers).content
#### bypass: read a file
with open('saida_curl', 'r') as f:
    page_content = f.read()
# print(page_content)

# Parsing the page
tree = html.fromstring(page_content)

# Get element using XPath
title = tree.xpath('head/title/text()')
print(title)
# x = tree.xpath('/html/body/div[7]/div[3]/section[1]/div[1]/text()')
x = tree.xpath('/html/body/div[4]')
print(x[0].text_content())
print(x[0].get('class'))

## .text.strip()

