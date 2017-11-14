class House:
	def __init__(self, streetlocation, price, size, color):
		"""Price is in millions
		size is in square feet

		"""
		self.streetlocation = streetlocation
		self.price = 1000000*price
		self.size = size
		self.color = color

	def priceperfoot(self):
		return self.price/self.size

	def expandHouse(self, expansionSize):
		"""Expands house size based on int value passed in as expansion size.
		Asks for confirmation once showing the effect on house price. 
		Cost is calculated using priceperfoot

		"""
		newprice = self.price + (expansionSize*self.priceperfoot())
		response = 'A'

		while(response != 'Y' and response != 'N'):
			print("This will increase your house price from " + str(self.price) + "\n")
			response = input("to $" + str(newprice) + ". Is this OK? Y or N. \n")

			if response == 'Y':
				self.price = newprice
				self.size += expansionSize

			elif response == 'N':
				print("This construction has been aborted.\n")

			else:
				print("That is not a valid response. Please try again.\n")


