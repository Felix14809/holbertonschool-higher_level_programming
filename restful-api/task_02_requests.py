#!/usr/bin/env python3
"""program that prints and saves responses"""
import requests
import csv

URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """Print the status code and the title of every post"""
    response = requests.get(URL)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        try:
            posts = response.json()
        except ValueError:
            return
        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """Save the id, title and body of every post to posts.csv"""

    response = requests.get(URL)
    if response.status_code == 200:
        try:
            posts = response.json()
            response_list = []
            for post in posts:
                response_list.append({
                    "id": post.get("id"),
                    "title": post.get("title"),
                    "body": post.get("body")
                })
        except ValueError:
            return
        with open("posts.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(response_list)
