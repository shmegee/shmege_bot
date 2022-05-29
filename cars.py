import requests
from lxml import html
import random
A = random.randint(0, 9)

def get_info():
    r = requests.get('https://auto.ru/sankt-peterburg/cars/vaz/2107/all/')
    tree = html.fromstring(r.content)
    titles_xpath = tree.xpath('//a[@class="Link ListingItemTitle__link"]//text()')
    prices_xpath = tree.xpath('//a[@class="Link ListingItemPrice__link"]//text()')
    probeg_xpath = tree.xpath('//div[@class="ListingItem__kmAge"]//text()')
    return(titles_xpath[A]+"\n"+probeg_xpath[A]+"\n"+ prices_xpath[A])

def get_image():
    r = requests.get('https://auto.ru/sankt-peterburg/cars/vaz/2107/all/')
    tree = html.fromstring(r.content)
    images_xpath = tree.xpath('//div[@class="Brazzers__image-wrapper undefined"]/img')

    ssylka = images_xpath[A].get('src')[2:]
    return(ssylka)

def get_offer():
    r = requests.get('https://auto.ru/sankt-peterburg/cars/vaz/2107/all/')
    tree = html.fromstring(r.content)
    href_xpath = tree.xpath('//a[@class="Link ListingItemTitle__link"]')
    ssylka = href_xpath[A].get("href")
    return(ssylka)

def get_info1():
    r = requests.get('https://auto.ru/sankt-peterburg/cars/vaz/2114/all/')
    tree = html.fromstring(r.content)
    titles_xpath = tree.xpath('//a[@class="Link ListingItemTitle__link"]//text()')
    prices_xpath = tree.xpath('//a[@class="Link ListingItemPrice__link"]//text()')
    probeg_xpath = tree.xpath('//div[@class="ListingItem__kmAge"]//text()')
    return(titles_xpath[A]+"\n"+probeg_xpath[A]+"\n"+ prices_xpath[A])

def get_image1():
    r = requests.get('https://auto.ru/sankt-peterburg/cars/vaz/2114/all/')
    tree = html.fromstring(r.content)
    images_xpath = tree.xpath('//div[@class="Brazzers__image-wrapper undefined"]/img')

    ssylka = images_xpath[A].get('src')[2:]
    return(ssylka)

def get_offer1():
    r = requests.get('https://auto.ru/sankt-peterburg/cars/vaz/2114/all/')
    tree = html.fromstring(r.content)
    href_xpath = tree.xpath('//a[@class="Link OfferThumb"]')
    ssylka = href_xpath[A].get("href")
    return(ssylka)

def get_info2():
    r = requests.get('https://auto.ru/sankt-peterburg/cars/vaz/2121/all/')
    tree = html.fromstring(r.content)
    titles_xpath = tree.xpath('//a[@class="Link ListingItemTitle__link"]//text()')
    prices_xpath = tree.xpath('//a[@class="Link ListingItemPrice__link"]//text()')
    probeg_xpath = tree.xpath('//div[@class="ListingItem__kmAge"]//text()')
    return(titles_xpath[A]+"\n"+probeg_xpath[A]+"\n"+ prices_xpath[A])

def get_image2():
    r = requests.get('https://auto.ru/sankt-peterburg/cars/vaz/2121/all/')
    tree = html.fromstring(r.content)
    images_xpath = tree.xpath('//div[@class="Brazzers__image-wrapper undefined"]/img')

    ssylka = images_xpath[A].get('src')[2:]
    return(ssylka)

def get_offer2():
    r = requests.get('https://auto.ru/sankt-peterburg/cars/vaz/2121/all/')
    tree = html.fromstring(r.content)
    href_xpath = tree.xpath('//a[@class="Link ListingItemTitle__link"]')
    ssylka = href_xpath[A].get("href")
    return(ssylka)

def get_info3():
    r = requests.get('https://auto.ru/sankt-peterburg/cars/vaz/vesta/all/')
    tree = html.fromstring(r.content)
    titles_xpath = tree.xpath('//a[@class="Link ListingItemTitle__link"]//text()')
    prices_xpath = tree.xpath('//a[@class="Link ListingItemPrice__link"]//text()')
    probeg_xpath = tree.xpath('//div[@class="ListingItem__kmAge"]//text()')
    return(titles_xpath[A]+"\n"+probeg_xpath[A]+"\n"+ prices_xpath[A])

def get_image3():
    r = requests.get('https://auto.ru/sankt-peterburg/cars/vaz/vesta/all/')
    tree = html.fromstring(r.content)
    images_xpath = tree.xpath('//div[@class="Brazzers__image-wrapper undefined"]/img')

    ssylka = images_xpath[A].get('src')[2:]
    return(ssylka)

def get_offer3():
    r = requests.get('https://auto.ru/sankt-peterburg/cars/vaz/vesta/all/')
    tree = html.fromstring(r.content)
    href_xpath = tree.xpath('//a[@class="Link OfferThumb"]')
    ssylka = href_xpath[A].get("href")
    return(ssylka)

