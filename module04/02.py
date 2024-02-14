

def find_max_vowels(text:str):
    vowels = "aeiou"
    
    for character in text:
        if character.lower not in vowels:
            text = text.replace(character, " . ")
            
            print(text)
            
            text = "aesaefsdsade  sa d Oleeeeeeh"
        find_max_vowels(text)  