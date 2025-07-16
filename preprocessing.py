import re
import string
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from nltk.corpus import stopwords

# Inisialisasi stemmer dan stopword
factory = StemmerFactory()
stemmer = factory.create_stemmer()

# Pastikan kamu sudah download stopwords saat pertama kali
try:
    stop_words = stopwords.words('indonesian')
except:
    import nltk
    nltk.download('stopwords')
    stop_words = stopwords.words('indonesian')

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r"http\S+|www\S+|https\S+", '', text)
    text = re.sub(r'\@[\w]*', '', text)
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    filtered_words = [word for word in words if word not in stop_words]
    stemmed_words = [stemmer.stem(word) for word in filtered_words]
    return ' '.join(stemmed_words)
