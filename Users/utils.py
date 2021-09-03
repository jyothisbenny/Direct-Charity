from twilio.rest import Client
from decouple import config


client = Client(config("TWILIO_ACCOUNT_SID"), config("TWILIO_AUTH_ID"))


def send_sms(otp, phone):
    phone = "+91" + phone

    message = client.messages.create(
        body=f'Hi there! You can use this OTP {otp} for verifying your DirectCharity Account',
        from_='+1 210 981 4291',
        to=f'{phone}'
    )

    print(message.sid)
