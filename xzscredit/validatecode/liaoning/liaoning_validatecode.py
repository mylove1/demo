# coding:utf-8
import pytesseract
import io
from PIL import Image
import urllib2



url = "http://gsxt.lngs.gov.cn/saicpub/commonsSC/loginDC/securityCode.action?tdate=39663"
r = urllib2.urlopen(url)
data_stream = io.BytesIO(r.read())
image = Image.open(data_stream)
image.show()
code = pytesseract.image_to_string(image)
print code