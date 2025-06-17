from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
# Create your views here.

def get_content(book):
    USER_AGENT = "Mozilla/5.0 "
    LANGUAGE = "en-US< en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html_content = session.get(f"https://openlibrary.org/search?q={book}").text
    return html_content

def book(request):
    product_info_list = []
    product = request.GET.get('book', '').strip()
    if not product:
        product = "books" 
    html_content = get_content(product)
    soup = BeautifulSoup(html_content, 'html.parser')
    

    product_items = soup.find_all('div', class_="sri__main")

    for items in product_items:
        name_tag = items.find('a', class_="results")
        author_wrapper = items.find('span', class_="bookauthor")
        author_tag = author_wrapper.find('a')
        image_wrapper = items.find('span', class_="bookcover")
        image_tag = image_wrapper.find('img')
        quantity = 15
        if name_tag and author_tag:
            name = name_tag.text
            author = author_tag.text
            image = image_tag['src']
            product_info = {'name': name, 'author': author, 'image': image, 'quantity': quantity}
            product_info_list.append(product_info)
            if len(product_info_list)==10:
                break

    return render(request, 'book.html', {'product_info_list': product_info_list})

