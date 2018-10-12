import pyqrcode
from PIL import Image
import csv

with open("passcode.tsv") as fd:
    rd = csv.reader(fd, delimiter="\t", quotechar='"')
    for row in rd:
        # print row
        passcode = pyqrcode.QRCode(row[1], error = 'H')
        passcode.png('test.png',scale=14)
        im = Image.open('test.png')
        im = im.convert("RGBA")
        logo = Image.open('logo.png')
        box = (165,165,245,245)
        im.crop(box)
        region = logo
        region = region.resize((box[2] - box[0], box[3] - box[1]))
        im.paste(region,box)
        im.save('export/'+row[0]+'.png', "PNG")