import qrcode

'''initialize
-CMD pip install qrcode[pil]
'''

# easy way
# qr = qrcode.make('hello world')
# qr.save('myQR.png')

qr = qrcode.QRCode(
	#range 1-40
	version = 1,
	#TODO:error correction not work
	#error_correction = qrcode.constants.ERROR_CORRECT_M
	box_size = 15,
	border = 5
	)
data = 'https://www.baidu.com'
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='yellow')
img.save('standard QR.png')
