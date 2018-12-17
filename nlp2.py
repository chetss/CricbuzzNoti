# Import the necessary modules
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
import pandas as pd
# 192.168.52.203
# linux123
# swatim.cdac.in

title = ['Julian Assange','Republican Natio',' PBS ','Anti-Trump',' Ethiopia — President ']
text = ['the quick brown fox jump over the lazy dog','The State Department told the Republican Natio','The ‘P’ in PBS Should Stand for ‘Plutocratic’','Anti-Trump Protesters Are Tools of the Oligar','ADDIS ABABA, Ethiopia —President Obama convene']
label = ['FAKE','REAL','FAKE','FAKE','REAL']
data = {
	'title':title,
	'text':text,
	'label':label
}
df  = pd.DataFrame(data)

y  = (df.label)

# Create training and test sets
# train_test_split will work  variable test_size 
#  here 0.33 means 33 %
X_train, X_test, y_train, y_test = train_test_split(df["title"],y,test_size=0.33,random_state=53)

# Initialize a CountVectorizer object: count_vectorizer
count_vectorizer = CountVectorizer(stop_words="english")

# Transform the training data using only the 'text' column values: count_train 
count_train = count_vectorizer.fit_transform(X_train.values)

# Transform the test data using only the 'text' column values: count_test 
count_test = count_vectorizer.transform(X_test.values)

# Print the first 10 features of the count_vectorizer
print(count_vectorizer.get_feature_names()[:10])
