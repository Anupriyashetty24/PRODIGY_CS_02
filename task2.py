from PIL import Image

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            # Check if the image has an alpha channel (RGBA)
            if len(pixels[i, j]) == 4:
                r, g, b, a = pixels[i, j]
                # Swap red and blue channels
                encrypted_pixel = (b, g, r, a)
            else:
                r, g, b = pixels[i, j]
                # Swap red and blue channels
                encrypted_pixel = (b, g, r)

            pixels[i, j] = encrypted_pixel

    img.save(output_path)
    print("Image encrypted successfully!")

def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            # Check if the image has an alpha channel (RGBA)
            if len(pixels[i, j]) == 4:
                r, g, b, a = pixels[i, j]
                # Swap blue and red channelss back
                decrypted_pixel = (b, g, r, a)
            else:
                r, g, b = pixels[i, j]
                # Swap blue and red channels back
                decrypted_pixel = (b, g, r)

            pixels[i, j] = decrypted_pixel

    img.save(output_path)
    print("Image decrypted successfully!")

# Image paths
input_image = r"C:\Users\Indu\Dropbox\PC\Downloads\evd\photo.png"
encrypted_image = r"C:\Users\Indu\Dropbox\PC\Downloads\evd\encrypted_photo.png"
decrypted_image = r"C:\Users\Indu\Dropbox\PC\Downloads\evd\decrypted_photo.png"

# Encrypt the image
encrypt_image(input_image, encrypted_image, key=None)

# Decrypt the images
decrypt_image(encrypted_image, decrypted_image, key=None)
