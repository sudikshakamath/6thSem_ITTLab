text = input("Enter the text to be encrypted: ")
shift = int(input("Enter the shift value: "))
encrypted_text = ""
for char in text:    
    if char.isupper():        
        encrypted_ascii = (ord(char) + shift - 65) % 26 + 65        
        encrypted_text += chr(encrypted_ascii)    
    elif char.islower():        
        encrypted_ascii = (ord(char) + shift - 97) % 26 + 97        
        encrypted_text += chr(encrypted_ascii)    
    else:        
        encrypted_text += char 

print("The encrypted text is:", encrypted_text)