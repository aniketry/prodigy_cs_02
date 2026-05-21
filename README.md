# Picture Encryption Tool

## Purpose

Create an easy-to-use Picture Encryption Tool that utilizes XOR Encryption to build a method for encrypting pictures and decrypting them back to their original state.

Users of this Tool will be able to:

- Encrypt Picture files
- Decrypt their encrypted Picture files
- Prevent others from accessing their pictures normally
- Learn about the basic principles of picture encryption and decryption.

This Project is part of Task-02 in my Cybersecurity Internship at Prodigy InfoTech.

---

# Features Implemented

XOR Encryption of Pictures
Function for Decrypting Encrypted Pictures
Interactive Application with GUI
File Selection Dialog Box
Generation of Encrypted File (`.enc`)
Decrypted Restoration of Original Picture
Error/Message Handling using Message Boxes
User-friendly Simple and Clean GUI

---

# Tools Used

- Python
- Tkinter
- File System
- XOR Encryption
- Binary Data Processing

---

# Lessons Learned

The following skills were learned throughout the process:

- Introduction to Picture Processing
- Overview of Encryption/Decryption Process
- Understanding of the XOR Encryption Process
- Working with Binary Files in Python
- Building an Application Using Tkinter
- Creating Interactive Tool Applications
- Understanding how to Protect Files in Cybersecurity
- Understanding Event-Driven Programming

---

# Working Principle

The tool works by reading image files in binary format and encrypting their data using XOR encryption.

During encryption:
- Original image bytes are converted into encrypted binary data
- Encrypted data is stored in a `.enc` file
- The encrypted file cannot be opened normally

During decryption:
- The encrypted `.enc` file is selected
- XOR decryption restores the original image
- The decrypted image is saved successfully

---

# Encryption Logic

The project uses XOR Encryption:

:contentReference[oaicite:0]{index=0}

Where:
- `x` = original byte
- `k` = encryption key

For decryption:

:contentReference[oaicite:1]{index=1}

Applying XOR twice with the same key restores the original data.

---

# Example Workflow

## Encryption

```text
photo.png
↓
encrypted_image.enc