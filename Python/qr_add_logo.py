import qrcode
import time
from PIL import Image


def qrcode_add_logo(data, logo_png='logo.png', output='myQR with logo.png'):
	qr_img = qrcode.make(data)
	qr_img.save('myQR.png')
	#get w,h of qrcode img, default 330 X 330
	qr_w, qr_h = qr_img.size
	#input logo png
	logo = Image.open(logo_png)
	logo_w, logo_h = logo.size
	print(logo_w, logo_h)
	#logo resize
	factor = 3 #setting
	size_w = int(qr_w / factor)
	size_h = int(qr_h / factor)
	if logo_w > size_w:
		logo_w = size_w
	if logo_h >size_h:
		logo_h = size_h
	logo = logo.resize((logo_w, logo_h), Image.ANTIALIAS)
	#Centered logo
	w = int((qr_w - logo_w) / 2)
	h = int((qr_h - logo_h) / 2)
	qr_img.paste(logo, (w, h), mask=None)
	qr_img.save(output)



if __name__ == '__main__':
	# ticks = time.time()
	data = 'qrcode add logo test.'
	qrcode_add_logo(data)