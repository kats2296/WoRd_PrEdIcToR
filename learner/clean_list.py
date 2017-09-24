import requests
from bs4 import BeautifulSoup
import r

def split_line(text):

    # split the text
    words = text.split()

    # for each word in the line:
    for word in words:

        # print the word
        listword.append(word)

listword=[]
symbols="!123456789@#$%^&*()_\"<>?:_-'"

url="https://twitter.com/realDonaldTrump"
r=requests.get(url)
r.content
soup=BeautifulSoup(r.content,"html.parser")

tweet = soup.find_all('p',{"class": "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"})
i=1
for p in tweet:
	split_line(p.getText())
	i=i+1


"""
with open('word3.txt', 'r') as f:
    for line in f:
        for word in line.split():
        	listword.append(word)
        	
            r = re.compile("([a-zA-Z]+)([0-9]+)")
            m = r.match(str(word))
            print(m.group(1))
"""



def clean_up_list(listword):
	clean_word_list=[]
	for word in listword:
		for i in range(0,len(symbols)):
			word=word.replace(symbols[i],"")
		if len(word)>0:
			clean_word_list.append(word)
			r.updatefile(word.lower())
	"""
	for i in clean_word_list:
		print(i)
	"""


clean_up_list(listword)
