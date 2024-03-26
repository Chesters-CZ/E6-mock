# Step 1

 - Remove deleted tags
 - Extract **ALL** user ids including those, who uploaded or rated deleted posts 
 - Extract actually used tags
 - Extract post_tags

# Step 2 - uniq v linuxu

 - Uniq user IDs
 - Uniq tags

# Step 3 (load tags to memory)

 - Remove tag implications mentioning removed tags
 - Remove non-tag wikis
 - extract wiki examples

# Step 4

 - remove wiki examples with deleted posts

---

tbd

todo: limit comment scraping searches by date to limit scraping results under unknown posts 

---

# Notes:

 - more user ids can be extracted from wiki_pages.csv