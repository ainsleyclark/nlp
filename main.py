from bottle import Bottle, request, response
from dataclasses import dataclass

import pke
import json
import re
import os

app = Bottle()

DEFAULT_LIMIT = 30
DEFAULT_LANGUAGE = "en"
TOKEN = os.getenv("NLP_TOKEN")
ENV = os.getenv("NLP_ENV")
debug = True
if ENV == "production" or ENV == "prod":
	debug = False


@dataclass
class Response:
	status: int
	message: str
	error: bool
	data: any


@app.get("/api/v1")
def pingHandler():
	response.headers['Content-Type'] = 'application/json'
	return respond("PONG", None)


@app.post("/api/v1")
def postHandler():
	if request.headers.get("X-Auth-Token") != TOKEN:
		response.status = 401
		return respond("Error: Unauthorised token", None)

	response.headers['Content-Type'] = 'application/json'

	body = request.json

	limit = DEFAULT_LIMIT
	lang = DEFAULT_LANGUAGE
	content = ""
	stopwords = loadStopwords()
	dirty = loadDirty()

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
		if "stopwords" in body:
			stopwords = stopwords + body["stopwords"]
		if "dirty" in body:
			dirty = dirty + body["dirty"]
	except Exception as e:
		response.status = 400
		return respond("Error merging stopwords", str(e))

	try:
		keywords = extract(content, lang, stopwords)
		return respond("Successfully obtained keywords.", process(keywords, limit, dirty))
	except Exception as e:
		response.status = 400
		return respond("Error obtaining keywords", str(e))


@app.error(404)
def error404(e):
	response.headers['Content-Type'] = 'application/json'
	return respond("404 endpoint not found", str(e))


@app.error(500)
def error500(e):
	response.headers['Content-Type'] = 'application/json'
	return respond("Internal server error", str(e))


def extract(content, language, stopwords):
	extractor = pke.unsupervised.TfIdf()  # initialize a keyphrase extraction model, here TFxIDF
	extractor.stoplist = stopwords
	extractor.load_document(input=content, language=language)  # load the content of the document  (str or spacy Doc)
	extractor.candidate_selection()  # identify keyphrase candidates
	extractor.candidate_weighting()  # weight keyphrase candidates
	return extractor.get_n_best(1000)  # select the 10-best candidates as keyphrases


def process(keywords, limit, dirty):
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


def loadStopwords():
	f = open('./exclude/stopwords.json')
	data = json.load(f)
	f.close()
	return data


def loadDirty():
	f = open('./exclude/dirty.json')
	data = json.load(f)
	f.close()
	return data


def respond(message, data):
	status = response.status_code
	error = False
	if status != 200:
		error = True
	return json.dumps(Response(status, message, error, data), default=vars)


port = 8080
if os.getenv("PORT"):
	port = os.getenv("PORT")

app.run(host='0.0.0.0', port=port, debug=debug)
