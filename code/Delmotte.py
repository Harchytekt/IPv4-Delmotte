import ui
from Ip import *
from Mask import *

v = ui.load_view('Delmotte')
myIPAddress = Ip('192.168.42.12')
myMask = Mask('24')
fr = ['IPv4- Méthode Delmotte', 'Adresse IP :', 'Masque :', 'Réseau :', 'Réseau suivant :', 'Broadcast :', 'Plage :', 'Nombre d\'hôtes réels :']
en = ['IPv4- Delmotte’s method', 'IP address:', 'Mask:', 'Network:', 'Next network:', 'Broadcast:', 'Scope:', 'Number of real hosts:']


def display_infos():
	"""
	Displays the network informations.
	"""
	mask = myMask.mask
	ip = myIPAddress.address
	if mask == '0':
		mask = '1'
	elif mask == '31' or mask == '32':
		mask = '30'
	v['mask_label'].text = cidrToDec(mask) + ' (/' + mask + ')'
	AR, ARS, BC, P1, P2, nbrHosts = calculates(ip, mask)
	realsHosts = str((2 ** nbrHosts) - 2)
	v['ar_label'].text = AR
	v['ars_label'].text = ARS
	v['bc_label'].text = BC
	v['scope_label1'].text = P1
	v['scope_label2'].text = P2
	v['hosts_label'].text = realsHosts


def inputField_action(sender):
	"""
	Gets the address from the text field and verifies if its format is good.
	Calls the display function
	"""
	global myIPAddress
	ip = sender.text
	if isAnAddress(ip):
		myIPAddress = Ip(ip)
		display_infos()
	else :
		v['inputField'].text = ''
		v['inputField'].placeholder = 'Format: 192.168.42.12❗️'


def slider_action(sender):
	"""
	Gets the subnet mask from the slider.
	Calls the display function.
	"""
	global myMask
	myMask = Mask(str(int(sender.value*32)))
	display_infos()


def langChoice_action(sender):
	"""
	Gets the chosen language for the GUI.
	Calls the function to set the language.
	"""
	if sender.selected_index == 0:
		setLang(fr)
	else:
		setLang(en)


def isAnAddress(ip):
	"""
	Verifies if the given IPv4 address has the good format.
	"""
	if not '.' in ip :
		return False
	elif not len(ip.split('.')) == 4 :
		return False
	else:
		for item in ip.split('.'):
			if not item.isdecimal():
				return False
	return True


def setLang(dic):
	"""
	Sets the GUI to the chosen language.
	"""
	v['title'].text = dic[0]
	v['label1'].text = dic[1]
	v['label2'].text = dic[2]
	v['label3'].text = dic[3]
	v['label4'].text = dic[4]
	v['label5'].text = dic[5]
	v['label6'].text = dic[6]
	v['label7'].text = dic[7]


def cidrToDec(cidr):
	"""
	Returns the subnet mask in decimal.
	"""
	t = ["0", "0", "0", "0"]
	(i, cidr) = (0, int(cidr))
	
	while (i < 4):
		if (cidr >= 8):
			t[i] = "255"
			cidr -= 8
			i += 1
		else:
			if (cidr == 7):
				t[i] = "254"
			elif (cidr == 6):
				t[i] = "252"
			elif (cidr == 5):
				t[i] = "248"
			elif (cidr == 4):
				t[i] = "240"
			elif (cidr == 3):
				t[i] = "224"
			elif (cidr == 2):
				t[i] = "192"
			elif (cidr == 1):
				t[i] = "128"
			i = 4
	
	return ".".join(t)


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


input = v['inputField']
input.action = inputField_action
slider = v['slider']
slider.continuous = True
slider.action = slider_action
lang = v['langChoice']
lang.action = langChoice_action

v.present('sheet')

