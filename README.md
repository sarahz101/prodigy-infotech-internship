
TASK 1:
Caesar cipher implementation in Python. It's a simple encryption/decryption tool that shifts letters by a fixed number of positions in the alphabet.

What it does:
Takes user input for text, a shift key (integer), and a choice (1 to encrypt, 2 to decrypt)
Encrypt function: Shifts each letter forward by the key amount while preserving case (uppercase/lowercase)
Decrypt function: Shifts each letter backward by the key amount to reverse the encryption
Non-alphabetic characters are left unchanged
Outputs the encrypted or decrypted result

Key details:
Uses modulo 26 arithmetic to wrap letters around the alphabet
Handles both uppercase (A-Z) and lowercase (a-z) letters separately
Invalid menu choices cause the program to exit
This is a classic cryptography exercise commonly used in programming courses and internship programs.


TASK 2:
This Python script implements a simple image encryption and decryption tool using pixel manipulation.

What it does:
encryption(): Takes an image, adds a numeric key to each pixel value (mod 256), and saves the encrypted result
decryption(): Takes an encrypted image, subtracts the same key from each pixel values (mod 256), and saves the decrypted result
Main flow: Prompts the user to input an image file, encryption key, choose between encrypt (1) or decrypt (2), and specify an output filename
How it works:

The script converts the image into a NumPy array of pixel values, performs modular arithmetic operations with the key, and converts it back to an image. This is a basic cipher — adding/subtracting the same value to all pixels shifts their brightness uniformly.

Note: This is a simple proof-of-concept encryption. For actual secure image encryption, you'd want to use proper cryptographic algorithms rather than basic pixel shifting.


TASK 3:
This file implements a password strength validator that checks if a user-entered password meets specific security requirements.

What it does:

Prompts the user to enter a password
Validates the password against five criteria:
Minimum 8 characters long
Contains at least one digit
Contains at least one uppercase letter
Contains at least one lowercase letter
Contains at least one special character from $, @, #, %, &
Prints specific error messages for each failed requirement
Outputs a final message indicating whether the password is "strong" or "weak"
How it works:

The script uses a is_strong flag that starts as True and is set to False whenever a requirement fails. After all checks, it displays the result based on whether is_strong is still True.


TASK 4:
This file is a keyboard logger that records all keypresses to a text file.

Here's how it works:

Listener Setup: Uses pynput.keyboard.Listener to monitor keyboard input and trigger the write_to_file() function on each keypress.

Key Mapping: The write_to_file() function translates special keys into readable characters:

Key.space → space character
Key.enter → newline
Modifier keys (Shift, Ctrl, Alt, Cmd, Caps Lock, Tab, Backspace) → empty string (filtered out)
Logging: Each processed key is appended to a file named log.txt.

Execution: The listener runs continuously in an infinite loop, capturing all keyboard activity until the program is terminated.


TASK 5:
This file is a simple packet sniffer built with Scapy, a Python library for network packet manipulation.

What it does:

Defines a packet_callback() function that prints a summary of each captured network packet
In main(), it uses sniff() to capture live network traffic for 5 seconds (or until interrupted)
Catches KeyboardInterrupt to allow graceful stopping with Ctrl+C
Key parameters:

prn=packet_callback — calls the callback function for each packet
store=0 — discards captured packets from memory (doesn't store them)
timeout=5 — stops after 5 seconds
This is a basic network monitoring tool, commonly used for learning packet analysis or debugging network issues.
