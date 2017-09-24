import requests
from bs4 import BeautifulSoup
from selenium import webdriver

driver=webdriver.Chrome()
#driver.set_page_load_timeout(50)

url="http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_A-B/?page=1"
driver.get("http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_A-B/?page=1")
i=2
k=2

fp=open("words.txt","w")

while(True):
	
	flag=1
	r= requests.get(url)
	r.content
	soup = BeautifulSoup(r.content , "html.parser")
	words = soup.find_all('ul',{"class":"result-list1 wordlist-oxford3000 list-plain"})
	#print driver.current_url

	for p in words:
		try:
			fp.write(p.getText())
		except:
			pass
		print(p.getText())



	st = '//*[@id="paging"]/div/ul/li['
	vt=']/a'
	var = st+str(i)+vt
	if(i==2):
		i=i+1
	i=i+1

	try:
		try:
			but_click = driver.find_element_by_xpath(var);
			but_click.click()
			url= driver.current_url
			
			
		except:

			es = '//*[@id="entries-selector"]/ul/li['
			est =']/a'
			var1=es+str(k)+est
			but_click1 = driver.find_element_by_xpath(var1);
			but_click1.click()
			url= driver.current_url
			i=2
			k=k+1
	except:
		flag=0
		break

fp.close()
print('Finished')

