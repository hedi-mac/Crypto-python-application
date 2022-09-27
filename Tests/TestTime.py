from TextBlobAnalysis import TextBlobAnalysis
from HuggingFaceTransformersAnalysis import HuggingFaceTransformersAnalysis
import pandas as pd
from datetime import datetime

time = []
methods = ['Text Blob', 'Transformers']

text = "Even the most profitable days eventually have their sunsets."
stTimetxtBlob = datetime.now()
TextBlobAnalysis.getPolarity(text)
t = datetime.now() - stTimetxtBlob
tStr = f"{t}"
tStr = f"{tStr[tStr.rindex(':')+1:]} s"
time.append(tStr)
stTimeTransformers = datetime.now()
HuggingFaceTransformersAnalysis.getSentiment(text)
t = datetime.now() - stTimeTransformers
tStr = f"{t}"
tStr = f"{tStr[tStr.rindex(':')+1:]} s"
time.append(tStr)
df = pd.DataFrame(methods, columns=['Method'])
df['Execution Time'] = time

print(df.head(2))

