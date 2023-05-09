import nltk

def word_type(word):
    pos = nltk.pos_tag([word])
    if pos[0][1] in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']:
        return 'verb'
    elif pos[0][1] in ['NN', 'NNS', 'NNP', 'NNPS']:
        return 'noun'
    else:
        return 'unknown'

# Example usage
print(word_type('run'))  # Output: verb
print(word_type('house'))  # Output: noun
print(word_type('apple'))  # Output: noun
print(word_type('jumping'))  # Output: verb
