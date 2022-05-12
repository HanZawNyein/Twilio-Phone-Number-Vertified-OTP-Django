from twilio.rest import Client

account_sid = 'ACf4f3a8db6760d3dd7edec01e002a3ea9'
auth_token = '664927e03a85312dcbff62162288fe0c'
client = Client(account_sid, auth_token)

message = client.messages.create(
    messaging_service_sid='MGa11e3ead56c5237833e779f317f1dffc',
    body='Hello Testing',
    to='+959979886604'
)

print(message.sid)

