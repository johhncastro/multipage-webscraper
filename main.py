from bs4 import BeautifulSoup
import requests

root = "https://subslikescript.com"
website = f'{root}/movies_letter-A'
result = requests.get(f'{root}/movies_letter-A')
content = result.text
soup = BeautifulSoup(content, 'lxml')

# pagination
pagination = soup.find('ul', class_='pagination')
pages = pagination.find_all('li', class_='page-item')
last_page = pages[-2].text

links = []
for page in range(1, int(last_page) + 1)[:3]:  # range (1, 133+1)
    result = requests.get(f'{website}?page={page}')
    content = result.text
    soup = BeautifulSoup(content, 'lxml')

    parentDiv = soup.find('article', class_='main-article')

    for link in parentDiv.find_all('a', href=True):
        links.append(link['href'])

    # print(links)
    # read a whole page w transcripts.
    for link in links:
        try:
            print(links)
            website = f'{root}/{link}'
            result = requests.get(website)
            content = result.text
            soup = BeautifulSoup(content, 'lxml')

            parentDiv = soup.find('article', class_='main-article')

            title = parentDiv.find('h1').get_text()
            transcript = parentDiv.find('div', class_='full-script').get_text(strip=True, separator=' ')

            with open(f'{title}.txt', 'w') as file:
                file.write(transcript)
        except:
            print("------------- link unavailable :( ")
            print(links)
