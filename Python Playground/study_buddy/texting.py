from twilio.rest import Client

def text_msg(Xmessage):
    account_sid = 'no'
    auth_token = 'nah'
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body=Xmessage,
                        from_='+ok',
                        to='+haha'
                    )
     
    return message.sid

