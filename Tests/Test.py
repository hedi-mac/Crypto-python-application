from TextBlobAnalysis import TextBlobAnalysis
from HuggingFaceTransformersAnalysis import HuggingFaceTransformersAnalysis
import pandas as pd
import emoji
import re

def convertEmoji(txt):
        res = emoji.demojize(txt, delimiters=("", ""))
        res = re.sub('_', ' ', res)
        res = re.sub('-', ' ', res)
        return res
        

TextData = ["Even the most profitable days eventually have their sunsets.",
        "Bitcoin will no longer go down.",
        "The cryptocurrency is up more than 10% for the week so far. Job growth remained strong.",
        "Bitcoin will fly high",
        "El Salvador adopted Bitcoin as its official currency",
        "No more ban for cryptocurrencies",
        "some states ban cryptocurrencies",
        "he didn't accept bitcoin transactions",
        "Money talks... money is getting tight. I'd hate to be playing with fake money.",
        "I hate bitcoin", 
        "Bitcoin market is weakly trending down current momentum suggests the market is neutral.",
        "Technical indicators point to a bottom, analysts say. Bitcoin has lost more than 70% since hitting November high",
        "We are aware of the issue and are working to resolve it.",
        "Bitcoin today 😍",
        "Bitcoin is 📉 these days"
        ]
ExpectedResult = [ "POSITIVE", "POSITIVE", "POSITIVE", "POSITIVE", "POSITIVE", "POSITIVE", "NEGATIVE",
                "NEGATIVE", "NEGATIVE", "NEGATIVE", "NEGATIVE", "NEGATIVE", "NEGATIVE", 
                "POSITIVE", "NEGATIVE" ]

df = pd.DataFrame(TextData, columns=['Text'])
df['Text Blob'] = df['Text'].apply(convertEmoji).apply(TextBlobAnalysis.getPolarity).apply(TextBlobAnalysis.getSentiment)
df['Transformers'] = df['Text'].apply(convertEmoji).apply(HuggingFaceTransformersAnalysis.getSentiment)
df['Expected'] = ExpectedResult

print('\n--------------------------------------------------------------------------------------\n')
print(df.head(11))
print('\n--------------------------------------------------------------------------------------\n')
print(df.tail(2))


