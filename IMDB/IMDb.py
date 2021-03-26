from bs4 import BeautifulSoup
import requests
import csv

source1 = requests.get('https://www.imdb.com/list/ls009668711/?st_dt=&mode=detail&page=1&sort=list_order,asc&ref_=ttls_vm_dtl')
#source2 = requests.get('https://www.imdb.com/search/title/?genres=drama&groups=top_250&sort=user_rating,desc&start=51&ref_=adv_nxt').text
soup1 = BeautifulSoup(source1.content, 'lxml')
#soup2 = BeautifulSoup(source2, 'lxml')
file_name = open('imdb.csv', 'w')
file_writer = csv.writer(file_name)
file_writer.writerow(['Title', 'Year_of_Release', 'Duration', 'Genre', 'Points_Rating', 'Meta_score', 'Director', 'Actors', 'Votes', 'Gross'])
movie_list = soup1.find(class_='lister-list')
movie1 = movie_list.find_all(class_='lister-item mode-detail')
for movie in movie1:
    #try:
    title = movie.find(class_='lister-item-header').a.text
    year = movie.find(class_='lister-item-year text-muted unbold').text.strip('()')
    rating = movie.find(class_='certificate').text
    duration = movie.find(class_='runtime').text
    genres = movie.find(class_='genre').text


    try:
        metascore = movie.find(class_='metascore').text
        people = movie.find_all(class_='text-muted text-small')[1].text

        director = people.split('|')[0].split(':')[1]
        actors = people.split('|')[1].split(':')[1].replace(',', '').split('\n')
        gross_votes = movie.find_all(class_='text-muted text-small')[2].text
        votes = gross_votes.split('|')[0].split(':')[1]
        gross = gross_votes.split('|')[1].split(':')[1]
    except Exception as e:
        # title = None
        # year = None
        # rating = None
        # duration = None
        # genres = None
        metascore = None
        director = None
        actors = None
        votes = None
        gross = None

    file_writer.writerow([title, year, duration, genres, rating, metascore,director,actors,votes,gross])

file_name.close()










