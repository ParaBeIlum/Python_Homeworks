with open('dataset_3363_3 (2).txt') as f:
    text = f.read().lower().split()
popular_word = max(set(text), key=text.count)
print(popular_word, text.count(popular_word))