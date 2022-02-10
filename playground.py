"""Playground for Programming Exercise"""
# Andreas Loutzidis

import requests
from bs4 import BeautifulSoup
from collections import Counter

def main():
    urls = [
        "https://innospot.de/en",
        "https://www.konux.com/",
        "https://techcrunch.com/",
        "https://www.telekom.com/en",
        "https://www.commerzbank.de/portal/en/englisch/english.html"
    ]

    for i in range(len(urls)):    
        flag = False
        page = requests.get(urls[i])
        if page.status_code != 200:
            print("The website {} does not allow web scraping.".format(urls[i]))
            flag = True
        if flag == False:
            soup = BeautifulSoup(page.content, 'html.parser')
            soup.select("html body")[0].get_text()
            data_set = soup.select("html body")[0].get_text()
            split_it = data_set.split()
            counter = Counter(split_it)
            most_occur = counter.most_common(10)
            least_occur = counter.most_common()[:-11:-1]
            n = 10
            print("The {} most common keywords in website {} are:\n".format(n, urls[i]))
            for i in range(10):
                print(most_occur[i][0])
            print("\n The {} least common keywords in the same website are:\n".format(n))
            for i in range(10):
                print(least_occur[i][0])

if __name__ == "__main__":
    main()
