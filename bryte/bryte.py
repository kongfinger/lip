import newsapi
from nltk.sentiment import SentimentIntensityAnalyzer
import datetime
import nltk
from newsapi import NewsApiClient

sia = SentimentIntensityAnalyzer()

tokenizer = RegexpTokenizer(r'\w+')

newsapi = NewsApiClient(api_key='your api key')

nw = newsapi.get_everything(q='ukraine russia')

b=open('b.log')
g=b.read()
b.close()
t=0.0
c=0.0
d=0.0

p=0.0
pp=0.0
ppp=0.0

for x in nw['articles']:
	p=p+len(nltk.tokenize.word_tokenize(x['title']))
	pp=pp+len(nltk.tokenize.word_tokenize(x['content']))
	ppp=ppp+len(nltk.tokenize.word_tokenize(x['description']))
	t=t+sia.polarity_scores(x['title'])['compound']
	c=c+sia.polarity_scores(x['content'])['compound']
	d=d+sia.polarity_scores(x['description'])['compound']
	print(p,pp,ppp,t,c,d)
lll = len(nw['articles'])
avgt=t/lll
avgtl=float(p)/lll
avgc=c/lll
avgcl = float(pp)/lll
avgd=d/lll
avgdl = float(ppp)/lll
f=str(datetime.datetime.now())+','+str(avgt)+','+str(avgtl)+','+str(avgc)+','+str(avgcl)+','+str(avgd)+','+str(avgdl)+'\n'
a=g+f
u=open('b.log','w')
u.write(a)
u.close()
