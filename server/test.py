import resend

resend.api_key = "re_chB8ktT1_EgTTewUqXk15U57vBzrnQ3AA"

r = resend.Emails.send({
  "from": "onboarding@resend.dev",
  "to": "fmwaniki986@gmail.com",
  "subject": "Hello World",
  "html": "<p>Congrats on sending your <strong>first email</strong>!</p>"
})


def send_email():
    return r


