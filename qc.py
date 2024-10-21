import qrcode as qr

isValid = True
prompt = None
while isValid:
    prompt = input("Enter the valid URL: ")
    if prompt[0:8] == "https://":
        isValid = False
    else:
        print("URL should start with https://\n")

img = qr.make(prompt)
img.save(prompt[9:] + ".png")
