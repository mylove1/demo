import requests
from PIL import Image
import pytesseract
import time

image = requests.get('http://wenshu.court.gov.cn/User/ValidateCode/8259').content
with open('jpg.jpg', 'wb') as imag:
    imag.write(image)
time.sleep(0.1)
image = Image.open('jpg.jpg')
code = pytesseract.image_to_string(image)
print code
codedata = {'ValidateCode': code}
a = requests.post('http://wenshu.court.gov.cn/Content/CheckVisitCode', headers=headers, data=codedata)
print 'ok'