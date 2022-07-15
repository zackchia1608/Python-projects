# Project 3 Natural Language Processing

## Problem Statement

<div style="text-align: justify">Our company is currently building a new wellness and mindfulness app to help promote better mental health. The app aims to provide thought of the day based on natural philosophies such as Buddhism and Stoicism. As a start, everyday, the app will allow the user to write one sentence against a prompt on certain topics. The app will then assess if the user is more in line with Buddhist or Stoic philosophies, and in return decide to return either Buddhist advice or Stoic advice based on the prompt written.

To train the app to gain an understanding of the types of people who will be more aligned with Buddhist or Stoic philosophies, we will be using posts from the subreddits r/Buddhism and r/Stoicism to machine train our model to distinguish and classify posts from the different subreddits.

---

## Technologies

Python 3.9.7<br>
GenSim Model

---

## Executive Summary

Both Buddhism and Stoicism have many things in common and helps people live better lives. Stoicism and Buddhism both deal with suffering by understanding its role in life and making peace with it. Studies have also shown that having mindfulness and meditation are beneficial to a person's mental health. Hence, we hope that an app that encourages users to abide by either philosophy depending on their alignment will help improve their mental health wellness.

To get a sense of the types of people and topics that people have gravitated towards for either philosophies, we used the Reddit API to scrape ~10,000 posts each from both r/Buddhism and r/Stoicism subreddits as data and apply machine training modelling to allow the app to possibly distinguish the similarities and differences between the types of users who browse such subreddits.

We used several classification models, of which Logistic Regression Modelling gave us the highest accuracy on our test data, with an accuracy score of 92.18%.

Our topic modelling results show that users who frequent the subreddits are intellectually curious who seek help from the various philosophies to apply to their life circumstances. Another subset of users are people who are facing difficulties in their lives and are seeking advice.

There are however differences between the various users. Stoic subreddit users tend to focus on Control and Positive Thinking while Buddhist subreddit users tend to focus on Meditation and Rituals.
Buddhism subreddit users are also less verbose versus Stoic users, and have a tendency to focus on religion compared to Stoicism users. Lastly, Buddhism subreddit users are more outward looking, and more ‘general’ in their thinking. Stoic users are more introspective and personal, focusing on one’s own circumstances. </div>

# Datasets

- ['subreddit_posts_preprocessed'](./subreddit_posts_preprocessed.csv): Subreddit Posts
  Preprocessed <br>
  <br>

# Data Dictionary

| Feature    | Type  | Datasets(s)                  | Value(s)            | Description                                  |
| ---------- | ----- | ---------------------------- | ------------------- | -------------------------------------------- |
| subreddit  | _str_ | subreddit_posts_preprocessed | Buddhism / Stoicism | Subreddit classification of post             |
| title      | _str_ | subreddit_posts_preprocessed | -                   | Title of post from subreddit                 |
| selftext   | _str_ | subreddit_posts_preprocessed | -                   | Text Description of subreddit posts (if any) |
| clean_text | _str_ | subreddit_posts_preprocessed | -                   | Preprocessed title and selftext              |
