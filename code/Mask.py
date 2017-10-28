class Mask(object):
	"""Creates a subnet mask object."""

	def __init__(self, givenMask):
		"""
		Initializes the mask.
		
		:param givenMask: The mask
		"""
		self.mask = givenMask

	def __str__(self):
		"""
		Prints the mask.
		
		:return: the mask
		"""
		return str(self.mask)

	def __repr__(self):
		"""
		Prints the mask.
		
		:return: the mask
		"""
		return str(self.mask)

	@property
	def address(self):
		"""
		Property to get the value of the mask.
		
		:return: the mask
		"""
		return self._mask
		
	@address.setter
	def address(self, mask):
		"""
		Property to set the value of the mask.
		"""
		self._mask = mask
