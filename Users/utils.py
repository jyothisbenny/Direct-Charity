from twilio.rest import Client

account_sid = 'AC838ae4615669dc8c39c858949bfcbe60'
auth_token = '9e1e3cde071fc1020b2843c7189078c9'
client = Client(account_sid, auth_token)


def send_sms(otp, phone):
    phone = "+91" + phone

    message = client.messages.create(
        body=f'Hi there! this is your One Time Password {otp}',
        from_='+1 210 981 4291',
        to=f'{phone}'
    )

    print(message.sid)
