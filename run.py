from flask import Flask, render_template
import feedparser

app = Flask(__name__)

#List of Variables storing links to RSS Feeds

rss_theverge = feedparser.parse("http://www.theverge.com/rss/index.xml.rss")

@app.route('/')
def index():

	title = rss_theverge['feed']['title']
	link = rss_theverge['feed']['link']
	no_of_links = (len(rss_theverge['entries']))

	links = {}
	for i in range (no_of_links):
		links[(rss_theverge['entries'][i]['title'])] = (rss_theverge['entries'][i]['link'])

	return render_template('index.html', title = title, 
		link = link, no_of_links = no_of_links, links = links)

if __name__ == "__main__":
	app.run(debug=True)