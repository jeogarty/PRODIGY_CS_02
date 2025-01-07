import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import numpy as np

class ImageEncryptorProg:
    def __init__(self, master):
        self.master = master
        master.title("Image Encryption Tool")

        self.key = 123  # This should be a value between 0-255 for pixel manipulation

        self.label = tk.Label(master, text="Select an image to encrypt or decrypt:")
        self.label.pack()

        self.select_button = tk.Button(master, text="Select Image", command=self.select_image)
        self.select_button.pack()

        self.encrypt_button = tk.Button(master, text="Encrypt Image", command=self.encrypt_image)
        self.encrypt_button.pack()

        self.decrypt_button = tk.Button(master, text="Decrypt Image", command=self.decrypt_image)
        self.decrypt_button.pack()

        self.image_path = None

    def select_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp")])
        if self.image_path:
            messagebox.showinfo("Selected Image", f"Image selected: {self.image_path}")

    def encrypt_image(self):
        if not self.image_path:
            messagebox.showwarning("Warning", "Please select an image first.")
            return

        output_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if not output_path:
            return

        try:
            image = Image.open(self.image_path)
            image_array = np.array(image)
            encrypted_array = image_array ^ self.key
            encrypted_image = Image.fromarray(encrypted_array)
            encrypted_image.save(output_path)
            messagebox.showinfo("Success", f"Image encrypted and saved as {output_path}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def decrypt_image(self):
        if not self.image_path:
            messagebox.showwarning("Warning", "Please select an image first.")
            return

        output_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if not output_path:
            return

        try:
            encrypted_image = Image.open(self.image_path)
            encrypted_array = np.array(encrypted_image)
            decrypted_array = encrypted_array ^ self.key
            decrypted_image = Image.fromarray(decrypted_array)
            decrypted_image.save(output_path)
            messagebox.showinfo("Success", f"Image decrypted and saved as {output_path}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEncryptorProg(root)
    root.mainloop()