# -*- coding: utf-8 -*-
"""
Created on Tue Oct 04 19:35:21 2016

@author: adnan
"""

from lxml import html
from lxml import etree
import xml.etree.cElementTree as ET
import requests
import csv


class Lazada:
    
    base_url = ""
    pages = 1
    
   
    def scrap(self):
        gabung = []
        arrkomoditi = []
        arrharga = []
        for url in [self.base_url % i for i in xrange(self.pages)]:
            page = requests.get(url)
            tree = html.fromstring(page.content)
            komoditi =  tree.xpath('//span[@class="product-card__name big"]/text()')
            prices = tree.xpath('//div[@class="product-card__price"]/text()')
            arrkomoditi.extend(komoditi)
            arrharga.extend(prices)
                    
        gabung = zip(arrkomoditi,arrharga)
        print gabung
        root = ET.Element("root")
        comment = ET.Comment('lazada.co.id')
        root.append(comment)
            
        for x,y in gabung:
            item = ET.SubElement(root,"item")
            ET.SubElement(item,"field1", name="namabarang").text = x
            ET.SubElement(item,"field2",name="harga").text = y
            
        trees = ET.ElementTree(root)
        trees.write("pakaian.xml") 
        
        
tes = Lazada()
tes.base_url = "http://www.lazada.co.id/pakaian-pria/?page=%d"
tes.pages = 3

tes.scrap()

