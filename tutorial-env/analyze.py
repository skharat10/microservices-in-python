from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
from collections import Counter
#from gevent.pywsgi import WSGIServer

app = Flask(__name__)

def count_words(url):
    # send a GET request to the specified URL
    response = requests.get(url)

    # parse the HTML content using beautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the text content from the HTML
    text = soup.get_text()

    # split the text into words by whitespace and punctuation
    words = text.split()

    # count the frequency of each word using Counter
    word_counts = Counter(words)

    return word_counts

    @app.route('/analyze', methods=['POST'])
    def analyze_url():
        data = request.get.json()

        if 'url' not in data:
            return jsonify({'error': 'URL not provided'})

        url = data['url']

        try:
            word_counts = count_words(url)
            return jsonify({'words': word_counts})
        except requests.exceptions.RequestException:
            return jsonify({'error': 'Failed to fetch URL'})

    if __name__ == '__main__':
        app.run(port=5001)
# @app.route('/word-frequency', methods=['POST'])
# def word_frequency():
#     url = requests.json['url']
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     text = soup.get_text()
#     words = text.split()
#     word_counts = Counter(words)
#     result = [{'word': word, 'count': count} for word, count in word_counts.items()]
#     return jsonify(result)

#  if __name__ == '__main__' :
#      app.run(port=3700)
# #if __name__ == "__main__":
#     # from waitress import serve
#     # serve(app, host="0.0.0.0", port=3700)
#      # http_server = WSGIServer(('', 3700), app)
        