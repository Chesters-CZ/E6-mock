import csv
import random
import sys
import time
import winsound
import hashlib


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

print("Increasing csv field size limit...")
while True:
    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt / 10)
        print(".", end="")
print("\nDone!\n")


users_raw = []
discard = []


load_csv("step10\\users.csv", discard, users_raw, False)

posts = []

load_csv("step7\\posts.csv", discard, posts, True)

print("Harvesting privileged user ids...")
privileged_users = [post[6] for post in posts if post[6] != ""]
print("Done!\n")

print("Harvesting post ids...")
post_ids = [post[0] for post in posts]
print("Done!\n")

del posts

users_parsed = []

linecount = (users_raw.__len__() / 1000).__floor__()
print("Generating user records...")
for i, row in enumerate(users_raw):
    if i % linecount == 0:
        print("\r" + (i / linecount / 10).__str__() + "%", end="")
    hash = hashlib.md5(str(row[1]).encode("utf-8")).hexdigest().__str__()
    users_parsed.append([row[0],
                         row[1],
                         hash,
                         random.choice(["Janitor", "Moderator", "Admin"]) if row[0] in privileged_users else "Member"])
print("\nDone!\n")

dump_database(users_parsed, ["id", "username", "password_hash", "role"], "step15\\user.csv")
del privileged_users

print("Harvesting user ids...")
user_ids = [user[0] for user in users_parsed]
print("Done!\n")

del users_parsed
del users_raw

blips = []

load_csv("step14\\blip_text_post.csv", discard, blips, False)

comments = []

load_csv("step13\\comments.csv", discard, comments, False)

print("Merging blips and comments into one...")
blips.append(comments)
print("Done!\n")

del comments

print("Harvesting text post ids")
text_post_ids = [blip[0] for blip in blips]
print("Done!\n")

dump_database(blips, ["id", "user", "content", "post"], "step15\\text_post.csv")
del blips

post_score = []

print("Generating post score...")
linecount = (text_post_ids.__len__() / 1000).__floor__()
for i, post in enumerate(text_post_ids):
    if i % linecount == 0:
        print("\r" + (i / linecount / 10).__str__() + "%", end="")

    score_chance = random.randint(0, 100) * 0.01 * 0.01 * 0.25

    negative_chance = random.randint(0, 100) * 0.01

    for user in user_ids:
        if random.random() < score_chance:
            post_score.append([user, post, "f" if random.random() < negative_chance else "t"])
print("\nDone!\n")
del post_ids

dump_database(post_score, ["user", "post", "is_like"], "step15\\post_score.csv")
del post_score

text_post_score = []

print("Generating text_post score")
linecount = (text_post_ids.__len__() / 1000).__floor__()
for i, post in enumerate(text_post_ids):
    if i % linecount == 0:
        print("\r" + (i / linecount / 10).__str__() + "%", end="")

    score_chance = random.randint(0, 100) * 0.01 * 0.01 * 0.25

    negative_chance = random.randint(0, 100) * 0.01

    for user in user_ids:
        if random.random() < score_chance:
            text_post_score.append([user, post, "f" if random.random() < negative_chance else "t"])
print("\nDone!\n")
del text_post_ids

dump_database(text_post_score, ["user", "text_post", "is_like"], "step15\\text_post_score.csv")

tags_raw = []

load_csv("step9\\tags_unique.csv", discard, tags_raw, False)

tags = [tag_raw[0] for tag_raw in tags_raw]
del tags_raw

blacklist = []

print("Generating blacklists...")
linecount = (user_ids.__len__() / 1000).__floor__()
for i, user in enumerate(user_ids):
    if i % linecount == 0:
        print("\r" + (i / linecount / 10).__str__() + "%", end="")

    for tag in tags:
        if random.random() < 0.00025:
            blacklist.append([tag, user])
print("\nDone!\n")

dump_database(blacklist, ["tag", "user"], "step15\\blacklist.csv")


print("\nDone!\n")

print("change the world;")
time.sleep(2)
print("my final message.")
time.sleep(3)
print("goodbye")
time.sleep(3)
winsound.PlaySound("./o95.wav", winsound.SND_FILENAME)
