from tkinter import *
from tkinter import filedialog, messagebox


# Encrypt Image Function
def encrypt_image():

    # Select Image File
    file_path = filedialog.askopenfilename(
        title="Select Image",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
    )

    if not file_path:
        return

    key = 123

    try:

        # Read Image in Binary Mode
        with open(file_path, "rb") as file:

            image_data = bytearray(file.read())

        # Encrypt Image Data using XOR
        encrypted_data = bytearray()

        for byte in image_data:

            encrypted_data.append(byte ^ key)

        # Save Encrypted File
        with open("encrypted_image.enc", "wb") as file:

            file.write(encrypted_data)

        messagebox.showinfo(
            "Encryption Successful",
            "Encrypted file saved as:\nencrypted_image.enc"
        )

    except Exception as e:

        messagebox.showerror("Error", str(e))


# Decrypt Image Function
def decrypt_image():

    # Select Encrypted File
    file_path = filedialog.askopenfilename(
        title="Select Encrypted File",
        filetypes=[("Encrypted Files", "*.enc")]
    )

    if not file_path:
        return

    key = 123

    try:

        # Read Encrypted Binary File
        with open(file_path, "rb") as file:

            encrypted_data = bytearray(file.read())

        # Decrypt using XOR
        decrypted_data = bytearray()

        for byte in encrypted_data:

            decrypted_data.append(byte ^ key)

        # Save Decrypted Image
        with open("decrypted_image.png", "wb") as file:

            file.write(decrypted_data)

        messagebox.showinfo(
            "Decryption Successful",
            "Decrypted image saved as:\ndecrypted_image.png"
        )

    except Exception as e:

        messagebox.showerror("Error", str(e))


# Main GUI Window
root = Tk()

root.title("Image Encryption Tool")
root.geometry("450x320")
root.config(bg="white")


# Heading
heading = Label(
    root,
    text="IMAGE ENCRYPTION TOOL",
    font=("Arial", 18, "bold"),
    bg="white",
    fg="black"
)

heading.pack(pady=30)


# Description
description = Label(
    root,
    text="Encrypt and Decrypt Images using XOR Encryption",
    font=("Arial", 11),
    bg="white",
    fg="black"
)

description.pack(pady=5)


# Encrypt Button
encrypt_button = Button(
    root,
    text="Encrypt Image",
    font=("Arial", 12),
    width=20,
    command=encrypt_image
)

encrypt_button.pack(pady=20)


# Decrypt Button
decrypt_button = Button(
    root,
    text="Decrypt Image",
    font=("Arial", 12),
    width=20,
    command=decrypt_image
)

decrypt_button.pack(pady=10)


# Exit Button
exit_button = Button(
    root,
    text="Exit",
    font=("Arial", 12),
    width=20,
    command=root.destroy
)

exit_button.pack(pady=20)


# Run GUI
root.mainloop()