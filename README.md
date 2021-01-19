"lucrat.net/blog" 

Script to scrape from https://blog.lucrat.net/. 

Notes:
- Date is formatted yy/mm/dd
- Articles appear in multiple categories, the one under 'category' is the one it was scraped from, any additional categories can be found under 'tags'

DB Schema:
- title: The title of the article
- date: The date of posting, formatted yy/mm/dd
- author: Author of the article
- category: Category of the article
- tags: all additional categories as well as any tags (can be empty)
- link: a link to the article
- content: all the text in the article
