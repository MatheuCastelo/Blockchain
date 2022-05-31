import hashlib
from time import sleep


"""
VARIAVEIS
"""



"""
FIM VARIAVEIS
"""


"""
Neste espaço irei criar as funções.
"""

def BlockFormer(block, nonce, data, hashBlock, hashPrev):
    verify = False

    while verify == False:
        blockData = str(block) +  ":" + str(nonce) +  ":" + str(data)  + ":" + str(hashPrev)
        hashBlockTest = hashlib.sha256(bytes(str(blockData), encoding='utf-8')).hexdigest()

        hashVerify = hashBlockTest[:4]

        #print(nonce)
        #sleep(0.2)
        #print(hashVerify == "0")bil
        if hashVerify == "0000":
            hashReturn = [block, nonce, data, hashBlockTest, hashPrev]
            verify = True
            
            return hashReturn

        else:
            nonce = nonce + 1

def BlockTester(block, nonce, data, hashBlock, hashPrev):

    blockData = str(block) +  ":" + str(nonce) +  ":" + str(data)  +  ":" + str(hashPrev)
    hashBlockTest = hashlib.sha256(bytes(blockData, encoding='utf8')).hexdigest()
    hashVerify = hashBlockTest[:4]

    return hashBlockTest

def BlockFormater(block, nonce, data, hashBlock, hashPrev):
    blockData = str(block) +  ":" + str(nonce) +  ":" + str(data)  +  ":" + str(hashPrev)
    
    print('#####################################')
    print('Block:           ' + str(block))
    print('Nonce:           ' + str(nonce))
    print('Data:            ' + str(data))
    print('Hash:            ' + str(hashBlock))
    print('Previous Hash:   ' + str(hashPrev))
    print('block all:       ' + str(blockData))
    print('#####################################\n')



"""
FIM FUNÇÕES
"""

def main():
    lets = True
    block = 0
    nonce = 0
    data = ""
    hashBlock = "0000000000000000000000000000000000000000000000000000000000000000"
    hashPrev = hashBlock
    result = []
    lets = True
    test = ""

    data = input("Insira os dados do bloco:")
    result.append(BlockFormer(block, nonce, data, hashBlock, hashPrev))
    BlockFormater(result[block][0], result[block][1], result[block][2], result[block][3], result[block][4])

    while lets == True:
        #print(hashPrev[:4])


        if hashPrev[:4] == "0000":
            test = BlockTester(block, result[block][1], data, hashBlock, hashPrev)
            #print(test)
            
            if test == result[block][3]:

                hashPrev = result[block][3]
                block = block + 1
                
                data = input("Insira os dados do bloco:")

                result.append(BlockFormer(block, nonce, data, hashBlock, hashPrev))

                BlockFormater(result[block][0], result[block][1], result[block][2], result[block][3], result[block][4])
                """
                lets = input("Digite s para criar outro bloco: ")
                
                if lets == "s":
                    lets = True
                else:
                    lets = False
                """

            else:
                print("A blockchain foi modificada")
                lets = False
        else:
            print("A blockchain foi modificada")
            lets = False
        
     

main()