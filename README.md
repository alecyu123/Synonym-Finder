# Synonym-Finder

# Natural Language Processing Intelligent System that can learn to find the most appropriate synonym from a list of words for a certain word input.

# In order to answer this question, it will approximate the semantic similarity using an n-dimension vector space and compute the cosine similarity of two word vectors. These word vectors are described by a semantic descriptor consisting of a dictionary of words that are in the same sentence as the base word.

# For example, in the following text: I am a sick man. I am a spiteful man. I am an unattractive man. I believe my liver is diseased.

# The word “man” only appears in the first three sentences. Its semantic descriptor vector would be: {"i": 3, "am": 3, "a": 2, "sick": 1, "spiteful": 1, "an": 1, "unattractive": 1}

# The word “liver” only occurs in the second sentence, so its semantic descriptor vector is: {"i": 1, "believe": 1, "my": 1, "is": 1, "diseased": 1}

# All words are stored as lowercase so that we don't consider for example "man" and "Man" as different words. All punctutation is discarded.

# The cosine similarity between two vectors u = {u1, u2, . . . , uN } and v = {v1, v2, . . . , vN } is defined as: sim(u, v) =        (u · v) / (|u||v|)


