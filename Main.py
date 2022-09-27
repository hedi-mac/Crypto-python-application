from TwitterData import TwitterData
from ArticlesData import ArticlesData
from HuggingFaceTransformersAnalysis import HuggingFaceTransformersAnalysis
import csv

monitored_tickers = ['BTC', 'ETH', 'DOGE']
#Twitter data : 
data = TwitterData(monitored_tickers)
tweets = data.getData()
#Articles data
data = ArticlesData(monitored_tickers)
articles = data.getData()

transformers = HuggingFaceTransformersAnalysis()
output = transformers.create_output(tweets, articles, data.urls, monitored_tickers)


with open('Analysis.csv', mode='w', newline='', encoding="utf-8") as f:
    csv_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerows(output)




