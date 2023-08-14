# Language Models: N-Gram and NLM
For parsing entire phrases or conducting language prediction, you will want to use a model that pays attention to each word’s neighbors. Unlike bag-of-words, the n-gram model considers a sequence of some number (n) units and calculates the probability of each unit in a body of language given the preceding sequence of length n. Because of this, n-gram probabilities with larger n values can be impressive at language prediction.

Take a look at our revised squid example: “The squids jumped out of the suitcases. The squids were furious.”

A bigram model (where n is 2) might give us the following count frequencies:

{('', 'the'): 2, ('the', 'squids'): 2, ('squids', 'jumped'): 1, ('jumped', 'out'): 1, ('out', 'of'): 1, ('of', 'the'): 1, ('the', 'suitcases'): 1, ('suitcases', ''): 1, ('squids', 'were'): 1, ('were', 'furious'): 1, ('furious', ''): 1}
 
There are a couple problems with the n gram model:

How can your language model make sense of the sentence “The cat fell asleep in the mailbox” if it’s never seen the word “mailbox” before? During training, your model will probably come across test words that it has never encountered before (this issue also pertains to bag of words). A tactic known as language smoothing can help adjust probabilities for unknown words, but it isn’t always ideal.

For a model that more accurately predicts human language patterns, you want n (your sequence length) to be as large as possible. That way, you will have more natural sounding language, right? Well, as the sequence length grows, the number of examples of each sequence within your training corpus shrinks. With too few examples, you won’t have enough data to make many predictions.

Enter neural language models (NLMs)! Much recent work within NLP has involved developing and training neural networks to approximate the approach our human brains take towards language. This deep learning approach allows computers a much more adaptive tack to processing human language. Common NLMs include LSTMs and transformer models.

Instructions
1.
If you run the code, you’ll see the 10 most commonly used words in Through the Looking Glass parsed with NLTK’s ngrams module — if you’re thinking this looks like a bag of words, that’s because it is one!

2.
What do you think the most common phrases in the text are? Let’s find out…

Where looking_glass_bigrams is defined, change the second argument to 2 to see bigrams. Change n to 3 for looking_glass_trigrams to see trigrams.

Hint
The ngrams() function takes two arguments: the text you want to use and the n value.

3.
Change n to a number greater than 3 for looking_glass_ngrams. Try increasing the number.

At what n are you just getting lines from poems repeated in the text? This is where there may be too few examples of each sequence within your training corpus to make any helpful predictions.