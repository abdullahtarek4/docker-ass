import nltk
from nltk.corpus import stopwords
from collections import Counter


nltk.download('stopwords')
nltk.download('punkt')


def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def process_text(text):
   
    words = nltk.word_tokenize(text)
    
   
    stop_words = set(stopwords.words('english'))
    filtered_words = [word.lower() for word in words if word.isalpha() and word.lower() not in stop_words]
    
    
    word_freq = Counter(filtered_words)
    
    return word_freq


def display_word_frequency(word_freq):
    for word, freq in word_freq.items():
        print(f"{word}: {freq}")


def main():
   
    file_path = "/app/paragraphs.txt"
    
    
    text = read_file(file_path)
    
    
    word_freq = process_text(text)
    
   
    display_word_frequency(word_freq)

if __name__ == "__main__":
    main()
