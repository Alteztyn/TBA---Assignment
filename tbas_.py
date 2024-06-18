def tokenRecognizer(word: str):
    word = word.lower()
    try:
        if isSubjek(word): return 'S'
        elif isPredikat(word): return 'P'
        elif isObjek(word): return 'O'
        elif isKeterangan(word): return 'K'
        else: raise Exception("TokenUnrecognizedError")
    except Exception as e: 
        print(f"ERROR: {e}")
        print(f"Word \"{word}\" tidak masuk ke kategori token manapun\n")
        return '?'

def isSubjek(word: str) -> bool:
    # Subjek = {'aku', 'anda', 'kamu', 'dia', 'saya'}
    current_State_Q = 0
    for letter in word:
        match current_State_Q:
            case -1: break
            case 0:
                if letter == 'a': current_State_Q = 1
                elif letter == 'k': current_State_Q = 2
                elif letter == 'd': current_State_Q = 3
                elif letter == 's': current_State_Q = 4
                else: current_State_Q = -1
            case 1:
                if letter == 'n': current_State_Q = 5
                elif letter == 'k': current_State_Q = 6
                else: current_State_Q = -1
            case 2: current_State_Q = 7 if letter == 'a' else -1
            case 3: current_State_Q = 8 if letter == 'i' else -1
            case 4: current_State_Q = 9 if letter == 'a' else -1
            case 5: current_State_Q = 8 if letter == 'd' else -1
            case 6: current_State_Q = 10 if letter == 'u' else -1
            case 7: current_State_Q = 11 if letter == 'm' else -1 
            case 8: current_State_Q = 12 if letter == 'a' else -1 
            case 9: current_State_Q = 8 if letter == 'y' else -1
            case 10: current_State_Q = 10 if letter == ' ' else -1 #final state
            case 11: current_State_Q = 10 if letter == 'u' else -1 
            case 12: current_State_Q = 12 if letter == ' ' else -1 #final state

    return current_State_Q == 10 or current_State_Q == 12 

def isPredikat(word: str) -> bool:
    # Predikat = {'makan', 'minum', 'baca', 'bermain', 'memakai'}
    current_State_Q = 0
    for letter in word:
        match current_State_Q:
            case -1: break
            case 0:
                if letter == 'm': current_State_Q = 1
                elif letter == 'b': current_State_Q = 16
                else: current_State_Q = -1
            case 1:
                if letter == 'a': current_State_Q = 6
                elif letter == 'i': current_State_Q = 2
                elif letter == 'e': current_State_Q = 10
                else: current_State_Q = -1
            case 16: 
                if letter == 'a': current_State_Q = 17
                elif letter == 'e': current_State_Q = 20
                else: current_State_Q = -1
            case 2: current_State_Q = 3 if letter == 'n' else -1
            case 3: current_State_Q = 4 if letter == 'u' else -1
            case 4: current_State_Q = 5 if letter == 'm' else -1
            case 5: current_State_Q = 5 if letter == ' ' else -1#final minum

            case 6: current_State_Q = 7 if letter == 'k' else -1
            case 7: current_State_Q = 8 if letter == 'a' else -1
            case 8: current_State_Q = 9 if letter == 'n' else -1
            case 9: current_State_Q = 9 if letter == ' ' else -1 #final makan

            case 10: current_State_Q = 11 if letter == 'm' else -1
            case 11: current_State_Q = 12 if letter == 'a' else -1
            case 12: current_State_Q = 13 if letter == 'k' else -1
            case 13: current_State_Q = 14 if letter == 'a' else -1
            case 14: current_State_Q = 15 if letter == 'i' else -1
            case 15: current_State_Q = 15 if letter == ' ' else -1#final memakai

            case 16: current_State_Q = 17 if letter == 'a' else -1
            case 17: current_State_Q = 18 if letter == 'c' else -1
            case 18: current_State_Q = 19 if letter == 'a' else -1
            case 19: current_State_Q = 19  if letter == ' ' else -1#final baca

            case 20: current_State_Q = 21 if letter == 'r' else -1
            case 21: current_State_Q = 22 if letter == 'm' else -1
            case 22: current_State_Q = 23 if letter == 'a' else -1
            case 23: current_State_Q = 24 if letter == 'i' else -1
            case 24: current_State_Q = 9 if letter == 'n' else -1

    return current_State_Q == 5 or current_State_Q == 9 or current_State_Q == 15 or current_State_Q == 19
