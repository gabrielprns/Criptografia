L1=['!¨%##%¨FDFGDFGD%ETYD%¨%%¨¨E%D%DTERTD%','FWYTUIRWYTURY1763sdhgfjh','247¨%¨&%&¨%&¨%)()(¨&E$$#sagefygfysua',
    'X&*()ADEArytu','*','&','67&¨&*56','(','?!@SHFU36573','/','$','i','5683',')','j','v','y','ç','#$%BN','@473376565%##$%#',
    'Kehguei7569583765%$%¨$%¨$','khuthgued79997745625$%¨$%','Y389753897$%%¨FFGGHJgjhdgfjhds','M','[','´','`','W','8&*(645','H','Ç',
    '3875)*¨*&¨%835','375JGHj0-','G','K','NBZNVCBNZAT678647454%¨$%¨$%','R','97¨&*8','B','d','7564','O%&¨%&¨jgadhje','l','c','´Ç´TDÇ','´54TY','$%¨$453545$%$%&$54546ftfYTF',
    'XBCIAHDCBIA*¨761371637$%¨$%',')*¨##$%%¨GHF','27428974URIYTUIREYT','¨&*¨*&BSFG67S64G54Y2T%$$#BDVBFYUDHS','&*&*&)(873251HJHGG536164','NVHUFYHgydhfsgHDUF754897']
def numaleatório():
    import random
    global p
    global q
    global r
    global chave
    p = random.randrange(0,1000000000000)
    while p%246==0 and p%487==0:
       break
    q = random.randrange(0,1000000000000)
    while q!=p and q%246==0 and q%487==0:
        break
    r = random.randrange(0,1000000000000)
    while r!=p and r!=q and r%246==0 and r%487==0:
        break
    chave=p*q*r


def cifra(mensagem,chave, p, q, r):
    global listacifra
    scale=len(mensagem)
    listacifra=[]
    for t in range(0,scale):
         letra=mensagem[t]
         s=ord(letra)
         o=s*(q*7)
         w=o*(p*9)
         z=w*(r*7)
         j=z*(2*chave)
         j=int(j)
         j=str(j)
         listacifra.append(j)
    

def cifra_2(listacifra):
    import random
    global listacifra_2
    listacifra_2=[]
    listacifra_3=L1+listacifra
    for y in listacifra:
        letra=listacifra.index(y)
        k = random.randrange(20,200)
        u=listacifra_3[(letra+k)%len(listacifra_3)]
        listacifra_2.append(u)
    return ''.join(listacifra_2)
        

   
def decifrar(cifra_2, chave, p, q, r):
    listadecifra=[]
    scale=len(listacifra)
    for t in range(0,scale):
         listacifra[t]=int(listacifra[t])
         deci=listacifra[t]/(q*7)
         tex=deci/(p*9)
         z=tex/(r*7)
         j=z/(2*chave)
         j=round(j)
         letter=int(j)
         letter=chr(letter)
         listadecifra.append(letter)
    return ''.join(listadecifra)
    

                
def principal():
    numaleatório()
    print('Bem-Vindo ao cifrador e decifrador de mensagens')
    mensagem=input('escreva uma mensagem qualquer com no máximo 128 carácteres: '[0:128])
    
    cifra(mensagem,chave, p, q, r)
    print('sua mensagem cifrada será: ',cifra_2(listacifra))
    

    print('chave publica : ',chave)
    

    input('aperte enter para retornar o valor original da mensagem')

    
    print('sua mensagem decifrada será: ',decifrar(cifra, chave, p, q, r))


    input('aperte enter para continuar')
    

    rnp=input('deseja cripitografar outra mensagem ?, digite s para sim, digite n para não: ')
    for i in rnp:
       if rnp=='s':
          principal()
       elif rnp=='n':
          print('obrigado por testar o programa!!!')
          break
         
    
    
    
    
 
principal()
