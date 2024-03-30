# Preparing consistent data to select from

## Step 1

 - Remove deleted posts
 - Extract **ALL** user ids including those, who uploaded or rated deleted posts 
 - Extract actually used tags
 - Extract post_tags

## Step 2 - uniq v linuxu

 - Uniq user IDs
 - Uniq tags

## Step 3 (load tags to memory)

 - Remove tag implications mentioning removed tags
 - Remove non-tag wikis
 - extract wiki examples

## Step 4

 - remove wiki examples with deleted posts

---

# Selecting data

# Step 5 - pools_final, pool_posts_final

 - choose pools
 - extract pool_posts mentioning existing posts
 - add one empty pool

# Step 6 - wikis_final, wiki_examples_final

 - choose random wikis
 - create final version of wiki_examples

tbd

todo: limit comment scraping searches by date to limit scraping results under unknown posts 

---

## Notes:

 - more user ids can be extracted from wiki_pages.csv