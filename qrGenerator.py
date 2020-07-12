# Generating svg file
# pip install pyqrcode
# import pyqrcode 
# s = "<Link>"
# url = pyqrcode.create(s) 
# url.svg("myqr.svg", scale = 8)

# -------------------------------------

# Generating other types
# pip install qrcode[pil]
import qrcode

data = "<Link>"
filename = "./image.png"
img = qrcode.make(data)
img.save(filename)