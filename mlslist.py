import requests

from bs4 import BeautifulSoup

url_page = "https://www.mlslistings.com/Search/Result/8955a349-6045-44b6-b00b-daa3c2b4036a/1"
page = requests.get(url_page)
result_page_count = BeautifulSoup(page.content, 'html.parser')
import pdb;pdb.set_trace()

for i in range(1, int(result_page_count.find('small').text.split()[-2].replace(",", ""))):
    print(i)
    url = "https://www.mlslistings.com/Search/Result/8955a349-6045-44b6-b00b-daa3c2b4036a/{}".format(i)


# for i in result.find_all('h5', {'class': 'card-title font-weight-bold listing-address mb-25'}):
#     i.find('a').get('href')