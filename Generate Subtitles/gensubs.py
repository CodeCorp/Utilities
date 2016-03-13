import speech_recognition as sr

import sys
import os
import subprocess as sp

from os import path

import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

import sys
from termcolor import *
import termcolor

import textblob
from textblob import TextBlob
from textblob.translate import Translator

#Training for then identifying verbs, nouns etc
train_text = state_union.raw("2005-GWBush.txt")
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

#Color Codes corresponding to Tags for Verbs, Nouns etc
TagCodes = {'CC': 6, 'CD': 1, 'DT': 6, 'EX': 6, 'FW': 6, 'IN': 6, 'JJ': 0, 'JJR': 0, 'JJS': 0, 'LS': 2, 'MD': 2, 'NN': 1, 'NNS': 1, 'NNP': 2, 'NNPS': 2, 'PDT': 6, 'POS': 6, 'PRP': 5, 'PRP$': 5, 'RB': 4, 'RBR': 4, 'RBS': 4, 'RP': 4, 'TO': 7, 'UH': 2, 'VB': 3, 'VBD': 3, 'VBG': 3, 'VBN': 3, 'VBP': 3, 'VBZ': 3, 'WDT': 6, 'WP': 5, 'WP$': 5, 'WRB': 5};

ColorCodes = {0: 'grey', 1: 'red', 2: 'green', 3: 'yellow', 4: 'blue', 5: 'magenta', 6: 'cyan', 7: 'white'}

#Each language is assigned a short code for translation
LanguageCodes = {'afrikaans' : 'af','albanian' : 'sq','arabic' : 'ar','armenian' : 'hy','azerbaijani' : 'az','basque' : 'eu','belarusian' : 'be','bengali' :'bn','bosnian' : 'bs','bulgarian' : 'bg','catalan' : 'ca','cebuano' : 'ceb','chichewa' : 'ny','chinese-simplified' : 'zh-CN','chinese-traditional' : 'zh-TW','croatian' : 'hr','czech' : 'cs','danish' : 'da','dutch' : 'nl','english' : 'en','esperanto' : 'eo','estonian' : 'et','filipino' : 'tl','finnish' : 'fi','french' : 'fr','galician' : 'gl','georgian' : 'ka','german' : 'de','greek' : 'el','gujarati' : 'gu','haitian-creole' : 'ht','hausa' : 'ha','hebrew' : 'iw','hindi' : 'hi','hmong' : 'hmn','hungarian' : 'hu','icelandic' : 'is','igbo' : 'ig','indonesian' : 'id','irish' : 'ga','italian' : 'it','japanese' : 'ja','javanese' : 'jw','kannada' :'kn','kazakh' : 'kk','khmer' : 'km','korean' : 'ko','lao' : 'lo','latin' : 'la','latvian' : 'lv','lithuanian' : 'lt','macedonian' : 'mk','malagasy' : 'mg','malay' : 'ms','malayalam' : 'ml','maltese' : 'mt','maori' : 'mi','marathi' : 'mr','mongolian' :'mn','burmese' : 'my','nepali' : 'ne','norwegian' : 'no','persian' : 'fa','polish' : 'pl','portuguese' : 'pt','punjabi' : 'ma','romanian' : 'ro','russian' : 'ru','serbian' : 'sr','sesotho' : 'st','sinhala' : 'si','slovak' : 'sk','slovenian' :'sl','somali' : 'so','spanish' : 'es','sudanese' : 'su','swahili' : 'sw','swedish' : 'sv','tajik' : 'tg','tamil' : 'ta','telugu' : 'te','thai' : 'th','turkish' : 'tr','ukrainian' : 'uk','urdu' : 'ur','uzbek' : 'uz','vietnamese' : 'vi','welsh' : 'cy','yiddish' : 'yi','yoruba' : 'yo','zulu' : 'zu'}


#Tags corresponding to Verbs, Nouns etc
'''
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


fileName = str(sys.argv[1])
fileExtension = os.path.splitext(fileName)[1]
mode=0

#Checking if Language Argument was passed or not
if len(sys.argv) >= 3:
	language = str(sys.argv[2])
	if language in LanguageCodes.keys():
		mode=1
	else:
		mode=0
		print "Language not found. Type the language, not the code. Please check the Accepted Language List\n"
converted = False

#Converting any file to .wav format
if fileExtension != ".wav":
	fnull = open(os.devnull, 'w')
	sp.call("pacpl -t wav " + fileName, shell = True, stdout = fnull, stderr = fnull)
	fnull.close()
	fileName = os.path.splitext(fileName)[0] + '.wav'
	converted = True

# use "filename" as the audio source
r = sr.Recognizer()

with sr.WavFile(fileName) as source:
    audio = r.record(source) # read the entire WAV file

proc=0

#Main Code which generates the subtitles
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("\nSubtitles Generated-:\n")
    text=str(r.recognize_google(audio))
    print text
    proc=1
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

sample_text=unicode(text)
tokenized = custom_sent_tokenizer.tokenize(sample_text)

#NLP used here to characterize words, whether they are verbs, nouns etc
def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            namedEnt = nltk.ne_chunk(tagged, binary=False)
	    return namedEnt
#            namedEnt.draw()
    except Exception as e:
        print(str(e))
	return 0

if proc==1:
	a=process_content()

	if a==0:
		print "Error Encountered"
	
	else:
		print '\nCharacterized Output-:\n'
		#Printing colored output to the terminal depending on the respective Color Codes
		for i in a:
			b=str(type(i))
			if "nltk.tree.Tree" in b:
				for j in i:
					print colored(str(j[0]), str(ColorCodes[TagCodes[str(j[1])]])),
			else:
				print colored(str(i[0]), str(ColorCodes[TagCodes[str(i[1])]])),


	if mode==1:
		c=TextBlob(str(text))
		d=str(c.translate(to=str(LanguageCodes[str(language)])))
		print "\nTranslated Text-:\n"
		print d

#Finally removing the converted file, if it was additionally created
if converted:
	os.remove(fileName)
