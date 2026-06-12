class PlayFairCipher:
    
    def __init__(self):
        pass

    def create_playfair_matrix(self, key):
        key = key.replace(" ", "")
        key = key.replace("J", "I")
        key = key.upper()

        key_set = set(key)

        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

        remaining_letters = [
            letter for letter in alphabet
            if letter not in key_set
        ]

        matrix = list(key)

        for letter in remaining_letters:
            matrix.append(letter)

            if len(matrix) == 25:
                break

        return [matrix[i:i + 5] for i in range(0, 25, 5)]

    def find_letter_coords(self, matrix, letter):

        for row in range(len(matrix)):
            for col in range(len(matrix[row])):

                if matrix[row][col] == letter:
                    return row, col

        return None

    def playfair_encrypt(self, plain_text, matrix):

        # CHẶN DẤU CÁCH
        if " " in plain_text:
            raise ValueError(
                "Plain text không được chứa dấu cách"
            )

        # CHẶN SỐ/KÝ TỰ ĐẶC BIỆT
        if not plain_text.isalpha():
            raise ValueError(
                "Plain text chỉ được chứa A-Z"
            )

        plain_text = plain_text.upper()
        plain_text = plain_text.replace("J", "I")

        encrypted_text = ""

        for i in range(0, len(plain_text), 2):

            pair = plain_text[i:i + 2]

            if len(pair) == 1:
                pair += "X"

            pos1 = self.find_letter_coords(matrix, pair[0])
            pos2 = self.find_letter_coords(matrix, pair[1])

            if pos1 is None or pos2 is None:
                raise ValueError(
                    "Ký tự không hợp lệ trong Plain Text"
                )

            row1, col1 = pos1
            row2, col2 = pos2

            if row1 == row2:

                encrypted_text += (
                    matrix[row1][(col1 + 1) % 5]
                    + matrix[row2][(col2 + 1) % 5]
                )

            elif col1 == col2:

                encrypted_text += (
                    matrix[(row1 + 1) % 5][col1]
                    + matrix[(row2 + 1) % 5][col2]
                )

            else:

                encrypted_text += (
                    matrix[row1][col2]
                    + matrix[row2][col1]
                )

        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):

        if " " in cipher_text:
            raise ValueError(
                "Cipher text không được chứa dấu cách"
            )

        if not cipher_text.isalpha():
            raise ValueError(
                "Cipher text chỉ được chứa A-Z"
            )

        if len(cipher_text) % 2 != 0:
            raise ValueError(
                "Cipher text phải có độ dài chẵn"
            )

        cipher_text = cipher_text.upper()

        decrypted_text = ""

        for i in range(0, len(cipher_text), 2):

            pair = cipher_text[i:i + 2]

            pos1 = self.find_letter_coords(matrix, pair[0])
            pos2 = self.find_letter_coords(matrix, pair[1])

            if pos1 is None or pos2 is None:
                raise ValueError(
                    "Ký tự không hợp lệ trong Cipher Text"
                )

            row1, col1 = pos1
            row2, col2 = pos2

            if row1 == row2:

                decrypted_text += (
                    matrix[row1][(col1 - 1) % 5]
                    + matrix[row2][(col2 - 1) % 5]
                )

            elif col1 == col2:

                decrypted_text += (
                    matrix[(row1 - 1) % 5][col1]
                    + matrix[(row2 - 1) % 5][col2]
                )

            else:

                decrypted_text += (
                    matrix[row1][col2]
                    + matrix[row2][col1]
                )

        return decrypted_text