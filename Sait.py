class BibaBoba:
    def create_playfair_matrix(key):
        key = key.replace(" ", "").upper()
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        matrix = []
        for letter in key:
            if letter not in matrix:
                matrix.append(letter)
        for letter in alphabet:
            if letter not in matrix:
                matrix.append(letter)
        playfair_matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
        return playfair_matrix

    def find_position(matrix, letter):
        for i in range(5):
            for j in range(5):
                if matrix[i][j] == letter:
                    return i, j

    def playfair_encrypt(plain_text, key):
        playfair_matrix = BibaBoba.create_playfair_matrix(key)
        plain_text = plain_text.replace(" ", "").upper()
        plain_text = [letter for letter in plain_text]
        encrypted_text = ""
        for i in range(0, len(plain_text), 2):
            if i == len(plain_text) - 1:
                plain_text.insert(i+1, "X")
            if plain_text[i] == plain_text[i+1]:
                plain_text.insert(i+1, "X")
        for i in range(0, len(plain_text), 2):
            first_position = BibaBoba.find_position(playfair_matrix, plain_text[i])
            second_position = BibaBoba.find_position(playfair_matrix, plain_text[i+1])
            if first_position[0] == second_position[0]:
                encrypted_text += playfair_matrix[first_position[0]][(first_position[1]+1)%5]
                encrypted_text += playfair_matrix[second_position[0]][(second_position[1]+1)%5]
            elif first_position[1] == second_position[1]:
                encrypted_text += playfair_matrix[(first_position[0]+1)%5][first_position[1]]
                encrypted_text += playfair_matrix[(second_position[0]+1)%5][second_position[1]]
            else:
                encrypted_text += playfair_matrix[first_position[0]][second_position[1]]
                encrypted_text += playfair_matrix[second_position[0]][first_position[1]]
        return encrypted_text

    def playfair_decrypt(encrypted_text, key):
        playfair_matrix = BibaBoba.create_playfair_matrix(key)
        encrypted_text = [letter for letter in encrypted_text]
        decrypted_text = ""
        for i in range(0, len(encrypted_text), 2):
            first_position = BibaBoba.find_position(playfair_matrix, encrypted_text[i])
            second_position = BibaBoba.find_position(playfair_matrix, encrypted_text[i+1])
            if first_position[0] == second_position[0]:
                decrypted_text += playfair_matrix[first_position[0]][(first_position[1]-1)%5]
                decrypted_text += playfair_matrix[second_position[0]][(second_position[1]-1)%5]
            elif first_position[1] == second_position[1]:
                decrypted_text += playfair_matrix[(first_position[0]-1)%5][first_position[1]]
                decrypted_text += playfair_matrix[(second_position[0]-1)%5][second_position[1]]
            else:
                decrypted_text += playfair_matrix[first_position[0]][second_position[1]]
                decrypted_text += playfair_matrix[second_position[0]][first_position[1]]
        return decrypted_text 

