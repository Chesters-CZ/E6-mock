import csv
import time
import sys
import numpy
import re

print("\nInitializing csv field size limit", end="")

maxInt = sys.maxsize

while True:
    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt / 10)
        print(".", end="")

print("\nDone!\n")

# loaded data
pools_header = []
posts_header = []
implications_header = []
#tags_header = []
wikis_header = []

pools = []
posts = []
implications = []
# tags = []
wikis = []

# generated data
users_header = ["id", "username", "password_hash", "role", "representing_image"]
parents_header = ["parent", "child"]
post_tags_header = ["post", "tag"]
tags_header = ["tag", "has_wiki"]
wiki_examples_header = ["tag", "post"]

users = []
user_ids = []
tags = []
tag_names = []
post_parents = []
post_tags = []
wiki_examples = []

# with open("D\\velký dbs fily\\zql_pools.sql", "w", encoding="utf-8", newline="") as pools_out:

print("Loading pools.csv")
with open("D:\\velký dbs fily\\pools.csv", 'r', encoding="utf-8") as pools_in:
    pools_reader = csv.reader(pools_in)

    print("0.0%", end="")
    for linecount, line in enumerate(pools_in):
        pass
    pools_in.seek(0)
    linecount = (linecount / 1000).__floor__()

    firstline = True
    for row in pools_reader:
        if firstline:
            pools_header.append(row)
            firstline = False
            continue
        pools.append(row)
        if pools_reader.line_num % linecount == 0:
            print("\r" + (pools_reader.line_num / linecount / 10).__str__() + "%", end="")
print("\nDone!\n")

print("Loading posts.csv")
with open("D:\\velký dbs fily\\posts.csv", encoding="utf-8") as posts_in:
    posts_reader = csv.reader(posts_in)

    print("0.0%", end="")
    for linecount, line in enumerate(posts_in):
        pass
    posts_in.seek(0)
    linecount = (linecount / 1000).__floor__()

    firstline = True
    for row in posts_reader:
        if firstline:
            posts_header.append(row)
            firstline = False
            continue
        posts.append(row)
        if posts_reader.line_num % linecount == 0:
            print("\r" + (posts_reader.line_num / linecount / 10).__str__() + "%", end="")
print("\nDone!\n")

print("Loading tag_implications.csv")
with open("D:\\velký dbs fily\\tag_implications.csv", encoding="utf-8") as implications_in:
    implications_reader = csv.reader(implications_in)

    print("0.0%", end="")
    for linecount, line in enumerate(implications_in):
        pass
    implications_in.seek(0)
    linecount = (linecount / 1000).__floor__()

    firstline = True
    for row in implications_reader:
        if firstline:
            implications_header.append(row)
            firstline = False
            continue
        implications.append(row)
        if implications_reader.line_num % linecount == 0:
            print("\r" + (implications_reader.line_num / linecount / 10).__str__() + "%", end="")
print("\nDone!\n")

# Not necessary, will be generated
#
# print("Loading tags.csv")
# with open("D:\\velký dbs fily\\tags.csv", encoding="utf-8") as tags_in:
#     tags_reader = csv.reader(tags_in)
#
#     print("0.0%", end="")
#     for linecount, line in enumerate(tags_in):
#         pass
#     tags_in.seek(0)
#     linecount = (linecount / 1000).__floor__()
#
#     firstline = True
#     for row in tags_reader:
#         if firstline:
#             tags_header.append(row)
#             firstline = False
#             continue
#         tags.append(row)
#         if tags_reader.line_num % linecount == 0:
#             print("\r" + (tags_reader.line_num / linecount / 10).__str__() + "%", end="")
# print("\nDone!\n")

print("Loading wiki_pages.csv")
with open("D:\\velký dbs fily\\wiki_pages.csv", encoding="utf-8") as wikis_in:
    wikis_reader = csv.reader(wikis_in)

    print("0.0%", end="")
    for linecount, line in enumerate(wikis_in):
        pass
    wikis_in.seek(0)
    linecount = (linecount / 1000).__floor__()

    firstline = True
    for row in wikis_reader:
        if firstline:
            wikis_header.append(row)
            firstline = False
            continue
        wikis.append(row)
        if wikis_reader.line_num % linecount == 0:
            print("\r" + (wikis_reader.line_num / linecount / 10).__str__() + "%", end="")
print("\nDone!\n")

print("Extracting post parent-child relationships and harvesting user IDs from posts")
arrlen = (posts.__len__() / 1000).__floor__()
parent_count = 0
for i, post in enumerate(posts):
    if i % arrlen == 0:
        print("\r" + (i / arrlen / 10).__str__() + "%", end="")

    # add parent - child relationship if exists and post not deleted
    if len(post[12]) > 0:
        post_parents.append([posts[12], posts[0]])
        parent_count += 1

    # add uploader to users
    user_ids.append(posts[1])

    # add approver if exists
    if len(post[14]) > 0:
        user_ids.append(post[14])
print("\nDone, extracted " + post_parents.__len__().__str__() + " post parent-child relationships and " +
      user_ids.__len__().__str__() + " user IDs of which " + numpy.unique(
    numpy.array(user_ids)).__len__().__str__() + " were unique\n")

