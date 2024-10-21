import qrcode as qr

img = qr.make("https://github.com/sudesh-tnbt")
img.save("github.png")
