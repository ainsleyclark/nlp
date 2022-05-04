# nlp

NLP (Natrual Language Processing) API via the pke (Python Keyphrase Extraction) engine to extract keywords and analyse
topics from text. Salience

This library ships with supervised models trained on the [SemEval-2010 dataset](http://aclweb.org/anthology/S10-1004).

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

## Authentication & URL

- Main production API URL sits at `https://nlp-vqyb5tu4fq-ew.a.run.app` **Note** - This will likely change.
- The base URL of the application is `/api/v1` and must be prepended to every request.
- A token must be passed for request to this application, it must be set as a header with the key of `X-Auth-Token`.

## Endpoints

Below is a list of endpoints the API serves.

### Ping

➡️ GET `/api/v1/`

Heartbeat endpoint that doesn't require any authorisation.

**Example response:**

```json
{
	"status": 200,
	"message": "PONG",
	"error": false,
	"data": null
}

```

### Extraction

➡️ POST `/api/v1/`

This endpoint extracts keywords from a given piece of text. The JSON body for the endpoint is described below. A slice
of objects is returned on successful submission which details the keyword and salience score.

| Key       | Example Value   | Default Value | Required | Notes                                     |
|-----------|:----------------|:--------------|:---------|:------------------------------------------|
| language  | `"en"`          | en            | ✅        | See below for available language keys     |
| limit     | `10`            | 30            | ✅        | The amount of keywords to extract.        |
| text      | `"My keywords"` | N/A           | ❌        | The content to extract the keywords from  |
| stopwords | `["exclude"]`   | N/A           | ❌        | Specific words to exclude                 |
| dirty     | `["exclude"]`   | N/A           | ❌        | Words that contain a substring to exclude |

**Example response:**

```json
{
	"status": 200,
	"message": "Successfully obtained keywords.",
	"error": false,
	"data": [
		{
			"term": "seo",
			"salience": 165.13790907034348
		},
		{
			"term": "reddico",
			"salience": 100.51872726020909
		},
		{
			"term": "serp",
			"salience": 28.719636360059738
		},
		{
			"term": "brands",
			"salience": 25.899545450074672
		},
		{
			"term": "insights",
			"salience": 23.97899999016428
		},
		{
			"term": "unique technology",
			"salience": 21.539727270044803
		},
		{
			"term": "blackrock",
			"salience": 21.539727270044803
		},
		{
			"term": "reddico digital",
			"salience": 21.539727270044803
		},
		{
			"term": "technology",
			"salience": 21.251797342284842
		},
		{
			"term": "learn",
			"salience": 20.368295910502656
		},
		{
			"term": "agency",
			"salience": 20.04992044286311
		},
		{
			"term": "optimised",
			"salience": 19.43192398051029
		},
		{
			"term": "talent",
			"salience": 18.539727270044803
		},
		{
			"term": "company",
			"salience": 18.16462612505645
		},
		{
			"term": "team",
			"salience": 16.725550003417045
		}
	]
}
```

## Excluding Words

To exclude words from the extraction you can either pass `stopwords` or `dirty` in the JSON body of the request, the
difference is explained below. If you notice a pattern with a word regularly occurring, please add the word
to `./exclude/stopwords.json` or `./exclude/dirty.json` and make a pull request.

### Stopwords

Stopwords are specific words to exclude from the analysis.

### Dirty

Dirty words will be compared by a substring to see if the keyword contains the word passed, if it does it will be
excluded from the analysis.

## Development

To get started with local development for the project, please see the following steps below.

### Setup

This library relies on relies on `spacy` (>= 3.2.3) for text processing and
requires [models](https://spacy.io/usage/models) to be installed. To set up the dependencies of the project, run the
following setup script.

```bash
sudo chmod -R 777 ./bin
./bin/start.sh
```

### Token

Export the environment variable `NLP_TOKEN` to set an authorisation token to be used for the API. Subsequent requests
should use `X-Auth-Token` with the value of the exported token.

```bash
export NLP_TOKEN=mytoken
```

### Docker

A dockerfile is included in this project, so you can run the API locally.

```bash
docker build . nlp
docker run -it -p 8080:8080 nlp
```

## Implemented Models

This library currently implements the following keyphrase extraction models:

* Unsupervised models
	* Statistical models
		* FirstPhrases
		* TfIdf
		* KPMiner [(El-Beltagy and Rafea, 2010)](http://www.aclweb.org/anthology/S10-1041.pdf)
		* YAKE [(Campos et al., 2020)](https://doi.org/10.1016/j.ins.2019.09.013)
	* Graph-based models
		* TextRank [(Mihalcea and Tarau, 2004)](http://www.aclweb.org/anthology/W04-3252.pdf)
		* SingleRank  [(Wan and Xiao, 2008)](http://www.aclweb.org/anthology/C08-1122.pdf)
		* TopicRank [(Bougouin et al., 2013)](http://aclweb.org/anthology/I13-1062.pdf)
		* TopicalPageRank [(Sterckx et al., 2015)](http://users.intec.ugent.be/cdvelder/papers/2015/sterckx2015wwwb.pdf)
		* PositionRank [(Florescu and Caragea, 2017)](http://www.aclweb.org/anthology/P17-1102.pdf)
		* MultipartiteRank [(Boudin, 2018)](https://arxiv.org/abs/1803.08721)
* Supervised models
	* Feature-based models
		* Kea [(Witten et al., 2005)](https://www.cs.waikato.ac.nz/ml/publications/2005/chap_Witten-et-al_Windows.pdf)