print("Removing deleted posts")
arrlen = (posts.__len__() / 1000).__floor__()
removed = 0
for i, post in enumerate(posts):
    if i % arrlen == 0:
        print(
            "\r" + (i / arrlen / 10).__str__() + "% (" + i.__str__() + " / " + (arrlen * 1000).__str__() + ")",
            end="")
    if post[20] == "t":
        posts.remove(post)
        removed += 1
print("\nDone, removed " + removed.__str__() + " entries.\n")

print("Harvesting tags and extracting post-tag relationships")
arrlen = (posts.__len__() / 1000).__floor__()
for i, post in enumerate(posts):
    if i % arrlen == 0:
        print(
            "\r" + (i / arrlen / 10).__str__() + "% (" + i.__str__() + " / " + (arrlen * 1000).__str__() + ")",
            end="")

    temp_tags = post[8].split(" ")

    for tag in temp_tags:
        tag_names.append(tag)
        post_tags.append([post[0], tag])
print("\nDone, found " + numpy.unique(numpy.array(tag_names)).__len__().__str__() + " tags and " + str(len(post_tags)) +
      " post-tag relationships\n")

print("Creating tag entries")
arrlen = (tag_names.__len__() / 1000).__floor__()
for i, tag_name in enumerate(tag_names):
    if i % arrlen == 0:
        print("\r" + (i / arrlen / 10).__str__() + "%", end="")
    haswiki = False
    for wiki in wikis:
        if wiki[3] == tag_name:
            haswiki = True
            break
    tags.append([tag_name, haswiki])
print("Done, created " + tags.__len__().__str__() + " tag entries")

# redundant, because tags have been extracted from posts, none are unused
#
# print("Removing tags with no posts")
# arrlen = (tags.__len__() / 1000).__floor__()
# removed = 0
# for i, row in enumerate(tags):
#     if row[3] == "0":
#         tags.remove(row)
#         removed += 1
#     if i % arrlen == 0:
#         print("\r" + (i / arrlen / 10).__str__() + "% (" + i.__str__() + " / " + (arrlen * 1000).__str__() + ")",
#               end="")
# print("\nDone, removed " + str(removed) + " entries.\n")

print("Removing inactive implications and entries with removed tags")
arrlen = (implications.__len__() / 1000).__floor__()
removed_inactive = 0
removed_removed = 0
for i, row in enumerate(implications):
    if i % arrlen == 0:
        print("\r" + (i / arrlen / 10).__str__() + "%", end="")

    # remove inactive implications
    if row[4] != "active":
        implications.remove(row)
        removed_inactive += 1
        continue

    # remove implications mentioning nonexistent tags
    remove = True
    for tag in tags:
        if row[1] == tag[1] or row[2] == tag[1]:
            remove = False
    if remove:
        implications.remove(row)
        removed_removed += 1
        continue
print("\nDone, removed " + str(removed_inactive + removed_removed) + " entries of which " + str(
    removed_inactive) + " were inactive and " + str(removed_removed) + " mentioned removed tags\n")

print("Removing non-tag wikis and extracting wiki_examples")
arrlen = (wikis.__len__() / 1000).__floor__()
removed = 0
for i, wiki in enumerate(wikis):
    if i % arrlen == 0:
        print("\r" + (i / arrlen / 10).__str__() + "%", end="")

    for tag in tags:
        if wiki[3] == tag[1]:
            thumbs = re.findall("thumb #[0-9]+", wiki[4])
            for thumb in thumbs:
                wiki_examples.append([tag[1], re.match("[0-9]+", thumb)])
            continue
    wikis.remove(wiki)
    removed += 1
print("\nDone, removed " + str(removed) + " entries.\n")

# with open("D:\\velký dbs fily\\zql_tag_implications.sql", "w", encoding="utf-8", newline="") as implications_out:
#     with open("D:\\velký dbs fily\\tag_implications.csv", encoding="utf-8") as implications_in:
#         implications_reader = csv.reader(implications_in)
#         firstline = True
#         for row in implications_reader:
#             if firstline:
#                 implications_out.write("INSERT INTO TAG_IMPLICATIONS (TAG, IMPLIES) VALUES ")
#                 print("-- READING TAG IMPLICATIONS --")
#                 firstline = False
#             else:
#                 if row[4] == "active":
#                     implications_out.write("( \"" + row[1] + "\", \"" + row[2] + "\" ), ")
#                 else:
#                     print("SKIPPING TAG IMPLICATION: " + row.__str__().encode(encoding="utf-8", errors="ignore").__str__())
#
# with open("D:\\velký dbs fily\\zql_tags.sql", "w", encoding="utf-8", newline="") as tags_out:
#     tags_writer = csv.writer(tags_out)
#     with open("D:\\velký dbs fily\\tags.csv", encoding="utf-8") as tags_in:
#         tags_reader = csv.reader(tags_in)
#         firstline = True
#         for row in tags_reader:
#             if firstline:
#                 tags_writer.writerow([row[0], row[1]])
#                 print("-- READING TAGS --")
#                 firstline = False
#             else:
#                 if row[3] != "0":
#                     tags_writer.writerow([row[0], row[1]])
#                 else:
#                     print("SKIPPING TAG: " + row.__str__().encode(encoding="utf-8", errors="ignore").__str__())
