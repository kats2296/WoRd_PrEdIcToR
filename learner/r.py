def updatefile(data): 
	fp = open("word3.txt" , "r")
	str2 = fp.read()

	str1 = str(data)
	l = len(str1)

	with open("word3.txt" , "r+") as f :
		content=f.read()
		try:
			i=content.index(str1)
		except:
			return
		f.seek(i,0)
		x=f.tell()
		#print(x)
		u=0
		n=0
		while u < x :
			if str2[u] == "\n" :
				n=n+1

			u=u+1

		if str2[x+l+1]=="\n" :
			ch = str2[x+l] 
			
			try:
				ch_i = int(ch)
				ch_i+=1
			except:
				return
		
			str2.replace(str2[x+l] , str(ch_i))

			f.seek(x+l+n,0)
			f.write(str(ch_i))


		else :

			ch = str2[x+l+1]
			try:
				ch_i = int(ch)
				ch_i+=1
			except:
				return
			str2.replace(str2[x+l+1] , str(ch_i))

			f.seek(x+l+1+n,0)
			f.write(str(ch_i))


	fp.close()
