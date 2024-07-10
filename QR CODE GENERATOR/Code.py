"""
GENERATOR QR Code

# for generate qr code use qrcode library
# for display qr code use pillow library

Step 1 :: get upi id from user
Step 2 :: for different applications difine different URL in this include upiId or some other details
Step 3 :: generate qr code for all applications like phone pe,paytm,Gpay using qrcode.make
Step 4 :: Save qrcode as img in your system folder
Step 5 :: Display Generated qrcode  using pillow viewer

-PIL or pillow viewer is library use for image processing

Payment URL formate :: #upi?pa=UPI_ID&apn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE
 - pa - payment action
 - pa=upi - for upi payment
 - upiId - upi id
 - apn - application name
 - am - amount
 - cu - currency
 - tn - transaction note
"""

import qrcode

# get upi id from user as input
upi_id = input("Enter UPI ID: ")



# define the payment URL based on the UPI ID and the payment application
# we can modify these URLs based on the payment apps we want to support

phonepe_url=f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234" # mc=merchant code
paytm_url=f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
google_pay_url=f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"

# create qr codes for each payment app

phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

# save qr codes as images in your system folder

phonepe_qr.save("phonepe_qr.png")
paytm_qr.save("paytm_qr.png")
google_pay_qr.save("google_pay_qr.png")

# display generated qr codes using pillow viewer
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()
