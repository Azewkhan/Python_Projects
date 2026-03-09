import pyqrcode

value = input("Enter the Phrase/Code/Password or anything you want to convert into QR code")
url = pyqrcode.create(value) # convert string into QR code
url.svg("My QR code.svg", scale=8) # save as svg file (not png or jpg)