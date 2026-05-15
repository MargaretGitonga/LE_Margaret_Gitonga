import qrcode

# The URL people will be directed to when scanning the QR code
url = "https://silvamontanaresort.github.io/leverage_expert/"

# Create the QR code
img = qrcode.make(url)

# Save the file
img.save("leverage_expert_vcard.png")

print("Success! Your QR code is saved as leverage_expert_vcard.png")