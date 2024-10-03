import  qrcode

#Taking UPI ID as a input
upi_id = input("enter your UPI ID = ")

#upi://pay?pa=<UPI_ID>&pn=<RecipientName>&am=<Amount>&cu=INR&tn=<MESSAGE>

#Defining the payment URL based on the UPI ID  the payment app
#You can modify these URLs based on the payment apps you want to support

phonepe_url = f'upi://pay?pa={upi_id}&pn=RecipientName&am=1&cu=INR'
paytm_url = f'upi://pay?pa={upi_id}&pn=RecipientName&am=1&cu=INR'
google_pay_url = f'upi://pay?pa={upi_id}&pn=RecipientName&am=1&cu=INR'

#create QR Code for each payment app
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

#Save thQR COde to image file (optional)
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')

#Display the QR Codes (you may need to install PIL?Pillow Library)
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()