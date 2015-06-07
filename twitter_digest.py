import urllib2
import unicodedata
import datetime
from bs4 import BeautifulSoup


day=int(datetime.date.today().day)
str_day = str(day)
day_len=len(str_day)

users=['BarackObama','narendramodi','BillGates','CNN',
		'nytimes','BBCBreaking','espn','TheEconomist','business',
		'TIME','Forbes','Reuters','TEDTalks','timesofindia',
		'the_hindu','ndtv']

for user in users:
	link = "https://twitter.com/"+user

	url2 = urllib2.urlopen(link)
	soup2 = BeautifulSoup(url2)
	var3 = soup2.find('title')
	
	print "\n"
	print user
	var2=soup2.find_all("li",{"data-item-type":"tweet"})
	#user_name = soup2.find('div',{"class","stream-item-header"})
	#print user_name.get('strong')
	i=1
	for items in var2:
		date=items.find('a',{"class":"tweet-timestamp js-permalink js-nav js-tooltip"})
		try:
			title=(date.get('title').encode('ascii','ignore'))
		except:
			pass
		 
		if (len(title)>16):
			title=title.lstrip('1')
		
		sample_date=title[8:10]
	
		if str_day in sample_date:
			if (day_len==1 and sample_date[1]==" "):
				l=str(i)+'.'
				print l,items.find("p").text
				i=i+1
			elif (day_len==2 and sample_date[1]!=" "):
				l=str(i)+'.'
				print l, items.find("p").text
				i=i+1
			else:
				pass