import usb.core

dev = usb.core.find(idVendor='0d28', idProduct='0204')
if dev is None:
	raise ValueError('maxsonar ez1 not found')
else:
	while True:
		data=dev.read()
		print data

