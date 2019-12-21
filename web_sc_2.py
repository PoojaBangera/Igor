#!/usr/bin/python

from bs4 import BeautifulSoup
import requests
from product import Electronics

def getProducts():
	page = requests.get(
	    "https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniq")

	html_soup = BeautifulSoup(page.text, 'html.parser')
	#print(type(html_soup))

	products = html_soup.find_all('div', class_='_3wU53n')
	products_price = html_soup.find_all('div', class_='_1vC4OE _2rQ-NK')
	#print(type(products))
	#print(len(products))
	wrapper_dict = {'data' : []} # or wrapper_dict = dict()
	print(wrapper_dict)

	#pdict = Electronics("d","d")
	for p, pr in zip(products, products_price):
		#print(p.string)
		#x = Electronics(p.string, "laptop")
		#temp = {p.string : "laptop"}
		
		wrapper_dict = {"data" : [{p.string : pr.string.encode(encoding="utf-8", errors="ignore")} for p in products]}
	
	#print(len(wrapper_dict))
	print (wrapper_dict)
	#print(repr(__name__))

if __name__ == "__main__":
	getProducts()
	#product = Ele()
	#print(product.name)
