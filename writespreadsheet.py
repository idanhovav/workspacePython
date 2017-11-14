def writespreadsheet(word):
	""" Must import csv before running

	"""
	#'practice.csv' is the file name. Since we're in mode w, writing, we create
	#this new file 'practice.csv'. 
	#w in mode is writing out, r is reading in
	#b in mode is binary, t is text
	#delimiter is what separates the elements of the sequence
	#quotechar is what's used to enquote the elements

	with open('practice.csv', mode='wt') as csvfile:
		myfile = csv.writer(csvfile, delimiter = ',', quotechar='"',
				    quoting = csv.QUOTE_MINIMAL)
		myfile.writerow(["4", "5", str(word)])

