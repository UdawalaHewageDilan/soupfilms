from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.imdb.com/list/ls009668711/?st_dt=&mode=detail&page=1&sort=list_order,asc&ref_=ttls_vm_dtl').text
soup = BeautifulSoup(source, 'lxml')

movie1 = soup.find_all(class_='lister-item mode-detail')
file_name = open('imdb_test.csv', 'w')
file_writer = csv.writer(file_name)
file_writer.writerow(['Title', 'Year_of_Release', 'Duration', 'Genre', 'Points_Rating'])#, 'Description', 'Rating', 'Meta_score'])

for item in movie1:
    title = item.find(class_='lister-item-header').a.text

    year = item.find(class_='lister-item-year text-muted unbold').text

    duration = item.find(class_='runtime').text

    genre = item.find(class_='genre').text

    points = item.find(class_='inline-block ratings-imdb-rating').strong.text

    descriptions = item.find_all(class_='text-muted')

    # for i in descriptions:
    #     description = i.text
    try:
        rating = item.find(class_='certificate').text
        meta_score = item.find(class_='metascore favorable').text
    except Exception as e:
        rating = None
        meta_score = None

    file_writer.writerow([title, year, duration, genre, points]) #description, rating, meta_score])

file_name.close()


