# import module
from pdf2image import convert_from_path


# Store Pdf with convert_from_path function
images = convert_from_path('bijlage-5-van-15-bij-tweede-deelbesluit-wob-verzoek-covid-19-iccb-stukken.pdf')

for i in range(len(images)):

	# Save pages as images in the pdf
	#WARNING it must be str(i)
	images[i].save('page'+ str(4) +'.jpg', 'JPEG')
