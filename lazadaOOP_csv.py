# -*- coding: utf-8 -*-
"""
Created on Tue Oct 04 19:35:21 2016

@author: adnan
"""

from lxml import html
import requests
import csv


class Lazada:
    
    base_url = ""
    pages = 1
    
    def scrap(self):
        csv_out = open('E:\pakaian_pria1.csv','wb')
        mywriter = csv.writer(csv_out)
        for url in [self.base_url % i for i in xrange(self.pages)]:
            page = requests.get(url)
            tree = html.fromstring(page.content)
            
            komoditi = tree.xpath('//span[@class="product-card__name big"]/text()')
            prices = tree.xpath('//div[@class="product-card__price"]/text()')
            #print 'Komoditi: ', komoditi
            #print 'Prices: ', prices
            gabung = zip(komoditi,prices)
            print 'Gabung: ', gabung
            mywriter.writerows(gabung)
        csv_out.close()    
            
tes = Lazada()
tes.base_url = "http://www.lazada.co.id/pakaian-pria/?page=%d"
tes.pages = 5

tes.scrap()
