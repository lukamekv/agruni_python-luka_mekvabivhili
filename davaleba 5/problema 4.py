from functools import reduce

sentence = "Data Science is fun and Data Analysis is powerful if data is understood well."

# 1
words = sentence.split()

# 2
lowercase_words = list(map(lambda w: w.lower(), words))

# 3
word_count = reduce(
    lambda acc, word: {**acc, word: acc.get(word, 0) + 1},
    lowercase_words,
    {}
)

# 4
most_frequent = max(word_count.items(), key=lambda x: x[1])[0]
max_count = max(word_count.values())
all_most_frequent = [w for w, c in word_count.items() if c == max_count]

# 5
long_words = list(filter(lambda w: len(w) > 3, lowercase_words))


print("1) სიტყვები:", words)
print("2) პატარა ასოებით:", lowercase_words)
print("3) სიხშირე:", word_count)
print("4) ყველაზე ხშირი:", all_most_frequent)
print("5) 3+ ასოთი:", long_words)