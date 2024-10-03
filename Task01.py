def caesar_encrypt(text,shift):
    result=""
    
    for i in range(len(text)):
       char=text[i]
       
    if char.isupper():
           result+=chr((ord(char)+shift+65)%26+65);
           
    elif char.islower():
            result+=chr((ord(char)+shift-97)%26+97);
            
    else:
           result+=char
           
    return result
           
def caesar_decrypt(text,shift):
    return caesar_encrypt(text,-shift)
    
def main():
    print("Caesar Cipher Program")
    choice= input("Do you want to (E)ncrypt or (D)ecrypt?").lower()
    text=input("Enter the message:")
    shift= int(input("Enter the shift value:"))
    
    if choice == "e":
     encrypt_message= caesar_encrypt(text,shift)
     print(f"Encrypt Message: { encrypt_message}")
     
    elif choice == "d":
     decrypt_message = caesar_decrypt(text,shift)
     print(f"Decrypt Message: {decrypt_message}")
     
    else:
     print("Invalid choice! Please select 'E' or 'D'.")
     
if __name__ == "__main__":
    main()
     
    



