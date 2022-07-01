import requests
from bs4 import BeautifulSoup
from win10toast_click import ToastNotifier
import pandas as pd
import re

toast = ToastNotifier()

newsTitle = []
newsLabel = []


def toast_notification(title: str, msg: str):
    toast.show_toast(title, msg, duration=30)


def get_soup(url: str):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding": "gzip, deflate",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT": "1",
               "Connection": "close", "Upgrade-Insecure-Requests": "1"}
    html_parser = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html_parser, "html.parser")
    data = soup.find_all("h3", class_="entry-title mh-loop-title")
    return data


def clean_data(data):
    for i in data:
        try:
            title = i.text
            title = re.sub(r'\W+', " ", title)
            title = title.strip()
            label = title.split()[0]
            title = re.sub(label, "", title)
            newsTitle.append(title)
            newsLabel.append(label)
        except:
            continue


if __name__ == "__main__":
    for i in range(1, 500):
        soup = get_soup(f"https://turnbackhoax.id/page/{i}/")
        print(f"Getting page {i}")
        clean_data(soup)

    headline = {"title": newsTitle, "label": newsLabel}
    df = pd.DataFrame(headline, columns=["title", "label"])
    print(df.head(5))
    df.to_csv(r"headline_data.csv", header=True, index=False)
    print('Fin.')
    toast_notification("Notification", "sudah selesai")
