import utils
import caesar

if __name__ == "__main__":
    #ciphertextInput = input("Input ciphertext: ")
    #cipherText = utils.cleanInput(ciphertextInput)
    cipher = "akfgh awbns qswbg siryf oebjy ibvak ehost yqakq isjsi rsovr hwsts jbfyq isifg jyisx bfvba vbiso ebagk sisvb qs"
    cipherText = utils.cleanInput(cipher)
    # caesar.letterFrequency(cipherText,"true")
    # caesar.bigramFrequency(cipherText,"true")
    # s = a, i = n,
    # b = i, v = t
    # a = j, k = e

    # is, si, ir, yi, qs
    # na, an, nu, on, ra
    
    # jy
    # ko
    
    # vb, eb, bf, ba
    # os, _s, s_, sj
    
    # ak
    # je

    lists = [("s","a"),("i","n"),("v","s"),("b","t"),("a","j"),("k","e")]
    print(caesar.replaceLetters(lists,cipher))
