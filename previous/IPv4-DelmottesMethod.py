def calculates(ip, mask):
	"""
	This is the main function of this programm.
	It takes th e IPv4 address and the subnet mask, and returns a tuple
	containing the addresses and the number of real hosts. 
	"""
	(t, msk) = (ip.split("."), int(mask))
	(alpha, i, q) = (int(mask), 0, 0)
	if 25 <= alpha <= 32:
		q = 2 ** (32 - alpha)
		addr = calcAddr(t, i)
		AR = greaterMult(int(t[len(t) - (i + 1)]), q)
		ARS = AR + q
		BC = ARS - 1
		(P1, P2) = (AR + 1, BC - 1)
		realHosts = (32 - msk)
	
	else:
		while alpha < 25:
			i += 1
			alpha += 8
	
		q = 2 ** (32 - alpha)
		addr = calcAddr(t, i)
		AR = greaterMult(int(t[len(t) - (i + 1)]), q)
		ARS = AR + q
		BC = ARS - 1
		(P1, P2) = (AR, BC)
		realHosts = (32 - msk)
	
	(addR, addRS, addBC) = (createsAdd(addr, AR, i, 0),
	createsAdd(addr, ARS, i, 0), createsAdd(addr, BC, i, -1))
	return (addR, addRS, addBC, createsAdd(addr, P1, i, 1),
	createsAdd(addr, P2, i, -2), realHosts)


def calcAddr(t, i):
	"""
	This function will return th IPv4 address until the (len(t) - i) - 1 index
	(the element before that we change for the different responces).
	"""
	(index, res) = (0, "")
	while index < (len(t) - i) - 1:
		res += t[index]
		res += "."
		index += 1
	return res


def greaterMult(value, q):
	"""
	Calculates the greater multiple of 'q', which will be smaller
	or equal to 'value'.
	"""
	if ((value - q) <= 0) and (value != q):
		return 0
	else:
		return value - (value % q)


def createsAdd(addr, value, i, x):
	"""
	Return the value of the index to change.
	"""
	val = str(value)
	if i == 0:
		return addr + val
	else:
		addr += val
		while i != 0:
			if (x == 0) or (x == 1 and i != 1):
				addr += ".0"
			elif (x == -1) or (x == -2 and i != 1):
				addr += ".255"
			elif x == -2:
				addr += ".254"
			elif x == 1:
				addr += ".1"
			i -= 1
		return addr


def addresseInput():
	"""
	Asks to the user to enter an IPv4 address and a subnet mask
	(with CIDR notation) in two steps.
	"""
	ipAdd = raw_input("Enter the IPv4 address (eg: 192.168.1.1): \n")
	subNet = raw_input("""Enter the subnet mask in 
	CIDR notation (eg: 26 for /26): \n""")
	return (ipAdd, subNet)


def addresseInput2():
	"""
	Asks to the user to enter an IPv4 address and a subnet mask
	(with CIDR notation) in one step.
	"""
	inpt = raw_input("Enter the IPv4 address (eg: 192.168.1.1/26): \n")
	t = inpt.split("/")
	return (t[0], t[1])



if __name__ == '__main__':
	(ipAdd, subNet) = addresseInput2()
	(AR, ARS, BC, P1, P2, realsHosts) = calculates(ipAdd, subNet)
	nbrH = (2 ** realsHosts) - 2
	
	print "\n" + ipAdd + "/" + subNet + " :"
	print "Network Address = " + AR + "/" + subNet
	print "Next Newtork Address = " + ARS + "/" + subNet
	print "Broadcast Address = " + BC + "/" + subNet
	print "Range of Addresses = " + P1 + " ==> " + P2
	print "Number of Available Hosts: 2^" + str(realsHosts)+" - 2 = "+str(nbrH)