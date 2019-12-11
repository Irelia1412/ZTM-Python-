from twilio.rest import Client

account_sid = 'AC5ffe406ff202eefbe14ff32ce624fa48'
auth_token = '54877ca2994403735b80589a2e080b93'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+13234319348',
    body='I love you LEWDS',
    to='+18638521294'
)

print(message.sid)