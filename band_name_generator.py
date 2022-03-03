from random import random
import wikipedia as wiki


random_article = wiki.random(pages=1)

# If it starts with a year, draw another article
if random_article[0:3].isnumeric():
    random_article = wiki.random(pages=1)

# If it's a list, remove "List of"
if (random_article.startswith("List of")):
    random_article = random_article.replace("List of", "").strip()

# This is to eliminate location names
comma_index = random_article.find(",")
if (comma_index != -1):
    random_article = random_article[:comma_index]

# What band name has something in parantheses?
paranthesis_index = random_article.find("(")
if (paranthesis_index != -1):
    random_article = random_article[:paranthesis_index]

print(random_article.title())


"""
Stuff to add:
- Human name detection
- Eliminate long names
"""