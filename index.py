# Task 1: Keyword Highlighter

# Write a program that searches through a series of product reviews for keywords such as "good", "excellent", "bad", "poor", and "average". Print out each review with the keywords in uppercase so they stand out.
# reviews = [
#     "This product is really good. I'm impressed with its quality.",
#     "The performance of this product is excellent. Highly recommended!",
#     "I had a bad experience with this product. It didn't meet my expectations.",
#     "Poor quality product. Wouldn't recommend it to anyone.",
#     "The product was average. Nothing extraordinary about it."
# ]
reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]
# "excellent", "bad", "poor", and "average". 
for r in reviews:
    if "bad" in r:
        modified_review= r.replace("bad","BAD")
        print(modified_review)
    elif "excellent" in r:
        modified_review= r.replace("excellent","EXCELLENT")
        print(modified_review)
    elif "poor" in r:
        modified_review=r.replace("poor","POOR")
        print(modified_review)
    elif "average" in r:
        modified_review=r.replace("average","AVERAGE")
        print(modified_review)
   
# Task 2: Sentiment Tally

# Develop a function that tallies the number of positive and negative words in each review. Use a predefined list of positive and negative words to check against. The function should return the count of positive and negative words for each review.
# positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
# negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]

negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def sentiment_tally(review):
    pass
    positive_count=0
    negative_count=0

    words = review.split()
    for word in words:
        if word in positive_words:
            positive_count += 1
        elif word in negative_words:
            negative_count -= 1
    return positive_count, negative_count

sentiment_tally()


# Task 3: Review Summary

# Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. Ensure that the summary does not cut off in the middle of a word.

def generate_summary():
    customer_review=input("Write your review below: ")
    first_30 = customer_review[:31]
#need help!!!!



