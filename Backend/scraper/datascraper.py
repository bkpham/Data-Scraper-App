from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from urllib.request import urlopen
from time import time

async def get_data(url):
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    pPrice = ((soup.find('div', class_='product-price')).findAll('div',class_='product-listing-price'))
    pName = (soup.find('div',class_='productspec')).find('h1')
    pQuantity = (soup.find('div',class_='stock-info'))
    price_clean = (((pPrice[1].text).replace(" ", "")).split("\r")[0]).split('$')[1]
    quantity_clean = (((pQuantity.text).replace(" ", "")).split("\n")[1]).split("in")[0]
    if quantity_clean == '':
        quantity_clean = '0'
    if quantity_clean == '99+':
        quantity_clean = '99'
    pType = (soup.find('span', class_='SectionTitleText')).findAll('a',class_='SectionTitleText')
    print(pType[1].text)
    if (pType[1].text) == 'HANDGUN AMMO':
        type = 1
    elif (pType[1].text) == 'RIFLE AMMO':
        type = 2
    elif (pType[1].text) == 'RIMFIRE AMMO':
        type = 3
    elif (pType[1].text) == 'SHOTGUN AMMO':
        type = 4
    myProduct = dict(name = pName.text, price = price_clean, quantity = quantity_clean, url=url,type=type)
    return myProduct

async def scrape_all_ammo():
    cat_links = []
    urls = []
    products = []
    ammoCategories = ['https://www.targetsportsusa.com/shotgun-ammo-c-28.aspx','https://www.targetsportsusa.com/handgun-ammo-c-26.aspx',
                      'https://www.targetsportsusa.com/rimfire-ammo-c-196.aspx','https://www.targetsportsusa.com/rifle-ammo-c-27.aspx']
    for categoryUrl in ammoCategories:
        page = urlopen(categoryUrl)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        ul = (soup.find('ul', class_='category-list'))
        for li in ul:
            try:
                temp_link = li.find('a')
                cat_links.append(temp_link.get('href'))
            except:
                pass
    for clink in cat_links:
        driver = webdriver.Edge()
        driver.get('https://www.targetsportsusa.com'+clink)
        try:
            select = Select(driver.find_element('id','per-page'))
            select.select_by_value('All')
            time.sleep(1)
        except:
            pass
        soup = BeautifulSoup(driver.page_source, "html.parser")
        ul = (soup.find('ul', class_='product-list'))
        for li in ul: 
            a = li.find('a') 
            try: 
                if 'href' in a.attrs: 
                        url = a.get('href') 
                        urls.append(url)
            except: 
                pass
    driver.close()
    for url in urls:
        page = urlopen('https://www.targetsportsusa.com'+url)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        pPrice = ((soup.find('div', class_='product-price')).findAll('div',class_='product-listing-price'))
        pName = (soup.find('div',class_='productspec')).find('h1')
        pQuantity = (soup.find('div',class_='stock-info'))
        price_clean = (((pPrice[1].text).replace(" ", "")).split("\r")[0]).split('$')[1]
        quantity_clean = (((pQuantity.text).replace(" ", "")).split("\n")[1]).split("in")[0]
        if quantity_clean == '':
            quantity_clean = '0'
        if quantity_clean == '99+':
            quantity_clean = '99'
        pType = (soup.find('span', class_='SectionTitleText')).findAll('a',class_='SectionTitleText')
        try:
            if (pType[1].text) == 'HANDGUN AMMO':
                type = 1
            elif (pType[1].text) == 'RIFLE AMMO':
                type = 2
            elif (pType[1].text) == 'RIMFIRE AMMO':
                type = 3
            elif (pType[1].text) == 'SHOTGUN AMMO':
                type = 4
        except:
            type = 0
        myProduct = dict(name = pName.text, price = price_clean, quantity = quantity_clean, url="https://www.targetsportsusa.com"+url, type=type)
        products.append(myProduct)
    return products