import qrcode

# The URL the QR code links to — your GitHub Pages site
url = "https://margaretgitonga.github.io/LE_Margaret_Gitonga/"

img = qrcode.make(url)
img.save("leverage_expert_vcard.png")

print("QR code saved as leverage_expert_vcard.png")
print("Scanning it opens: " + url)