from flask import Flask
import feedparser




app = Flask(__name__)
rss_feed = {'bbc':'http://feed.bcci.co.uk/news/rss.xml',
            'cnn':'http://rss.cnn.com/rss/edition.rss',
            'fox':'http://feeds.foxnews.com/foxnews/latest',
            'iol':'http://iol.co.za/cmlink'}




@app.route('/')
@app.route('/bbc')
def bbc():
    return get_news(bbc)

@app.route('/cnn')
def cnn():
    return get_news(cnn)



def get_news(publication):
    feed =  feedparser.parse(rss_feed[publication])
    first_article = feed['entries'][0]
    return """ <html>
            <body>
                <h1>bbc headlines</h1>
                <b>{0}</b><br/>
                <i>{1}</i><br/>
                <p>{2}</p><br/>
            </body>
        </html>""".format(first_article.get("arcticle"),first_article.get("published"),first_article.get("summary"))





if __name__ == "__main__":
    app.run(debug=True)