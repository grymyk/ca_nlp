# Topic Models
We’ve touched on the idea of finding topics within a body of language. But what if the text is long and the topics aren’t obvious?

Topic modeling is an area of NLP dedicated to uncovering latent, or hidden, topics within a body of language. For example, one Codecademy curriculum developer used topic modeling to discover patterns within Taylor Swift songs related to love and heartbreak over time.

A common technique is to deprioritize the most common words and prioritize less frequently used terms as topics in a process known as term frequency-inverse document frequency (tf-idf). Say what?! This may sound counter-intuitive at first. Why would you want to give more priority to less-used words? Well, when you’re working with a lot of text, it makes a bit of sense if you don’t want your topics filled with words like “the” and “is.” The Python libraries gensim and sklearn have modules to handle tf-idf.

Whether you use your plain bag of words (which will give you term frequency) or run it through tf-idf, the next step in your topic modeling journey is often latent Dirichlet allocation (LDA). LDA is a statistical model that takes your documents and determines which words keep popping up together in the same contexts (i.e., documents). We’ll use sklearn to tackle this for us.

If you have any interest in visualizing your newly minted topics, word2vec is a great technique to have up your sleeve. word2vec can map out your topic model results spatially as vectors so that similarly used words are closer together. In the case of a language sample consisting of “The squids jumped out of the suitcases. The squids were furious. Why are your suitcases full of jumping squids?”, we might see that “suitcase”, “jump”, and “squid” were words used within similar contexts. This word-to-vector mapping is known as a word embedding.

Instructions
1.
Check out how the bag of words model and tf-idf models stack up when faced with a new Sherlock Holmes text!

Run the code as is to see what topics they uncover…

2.
Tf-idf has some interesting findings, but the regular bag of words is full of words that tell us very little about the topic of the texts!

Let’s fix this. Add some words to stop_list that don’t tell you much about the topic and then run your code again. Do this until you have at least 10 words in stop_list so that the bag of words LDA model has some interesting topics.

Hint
Some words you may want to add to the stop_list:

"say", "see", "holmes", "shall", "say", 
"man", "upon", "know", "quite", "one", 
"well", "could", "would", "take", "may", 
"think", "come", "go", "little", "must", 
"look"
 