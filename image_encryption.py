# Import the required library for image processing
from PIL import Image 

# Function to apply a transformation to an image's pixel data
def transform_image(input_path, output_path, key, mode):
    """
    Transforms an image by modifying its pixel values based on the given key.
    Can encrypt or decrypt based on the mode.

    Args:
        input_path (str): Path to the input image.
        output_path (str): Path to save the transformed image.
        key (int): Transformation key (integer between 1 and 255).
        mode (str): 'encrypt' or 'decrypt'.
    """
    try:
        # Open the image file
        img = Image.open(input_path)
        pixels = img.load()  # Load pixel data for manipulation

        # Retrieve the dimensions of the image
        width, height = img.size

        # Loop through each pixel in the image
        for x in range(width):
            for y in range(height):
                # Get the RGB values of the current pixel
                r, g, b = pixels[x, y]

                # Apply the transformation based on the mode
                if mode == 'encrypt':
                    # For encryption, add the key to each RGB value and wrap around using modulo 256
                    r = (r + key) % 256
                    g = (g + key) % 256
                    b = (b + key) % 256
                elif mode == 'decrypt':
                    # For decryption, subtract the key from each RGB value and wrap around using modulo 256
                    r = (r - key) % 256
                    g = (g - key) % 256
                    b = (b - key) % 256
                else:
                    # Raise an error if the mode is invalid
                    raise ValueError("Invalid mode. Use 'encrypt' or 'decrypt'.")

                # Update the pixel value with the transformed RGB values
                pixels[x, y] = (r, g, b)

        # Save the transformed image to the specified output path
        img.save(output_path)
        print(f"{mode.capitalize()}ed image saved at: {output_path}")
    except Exception as e:
        # Handle any errors that occur during the transformation process
        print(f"Error during {mode}ion: {e}")

# Main function to demonstrate the image encryption and decryption process
def main():
    """
    Entry point for the Image Encryption and Decryption Tool.
    Prompts the user for input and demonstrates the process of encrypting and decrypting an image.
    """
    print("=== Image Encryption and Decryption Tool ===")

    # Get the path of the input image from the user
    input_image = input("Enter the path of the image to process: ").strip()

    # Set default file names for the encrypted and decrypted images
    encrypted_image = "encrypted_output.png"
    decrypted_image = "decrypted_output.png"

    # Prompt the user for an encryption key
    try:
        key = int(input("Enter an encryption key (integer between 1 and 255): "))
        if not (1 <= key <= 255):
            raise ValueError("Key must be in the range 1-255.")
    except ValueError as e:
        # Handle invalid key input
        print(f"Invalid input: {e}")
        return

    # Encrypt the image
    print("\nEncrypting the image...")
    transform_image(input_image, encrypted_image, key, mode='encrypt')

    # Decrypt the image
    print("\nDecrypting the image...")
    transform_image(encrypted_image, decrypted_image, key, mode='decrypt')

    # Display the completion message
    print(f"\nProcess completed. Encrypted and decrypted images are saved as:\n{encrypted_image}\n{decrypted_image}")

# Entry point for the script
if __name__ == "__main__":
    main()
