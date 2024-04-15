import csv
import re
import sys
import time

import requests
import winsound
from bs4 import BeautifulSoup


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


def get_user_comments(user_id: int):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}
    response = requests.get('https://e621.net/comments?group_by=comment&search%5Bcreator_id%5D=' + str(user_id),
                            headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    comments = soup.find_all("div", class_="comment-post")
    comments_out = []
    # fixme: does not detect captcha or invalid response
    for comment in comments:
        try:
            comment_inner = comment.find_all("div", class_="comments list-of-comments")
            comments_out.append([comment_inner[0].findChildren()[0]["data-comment-id"],
                                 user_id,
                                 comment_inner[0].findChildren()[12].text,
                                 comment_inner[0].findChildren()[0]["data-post-id"]])
        except AttributeError:
            pass

    return comments_out


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

print("\nWARNING: SCRIPT APPENDS TO step12\\comment_text_post.csv AND WILL NOT REPLACE EXISTING DATA\n")

discard = []
already_scraped = []

load_csv("step12\\comment_text_post.csv", discard, already_scraped, False)

already_scraped_ids = [comment[1] for comment in already_scraped]
del already_scraped

raw_user_ids = []

load_csv("step9\\user_ids_unique.csv", discard, raw_user_ids, True)

# todo: check if this works
user_ids_to_be_scraped = [uid for uid in raw_user_ids if uid[0] not in already_scraped_ids]
del raw_user_ids
del already_scraped_ids

with open("D:\\velký dbs fily\\step12\\comment_text_post.csv", mode="a", encoding="utf-8", newline="") as favorites_out:
    favorites_writer = csv.writer(favorites_out)

    linecount = (user_ids_to_be_scraped.__len__() / 1000).__floor__()
    for i, user in enumerate(user_ids_to_be_scraped):
        start_time = time.time()
        print(
            "\r Scraping user " + user[
                0] + " (" + i.__str__() + "/" + user_ids_to_be_scraped.__len__().__str__() + " " + (
                    i / linecount / 10).__str__() + "%)", end="")

        try:
            comments = get_user_comments(user[0])
        except Exception as e:
            print("ERROR WHEN SCRAPING COMMENTS OF USER " + user[0])
            print(e.__str__())
            break

        print(" " + comments.__len__().__str__() + " found in " + (time.time() - start_time).__str__() + "s",
              end="")

        for comment in comments:
            favorites_writer.writerow(comment)
        time.sleep(0.5)

print("\nDone!\n")

print("change the world;")
time.sleep(2)
print("my final message.")
time.sleep(3)
print("goodbye")
time.sleep(3)
winsound.PlaySound("./o95.wav", winsound.SND_FILENAME)
