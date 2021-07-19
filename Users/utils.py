from twilio.rest import Client

account_sid = 'AC838ae4615669dc8c39c858949bfcbe60'
auth_token = 'a6fe90246c9783e7ee0e6567950afc43'
client = Client(account_sid, auth_token)


def send_sms(otp, phone):
    phone = "+91" + phone

    message = client.messages.create(
        body=f'Hi there! You can use this OTP {otp} for verifying your DirectCharity Account',
        from_='+1 210 981 4291',
        to=f'{phone}'
    )

    print(message.sid)
