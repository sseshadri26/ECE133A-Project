import csv
import re
import requests
from bs4 import BeautifulSoup
from collections import defaultdict

import sys
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

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
with open("all_games3.csv", "r+", encoding='utf-8') as file:
    reader = csv.reader(file)
    header = next(reader) + ["sources", "scores"]
    # Skip the first row (titles)

    data = [row for row in reader]


with open("updated_games_c.csv", "w", newline="", encoding='utf-8') as output_file:
    writer = csv.writer(output_file)
    writer.writerow(header)

    for row in data:
        sources = []
        scores = []
        
        print(row[0] + " " + row[1])
        
        val1 = re.sub(r" & ", "-", row[0])
        val1 = re.sub(r" / ", "-", val1)
        val1 = re.sub(r" : ", "-", val1)
        
        val1 = re.sub(r"[^a-zA-Z0-9!+-]+", "", val1.lower().replace(" ", "-"))
        if row[0] in exceptions:
            val1 = exceptions[row[0]]
            
        val2 = value_mapping[row[1].strip()]

        url = f"https://www.metacritic.com/game/{val2}/{val1}/critic-reviews"
        # print(url)
        response = requests.get(url, allow_redirects=True, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")

        if response.status_code != 200:
            print("Error:", response.status_code)
            sources = ",".join(str(source) for source in sources)
            scores = ",".join(str(score) for score in scores)
            # print(sources)
            # print(scores)

            updated_row = row + [sources, scores]
            writer.writerow(updated_row)
   
            continue
            
        body_product_reviews = soup.find("div", {"class": "body product_reviews"})
        if not body_product_reviews:
            print("No body_product_reviews found")

            sources = ",".join(str(source) for source in sources)
            scores = ",".join(str(score) for score in scores)
            # print(sources)
            # print(scores)

            updated_row = row + [sources, scores]
            writer.writerow(updated_row)
            continue
        review = body_product_reviews.find("li", class_="review critic_review first_review")
        
        if review:
            source = "No source"
            source_element_no_link = review.find("div", class_="source")
            if(source_element_no_link):
                source_element = review.find("div", class_="source").find("a")
                source = source_element.text.strip() if source_element else source_element_no_link.text.strip()
            grade_element = review.find("div", class_="review_grade").find("div", class_=re.compile("metascore_w.*"))
            grade = int(grade_element.text.strip()) if grade_element else None

            sources.append(source)
            scores.append(grade)
        else:
            print("No review found")
            # print("No scores found")

            sources = ",".join(str(source) for source in sources)
            scores = ",".join(str(score) for score in scores)

            updated_row = row + [sources, scores]
            writer.writerow(updated_row)
            continue
            
        reviews = body_product_reviews.find_all("li", class_="review critic_review")
        for review in reviews:
            source = "No source"
            source_element_no_link = review.find("div", class_="source")
            if(source_element_no_link):
                source_element = review.find("div", class_="source").find("a")
                source = source_element.text.strip() if source_element else source_element_no_link.text.strip()
            grade_element = review.find("div", class_="review_grade").find("div", class_=re.compile("metascore_w.*"))
            grade = int(grade_element.text.strip()) if grade_element else None
            
            sources.append(source)
            scores.append(grade)
            
        review = body_product_reviews.find("li", class_="review critic_review last_review")
        
        if review:
            source = "No source"
            source_element_no_link = review.find("div", class_="source")
            if(source_element_no_link):
                source_element = review.find("div", class_="source").find("a")
                source = source_element.text.strip() if source_element else source_element_no_link.text.strip()
            grade_element = review.find("div", class_="review_grade").find("div", class_=re.compile("metascore_w.*"))
            grade = int(grade_element.text.strip()) if grade_element else None

            sources.append(source)
            scores.append(grade)
        
        # print each value of sources and scores

        # for source, score in zip(sources, scores):
        #     print(source + ": " + str(score))
        
        # turn sources and scores into strings
        sources = ",".join(str(source) for source in sources)
        scores = ",".join(str(score) for score in scores)


        updated_row = row + [sources, scores]
        writer.writerow(updated_row)
        i=i+1


        

game_info = defaultdict(list)

with open("updated_games_c.csv", "r", encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # skip the header row
    for row in reader:
        name = row[0]
        platform = row[1]
        sources = row[2]
        scores = row[3]
        
        # Update the information for this game in the dictionary
        game_info[name].append([platform, sources, scores])

# Write the consolidated information to the updated_games file
with open("updated_games2_c.csv", "w", newline="", encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Platform", "Sources", "Scores"])
    for name, rows in game_info.items():
        platforms = ",".join([row[0] for row in rows])
        sources = ",".join([row[1] for row in rows])
        scores = ",".join([row[2] for row in rows])
        writer.writerow([name, platforms, sources, scores])
