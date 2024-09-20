import requests
from bs4 import BeautifulSoup
import json


# Функція парсингу
def parse_quotes():
    # Списки для зберігання даних
    store_quotes = []
    store_authors = []

    # Ітерації для кожної з 10-ти стрінок сайта
    for i in range(10):

        url = 'http://quotes.toscrape.com/'
        html_doc = requests.get(url+f'page/{i+1}/')

        if html_doc.status_code == 200:
            soup = BeautifulSoup(html_doc.content, 'html.parser')
            
            # Розділ, що містить все потрібне про цитати
            quotes = soup.find_all('div', class_='quote')

            # Цикл для кожної цитати на сторінці
            for quote in quotes:

                # Парсинг усіх фіч для цитат
                tags = [tag.text for tag in quote.find('div', class_='tags').find_all('a', class_='tag')]
                author = quote.find('small', class_='author').text
                quote_text = quote.find('span', class_='text').text
                store_quotes.append({"tags": tags, "author": author, "quote": quote_text})

                # Нове підключення до сторінки з відповідним автором
                author_page = requests.get(f"{url}{quote.find('a', class_=None)['href']}")
                author_contents = BeautifulSoup(author_page.content, 'html.parser')
                author_details = author_contents.find('div', class_='author-details')

                # Парсинг усіх фіч для авторів
                fullname = author_details.find('h3', class_='author-title').text
                born_date = author_details.find('span', class_='author-born-date').text
                born_location = author_details.find('span', class_='author-born-location').text
                description = author_details.find('div', class_='author-description').text

                # Якщо автор уже зустрічався - пропуск
                if fullname in [author["fullname"] for author in store_authors]:
                    continue
                store_authors.append({"fullname": fullname, "born_date": born_date, "born_location": born_location, 
                                      "description": description.lstrip()})

                # Запис у json файли
                with open('authors.json', 'w') as file:
                    json.dump(store_authors, file, indent=4)

                with open('quotes.json', 'w') as file:
                    json.dump(store_quotes, file, indent=4)


if __name__ == '__main__':
    parse_quotes()