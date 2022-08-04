# Capstone Project: Choosing the best heroes to climb the rankings in Dota 2

## Problem Statement

<p style='text-align: justify;'>ESports, short for electronic sports has been a growing sport around the world and viewed by many around the world.  One popular esports game is Dota 2, a multiplayer online battle arena (MOBA) video game developed by Valve, with a huge prize pool of US$40m in 2021 for the Dota 2 world championship. This project will seek to create a predictive model to predict match wins before the start of the match by only looking at hero selection. This project will also seek to build a hero recommender system to recommend the best heroes to achieve the highest winning probability given the selection of heroes already chosen.

</p>

---

## Executive Summary

<div style='text-align: justify;'>

There are many factors which contribute to a match win success, one of which is team composition as having the right hero synergies within your team and picking heroes that counter opponent's heroes provides an implicit advantage to teams. As Dota 2 is a zero-sum game and is extremely competitive, every win percentage improvement over the opponent is significant. Hence, this project will use machine learning models to create a recommender system to recommend heroes given the current team and opponent's composition to maximise their winning chances.

Approximately 2.5 million rows of match data was scraped from the Open Dota 2 API. After filtering for high ranked matches and All Pick/All Draft game mode, approximately 77,000 rows of data was kept for training purposes. A reverse mapping of data was also done, where the team compositions for both sides were swapped and labels reversed in order to maximise the use of the data so as to take into consideration team compositions from both teams. The data was then fitted through several machine learning models and neural networks.

The results showed that the best model was the neural network model, with a 55.6% validation accuracy. This is to be expected as there are many other factors that contributes to a match win.

Using the model created, a heroku web app was deployed. The app uses a greedy algorithm to determine which heroes would be best chosen given the current teams compositions. The repository with the full code can be assessed separately at https://github.com/zackchia1608/Dota-2-Hero-Recommender-Demo. The link to the web app is: https://dota-2-hero-recommender.herokuapp.com/.

_Please note that it will take some time for the app to load initially._

</div>

---

## Requirements

- Python=3.8
- Pycaret[full]
- Tensorflow=2.9

---
