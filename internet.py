import urllib.request
def getFriends():
	a = urllib.request.urlopen("https://idanhovav.github.io")
	code = a.read(100000)
	

if __name__ == '__main__':
	getFriends()