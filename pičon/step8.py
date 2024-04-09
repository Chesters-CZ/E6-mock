import csv
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
        if header.__len__() > 0:
            writer.writerow(header)

        arrlen = (dbs.__len__() / 1000).__floor__()
        for i, row in enumerate(dbs):
            if i % arrlen == 0:
                print("\r" + (i / arrlen / 10).__str__() + "%", end="")
            writer.writerow([row])
    print("\nDone\n")


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

discard = []
post_tags = []
tags = []

load_csv("step7\\post_tags.csv", discard, post_tags, True)

linecount = (post_tags.__len__() / 1000).__floor__()
print("Picking tags from post_tags...")
for i, row in enumerate(post_tags):
    if i % linecount == 0:
        print("\r" + (i / linecount / 10).__str__() + "%", end="")
    tags.append(row[1])
del post_tags

wikis = []

load_csv("step6\\wikis.csv", discard, wikis, False)

linecount = (wikis.__len__() / 1000).__floor__()
print("Picking tags from wikis...")
for i, row in enumerate(wikis):
    if i % linecount == 0:
        print("\r" + (i / linecount / 10).__str__() + "%", end="")
    tags.append(row[0])
del wikis

wikis_raw = []

load_csv("step3\\wikis.csv", discard, wikis_raw, True)

print("Creating list of unused wikis...")
wikis_unused = [wiki for wiki in wikis_raw if wiki[0] not in tags]
del wikis_raw

print("Adding a random unused wiki to step6\\wikis")
with open("step6\\wikis.csv", mode="a", encoding="utf-8") as wikis_append:
    wikis_writer = csv.writer(wikis_append)
    wikis_writer.writerow(random.choice(wikis_unused))
del wikis_unused

tags_raw = []

load_csv("step2\\tags_unique.csv", discard, tags_raw, False)

print("Creating list of unused tags...")
tags_unused = [tag for tag in tags_raw if tag not in tags]
del tags_raw

print("Adding a random unused tag to tags")
tags.append(random.choice(tags_unused))
del tags_unused

print("Saving tags to step8\\extracted_tags.csv")
dump_single_column_database(tags, [], "step8\\extracted_tags.csv")
del tags

posts = []

load_csv("step8\\posts.csv", discard, posts, True)

print("Extracting user ids from chosen posts...")
user_ids = [post[3] for post in posts] + [post[6] for post in posts]
del posts

raw_user_ids = []

load_csv("step2\\user_ids_unique.csv", discard, raw_user_ids, False)

print("Adding random users to user ids")
user_ids.append(random.sample(raw_user_ids, (len(raw_user_ids) / 2).__floor__()))
del raw_user_ids

print("Saving user ids to step8\\user_ids.csv")
dump_single_column_database(user_ids, [], "step8\\user_ids.csv")

print("\nDone!\n")

print("change the world;")
time.sleep(2)
print("my final message.")
time.sleep(3)
print("goodbye")
time.sleep(3)
winsound.PlaySound("./o95.wav", winsound.SND_FILENAME)
