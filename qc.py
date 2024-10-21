import qrcode as qr

def filename(url):
    elements = url.split("/")
    return elements[len(elements) - 1] + ".png"

isValid = True
prompt = None
while isValid:
    prompt = input("Enter the valid URL: ")
    if prompt[0:8] == "https://":
        isValid = False
    else:
        print("URL should start with https://")

img = qr.make(prompt)
filename = filename(prompt)
img.save(filename)