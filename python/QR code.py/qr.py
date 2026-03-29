import qrcode
qr =qrcode.make("https://www.instagram.com/reel/DWJFnhVjYqv/?igsh=MWxhOW10azhwYmcwMA==")
qr.save ('img.png')
qr.show()



# import qrcode

# qr =qrcode.QRCode(box_size=100)
# qr.add_data("hii")  #to add data
# qr.make()
# img=qr.make_image(fill_color="blue")
# img.save ("img.png")
# img.show()