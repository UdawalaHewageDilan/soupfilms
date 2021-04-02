def get_film_info(url):
    from bs4 import BeautifulSoup
    import requests

    source = requests.get(url)
    soup = BeautifulSoup(source.content, 'lxml')

    info_card = soup.find(class_='infobox vevent')
    all_info = info_card.find_all(class_='infobox-data')
    director = all_info[0].text
    produced_by = all_info[1].text
    written_by = all_info[2].text
    starring = all_info[3].text
    music = all_info[4].text
    cinematography = all_info[5].text
    edited_by = all_info[6].text
    production_comps = all_info[7].text
    distribution = all_info[8].text
    release = all_info[9].text
    duration = all_info[10].text
    country = all_info[11].text
    language = all_info[12].text
    budget = all_info[13].text
    box_office = all_info[14].text


