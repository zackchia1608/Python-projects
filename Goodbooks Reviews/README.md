# Goodbook Reviews Kaggle Competition

---

## Goodreads Books Review Rating Prediction

Reviews are a good way to judge the quality of any product, whether it's books, clothes, technology, or anything else. When you want to buy something online these days, the first thing that comes to mind is the reviews from past buyers and the overall rating the product has received. Reader feedback, whether positive or negative, five stars or one star, will encourage the product owner to make improvements.

Reader connection and engagement will be encouraged by book reviews, whether they be left on Amazon, Goodreads, or social media. Readers must determine whether or not other readers are enjoying the book.

In this competition the purpose is to work with a challenging dataset consisting reviews from the Goodreads book review website, and a variety of attributes describing the items and to predict review rating which ranges from 0 to 5.

---

## Results

The review data is first processed through a transformer based sentiment analysis model to derive the sentiment of the review text, as well as the probability of the sentiment. The sentiment - Positive, Neutral, or Negative - is then mapped to an ordinal scale and multiplied by the probability to derive a sentiment score.

The review data is then tokenized and sequenced. At 80% quintile, the sentence length for each document is 319. Hence, to balance between training time and accuracy, sequences above 319 length were truncated to max 319 length. Post padding was used for sequences below 319.

The text data is then fed into a bidirectional LSTM layers first, before combining with the meta-data and processed through a hidden layer. The output shows a training accuracy score of 59%.

When test data was submitted to kaggle, the F1-score was 55.2%, which at the time of this writing, placed Top 20 on the leaderboard.