def isObjek(word: str) -> bool:
    # Objek = {'rendang', 'jus', 'novel', 'bola', 'baju'}
    current_State_Q = 0
    for letter in word:
        match current_State_Q:
            case -1: break
            case 0:
                if letter == 'r': current_State_Q = 1
                elif letter == 'j': current_State_Q = 2
                elif letter == 'n': current_State_Q = 3
                elif letter == 'b': current_State_Q = 4
                else: current_State_Q = -1
            case 1: current_State_Q = 5 if letter == 'e' else -1
            case 2: current_State_Q = 6 if letter == 'u' else -1
            case 3: current_State_Q = 7 if letter == 'o' else -1
            case 4: 
                if letter == 'a': current_State_Q = 8 
                elif letter == 'o': current_State_Q = 20
                else: current_State_Q = -1
            case 5: current_State_Q = 9 if letter == 'n' else -1
            case 6: current_State_Q = 10 if letter == 's' else -1
            case 7: current_State_Q = 11 if letter == 'v' else -1
            case 8: current_State_Q = 12 if letter == 'j' else -1
            case 9: current_State_Q = 13 if letter == 'd' else -1
            case 10: current_State_Q = 10 if letter == ' ' else -1 #Final State
            case 11: current_State_Q = 14 if letter == 'e' else -1
            case 12: current_State_Q = 15 if letter == 'u' else -1
            case 13: current_State_Q = 16 if letter == 'a' else -1
            case 14: current_State_Q = 17 if letter == 'l' else -1
            case 15: current_State_Q = 15 if letter == ' ' else -1 #Final State
            case 16: current_State_Q = 18 if letter == 'n' else -1
            case 17: current_State_Q = 17 if letter == ' ' else -1 #Final State
            case 18: current_State_Q = 19 if letter == 'g' else -1
            case 19: current_State_Q = 19 if letter == ' ' else -1 #Final State
            case 20: current_State_Q = 21 if letter == 'l' else -1
            case 21: current_State_Q = 22 if letter == 'a' else -1
            case 22: current_State_Q = 22 if letter == ' ' else -1 #Final State
            

    return current_State_Q == 10 or current_State_Q == 17 or current_State_Q == 15 or current_State_Q == 19  or current_State_Q == 22
    
