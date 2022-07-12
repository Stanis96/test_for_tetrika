from bs4 import BeautifulSoup

import requests


main_url = "https://ru.wikipedia.org"
url = "https://ru.wikipedia.org/w/index.php?title=Категория%3AЖивотные_по_алфавиту&from=А"


def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except (requests.RequestException, ValueError):
        print("Error")
        return False


def get_all_animal_names(url):
    all_animal_range = [chr(i) for i in range(ord("А"), ord("А") + 32)]
    animal_dict = {i: 0 for i in all_animal_range}
    while True:
        html = get_html(url)
        soup = BeautifulSoup(html, "html.parser")
        all_animal_names = soup.find("div", class_="mw-category mw-category-columns").find_all("li")
        next_page = main_url + soup.find("a", text="Следующая страница").get("href")
        url = next_page
        for animal in all_animal_names:
            if animal.text[0] in animal_dict.keys():
                animal_dict[animal.text[0]] += 1
            elif animal.text[0] == "A":
                return animal_dict


if __name__ == "__main__":
    answer = get_all_animal_names(url)
    for key, value in answer.items():
        if value == 0:
            del value
        else:
            print(f"{key}:{value}")
