import requests
import re
from bs4 import BeautifulSoup
import time


def get_username_from_user_id(user_id: int):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}
    response = requests.get('https://e926.net/users/' + str(user_id), headers=headers)
    return re.search("User - .* - e926", response.text.replace("\n", "")).group()[7:-7]


def get_user_favorites(user_id: int):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}
    response = requests.get('https://e621.net/favorites?user_id=' + str(user_id), headers=headers)
    raw_post_ids = re.findall("<article id=\".*?\"", response.text.replace("\n", ""))
    processed_post_ids = []
    for raw_post_id in raw_post_ids:
        processed_post_ids.append(raw_post_id[18:-1])
    return processed_post_ids


def get_user_comments(user_id: int):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}
    response = requests.get('https://e621.net/comments?group_by=comment&search%5Bcreator_id%5D=' + str(user_id),
                            headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    comments = soup.find_all("div", class_="comment-post")
    comments_out = []
    for comment in comments:
        try:
            comments_out.append([re.search("[0-9]+", re.search("id=\"post_[0-9]+\"", comment.__str__().replace("\n",
                                                                                                               "")).group().__str__()).group().__str__(),
                                 comment.findNext("div", class_="styled-dtext").text])
        except AttributeError:
            comments_out.append(["", comment.findNext("div", class_="styled-dtext").text])
    return comments_out


# TODO: implement blip scraping (https://e926.net/blips?commit=Search&search%5Bcreator_name%5D=<username>)

print(get_username_from_user_id(1376250))
time.sleep(0.5)
print(get_user_favorites(1005864))
time.sleep(0.5)
print(get_user_comments(81259))
