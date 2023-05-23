alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def encrypt (txt, sft):
    Encrypted_Word = []
    New_Encrypted_Word = ""
    for letter in txt:
        #in case user puts text as 'shikhar'. letter would be 's' in the 1st iteration, 'h' in the 2nd iteration and so on.
        Index_Of_letter = alphabet.index(letter)
        New_Index = Index_Of_letter + sft
        New_Letter = alphabet[New_Index]
        Encrypted_Word += New_Letter

    for letter in Encrypted_Word:
        New_Encrypted_Word += letter

    print (f"The encrypted word is {New_Encrypted_Word}")


def decrypt (txt, sft):
    #Now we're going to decrypt the data as given by the user, using the shift amount. Eg: 'ujk' to 'shi', using a shift of 2 spaces.
    Decrypted_Word = []
    New_Decrypted_Word = ""
    for letter in txt:
        index_of_letter = alphabet.index(letter)
        Decrypt_Index = index_of_letter - sft
        new_decrypted_letter = alphabet[Decrypt_Index]
        Decrypted_Word += new_decrypted_letter

    for word in Decrypted_Word:
        New_Decrypted_Word += word

    print (f'The decrypted word is {New_Decrypted_Word}')

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 

if direction == "encode":
    encrypt (txt = text, sft = shift)
else:
    decrypt (txt = text, sft = shift)