from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
# Create your views here.

def get_content(product):
    USER_AGENT = "Mozilla/5.0 "
    LANGUAGE = "en-US< en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html_content = session.get(f"https://www.flipkart.com/search?q={product}").text
    return html_content

def home(request):
    product_info_list = []
    product = request.GET.get('product', '').strip()
    if not product:
        product = "washing machine" 
    html_content = get_content(product)
    soup = BeautifulSoup(html_content, 'html.parser')
    

    big_card = soup.find_all('div', class_="tUxRFH")
    if big_card:
        for items in big_card:
            name_tag = items.find('div', class_="KzDlHZ")
            price_tag = items.find('div', class_="Nx9bqj _4b5DiR")
            image_tag = items.find('img')
            link_tag = items.find('a', class_="CGtC98")
            if name_tag and price_tag:
                name = name_tag.text
                price = price_tag.text
                image = image_tag['src']
                link = link_tag['href']
                product_info = {'name': name, 'price': price, 'image': image, 'link': link}
                product_info_list.append(product_info)
                if len(product_info_list)==10:
                    break

    mid_card = soup.find_all('div', class_="slAVV4")
    if mid_card:
        for items in mid_card:
            name_tag = items.find('a', class_="wjcEIp")
            price_tag = items.find('div', class_="Nx9bqj")
            image_tag = items.find('img')
            link_tag = items.find('a', class_="VJA3rP")
            if name_tag and price_tag:
                name = name_tag.text
                price = price_tag.text
                image = image_tag['src']
                link = link_tag['href']
                product_info = {'name': name, 'price': price, 'image': image, 'link': link}
                product_info_list.append(product_info)
                if len(product_info_list)==10:
                    break

    small_card = soup.find_all('div', class_="_1sdMkc LFEi7Z")
    if small_card:
        for items in small_card:
            name_tag = items.find('a', class_="WKTcLC")
            price_tag = items.find('div', class_="Nx9bqj")
            image_tag = items.find('img')
            link_tag = items.find('a', class_="rPDeLR")
            if name_tag and price_tag:
                name = name_tag.text
                price = price_tag.text
                image = image_tag['src']
                link = link_tag['href']
                product_info = {'name': name, 'price': price, 'image': image, 'link': link}
                product_info_list.append(product_info)
                if len(product_info_list)==10:
                    break
    

    return render(request, 'home.html', {'product_info_list': product_info_list})

