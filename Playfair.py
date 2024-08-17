def preprocessPlaintext(plainText):
    # add 'X' if two consecutive letters are the same
    for s in range(0, len(plainText) + 1, 2):
        if s < len(plainText) - 1:
            if plainText[s] == plainText[s + 1]:
                plainText = plainText[:s + 1] + 'X' + plainText[s + 1:]

    # add 'X' if the total number of letters is odd to make plaintext even
    if len(plainText) % 2 != 0:
        plainText = plainText[:] + 'X'

    return plainText

def createKeyMatrix(key):
    # create a 5x5 matrix with all values as 0
    key_matrix  = [[0 for i in range(5)] for j in range(5)]

    processed_key  = []


    for i in key:
        if i not in processed_key : #Characters should not be repeated
            if i == 'J':
                processed_key .append('I') #Replace 'J' with 'I'
            else:
                processed_key .append(i)

    
#Fill processed_key with unused letters from the alphabet
    contains_I = "I" in processed_key 

    for i in range(65, 91):     #ASCII values range from 65 to 90
        if chr(i) not in processed_key :
            # We want 'I' in simpleKeyArr, not 'J'
            if i == 73 and not contains_I:
                processed_key .append("I")
                contains_I = True
            elif i == 73 or i == 74 and contains_I:
            # Skip 'J' or if 'I' already exists
                pass
            else:
                processed_key.append(chr(i))


    #convert  to matrix 5x5
    index = 0
    for i in range(0, 5):
        for j in range(0, 5):
            key_matrix [i][j] = processed_key [index]
            index += 1

    return key_matrix 

def findCharacterPosition(char, cipherKeyMatrix):
    # List to store the row and column index of the character
    char_position  = []

    # Convert 'J' to 'I'
    if char == "J":
        char = "I"

    for i, j in enumerate(cipherKeyMatrix):
        for k, l in enumerate(j):
            if char == l:
                char_position .append(i)  # Add row index
                char_position .append(k)  # Add column index
                return char_position 

def encryptMessage(plainText, key):
    ciphertext = []
    # Generate Key Matrix
    key_matrix = createKeyMatrix(key)

    # Encrypt according to the rules of the Playfair cipher
    i = 0
    while i < len(plainText):
        # Calculate the indices of the two grouped characters from the key matrix
        pos1 = findCharacterPosition(plainText[i], key_matrix)
        pos2 = findCharacterPosition(plainText[i + 1], key_matrix)

        # Same column
        if pos1[1] == pos2[1]:
            new_pos1 = (pos1[0] + 1) % 5
            col1 = pos1[1]

            new_pos2 = (pos2[0] + 1) % 5
            col2 = pos2[1]
            ciphertext.append(key_matrix[new_pos1][col1])
            ciphertext.append(key_matrix[new_pos2][col2])

        # Same row
        elif pos1[0] == pos2[0]:
            row1 = pos1[0]
            new_col1 = (pos1[1] + 1) % 5

            row2 = pos2[0]
            new_col2 = (pos2[1] + 1) % 5
            ciphertext.append(key_matrix[row1][new_col1])
            ciphertext.append(key_matrix[row2][new_col2])

        # Form a rectangle
        else:
            row1 = pos1[0]
            col1 = pos1[1]

            row2 = pos2[0]
            col2 = pos2[1]

            ciphertext.append(key_matrix[row1][col2])
            ciphertext.append(key_matrix[row2][col1])
        i += 2  
    return ciphertext

def playfair(msg, key):
    # Normalize the key and message by removing spaces and converting to uppercase
    key = key.replace(" ", "").upper()
    msg = msg.replace(" ", "").upper()

    # Convert the plaintext message to digraphs according to Playfair cipher rules
    convertedPlainText = preprocessPlaintext(msg)
    
    # Encrypt the converted plaintext using the key and return the ciphertext
    cipherText = "".join(encryptMessage(convertedPlainText, key))
    return cipherText
