from lxml import html
import requests

page = requests.get('https://www.essensedesigns.com/essense-of-australia/wedding-dresses/?fwp_per_page=2000')
tree = html.fromstring(page.content)
product_urls = tree.xpath('/html/body/div/section/div/article/a/@href')
print product_urls