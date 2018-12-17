from nltk import pos_tag, ne_chunk
from collections import Counter
from nltk.tokenize import word_tokenize, PunktSentenceTokenizer

from nltk.corpus import stopwords, state_union, wordnet, movie_reviews
from nltk.stem import WordNetLemmatizer , PorterStemmer

from gensim.corpora.dictionary import Dictionary

import matplotlib.pyplot as plt
import random

'''POS tag list:
        POS tag list:

        CC	coordinating conjunction
        CD	cardinal digit
        DT	determiner
        EX	existential there (like: "there is" ... think of it like "there exists")
        FW	foreign word
        IN	preposition/subordinating conjunction
        JJ	adjective	'big'
        JJR	adjective, comparative	'bigger'
        JJS	adjective, superlative	'biggest'
        LS	list marker	1)
        MD	modal	could, will
        NN	noun, singular 'desk'
        NNS	noun plural	'desks'
        NNP	proper noun, singular	'Harrison'
        NNPS	proper noun, plural	'Americans'
        PDT	predeterminer	'all the kids'
        POS	possessive ending	parent's
        PRP	personal pronoun	I, he, she
        PRP$	possessive pronoun	my, his, hers
        RB	adverb	very, silently,
        RBR	adverb, comparative	better
        RBS	adverb, superlative	best
        RP	particle	give up
        TO	to	go 'to' the store.
        UH	interjection	errrrrrrrm
        VB	verb, base form	take
        VBD	verb, past tense	took
        VBG	verb, gerund/present participle	taking
        VBN	verb, past participle	taken
        VBP	verb, sing. present, non-3d	take
        VBZ	verb, 3rd person sing. present	takes
        WDT	wh-determiner	which
        WP	wh-pronoun	who, what
        WP$	possessive wh-pronoun	whose
        WRB	wh-abverb	where, when
'''

def temp():
        # opening the file article.text
	with open('article.text', 'r') as file:
		# reading the file
		article = file.read()

		# convert article into lower case
		article_lower = article.lower()
		# generating the tokens with word_tockenzie()
		# isalpha() will check for the alphabets
		article_words = [w for w in word_tokenize(
			article_lower) if w.isalpha()]

		no_stops = [
			t for t in article_words if t not in stopwords.words('english')]

		# print(Counter(no_stops))
		# print(Counter(no_stops).most_common(5))

		wordnet_lemmatizer = WordNetLemmatizer()
		lemmatized = [wordnet_lemmatizer.lemmatize(t) for t in no_stops]

		# ? Stemming
		ps = PorterStemmer()
		stemmed_words = [ps.stem(t) for t in lemmatized]
		print(Counter(stemmed_words))


def temp2():
	'''description of this function'''
	train_text = state_union.raw('2005-GWBush.txt')
	sample_text = state_union.raw('2006-GWBush.txt')

	custom_text_tokenizer = PunktSentenceTokenizer(train_text)

	tokenized_data = custom_text_tokenizer.tokenize(sample_text)

	try:
		for x in tokenized_data[5:]:
			words = word_tokenize(x)
			tags = pos_tag(words)
			name_entity = ne_chunk(tags, binary=True)
			print(name_entity)
	except Exception as e:
		print(str(e))


def temp3():
	sysn = wordnet.synsets('cats')
	#  word definations
	sysn_word_definitions = [
		(w.lemmas()[0].name(), w.definition()) for w in sysn]
	print(sysn_word_definitions)
	# word example
	print(sysn[0].examples())

	synonyms = []
	antonyms = []
	# syno = [ l.name() for syn in wordnet.synsets('bad') for l in syn.lemmas()]
	# ! antonyms and synonyms
	for syn in wordnet.synsets('bad'):
			for l in syn.lemmas():
					synonyms.append(l.name())
					if l.antonyms():
							antonyms.append(l.antonyms()[0].name())
	print(set(synonyms))
	print(set(antonyms))


def temp4():
	w1 = wordnet.synset('ship.n.01')
	w2 = wordnet.synset('car.n.01')
	print(w1.wup_similarity(w2))
	# ! be carefull here we are using synset not synsets
	# wup_similarity take synset as an input not synsets 

def temp5():
	documents = [ (list(movie_reviews.words(fileid)),category)
	                for category in movie_reviews.categories()
	                for fileid in movie_reviews.fileids(category)]
	
	all_words_lower = [w.lower() for w in (movie_reviews.words()) if w.isalpha()]
	all_words_without_stopword = [ w for w in all_words_lower if w not in stopwords.words('english')]

	word_features = [x[0] for x in Counter(all_words_without_stopword).most_common(3000)]
	# saving the top 3000 word from the documents
	with open(word_features,'w') as file:
		file.write(str(word_features))

def temp6():
	# preprocessing the data for NLP
	# lowercasing the word
	# only selecting the alphabets 
	# removing stopwords 
	document_words = [] 
	
	for category in movie_reviews.categories():
		for index,fileid in enumerate(movie_reviews.fileids(category)):
			if index == 1:
				break
			else:
				document_words.append(movie_reviews.words(fileid))
	
	print(document_words)
	for w in document_words:
		print(w)
	# document_words_lower = [word_tokenize(w.lower()) for w in document_words if w.isalpha()]
	# document_words_without_stopword = [ w for w in document_words_lower if w not in stopwords.words('english')]

	# wnl = WordNetLemmatizer()
	# wnl_document_words_without_stopword = [wnl.lemmatize(word) for word in document_words_without_stopword]

	# print(wnl_document_words_without_stopword)
	# dicti = Dictionary(wnl_document_words_without_stopword)
	# print(dicti)

def temp7():
	my_documents = ['The movie was about a spaceship and aliens.',
				'I really liked the movie!',
				'Awesome action scenes, but boring characters.',
				'The movie was awful! I hate alien films.',
				'Space is cool! I liked the movie.',
				'More space films, please!',]
	tokenized_docs = [word_tokenize(doc.lower()) for doc in my_documents]

	# filterd_docs = [[doc] for doc  in tokenized_docs for word in doc if word not in stopwords.words('english') or word.isalpha()]
	print(tokenized_docs)

	# dictionary = Dictionary(tokenized_docs)

temp6()