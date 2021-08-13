import send_email

user = "abhi@test.com"
password = "AbhiPass@321"

def send(user, pass):
    send_email(user,pass)

send(user, password)
