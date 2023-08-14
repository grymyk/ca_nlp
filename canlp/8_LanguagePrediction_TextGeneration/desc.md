Language Prediction & Text Generation
How does your favorite search engine complete your search queries? How does your phone’s keyboard know what you want to type next? Language prediction is an application of NLP concerned with predicting text given preceding text. Autosuggest, autocomplete, and suggested replies are common forms of language prediction.

Your first step to language prediction is picking a language model. Bag of words alone is generally not a great model for language prediction; no matter what the preceding word was, you will just get one of the most commonly used words from your training corpus.

If you go the n-gram route, you will most likely rely on Markov chains to predict the statistical likelihood of each following word (or character) based on the training corpus. Markov chains are memory-less and make statistical predictions based entirely on the current n-gram on hand.

For example, let’s take a sentence beginning, “I ate so many grilled cheese”. Using a trigram model (where n is 3), a Markov chain would predict the following word as “sandwiches” based on the number of times the sequence “grilled cheese sandwiches” has appeared in the training data out of all the times “grilled cheese” has appeared in the training data.

A more advanced approach, using a neural language model, is the Long Short Term Memory (LSTM) model. LSTM uses deep learning with a network of artificial “cells” that manage memory, making them better suited for text prediction than traditional neural networks.

Instructions
1.
Add three short stories by your favorite author or the lyrics to three songs by your favorite artist to document1.py, document2.py, and document3.py. Then run script.py to see a short example of text prediction.

Does it look like something by your favorite author or artist?

If you accidentally close one of the files, just click the file folder in the top left corner of the code editor to find the file and re-open it.

Hint
If you need some text to play around with, Project Gutenberg is an excellent resource.