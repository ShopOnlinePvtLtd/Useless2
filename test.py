import send_email

user = "abhi@test.com"
password = "AbhiPass@321"

def send(user, pass):
    send_email(user,pass)


pass_sec = "abhiAbhiABhi310a##"

pass_sec2 = "abhiiABhi310a##@@"

pass_sec3 = "abhiiA$#$#123" # BluBracketIgnore

pass_sec4 = "abhiiA$#$#123Sec" # BluBracketIgnore

pass_sec5 = "abhiiA$#$#123Secingnoreme"  #BluBracketIgnore

send(user, password)
