import pyqrcode
from PIL import Image

def qr():
    link=input("enter qr: ")
    qr_code=pyqrcode.create(link)
    qr_code.png("QRCode.png", scale=5)
    Image.open("QRCode.png")
    
    
if __name__ == "__main__":
    qr()