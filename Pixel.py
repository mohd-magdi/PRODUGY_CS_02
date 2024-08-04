#pip install Pillow

from PIL import Image

def encrypt_image(input_file, output_file, key):
  """Encrypts an image using pixel manipulation.

  Args:
    input_file: Path to the input image file.
    output_file: Path to the output encrypted image file.
    key: A numerical key for encryption.
  """

  image = Image.open(input_file)
  pixels = image.load()

  width, height = image.size

  for x in range(width):
    for y in range(height):
      r, g, b = pixels[x, y]
      new_r = (r + key) % 256
      new_g = (g + key) % 256
      new_b = (b + key) % 256
      pixels[x, y] = (new_r, new_g, new_b)

  image.save(output_file)

def decrypt_image(input_file, output_file, key):
  """Decrypts an image using pixel manipulation.

  Args:
    input_file: Path to the input encrypted image file.
    output_file: Path to the output decrypted image file.
    key: A numerical key for decryption.
  """

  image = Image.open(input_file)
  pixels = image.load()

  width, height = image.size

  for x in range(width):
    for y in range(height):
      r, g, b = pixels[x, y]
      new_r = (r - key + 256) % 256  # Handle negative values
      new_g = (g - key + 256) % 256
      new_b = (b - key + 256) % 256
      pixels[x, y] = (new_r, new_g, new_b)

  image.save(output_file)

if __name__ == "__main__":
  input_image = "input.jpg"
  encrypted_image = "encrypted.jpg"
  decrypted_image = "decrypted.jpg"
  key = 42

  encrypt_image(input_image, encrypted_image, key)
  decrypt_image(encrypted_image, decrypted_image, key)
