from transformers import pipeline
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd
import re
import emoji 

class HuggingFaceTransformersAnalysis : 
    
    sentiment = pipeline('sentiment-analysis')

    def plotPie(self, scores, crypto): 
        df = pd.DataFrame(scores, columns=['label'])
        df['label'].value_counts().plot(kind='pie', colors=["#f45b5b", "#90ed7d"], autopct='%1.2f%%')
        plt.title(f'Percentage of positive and negative reviews for {crypto}')
        plt.show()
    
    def plotBar(self, scores, crypto): 
        df = pd.DataFrame(scores, columns=['label'])
        df['label'].value_counts().plot(kind='bar', color="#7cb5ec")
        plt.title(f'Sentiment Analysis Bar Plot {crypto}')
        plt.xlabel('Sentiment')
        plt.ylabel('number of reviews')
        plt.show()

    def convertEmoji(self, txt):
        res = emoji.demojize(txt, delimiters=("", ""))
        res = re.sub('_', ' ', res)
        res = re.sub('-', ' ', res)
        return res

    def create_output(self, dataTweets, dataArticles, urls, monitored_tickers):
        scoresArticles = {ticker:self.sentiment(dataArticles[ticker]) for ticker in monitored_tickers}
        label = []
        output = []
        for ticker in monitored_tickers:
            label = []
            for counter in range(len(dataTweets[ticker])):
                score = self.sentiment(self.convertEmoji(dataTweets[ticker][counter]))
                output_this = [
                    ticker,
                    dataTweets[ticker][counter],
                    "Twitter",
                    score[0]['label'],
                    score[0]['score']
                ]
                label.append(score[0]['label'])
                output.append(output_this)
            for counter in range(len(dataArticles[ticker])):
                try:
                    output_this = [
                        ticker,
                        dataArticles[ticker][counter],
                        urls[ticker][counter],
                        scoresArticles[ticker][counter]['label'],
                        scoresArticles[ticker][counter]['score']
                    ]
                    label.append(scoresArticles[ticker][counter]['label'])
                    output.append(output_this)
                except IndexError:
                    print('List index out of range')                 
            self.plotPie(label, ticker)
            self.plotBar(label, ticker)
        output.insert(0, ['Ticker', 'Text', 'URLs', 'label', 'score'])
        return output







