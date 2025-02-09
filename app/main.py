"""
from db.vector import Vectorize

obj = Vectorize()

url_list = [
    "https://www.mongodb.com/docs/manual/core/databases-and-collections/",
    "https://www.webmd.com/add-adhd/adhd-adults",
    "https://www.geeksforgeeks.org/nodejs/?ref=shm",
]
#obj.client_setup()
obj.chunker(urls=url_list)

flag = obj.store()

if flag:
    print("Embedding & storage done")
else:
    print("Operation Failed")
"""

from bot.query import Bot

obj = Bot()

obj.retrieval()

query = input("User query :- ")

answer = obj.response(query=query)

print(answer)