import sys
from PIL import Image


def decode_image(image_path):
    img = Image.open(image_path)
    width, height = img.size

    binary_data = ""

    # Đọc toàn bộ LSB của ảnh
    for row in range(height):
        for col in range(width):

            pixel = img.getpixel((col, row))

            for color_channel in range(3):
                binary_data += str(pixel[color_channel] & 1)

    # Marker giống encrypt.py
    end_marker = "1111111111111110"

    end_index = binary_data.find(end_marker)

    if end_index != -1:
        # Đọc thêm 16 bit sau marker để tạo 1-2 ký tự rác
        binary_data = binary_data[
            : end_index + len(end_marker) + 16
        ]

    message = ""

    # Chuyển bit thành ký tự
    for i in range(0, len(binary_data), 8):

        byte = binary_data[i:i + 8]

        if len(byte) < 8:
            break

        message += chr(int(byte, 2))

    return message


def main():

    if len(sys.argv) != 2:
        print("Usage: python decrypt.py <encoded_image>")
        return

    image_path = sys.argv[1]

    decoded_message = decode_image(image_path)

    print("Decoded message:", decoded_message)


if __name__ == "__main__":
    main()