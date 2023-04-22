import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer
import os

# Define function to get number of tokens
def num_tokens(file_path):
    with open(file_path, 'r', encoding='utf8') as f:
        text = f.read()
    tokens = word_tokenize(text)
    return len(tokens)

# Define function to get number of lexical words
def num_lexical_words(file_path):
    with open(file_path, 'r', encoding='utf8') as f:
        text = f.read()
    tokens = word_tokenize(text)
    lexical_words = [token for token in tokens if token.isalpha()]
    return len(lexical_words)

# Define function to get vocabulary size (lexical words)
def vocab_size_lexical(file_path):
    with open(file_path, 'r', encoding='utf8') as f:
        text = f.read()
    tokens = word_tokenize(text)
    lexical_words = set([token for token in tokens if token.isalpha()])
    return len(lexical_words)

# Define function to get vocabulary size (stems)
def vocab_size_stems(file_path):
    with open(file_path, 'r', encoding='utf8') as f:
        text = f.read()
    tokens = word_tokenize(text)
    stemmer = PorterStemmer()
    stems = set([stemmer.stem(token) for token in tokens if token.isalpha()])
    return len(stems)

# Define function to get number of sentences
def num_sentences(file_path):
    with open(file_path, 'r', encoding='utf8') as f:
        text = f.read()
    sentences = sent_tokenize(text)
    return len(sentences)

# Define function to get average sentence length (tokens)
def avg_sentence_length_tokens(file_path):
    with open(file_path, 'r', encoding='utf8') as f:
        text = f.read()
    sentences = sent_tokenize(text)
    tokens_per_sentence = [len(word_tokenize(sentence)) for sentence in sentences]
    return sum(tokens_per_sentence) / len(tokens_per_sentence)

# Define function to get average sentence length (lexical words)
def avg_sentence_length_lexical(file_path):
    with open(file_path, 'r', encoding='utf8') as f:
        text = f.read()
    sentences = sent_tokenize(text)
    lexical_tokens_per_sentence = [len([token for token in word_tokenize(sentence) if token.isalpha()]) for sentence in sentences]
    return sum(lexical_tokens_per_sentence) / len(lexical_tokens_per_sentence)

# Define function to get lexical diversity
def lexical_diversity(file_path):
    with open(file_path, 'r', encoding='utf8') as f:
        text = f.read()
    tokens = word_tokenize(text)
    lexical_words = [token for token in tokens if token.isalpha()]
    return len(set(lexical_words)) / len(lexical_words)

# Replace "file1.txt", "file2.txt", and "file3.txt" with the actual file paths
file1 = "2007 - ertms.txt"
file2 = "2007 - eirene fun 7.txt"
file3 = "2006 - eirene sys 16.txt"
directory = 'requirements_6'
# nltk.download()
# Calculate statistics for each file
for filename in os.listdir(directory):
    file = os.path.join(directory, filename)
    print("Statistics for ", file)
    print("Number of Tokens:", num_tokens(file))
    print("Number of Lexical Words:", num_lexical_words(file))
    print("Vocabulary Size (Lexical Words):", vocab_size_lexical(file))
    print("Vocabulary Size (Stems):", vocab_size_stems(file))
    print("Number of Sentences:", num_sentences(file))
    print("Average Sentence Length (Tokens):", avg_sentence_length_tokens(file))
    print("Average Sentence Length (Lexical Words):", avg_sentence_length_lexical(file))
    print("Lexical Diversity:", lexical_diversity(file))
    print()
