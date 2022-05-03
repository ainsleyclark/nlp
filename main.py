import os

from bottle import Bottle, request, response, abort
from stopwords import stopwords, dirty
from dataclasses import dataclass

import pke
import json
import re

app = Bottle()

DEFAULT_LIMIT = 30
DEFAULT_LANGUAGE = "en"


@dataclass
class Response:
	status: int
	message: str
	error: bool
	data: any


@app.get("/")
def pingHandler():
	return respond("PONG", None)


@app.post("/")
def postHandler():
	response.headers['Content-Type'] = 'application/json'

	body = request.json

	limit = DEFAULT_LIMIT
	lang = DEFAULT_LANGUAGE
	content = ""

	if "limit" in body:
		limit = body["limit"]

	if "language" in body:
		lang = body["language"]

	if "text" in body:
		content = body["text"]
	else:
		response.status = 400
		return respond("Error: Text in body cannot be empty", None)

	try:
		keywords = extract(content, lang)
		return respond("Successfully obtained keywords.", process(keywords, limit))
	except Exception as e:
		response.status = 400
		print("here:", e)
		return respond("Error obtaining keywords", str(e))


def extract(content, language):
	extractor = pke.unsupervised.TfIdf()  # initialize a keyphrase extraction model, here TFxIDF
	extractor.stoplist = stopwords
	extractor.load_document(input=content, language=language)  # load the content of the document  (str or spacy Doc)
	extractor.candidate_selection()  # identify keyphrase candidates
	extractor.candidate_weighting()  # weight keyphrase candidates
	return extractor.get_n_best(1000)  # select the 10-best candidates as keyphrases


def process(keywords, limit):
	list = []
	for keyword in keywords:
		ok = True
		match = re.match(r'.*([1-3][0-9]{3})', keyword[0])
		if match is not None:
			continue
		for word in dirty:
			if word in keyword[0]:
				ok = False

		if ok is False:
			continue

		list.append({"term": keyword[0], "salience": keyword[1]})
	return list[:limit]


def respond(message, data):
	status = response.status_code
	error = False
	if status != 200:
		error = True
	return json.dumps(Response(status, message, error, data), default=vars)


port = 8080
if os.getenv("PORT"):
	port = os.getenv("PORT")

app.run(host='localhost', port=port, debug=True)
