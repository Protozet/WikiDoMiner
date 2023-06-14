# WikiDoMiner: Wikipedia Domain-specific Miner

WikiDoMiner is a tool that automatically generates domain-specific corpora by crawling Wikipedia. 



## Installation

Clone and install the required libraries

```bash
git clone https://gitlab.uni.lu/sezzini/WikiDoMiner.git
cd WikiDoMiner
pip install -r requirements.txt 
```

## Usage example

CLI:

```python
python WikiDoMiner.py --doc Xfile.txt --output-path ../research/nlp --wiki-depth 1
```

checkout available arguments using 

```python
python WikiDoMiner.py --help
```

Run the notebook [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1dV0maoPKdpDy7jnJ0TfVJGfa4zhiFejZ?usp=sharing/)


```python

# extract keywords
keywords = getKeywords(document, spacy_pipeline)

# query wikipedia to get your corpus
corpus = getCorpus(keywords, depth=1)

# locally save your corpus 
saveCorpus(corpus, parent_dir='Documents', folder='Corpus')
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)


Command used to run: python WikiDoMiner.py --doc cctns.pdf --output-path ./research/nlp --wiki-depth 1

# KeyBERT for Keyword Extraction

To run KeyBERT, follow the instructions within the README.md file within the KeyBERT-Master folder.
After ensuring all of the necessary libraries are installed, change to the WikiDoMiner directory before running bert.py. The "all_requirements" folder is used by default, but if you wish to run the program on different documents, be sure to add the folder in the same format that "all_requirements" follows while also changing the "directory" variable to match the name of your folder.