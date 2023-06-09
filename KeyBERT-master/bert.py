from PyPDF2 import PdfReader
from wordcloud import WordCloud
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from sentence_transformers import SentenceTransformer
from keybert import KeyBERT
import matplotlib.pyplot as plt
import wikipedia as wiki
import os, re

def calculate_jaccard(text1,text2):  # Calculates jaccard similarity between two string
  word_tokens1=word_tokenize(text1.lower())
  word_tokens2=word_tokenize(text2.lower())
  both_tokens = word_tokens1 + word_tokens2
  union = set(both_tokens)
  # Calculate intersection.
  intersection = set()
  for w in word_tokens1:
    if w in word_tokens2:
      intersection.add(w)
  jaccard_score = len(intersection)/len(union)
  return jaccard_score

stemmer = PorterStemmer()
wordnet_lemmatizer = WordNetLemmatizer()
# Folder name with requirement specification PDFs
# Make sure there is > 1 PDF in folder
directory = 'all_requirements' 
sentence_model = SentenceTransformer("all-mpnet-base-v2")
kw_model = KeyBERT(model=sentence_model)
lst = []
count = 0

# Iterate through folder to get PDF files
for filename in os.listdir(directory):
    str = ""
    final = ""
    box = []
    f = os.path.join(directory, filename)
    if f.lower().endswith('.pdf'):
      raw = PdfReader(f)
      for page in raw.pages:
            box.append(page.extract_text())
      a = "".join(box)
      # minimal pre-processing
      b = re.sub("requirements", "", a.lower())
      c = re.sub("requirement", "", b)
      d = re.sub("specifications", "", c)
      final = re.sub("specification", "", d)
      lst.append(final)
      
print("PDFs extracted")
# KeyBERT keyword/keyphrase extraction
# keyword: (1, 1), keyphrase(1, 2)
keywords = kw_model.extract_keywords(lst, keyphrase_ngram_range=(1, 2), 
                                     stop_words=None, use_maxsum=True, nr_candidates=25, top_n=25)
for group in keywords: print(group)

corpus = []
i = 1
# width=1000, height=500, 
WC = WordCloud(max_font_size=50, max_words=100, include_numbers=False, background_color="white")

for a in keywords:
    j = 1
    scores = []
    for b in a:
           keyword = b[0]
           corpus.append(keyword)
           # Search Wikipedia
           matching_titles=wiki.search(keyword,suggestion=True)
           if not matching_titles:
                continue
           for title in matching_titles[0]:
                # calculate mean of jaccard scores per domain
                jaccard = calculate_jaccard(title,keyword)
                if jaccard < 0.4:
                    continue
                else: print(title, ": ", jaccard)
                j+=1
                scores.append(jaccard)
                # Combine Wikipedia titles with keywords
                corpus.append(title)
                try: corpus.append(wiki.page(wiki.search(title)[0]).content)
                except: None

     # Generate wordcloud for each PDF document
    print("total articles: ", j)
    wordcloud = WC.generate(" ".join(corpus))
    plt.figure(figsize=(15,8))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.savefig("wc_{}.png".format(i), bbox_inches='tight')
    corpus.clear()
    i+=1
    
    sum = 0
    for c in scores:
      sum += c
    avg = sum/j
    print("average Jaccard: ", avg)


print("Wordclouds created")
