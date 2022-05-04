# nlp

NLP (Natrual Language Processing) API via the pke (Python Keyphrase Extraction) engine to extract keywords and analyse
topics from text. Salience

This library ships with supervised models trained on the [SemEval-2010 dataset](http://aclweb.org/anthology/S10-1004).

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)


## Usage

## Authentication & URL

- Main production API URL sits at `https://nlp-vqyb5tu4fq-ew.a.run.app` **Note** - This will likely change.
- The base URL of the application is `/api/v1` and must be prepended to every request.
- A token must be passed for request to this application, it must be set as a header with the key of `X-Auth-Token` with
	a value of `vPz5LVNvYMLruAgy6BCMxM9F8FZYDpq6Bk3N`

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

This endpoint extracts keywords from a given piece of text. The JSON body for the endpoint is described below.

| Key      | Example Value | Default Value | Required | Notes                                    |
|----------|:--------------|:--------------|:---------|:-----------------------------------------|
| language | en            | en            | ✅        | See below for available language keys    |
| limit    | 10            | 30            | ✅        | The amount of keywords to extract.       |
| text     | My keywords   | N/A           | ❌        | The content to extract the keywords from |

```json
{
	"language": "en",
	"limit": 30,
	"text": "SEO SEO SEO talent combined with unique technology. SEO Services SEO talent combined with unique technology. Learn more Industries Find out about our work with these industries. Financial Services Law Firms Automotive Technology Technology SEO technology for our clients. Our Technology SEO technology for our clients. Learn more SERP Speed Our FREE tool compares your page speed at keyword level with the top 10 and provides insights and recommendations for improvements. Learn more Work Work The work and results that we’ve delivered for our clients. Our Work The work and results that we’ve delivered for our clients. Learn more Case Studies Clients who understand the value of SEO done the right way. The Cotswold Company BlackRock Direct Line Energy Helpline Driving.co.uk Building Materials Ecommerce migration About Reddico About Reddico We're a people-first company, focused on making our team's lives better. Team Discover who’s who in our talented team of professionals. Learn more Careers What it’s like to work at Reddico and how apply for open positions. Learn more Values What we stand for, from our core values to caring for the environment and giving back to the communities in which we live and work. Learn more News & Insights News & Insights The latest Reddico news and insights on the SEO world. News & Insights The latest Reddico news and insights on the SEO world. Learn more Reddico in the News Media coverage that we’ve garnered, including contributions to a range of industry podcasts. Learn more Marketplace Intelligence SEO insights on how the top 50 competitors are performing in your industry sector. Coming soon... Contact us Or email us at hello@reddico.co.uk We’ll help youbecome an industry leader Combining unmatched expertise in SEO with unique technology, we solve the problems your last agency couldn’t. What we do Trusted By We’re the SEO agency for ambitious brands We want to make a measurable difference to your business. Every project is built from scratch, so tell us your goals and we’ll make a bespoke SEO campaign that’ll deliver results. We take the time to look at your brand’s potential, and the challenges that are holding it back. That’s how we fix the problems other agencies struggle with, and identify new opportunities for growth. It’s all about a return on your investment. Learn more Results and relationships are what matter to us No one tells you this, but we will. If SEO doesn’t work, it can be expensive. If it works, it’s the best investment you’ll make. That’s why we’re trusted by global brands like Direct Line, BlackRock and Groupon, who switched to us when they weren’t getting results. We specialise in search, developing our own technology to explore data from numerous sources and provide actionable insights and competitor analysis. We can help you navigate what sometimes feels like a complicated game. When you partner with us, you get all the extra search marketing capabilities your business needs. We’re only doing our job well if your brand is succeeding. Our work Search optimised People’s experience of SEO is often tainted by ill-planned, off-the-shelf campaigns. Instead, we start from scratch with each project. Learn more Our technology When we found the usual SEO tools couldn’t give us the insights we wanted, we decided to do something about it and build our own. Learn more Awards aren’t everything, but they help Best eCommerce/Retail & B2C campaign European Search Awards 2022 Best Large SEO Agency European Search Awards 2021 Best Agency to Work For Winner Company Culture Awards 2021 5th in UK’s Best Workplaces™ Great Place To Work® 2021 Working with our company is very demanding and there are many levels of approval to go through, for work to be implemented. The Reddico team has always been very responsive and goes beyond the typical scope of any project, providing us all angles of a technical solution and detailed recommendations for content optimisations. Jennifer Xiques, Global SEO Lead, BlackRock Insights and interesting reads Guides 28 Apr 2022 Optimising site architecture for your brand, the user and Google  Technical SEO, Eva Mermingi, looks at how to optimise site architecture for SEO success. Learn more Sustainability 21 Apr 2022 Why we’ve taken the Million Tree Pledge Learn more Guides 4 Apr 2022 Getting a foothold in SERP reputation management We look at proactive steps you can take to manage your SERP reputation. Learn more Culture 8 Mar 2022 International Women’s Day Interview with Rachel McDonald Reddico Board Advisor Rachel McDonald talks about boundaries, bias, and why companies need to listen to and support their team members. Learn more Get in touch We'd love to hear from you. Get in touch and talk directly to our SEO experts to see how we can transform your online visibility. * * Next Monthly budget? Not applicable £3,000 - £5,000 £5,000 - £10,000 £10,000 - £15,000 £15,000+ Back Next * Back Send Thank you for contacting us. One of our experts will be in touch with you on the email provided. Okay One last thing. We never sell your data. I would like to receive Reddico News and other information. I have read and accept the Privacy Policy terms relating to UK data protection laws and GDPR. Back Accept Contact us Email ushello@reddico.co.uk Connect with us SEO Services Work Technology SERP Speed Careers Team Values Carbon Footprint News & Insights Contact us ISO 9001 certified (Quality Management System). ISO 27001 certified (Information Security Management) Terms & Conditions Privacy Policy Cookie Policy Reddico Digital Ltd. is a registered company in England and Wales. Company Number 12478393. VAT Number: GB 343939180. ©2022 Reddico Digital Ltd. All rights reserved. Reddico and the Reddico logo are registered trademarks of Reddico Digital Ltd. Close"
}
```

## Stopwords

## Example Response

Below is an example response for the Reddico website.

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
		},
		{
			"term": "industries",
			"salience": 16.365092472032078
		},
		{
			"term": "awards",
			"salience": 16.03993635429049
		},
		{
			"term": "touch",
			"salience": 15.539727270044803
		},
		{
			"term": "seo seo",
			"salience": 14.359818180029869
		},
		{
			"term": "seo talent",
			"salience": 14.359818180029869
		},
		{
			"term": "seo talent combined",
			"salience": 14.359818180029869
		},
		{
			"term": "talent combined",
			"salience": 14.359818180029869
		},
		{
			"term": "seo services",
			"salience": 14.359818180029869
		},
		{
			"term": "technology seo",
			"salience": 14.359818180029869
		},
		{
			"term": "technology seo technology",
			"salience": 14.359818180029869
		},
		{
			"term": "seo technology",
			"salience": 14.359818180029869
		},
		{
			"term": "serp speed",
			"salience": 14.359818180029869
		},
		{
			"term": "direct line",
			"salience": 14.359818180029869
		},
		{
			"term": "latest reddico",
			"salience": 14.359818180029869
		},
		{
			"term": "latest reddico news",
			"salience": 14.359818180029869
		}
	]
}
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





