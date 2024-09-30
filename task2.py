from PIL import Image
import numpy as np

def encryption(img, key, outputname):
    img1=Image.open(img)
    pxarray=np.array(img1,dtype=np.uint16)
    pxarray=(pxarray+key)%256
    pxarray = pxarray.astype(np.uint8)
    encrypted_img=Image.fromarray(pxarray)
    encrypted_img.save(outputname)
    print("Image encrypted successfully")

def decryption(img, key, outputname):
    img1=Image.open(img)
    pxarray=np.array(img1,dtype=np.uint16)
    pxarray=(pxarray-key)%256
    pxarray = pxarray.astype(np.uint8)
    decrypted_img=Image.fromarray(pxarray)
    decrypted_img.save(outputname)
    print("Image decrypted successfully")

input_image = input("Enter the image name with format: ")
key = int(input("Enter the key: "))
choice = int(input("Press '1' to encrypt or '2' to decrypt: "))
output_image = input("Enter the output image name with format: ")

if choice == 1:
    encryption(input_image, key, output_image)
elif choice == 2:
    decryption(input_image, key, output_image)
else:
    print("Invalid choice")
    exit()