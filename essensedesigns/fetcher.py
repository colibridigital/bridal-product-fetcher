from lxml import html
import requests
from dynamodb import create_product

page = requests.get('https://www.essensedesigns.com/essense-of-australia/wedding-dresses/?fwp_per_page=2000')
tree = html.fromstring(page.content)
product_urls = tree.xpath('/html/body/div/section/div/article/a/@href')

for product_url in product_urls:
    print('Adding ' + product_url + ' to dynamo')
    create_product.insert('essense_products', product_url)