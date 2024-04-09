import csv
import re
import sys
import time

import requests
import winsound


def load_csv(path, header_return, data_return, has_header):
    print("Loading " + path)
    with (open("D:\\velký dbs fily\\" + path, 'r', encoding="utf-8") as file_in):
        file_reader = csv.reader(file_in)

        print("0.0%", end="")
        lines = 0
        for line in file_reader:
            lines += 1
        file_in.seek(0)
        lines = (lines / 1000).__floor__()
        if lines == 0:
            lines = 1

        firstline = True
        for i, row in enumerate(file_reader):
            if i % lines == 0:
                print("\r" + (i / lines / 10).__str__() + "%", end="")

            if firstline:
                if has_header:
                    header_return.clear()
                    header_return.append(row)
                else:
                    data_return.append(row)
                firstline = False
                continue
            data_return.append(row)
    print("\nDone!\n")


def dump_database(dbs: list, header: list, filename: str):
    with open("D:\\velký dbs fily\\" + filename, "w", encoding="utf-8", newline="") as file_out:
        writer = csv.writer(file_out)
        writer.writerow(header)

        arrlen = (dbs.__len__() / 1000).__floor__()
        for i, row in enumerate(dbs):
            if i % arrlen == 0:
                print("\r" + (i / arrlen / 10).__str__() + "%", end="")
            writer.writerow(row)
    print("\nDone\n")


def dump_single_column_database(dbs: list, header: list, filename: str):
    with open("D:\\velký dbs fily\\" + filename, "w", encoding="utf-8", newline="") as file_out:
        writer = csv.writer(file_out)
        writer.writerow(header)

        arrlen = (dbs.__len__() / 1000).__floor__()
        for i, row in enumerate(dbs):
            if i % arrlen == 0:
                print("\r" + (i / arrlen / 10).__str__() + "%", end="")
            writer.writerow([row])
    print("\nDone\n")


def get_user_favorites(user_id: int):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}
    response = requests.get('https://e621.net/favorites?user_id=' + str(user_id), headers=headers)
    raw_post_ids = re.findall("<article id=\".*?\"", response.text.replace("\n", ""))
    processed_post_ids = []
    # fixme: does not detect captcha or invalid responses
    for raw_post_id in raw_post_ids:
        processed_post_ids.append(raw_post_id[18:-1])
    return processed_post_ids


maxInt = sys.maxsize

print("Increasing csv field size limit...")
while True:
    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt / 10)
        print(".", end="")

print("\nDone!\n")

print("\nWARNING: SCRIPT APPENDS TO step11\\favorites.csv AND WILL NOT REPLACE EXISTING DATA\n")

discard = []
already_scraped = []

load_csv("step11\\favorites.csv", discard, already_scraped, False)

already_scraped_ids = [favorite[0] for favorite in already_scraped if favorite[1] is not ""]
del already_scraped

raw_user_ids = []

load_csv("step9\\user_ids_unique.csv", discard, raw_user_ids, True)

user_ids_to_be_scraped = [uid for uid in raw_user_ids if uid not in already_scraped_ids]
del raw_user_ids
del already_scraped_ids

with open("D:\\velký dbs fily\\step11\\favorites.csv", mode="a", encoding="utf-8") as favorites_out:
    favorites_writer = csv.writer(favorites_out)

    linecount = (user_ids_to_be_scraped.__len__() / 1000).__floor__()
    for i, user in enumerate(user_ids_to_be_scraped):
        print(
            "\r Scraping user " + user + " (" + i.__str__() + "/" + user_ids_to_be_scraped.__len__().__str__() + " " + (
                    i / linecount / 10).__str__() + "%)", end="")

        try:
            user_favorites = get_user_favorites(user)
        except Exception as e:
            print("ERROR WHEN SCRAPING USERNAME OF USER " + user)
            print(e.__str__())
            break

        for user_favorite in user_favorites:
            favorites_writer.writerow([user, user_favorite])
        time.sleep(0.5)

print("\nDone!\n")

print("change the world;")
time.sleep(2)
print("my final message.")
time.sleep(3)
print("goodbye")
time.sleep(3)
winsound.PlaySound("./o95.wav", winsound.SND_FILENAME)
