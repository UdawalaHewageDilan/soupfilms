from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.imdb.com/search/title/?genres=drama&groups=top_250&sort=user_rating,desc&view=advanced').text
soup = BeautifulSoup(source, 'lxml')

movie1 = soup.find_all(class_='lister-item mode-advanced')
file_name = open('imdb_test.csv', 'w')
file_writer = csv.writer(file_name)
file_writer.writerow(['Title', 'Year_of_Release', 'Duration', 'Points_Rating', 'Description','Rating', 'Meta_score'])

for item in movie1:
    title = item.find(class_='lister-item-header').a.text

    year = item.find(class_='lister-item-year text-muted unbold').text

    duration = item.find(class_='runtime').text

    points = item.find(class_='inline-block ratings-imdb-rating').strong.text

    descriptions = item.find_all(class_='text-muted')

    for i in range(len(descriptions)):
        description = (descriptions[i].text.replace('Gross:', ''))
    try:
        rating = item.find(class_='certificate').text
        meta_score = item.find(class_='metascore favorable').text
    except Exception as e:
        rating = None
        meta_score = None

    file_writer.writerow([title, year, duration, points, description, rating, meta_score])

file_name.close()


