import requests
import re


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


print(get_username_from_user_id(1376250))
print(get_user_favorites(1005864))
