import os
import time
import requests

page_dir=os.path.join(os.getcwd(), 'pages')
review_url_template="https://www.rottentomatoes.com/m/star_wars_the_last_jedi/reviews/?page={page}&type=user&sort="
starting_page=1
ending_page=51

if not os.path.isdir(page_dir):
    os.mkdir(page_dir)

print("Saving to {}".format(page_dir))
for page in range(starting_page, ending_page+1):
    print("Downloading page {}".format(page))
    review_url = review_url_template.format(page=page)
    page_file = os.path.join(page_dir, "{}.html".format(page))
    r = requests.get(review_url)
    with open(page_file, "wb") as f:
        f.write(r.content)
    time.sleep(2)
