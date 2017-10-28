class Ip(object):
	"""Creates an IP address object."""

	def __init__(self, givenAddress):
		"""
		Initializes the address.
		
		:param givenAddress: The address
		"""
		self.address = givenAddress

	def __str__(self):
		"""
		Prints the address.
		
		:return: the address
		"""
		return str(self.address)

	def __repr__(self):
		"""
		Prints the address.
		
		:return: the address
		"""
		return str(self.address)

	@property
	def address(self):
		"""
		Property to get the value of the address.
		
		:return: the address
		"""
		return self._address
		
	@address.setter
	def address(self, address):
		"""
		Property to set the value of the address.
		"""
		self._address = address
