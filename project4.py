import qrcode

upi_id = input("Enter your UPI ID = ")

phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

phonepe_qr = qrcode.make(phonepe_url)

phonepe_qr.save('phonepe_qr.png')

phonepe_qr.show()