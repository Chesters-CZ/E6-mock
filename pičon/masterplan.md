# Preparing consistent data to select from

## Step 1

 - Remove deleted posts
 - Extract **ALL** user ids including those, who uploaded or rated deleted posts 
 - Extract actually used tags
 - Extract post_tags
 - Extract post parents
   - (used only to speed up step 7)

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

## Step 5 - pools_final, pool_posts_final

 - choose pools
 - extract pool_posts mentioning existing posts
 - add one empty pool

## Step 6 - wikis_final, wiki_examples_final

 - choose random wikis
 - create final version of wiki_examples

## Step 7, the destroyer of RAM - posts_final, post_tags_final

 - cherry-pick posts used in wiki_examples_final and pool_posts_final
 - add random posts
 - add families of all posts
 - match chosen posts to post_tags

## Step 8 - tags_final, user_ids_final

 - extract used tags from post tags
 - add a wiki of unused tags
 - extract used tags from wikis
 - add unused tag and dump to disk
 - extract user ids from posts

## Step 9 - uniq v linuxu 2

 - uniq tags
 - uniq user ids

---

# Scraping data

## Step 10 - scrape usernames

 - only scrape if username not already scraped

## Step 11 - scrape favorites

 - only scrape if username's favorites not already scraped

## Step 12 - scrape comments 

## Step 13 - favorites_final, comments_final

 - remove favorites with nonexistent posts
 - remove comments under nonexistent posts

## Step 14 - scrape blips (blips_final)

 - only scrape if username's blips not already scraped

---

# Generating data

## Step 15 - blacklist_final, text_post_final, text_post_score, post_score, users_final

 - generate random blacklists
 - merge blips and comments to text_post_final
 - generate text post score
 - generate post score
 - generate user password hashes, assign roles

 

---

## Notes:

 - more user ids can be extracted from wiki_pages.csv
 - after finishing, check count of text_post entries