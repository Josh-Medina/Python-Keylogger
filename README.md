# Python Keylogger

This Python keylogger records keystrokes and emails them when a preset number is reached.

This project represents my first venture into Python cybersecurity tools, showcasing my learning journey and exploration of practical applications in the field. You can check out the video demonstration here: https://youtu.be/icJmkVbXp0g

If you just want the code with no descriptive comments use the Code-only-keylogger file.
## Description

- **Keylogger Functionality**: The Python script serves as a proof of concept keylogger designed to record keystrokes and transmit them via email. 
- **Email Transmission**: Upon execution, it captures typed keys, storing them in RAM until a predefined limit is reached. At this threshold, the accumulated keystrokes are formatted into an email message and sent. 
- **Memory Management**: After sending the email, the memory storage is cleared to accommodate new keystrokes. 
- **Concurrency**: The script utilizes threading to concurrently log keystrokes and handle email transmission. 
- **Email Formatting**: The script formats the email for easier readability of the logged keystrokes. 
- **Enhanced Security**: Users can enhance security by setting an environmental variable to obscure the email password.

**It's essential to emphasize that this tool is intended solely for educational purposes!**
