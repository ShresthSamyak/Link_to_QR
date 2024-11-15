import qrcode
from PIL import Image

def generate_qr(url, filename="qr_code.png"):
    """
    Generate a QR code from a URL and save it as an image
    
    Args:
        url (str): The URL to encode in the QR code
        filename (str): The output filename (default: qr_code.png)
    """
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Add data to the QR code
    qr.add_data(url)
    qr.make(fit=True)
    
    # Create an image from the QR code
    qr_image = qr.make_image(fill_color="black", back_color="white")
    
    # Save the image
    qr_image.save(filename)
    print(f"QR code has been generated and saved as {filename}")

def main():
    while True:
        # Get URL from user
        url = input("Enter the URL (or 'quit' to exit): ")
        
        if url.lower() == 'quit':
            break
        
        # Get custom filename (optional)
        filename = input("Enter filename for the QR code (press Enter for default name):  ")
        
        if not filename:
            filename = "qr_code.png"
        elif not filename.endswith(('.png', '.jpg', '.jpeg')):
            filename += '.png'
        
        # Generate QR code
        generate_qr(url, filename)

if __name__ == "__main__":
    main()