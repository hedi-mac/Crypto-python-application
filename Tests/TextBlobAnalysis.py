from textblob import TextBlob

class TextBlobAnalysis : 

    #Get the subjectivity of the tweets
    def getSubjectivity(txt):
        return TextBlob(txt).sentiment.subjectivity
    #Get the polarity of the tweets 
    def getPolarity(txt):
        return TextBlob(txt).sentiment.polarity

    #Get the text sentiment of the tweets
    def getSentiment(score):
        if score < 0 :
            return 'Negative'
        elif score == 0 :
            return 'Neutral'
        else : 
            return 'Positive'

