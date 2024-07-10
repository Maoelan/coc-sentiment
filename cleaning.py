import re
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from nltk.stem import PorterStemmer

# Function untuk membersihkan teks review dengan penghapusan stopwords dan stemming
def preprocessing_text(text):
    def cleaning_text(text):
        text = re.sub(r'@\w+', '', text)  # Hapus mention
        text = re.sub(r'#\w+', '', text)  # Hapus hashtag
        text = re.sub(r'RT[\s]', '', text)  # Menghapus RT
        text = re.sub(r'https?://\S+|www.\S+', '', text)  # Hapus URL
        text = re.sub(r'<.*?>', '', text)  # Hapus tag HTML
        text = re.sub(r'\d+', '', text)  # Hapus angka
        text = text.lower()  # Ubah teks menjadi lowercase
        text = re.sub(r'[^\w\s]', '', text)  # Menghapus karakter selain huruf dan angka
        text = text.replace('\n', ' ')  # Mengganti baris baru dengan spasi
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
    
    '''def stemming_text(tokens):
        factory = StemmerFactory()
        stemmer = factory.create_stemmer()
        return ' '.join([stemmer.stem(word) for word in tokens])'''
    
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