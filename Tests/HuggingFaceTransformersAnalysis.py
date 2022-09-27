from asyncio.windows_events import NULL
from transformers import PegasusTokenizer, PegasusForConditionalGeneration
from bs4 import BeautifulSoup
import requests 
from transformers import pipeline
import matplotlib.pyplot as plt
import pandas as pd 

class HuggingFaceTransformersAnalysis : 
    
    sentiment = pipeline('sentiment-analysis')
    model_name = "human-centered-summarization/financial-summarization-pegasus"
    tokenizer = PegasusTokenizer.from_pretrained(model_name)
    model = PegasusForConditionalGeneration.from_pretrained(model_name)

    def summarize(article):
        input_ids = HuggingFaceTransformersAnalysis.tokenizer.encode(article, return_tensors='pt')
        output = HuggingFaceTransformersAnalysis.model.generate(input_ids, max_length=25, num_beams=5, early_stopping=True)
        return HuggingFaceTransformersAnalysis.tokenizer.decode(output[0], skip_special_tokens=True)

    def getSentiment(text):
        #text = HuggingFaceTransformersAnalysis.summarize(text)
        tab = HuggingFaceTransformersAnalysis.sentiment(text)
        return tab[0]['label']







