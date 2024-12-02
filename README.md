# Introduction to PyImageEncrypter

# Pixel Manipulation Image Encryption Tool

Pixel manipulation for image encryption involves modifying the RGB values of each pixel in an image using cryptographic algorithms or secret keys. This process renders the image unreadable without proper decryption. During encryption, the RGB values of pixels are altered in a controlled manner to obscure the image's content while maintaining its visual appearance.

## How It Helps in Encryption and Decryption

### Encryption
To encrypt an image using pixel manipulation, you apply specific operations like pixel value swapping or mathematical transformations to each pixel. This transforms the original image into an encrypted one that appears meaningless to anyone who doesn't have the decryption key. For example, you might add a secret key value to each pixel's RGB values, effectively scrambling the image.

### Decryption
Decryption is the reverse process of encryption. By knowing the secret key or the specific operations used during encryption, you can reverse the changes made to the pixel values and restore the original image. This ensures that the image remains confidential and can only be viewed by those who possess the correct decryption key or algorithm.

# Steps for execution

### Install python on any linux based system like "Kali Linux".
### To install python on kali linux use command
1. sudo apt update
2. sudo apt install python3 -y
### Open a text editor to create the script file. Use 'nano' or any other text editor available in Kali Linux
3. nano image_encryption.py
### write image encryption program code in text editor.
### Save the file 
4. Press 'CTRL+O' to save.
5. Hit 'Enter' to confirm the file name.
6. Press 'CTRL+X' to exit the editor.
### Run the code/script
7. python3 image_encryption.py
### Use the program
8. Download any image (.png, .jpeg, .jpg) from websites like chrome
9. Enter the path of the image to process 
10. Enter any encryption key (between 1 and 225)
11. Image will be encrypted and decrypted 
12. Encrypted image saved as encrypted_output.png
13. Decrypted image saved as decrypted_output.png
14. Process is completed.
### Image encryption decryption done using Pixel manipulation



