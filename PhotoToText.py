from PIL import Image
import pytesseract
import re
from autocorrect import spell
import pprint

def PhotoToText():
	pytesseract.pytesseract.tesseract_cmd = r'/usr/local/Cellar/tesseract/4.0.0/bin/tesseract'


	text = pytesseract.image_to_string(Image.open('test.png'))

	locs = [-1] + [m.start() for m in re.finditer('\n', text)] + [len(text)]

	sentences = []
	for i in range(1,len(locs)):
		sentences += [text[locs[i-1]+1:locs[i]]]
	sentences = [sent for sent in sentences if sent]
	sentences = [[spell(word) for word in sent.split()] for sent in sentences]

	print(len(sentences))
	titleLoc = []
	flag = True
	for loc in range(len(sentences)):
		if len(sentences[loc]) <= 2 and sentences[loc] and sentences[loc][0][0].isupper():
			titleLoc += [loc]
	if titleLoc[0] != 0:
		flag = False

	resumeInfo = {}
	if flag:
		resumeInfo['Basic Info'] = sentences[:titleLoc[1]]
		titleLoc = titleLoc[1:]
	else:
		resumeInfo['Basic Info'] = sentences[:titleLoc[0]]

	titleLoc += [len(sentences)]
	for i in range(len(titleLoc)-1):
		resumeInfo[''.join([word+' ' for word in sentences[titleLoc[i]]])[:-1]] = sentences[titleLoc[i]+1:titleLoc[i+1]]

	pprint.pprint(resumeInfo)
	
	return resumeInfo

PhotoToText()