import csv
import re
import requests
from bs4 import BeautifulSoup
from collections import defaultdict

import sys
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='latin-1', buffering=1)

i=0

exceptions = {
"name2": "value2",
}


headers = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
}

# Define the mapping of unique values in column 2 to strings
value_mapping = {   
    "PlayStation": "playstation",
    "PlayStation 2": "playstation-2",
    "PlayStation 3": "playstation-3",
    "PlayStation 4": "playstation-4",
    "PlayStation 5": "playstation-5",
    "Xbox": "xbox",
    "Xbox 360": "xbox-360",
    "Xbox One": "xbox-one",
    "Xbox Series X": "xbox-series-x",
    "Dreamcast": "dreamcast",
    "Nintendo 64": "nintendo-64",
    "GameCube": "gamecube",
    "Wii": "wii",
    "Wii U": "wii-u",
    "Switch": "switch",
    "PC": "pc",
    "PlayStation Vita": "playstation-vita",
    "PSP": "psp",
    "iOS": "ios",
    "3DS": "3ds",
    "DS": "ds",
    "Game Boy Advance": "game-boy-advance",
    "Stadia": "stadia",

}

# Read the CSV file
with open("all_reviews - Copy.csv", "r+", encoding='latin-1') as file:
    reader = csv.reader(file)
    header = next(reader) + ["dev", "genres", "rating"]
    # Skip the first row (titles)

    data = [row for row in reader]


with open("updated_games.csv", "w", newline="", encoding='utf-8') as output_file:
    writer = csv.writer(output_file)
    writer.writerow(header)

    for row in data:

        
        print(row[0] + " " + row[1])
        
        val1 = re.sub(r" & ", "-", row[0])
        val1 = re.sub(r" / ", "-", val1)
        val1 = re.sub(r" : ", "-", val1)
        
        val1 = re.sub(r"[^a-zA-Z0-9!+-]+", "", val1.lower().replace(" ", "-"))
        if row[0] in exceptions:
            val1 = exceptions[row[0]]
            
        val2 = value_mapping[row[1].strip()]

        url = f"https://www.metacritic.com/game/{val2}/{val1}"
        print(url)
        response = requests.get(url, allow_redirects=True, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")

        developer, genres, rating = [], [], []
        
        if response.status_code != 200:
            print("Error:", response.status_code)


            updated_row = row + [developer, genres, rating]
            writer.writerow(updated_row)
   
            continue
            
        genredetails = soup.find("li", {"class": "summary_detail product_genre"})
        
        # developerge = soup.find("li", {"class": "summary_detail developer"})
        # if developerge:
        #     dev_element_no_link = developerge.find("div", class_="data")
        #     if(dev_element_no_link):
        #         dev_element = developerge.find("span", class_="data").find("a")
        #         dev = dev_element.text.strip() if dev_element else dev_element_no_link.text.strip()

        #         developer.append(dev)
        
        ratingge = soup.find("li", {"class": "summary_detail developer"})
        if ratingge:
            ratingges = ratingge.find("a", class_="button")
            developer.append(ratingges.text.strip())
            # print type of ratingges.text.strip()
                    
        
        genresi = genredetails.find_all("span", class_="data")
        for genre in genresi:
            garr = genre.text.strip()
            genres.append(garr)
            
        ratingge = soup.find("li", {"class": "summary_detail product_rating"})
        if ratingge:
            ratingges = ratingge.find("span", class_="data")
            rating.append(ratingges.text.strip())
            # print type of ratingges.text.strip()
            print(type(ratingges.text.strip()))
            
            
    
        # print each value of sources and scores

        # for source, score in zip(sources, scores):
        #     print(source + ": " + str(score))
        
        # turn sources and scores into strings
        developer = ",".join(str(genre) for genre in developer)
        genres = ",".join(str(genre) for genre in genres)
        rating = ",".join(str(genre) for genre in rating)

        updated_row = row + [developer, genres, rating]
        writer.writerow(updated_row)
        i=i+1
        
        # if(i==5):
        #     break


        



