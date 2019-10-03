import requests
from bs4 import BeautifulSoup

for i in range(0,980,20):
    url = 'https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4'+'?start=%d&type=T'%i
    douban_data = requests.get(url)
    soup = BeautifulSoup(douban_data.text,'lxml')
    titles = soup.select('#subject_list > ul > li > h2 > a')
    stars = soup.select('#subject_list > ul > li > div.info > div.star.clearfix > span.rating_nums')
    prices = soup.select('div.pub')
    for title,star,price in zip(titles,stars,prices):
        data = {
            'title':title.get_text().strip().split()[0],
            'star':float(star.get_text()),
            'price':price.get_text().strip().split('/')[-1]
        }
        print(data)