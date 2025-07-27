# Write a Python program to count the occurrences of each word in a given sentence

sentence = input("Enter a sentence: ")

#split sentences
words = sentence.split()

#empty dict to store word count
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1


print("Word Occurrences:")
for word, count in word_count.items():
    print(word, ":", count)
