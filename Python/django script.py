def water_mark(request):
	#add_mark(r'myQR.png', 'mark')
	if request.method == 'POST':
		fp = request.FILES.get('file')
		watermark = request.POST['watermark']
		if fp:
			path = 'input/' + fp.name
			print(path)
			with open(path, 'wb') as f:
				f.write(fp.read())
			print('Upload ok!')
		add_mark(r'input/'+fp.name, watermark)
		return FileResponse(open('output/'+fp.name, 'rb'))
	return render(request, 'Watermark.html')

def tax_cacl(request):
	if request.method == 'POST':
		form = TaxcaclForm(request.POST)
		if form.is_valid():
			quote = form.cleaned_data['quote'] # type:str
			if_tax = form.cleaned_data['if_tax'] # type:str
			tax_rate = form.cleaned_data['tax_rate'] # type:str
			price = quote
			# TODO: debug quote & if_tax & tax_rate to correct type
			if if_tax == 'True':
				price = float(price)
				tax_rate = float(tax_rate)
				tax = (tax_rate*price)/(tax_rate+1)
				return HttpResponse(f'Tax include, Price:{price}, Tax:{tax}')
			elif if_tax == 'False':
				price = float(price)
				tax_rate = float(tax_rate)
				tax = price*tax_rate
				price += tax
				return HttpResponse(f'Tax not include, Price:{price},Tax:{tax}')
	else:
		form = TaxcaclForm()
	return render(request, 'TaxCacl.html', {'form': form})

def qr(request):
	if request.method == 'POST':
		qr_type = request.POST['type']
		qr_data = request.POST['data']
		logo = request.FILES['logo']
		#logo Type:<class 'django.core.files.uploadedfile.InMemoryUploadedFile'>
		logo = Image.open(logo)
		#logo Type:<class 'PIL.JpegImagePlugin.JpegImageFile'>
		# Create qrcode
		qr_png = qrcode.make(qr_data)
		#qr_png.save('myQR.png')
		# Add logo inside the qrcode
		qr_w, qr_h = qr_png.size
		logo_w, logo_h = logo.size
		print(logo_w, logo_h)
		#logo resize
		######Setting########
		factor = 5 			#
		#####################
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
		qr_png.paste(logo, (w, h), mask=None)
		qr_png.save('myQR.png')
		#return HttpResponse(f'Submit OK! Data:{qr_data}')
		return FileResponse(open('myQR.png', 'rb'))
	return render(request, 'QRcode.html')


def json_ui(request):
	return render(request, 'ajax test.html')

def json_api_get(request):
	return JsonResponse({'code':200, 'msg':'ok', 'data':'get no params'})

def json_api_getparams(request):
	id = request.GET.get('id')
	return JsonResponse({'code':200, 'msg':'ok', 'data':'get with params, id={0}'.format(id)})

@csrf_exempt
def json_api_post(request):
	return JsonResponse({'code':200, 'msg':'ok', 'data':'post no params'})

@csrf_exempt
def json_api_postparams(request):
	id = request.POST.get('id')
	return JsonResponse({'code':200, 'msg':'ok', 'data':'post with params, id={0}'.format(id)})

@csrf_exempt
def json_api_postform(request):
	params = json.loads(request.body)
	name = params.get('name')
	age = params.get('age')
	return JsonResponse({'code':200, 'msg':'ok', 'data':'post with params, name={0}, age={1}'.format(name,age)})