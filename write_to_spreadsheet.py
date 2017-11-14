def writespreadsheet():
	s = "Hello"
	
	with open('practice.csv', mode='wt') as csvfile:
		myfile = csv.writer(csvfile, delimiter = ',', quotechar='"',
				    quoting = csv.QUOTE_MINIMAL)
		myfile.writerow(["4", "5"])

