import csv
import os
import random
import sys
import time
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


maxInt = sys.maxsize

post_count = 5000

print("Increasing csv field size limit...")
while True:
    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt / 10)
        print(".", end="")

print("\nDone!\n")

with open("D:\\velký dbs fily\\step7\\.unfinished", "w", encoding="utf-8", newline="") as unfinished:
    pass;

posts = []  #
pool_posts = []  #
post_parents = []  #
wiki_examples = []  #

post_tags = []
chosen_posts = []

posts_header = []
discard = []

load_csv("step6\\wiki_examples.csv", discard, wiki_examples, False)
load_csv("step5\\pool_posts.csv", discard, pool_posts, True)
load_csv("step1\\posts.csv", posts_header, posts, True)
load_csv("step1\\post_parents.csv", discard, post_parents, True)

linecount = (pool_posts.__len__() / 1000).__floor__()
print("Picking posts from pool_posts...")
for i, row in enumerate(pool_posts):
    if i % linecount == 0:
        print("\r" + (i / linecount / 10).__str__() + "%", end="")
    for post in posts:
        if post[0] == row[1]:
            chosen_posts.append([post[0], post[3], post[2], post[1], post[12], post[5], post[14]])
            temp_tags = post[8].split(" ")
            for tag in temp_tags:
                post_tags.append([post[0], tag])
            posts.remove(post)
            break
print("\nDone!\n")

del pool_posts

linecount = (wiki_examples.__len__() / 100).__floor__()
print("Picking posts from wiki_examples...")
for i, row in enumerate(wiki_examples):
    if i % linecount == 0:
        print("\r" + (i / linecount / 1).__str__() + "%", end="")
    for post in posts:
        if post[0] == row[1]:
            chosen_posts.append([post[0], post[3], post[2], post[1], post[12], post[5], post[14]])
            temp_tags = post[8].split(" ")
            for tag in temp_tags:
                post_tags.append([post[0], tag])
            posts.remove(post)
            break
print("\nDone!\n")

del wiki_examples

print("Adding random posts...")
random_posts = random.sample(posts, post_count)
linecount = (random_posts.__len__() / 1000).__floor__()
for i, row in enumerate(random_posts):
    if i % linecount == 0:
        print("\r" + (i / linecount / 10).__str__() + "%", end="")
    chosen_posts.append([row[0], row[3], row[2], row[1], row[12], row[5], row[14]])
    temp_tags = row[8].split(" ")
    for tag in temp_tags:
        post_tags.append([row[0], tag])
    posts.remove(row)
print("\nDone!\n")

del random_posts

print("Adding posts' parents...")
linecount = (chosen_posts.__len__() / 1000).__floor__()
pass_count = 1
while True:
    found_new = False
    # take every chosen post, check if there is a post_parent mentioning it. if there is, add the other post
    # do this until you go through all chosen posts without adding any
    for i, final_post in enumerate(chosen_posts):
        if i % linecount == 0:
            print("\r" + (
                    i / linecount / 10).__str__() + "% (pass #" + pass_count.__str__() + ", will " + (
                      "not " if not found_new else "") + "repeat)",
                  end="")

        for post_parent in post_parents:
            if final_post[0] == post_parent[0] or final_post[0] == post_parent[1]:
                for post in posts:
                    if post[0] == post_parent[0] or post[0] == post_parent[1]:
                        chosen_posts.append([post[0], post[3], post[2], post[1], post[12], post[5], post[14]])
                        temp_tags = post[8].split(" ")
                        for tag in temp_tags:
                            post_tags.append([post[0], tag])
                        posts.remove(post)
                        post_parents.remove(post_parent)
                        found_new = True
                        break
    pass_count += 1
    if not found_new:
        break
print("\nDone!\n")

print("Dumping posts to file...")
dump_database(chosen_posts, ["id", "file", "upload_date", "uploader", "parent", "rating", "verified_by"],
              "\\step7\\posts.csv")
del chosen_posts

print("Dumping post_tags to file...")
dump_database(post_tags, ["post", "tag"], "\\step7\\post_tags.csv")
del post_tags

print("Dumping unused posts to file...")
dump_database(posts, posts_header, "\\step7\\unused_posts.csv")
del posts

os.remove("D:\\velký dbs fily\\step7\\.unfinished")

print("change the world;")
time.sleep(2)
print("my final message.")
time.sleep(3)
print("goodbye")
time.sleep(3)
winsound.PlaySound("./o95.wav", winsound.SND_FILENAME)
