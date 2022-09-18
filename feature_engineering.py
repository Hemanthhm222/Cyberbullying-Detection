from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from imblearn.over_sampling import SMOTE
from Logging_files import logger

class vectorization_and_augmentation:
    
    def __init__(self):
        self.log_writter = logger.Logger()
    
    def word_vectorization(self,df):
        
        # vectoriation is converting text into sequence of numbers
        try:
            tfidf = TfidfTransformer()
            clf = CountVectorizer()

            x_cv = clf.fit_transform(df['cleaned_text'])

            tf_transform = TfidfTransformer(use_idf=True).fit(x_cv)
            x_tf = tf_transform.transform(x_cv)
            return x_tf
        
        except Exception as e:
            
            file_object = open("Logging_files/Training_logs.txt","a+")
            self.log_writter.log(file_object,f"Error occured : {e}")
            file_object.close()
            raise e
    
    def data_augmentation(self,x_train,y_train):
        
        # data augmentation is used to  increase the amount of data by adding slightly -
        # - modified copies of already existing data or newly created synthetic data from existing data
        try:        
            for i in range(5):
                smote = SMOTE(sampling_strategy='minority')
                x_train,y_train = smote.fit_resample(x_train,y_train) 
            return x_train,y_train 
            
        except Exception as e:
            
            file_object = open("Logging_files/Training_logs.txt","a+")
            self.log_writter.log(file_object,f"An Errror occurred :: {e}")
            file_object.close()
            raise e
