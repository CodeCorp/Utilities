# GenSubs

Generates subtitles for any video, analyzes the video, and identifies the adverbs, verbs, nouns etc by a colored output. Also supports a feature of translation to over **90+ worldwide languages**, including **several Indian regional languages** as well.

## Files Description-:

`gensubs.py` - It takes path of video as input, along with the desired language for the text to be translated to, and then generates the corresponding subtitles in the language specifies. By Default, the language is set to `English`

## Test Run-:

In this case `video.mp4` is in the same directory as of the Python Script and hence, there's no need to provide the `Absolute Path`, else the `Absolute Path` must be specified.

This is how the script runs - http://postimg.org/image/gdnpc28bl/

Just verifying if the translation is fine - http://postimg.org/image/j5c0tr14t/ . :)

##Langugages Supported-:

<ul>
<li>'Afrikaans'</li>
<li>'Albanian'</li>
<li>'Arabic'</li>
<li>'Armenian'</li>
<li>'Azerbaijani'</li>
<li>'Basque'</li>
<li>'Belarusian'</li>
<li>'Bengali'</li>
<li>'Bosnian'</li>
<li>'Bulgarian'</li>
<li>'Catalan'</li>
<li>'Cebuano'</li>
<li>'Chichewa'</li>
<li>'Chinese-Simplified'</li>
<li>'Chinese-Traditional'</li>
<li>'Croatian'</li>
<li>'Czech'</li>
<li>'Danish'</li>
<li>'Dutch'</li>
<li>'English'</li>
<li>'Esperanto'</li>
<li>'Estonian'</li>
<li>'Filipino'</li>
<li>'Finnish'</li>
<li>'French'</li>
<li>'Galician'</li>
<li>'Georgian'</li>
<li>'German'</li>
<li>'Greek'</li>
<li>'Gujarati'</li>
<li>'Haitian-Creole'</li>
<li>'Hausa'</li>
<li>'Hebrew'</li>
<li>'Hindi'</li>
<li>'Hmong'</li>
<li>'Hungarian'</li>
<li>'Icelandic'</li>
<li>'Igbo'</li>
<li>'Indonesian'</li>
<li>'Irish'</li>
<li>'Italian'</li>
<li>'Japanese'</li>
<li>'Javanese'</li>
<li>'Kannada'</li>
<li>'Kazakh'</li>
<li>'Khmer'</li>
<li>'Korean'</li>
<li>'Lao'</li>
<li>'Latin'</li>
<li>'Latvian'</li>
<li>'Lithuanian'</li>
<li>'Macedonian'</li>
<li>'Malagasy'</li>
<li>'Malay'</li>
<li>'Malayalam'</li>
<li>'Maltese'</li>
<li>'Maori'</li>
<li>'Marathi'</li>
<li>'Mongolian'</li>
<li>'Burmese'</li>
<li>'Nepali'</li>
<li>'Norwegian'</li>
<li>'Persian'</li>
<li>'Polish'</li>
<li>'Portuguese'</li>
<li>'Punjabi'</li>
<li>'Romanian'</li>
<li>'Russian'</li>
<li>'Serbian'</li>
<li>'Sesotho'</li>
<li>'Sinhala'</li>
<li>'Slovak'</li>
<li>'Slovenian'</li>
<li>'Somali'</li>
<li>'Spanish'</li>
<li>'Sudanese'</li>
<li>'Swahili' </li>
<li>'Swedish' </li>
<li>'Tajik' </li>
<li>'Tamil' </li>
<li>'Telugu'</li>
<li>'Thai' </li>
<li>'Turkish' </li>
<li>'Ukrainian'</li>
<li>'Urdu'</li>
<li>'Uzbek'</li>
<li>'Vietnamese'</li>
<li>'Welsh'</li>
<li>'Yiddish'</li>
<li>'Yoruba'</li>
<li>'Zulu'</li>
</ul>

## Packages Requirements-:

<ol>
<li> Speech Recognition 3.3.3 - https://pypi.python.org/pypi/SpeechRecognition/ </li>
<li> NLTK - http://www.nltk.org/install.html and http://www.nltk.org/data.html both are required to be installed </li>
<li> Termcolor - https://pypi.python.org/pypi/termcolor </li>
<li> Textblob - https://textblob.readthedocs.org/en/latest/index.html </li>
<li> Perl Audio Converter - http://vorzox.wix.com/pacpl </li>
<li> PyAudio - http://people.csail.mit.edu/hubert/pyaudio/ </li>
</ol>

It's better to install all these packages in a virtual environment `virtualenv`.

Install these packages first, and just run the python file - `python gensubs.py <videopathwithextension> <language>` from the terminal. 

If no `<language>` is passed as an argument while executing the script, text is by default shown in `English` language.


## Color Codes-:

CC	coordinating conjunction - Cyan <br>
CD	cardinal digit - Red <br>
DT	determiner - Cyan <br>
EX	existential there (like: "there is" ... think of it like "there exists") - Cyan <br>
FW	foreign word - Cyan <br>
IN	preposition/subordinating conjunction - Cyan <br>
JJ	adjective	'big' - Grey <br>
JJR	adjective, comparative	'bigger' - Grey <br>
JJS	adjective, superlative	'biggest' - Grey <br>
LS	list marker	1) - Green <br>
MD	modal	could, will - Green <br>
NN	noun, singular 'desk' - Red <br>
NNS	noun plural	'desks' - Red <br>
NNP	proper noun, singular	'Harrison' - Green <br>
NNPS	proper noun, plural	'Americans' - Green <br>
PDT	predeterminer	'all the kids' - Cyan <br>
POS	possessive ending	parent's - Cyan <br>
PRP	personal pronoun	I, he, she - Magenta <br>
PRP$	possessive pronoun	my, his, hers - Magenta <br>
RB	adverb	very, silently, - Blue <br>
RBR	adverb, comparative	better - Blue <br>
RBS	adverb, superlative	best - Blue <br>
RP	particle	give up - Blue <br>
TO	to	go 'to' the store. - White <br> 
UH	interjection	errrrrrrrm - Green <br>
VB	verb, base form	take - Yellow <br>
VBD	verb, past tense	took - Yellow <br>
VBG	verb, gerund/present participle	taking - Yellow <br>
VBN	verb, past participle	taken - Yellow <br>
VBP	verb, sing. present, non-3d	take - Yellow <br>
VBZ	verb, 3rd person sing. present	takes - Yellow <br> 
WDT	wh-determiner	which - Cyan <br>
WP	wh-pronoun	who, what - Magenta <br>
WP$	possessive wh-pronoun	whose - Magenta <br>
WRB	wh-abverb	where, when - Magenta <br>

## Credits-:

Ashutosh Saboo - https://github.com/ashutoshsaboo - https://github.com/ashutoshsaboo/GenSubs

