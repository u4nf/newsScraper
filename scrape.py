from requests_html import HTML, HTMLSession

rawSources = [['Security Magazine', 'https://www.securitymagazine.com/topics/2189-security-newswire/', 'h2', 'p', 'a'], 
			  ['Cyber Security News', 'https://thecybersecurity.news/vulnerabilities/', '.entry-title', 'p', 'a']]

newsSource = []

output = []


class NewsSource:
	def __init__(self, name, url, headlineTag, summaryTag, linkTag):
		self.name = name
		self.url = url
		self.headlineTag = headlineTag
		self.summaryTag = summaryTag
		self.linkTag = linkTag


class Article:
	def __init__(self, headline, summary, link):
		self.headline = headline
		self.summary = summary
		self.link = link


def makeHTML():
	h = open('news.html', 'w')
	h.write('<!doctype html>\n')
	h.write('<html><head><title>News</title></head><body>\n')
	h.write('<h1>News</h1>')

	for i, j in enumerate(output):
		h.write('<h2>' + output[i].headline + '</h2>\n')
		h.write('<p>' + output[i].summary + '</p>\n')
		h.write('<a href=' + output[i].link + 'target="_blank" rel="noopener">' + output[i].link + '</a><br><br><br>\n')

	h.write('</body></html>')	
	h.close()	


#create NewsSource objects
for i in rawSources:
	j = NewsSource(i[0], i[1], i[2], i[3], i[4])
	newsSource.append(j)


for i, j in enumerate(newsSource):
	session = HTMLSession()

	r = session.get(newsSource[i].url)
	articles = r.html.find('article')

	for article in articles:

		try:
			headline = article.find(newsSource[i].headlineTag, first=True).text
			summary = article.find(newsSource[i].summaryTag, first=True).text
			link = article.find(newsSource[i].linkTag, first=True).attrs['href']

		except:
			continue

		art = Article(headline, summary, link)
		output.append(art)

makeHTML()
