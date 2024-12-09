import requests as rq
from bs4 import BeautifulSoup
from bs4 import NavigableString
import pandas as pd
from extractfunction import extractBook

Burl = 'https://books.toscrape.com/'
Bheader = {'user-agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36'

}
Bk=rq.get(url=Burl, headers=Bheader)
BkBeautiful = BeautifulSoup(Bk.content,'html.parser')
books = [extractBook(book) for book in BkBeautiful.find_all('article', {'class':"product_pod"})]

booksDf = pd.DataFrame(books)

booksDf.to_csv('BOOK.csv')
