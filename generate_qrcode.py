import qrcode

# The URL people will land on when scanning the QR code
url = "https://margaretgitonga.github.io/LE_Margaret_Gitonga/"

img = qrcode.make(url)
img.save("leverage_expert_vcard.png")

print("QR code saved as leverage_expert_vcard.png")
print("Scanning it opens: " + url)