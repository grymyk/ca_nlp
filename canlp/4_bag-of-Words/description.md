# Language Models: Bag-of-Words
How can we help a machine make sense of a bunch of word tokens? We can help computers make predictions about language by training a language model on a corpus (a bunch of example text).

Language models are probabilistic computer models of language. We build and use these models to figure out the likelihood that a given sound, letter, word, or phrase will be used. Once a model has been trained, it can be tested out on new texts.

One of the most common language models is the unigram model, a statistical language model commonly known as bag-of-words. As its name suggests, bag-of-words does not have much order to its chaos! What it does have is a tally count of each instance for each word. Consider the following text example:

![image](/canlp/4_bag-of-Words/bag-of-words.gif)

Provided some initial preprocessing, bag-of-words would result in a mapping like:

{"the": 2, "squid": 1, "jump": 1, "out": 1, "of": 1, "suitcase": 1}
 
Now look at this sentence and mapping: “Why are your suitcases full of jumping squids?”

{"why": 1, "be": 1, "your": 1, "suitcase": 1, "full": 1, "of": 1, "jump": 1, "squid": 1}
 
You can see how even with different word order and sentence structures, “jump,” “squid,” and “suitcase” are shared topics between the two examples. Bag-of-words can be an excellent way of looking at language when you want to make predictions concerning topic or sentiment of a text. When grammar and word order are irrelevant, this is probably a good model to use.

Instructions
1.
We’ve turned a passage from Through the Looking Glass by Lewis Carroll into a list of words (aside from stopwords, which we’ve removed) using nltk preprocessing. Run your code to see the full list.

2.
Now let’s turn this list into a bag-of-words using Counter()!

Comment out the print statement and set bag_of_looking_glass_words equal to a call of Counter() on normalized. Print bag_of_looking_glass_words. What are the most common words?

Hint
bag_of_looking_glass_words = Counter(normalized)

3.
Try changing text to another string of your choosing and see what happens!