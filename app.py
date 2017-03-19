from flask import Flask, render_template
import feedparser

app = Flask(__name__)

#List of Variables storing links to RSS Feeds

rss_theverge = feedparser.parse("http://www.theverge.com/rss/index.xml.rss")

@app.route('/', methods=['GET'])
def index():

	sites = list_of_sites() # List of websites

	contents = []

	for site in sites:
		_rss = feedparser.parse(site)

		site_content = {}

		site_content['name'] = _rss['feed']['title'] #Title of the website
		site_content['link'] = _rss['feed']['link'] #Link to the Website
		links =  {} #Empty dict that will store Article Title (key) and it's link (Value)

		no_of_links = (len(_rss['entries']))

		if(no_of_links > 30):
			no_of_links = 30

		for i in range(no_of_links):
			links[_rss['entries'][i]['title']] = _rss['entries'][i]['link']

		site_content['count'] = no_of_links
		site_content['links'] = links

		contents.append(site_content)

	return render_template('index.html', contents = contents)

def list_of_sites():
	sites = []

	sites.append("http://www.theverge.com/rss/index.xml.rss") #The Verge
	sites.append("http://feeds.arstechnica.com/arstechnica/index/") #Ars Technica
	sites.append("http://feeds.gawker.com/gizmodo/full") #Gizmodo

	return (sites)

if __name__ == "__main__":
	app.run(debug=True)