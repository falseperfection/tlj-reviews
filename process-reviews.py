import glob
import os
from bs4 import BeautifulSoup

page_dir = os.path.join(os.getcwd(), 'pages')

rating_distribution = [0] * 11
total_reviews = 0
review_sum = 0

for page_file in glob.glob(os.path.join(page_dir, '*')):
    print("Processing file {}".format(page_file))
    with open(page_file, encoding = "ISO-8859-1") as f:
        soup = BeautifulSoup(f, 'html.parser')
        table = soup.find('div', { 'class' : 'review_table' })
        for review in table.find_all('div', {'class': 'review_table_row'}):
            rating = 0
            rating_section = review.find('span', {'class': 'fl'})
            if not rating_section:
                # "Want to see it" reviews don't have stars
                continue
            stars = rating_section.find_all('span', {'class': 'glyphicon-star'})
            star_count = len(stars)
            if rating_section.text == ' ½':
                star_count += 0.5
            rating = int(star_count * 2) # normalize to 10
            # print(rating)
            total_reviews += 1
            review_sum += rating
            rating_distribution[rating] += 1

print(total_reviews)
print(review_sum / total_reviews)
print(rating_distribution)