def isKeterangan(word: str) -> bool:
    # Ket = {'dikantin', 'dikamar', 'dikelas', 'dilapangan', 'diatap'}
    current_State_Q = 0
    for letter in word:
        match current_State_Q:
            case -1: break
            case 0: current_State_Q = 1 if letter == 'd' else -1
            case 1: current_State_Q = 2 if letter == 'i' else -1
            case 2:
                if letter == 'k': current_State_Q = 3
                elif letter == 'l': current_State_Q = 16
                elif letter == 'a': current_State_Q = 24
                else: current_State_Q = -1
            case 3: 
                if letter == 'a': current_State_Q = 4
                elif letter == 'e': current_State_Q = 12
                else: current_State_Q = -1
            case 4: 
                if letter == 'm': current_State_Q = 9
                elif letter == 'n': current_State_Q = 5 
                else: current_State_Q = -1
            case 5: current_State_Q = 6 if letter == 't' else -1
            case 6: current_State_Q = 7 if letter == 'i' else -1
            case 7: current_State_Q = 8 if letter == 'n' else -1 
            case 8: current_State_Q = 8 if letter == ' ' else -1 #final state
            # kamar 
            case 9: current_State_Q = 10 if letter == 'a' else -1
            case 10: current_State_Q = 11 if letter == 'r' else -1
            case 11: current_State_Q = 11 if letter == ' ' else -1 #final state 
            #kelas
            case 12: current_State_Q = 13 if letter == 'l' else -1 
            case 13: current_State_Q = 14 if letter == 'a' else -1
            case 14: current_State_Q = 15 if letter == 's' else -1
            case 15: current_State_Q = 15 if letter == ' ' else -1 #final state
            #lapangan
            case 16: current_State_Q = 17 if letter == 'a' else -1 
            case 17: current_State_Q = 18 if letter == 'p' else -1
            case 18: current_State_Q = 19 if letter == 'a' else -1
            case 19: current_State_Q = 20 if letter == 'n' else -1
            case 20: current_State_Q = 21 if letter == 'g' else -1
            case 21: current_State_Q = 22 if letter == 'a' else -1
            case 22: current_State_Q = 23 if letter == 'n' else -1
            case 23: current_State_Q = 23 if letter == ' ' else -1 #final state
            #atap
            case 24: current_State_Q = 25 if letter == 't' else -1
            case 25: current_State_Q = 26 if letter == 'a' else -1
            case 26: current_State_Q = 27 if letter == 'p' else -1
            case 27: current_State_Q = 27 if letter == ' ' else -1 #Final state
    return current_State_Q == 8 or current_State_Q == 11 or current_State_Q == 15 or current_State_Q == 23 or current_State_Q == 27

def parser(sentence):
    ERR = Exception('ParsingError')
    
    # Memecah kalimat menjadi kata-kata individu dan menambahkan string kosong di akhir
    words = sentence.split()
    words.append('')
    
    struktur = []
    
    stack = []
    
    state = 0
    print("Stack:")
    print(stack)
    
    stack.append('#')
    state = 1
    print(stack)
    
    stack.append('START')
    state = 2
    
    # Indeks untuk iterasi
    i = 0
    
    try:
        while stack[-1] != '#':
            print(stack)
            
            word = words[i]
            
            if word != '': 
                token = tokenRecognizer(word)
            
            match stack[-1]:
                case 'START':
                    if token == 'S':
                        stack.pop()
                        stack.append('O OR K')
                        stack.append('P')
                        stack.append('S')
                    else: 
                        raise ERR
                case 'O OR K':
                    if word == '':
                        stack.pop()
                    else:
                        if token == 'O':
                            stack.pop()
                            stack.append('Z')
                            stack.append('O')
                        elif token == 'K':
                            stack.pop()
                            stack.append('Z')
                        else: 
                            raise ERR
                case 'Z':
                    if word == '':
                        stack.pop()
                    elif token == 'K':
                        stack.pop()
                        stack.append('K')
                    else: 
                        raise ERR
                case 'S':
                    if token == 'S':
                        struktur.append(stack.pop())
                        stack.append(word)
                    else: 
                        raise ERR
                case 'P':
                    if token == 'P':
                        struktur.append(stack.pop())
                        stack.append(word)
                    else: 
                        raise ERR
                case 'O':
                    if token == 'O':
                        struktur.append(stack.pop())
                        stack.append(word)
                    else: 
                        raise ERR
                case 'K':
                    if token == 'K':
                        struktur.append(stack.pop())
                        stack.append(word)
                    else: 
                        raise ERR
                case _:
                    if token != '?':
                        stack.pop()
                        i += 1
                    else: 
                        raise ERR
        
        print(stack)
        stack.pop()
        print(stack)

        print("Struktur: ", end='')
        for i in struktur[:-1]:
            print(f"{i} - ", end='')
        print(struktur[-1], "\n")

        return True 
    except Exception as e:
        print(f"ERROR: {e}")
        print(f"Kalimat \"{sentence}\" struktur tidak sesuai\n")
        return False


if __name__ == '__main__':  
    sentence = input("Kalimat: ")
    print()
    print(f"String: {sentence}\nStatus: Diterima\n") if parser(sentence) else print(f"String: {sentence}\nStatus: Ditolak \n") 
