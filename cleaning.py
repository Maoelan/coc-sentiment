import re
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

def preprocessing_text(text):
    def cleaning_text(text):
        text = re.sub(r'@\w+', '', text)
        text = re.sub(r'#\w+', '', text)
        text = re.sub(r'RT[\s]', '', text)
        text = re.sub(r'https?://\S+|www.\S+', '', text)
        text = re.sub(r'<.*?>', '', text)
        text = re.sub(r'\d+', '', text)
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)
        text = text.replace('\n', ' ')
        text = text.translate(str.maketrans('', '', string.punctuation))
        text = text.strip()
        return text
    
    def casefolding_text(text):
        return text.lower()
    
    def tokenizing_text(text):
        return word_tokenize(text)
    
    def filtering_text(tokens):
        list_stopwords = set(stopwords.words('english'))
        return [word for word in tokens if word.lower() not in list_stopwords]
    
    def stem_text(tokens):
        stemmer = PorterStemmer()
        stemmed_text = ' '.join([stemmer.stem(word) for word in tokens])
        return stemmed_text

    
    text = cleaning_text(text)
    text = casefolding_text(text)
    tokens = tokenizing_text(text)
    tokens = filtering_text(tokens)
    text = stem_text(tokens)

    return text