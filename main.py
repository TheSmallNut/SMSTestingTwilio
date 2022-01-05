import secretVariables
from twilio.rest import Client

account_sid = secretVariables.accountID
auth_token = secretVariables.authToken

client = Client(account_sid, auth_token)


message = client.messages \
                .create(
                    body="Did this work?",
                    from_='+16602353227',
                    to='+14253267909'
                )
