import string
import nltk
import re
from string import punctuation
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from contractions import contractions_dict
from autocorrect import Speller
from Logging_files import logger
global text

stop_words = set(stopwords.words('english'))

class preprocess:
    """
    This class will handle the preprocessiPre-processing of the data which incudes
    * Data transform
    * Tokenize sentences
    * Change to lower case
    * correct spelling
    * remove numbers
    * remove punctuation
    * remove stopwords
    * normalize(lemmatize or Lemmatization"""
    
    def __init__(self):
        self.log_writter = logger.Logger()
        
    def decontract(self,text):
        try:
            text = re.sub(r"can\'t", "can not", text)
            text = re.sub(r"n\'t", " not", text)
            text = re.sub(r"\'re", " are", text)
            text = re.sub(r"\'s", " is", text)
            text = re.sub(r"\'d", " would", text)
            text = re.sub(r"\'ll", " will", text)
            text = re.sub(r"\'t", " not", text)
            text = re.sub(r"\'ve", " have", text)
            text = re.sub(r"\'m", " am", text)
            return text
    
        except Exception as e:
            file_object = open("Logging_files/Training_logs.txt","a+")
            self.log_writter.log(file_object,f"An Errror occurred :: {e}")
            file_object.close()
            raise e
        
    def strip_all_entities(self,text): 
        try:
            text = text.replace('\r', '').replace('\n', ' ').lower() #remove \n and \r and lowercase
            text = re.sub(r"(?:\@|https?\://)\S+", "", text) #remove links and mentions
            text = re.sub(r'[^\x00-\x7f]',r'', text) #remove non utf8/ascii characters such as '\x9a\x91\x97\x9a\x97'
            banned_list= string.punctuation
            table = str.maketrans('', '', banned_list)
            text = text.translate(table)
            text = [word for word in text.split() if word not in stop_words]
            text = ' '.join(text)
            text =' '.join(word for word in text.split() if len(word) < 14) # remove words longer than 14 characters
            return text
        
        except Exception as e:
            file_object = open("Logging_files/Training_logs.txt","a+")
            self.log_writter.log(file_object,f"An Error occured : {e}")
            file_object.close()
            raise e          
             
    #clean hashtags at the end of the sentence, and keep those in the middle of the sentence by removing just the "#" symbol
    def clean_hashtags(self,text):
        try:
            new_tweet = " ".join(word.strip() for word in re.split('#(?!(?:hashtag)\b)[\w-]+(?=(?:\s+#[\w-]+)*\s*$)', text)) #remove last hashtags
            new_tweet2 = " ".join(word.strip() for word in re.split('#|_', new_tweet)) #remove hashtags symbol from words in the middle of the sentence
            return new_tweet2
        
        except Exception as e:
            file_object = open("Logging_files/Training_logs.txt","a+")
            self.log_writter.log(file_object,f"An Error occured : {e}")
            file_object.close()
            raise e 

    #Filter special characters such as "&" and "$" present in some words
    def filter_chars(self,text):
        try:
            sent = []
            for word in text.split(' '):
                if ('$' in word) | ('&' in word):
                    sent.append('')
                else:
                    sent.append(word)
            return ' '.join(sent)
        
        except Exception as e:
            file_object = open("Logging_files/Training_logs.txt","a+")
            self.log_writter.log(file_object,f"An Errror occurred :: {e}")
            file_object.close()
            raise e
    

    #Remove multiple sequential spaces
    def remove_mult_spaces(self,text):
        try:
            return re.sub("\s\s+" , " ", text)
        
        except Exception as e:
            file_object = open("Logging_files/Training_logs.txt","a+")
            self.log_writter.log(file_object,f"An Errror occurred :: {e}")
            file_object.close()
            raise e

    #Stemming
    def stemmer(self,text):
        try:
            tokenized = nltk.word_tokenize(text)
            ps = PorterStemmer()
            return ' '.join([ps.stem(words) for words in tokenized])
        
        except Exception as e:
            file_object = open("Logging_files/Training_logs.txt","a+")
            self.log_writter.log(file_object,f"An Errror occurred :: {e}")
            file_object.close()
            raise e

    #Lemmatization 
    def lemmatize(self,text):
        try:
            tokenized = nltk.word_tokenize(text)
            lm = WordNetLemmatizer()
            return ' '.join([lm.lemmatize(words) for words in tokenized])
        
        except Exception as e:
            file_object = open("Logging_files/Training_logs.txt","a+")
            self.log_writter.log(file_object,f"An Errror occurred :: {e}")
            file_object.close()
            raise e
      