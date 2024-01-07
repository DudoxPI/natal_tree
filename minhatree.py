# minha arvore de natal
def arvore(tamanho):
    estrela = 1
    dobro = tamanho * 2
    for i in range(tamanho):
        print(f'{estrela * '*':^{dobro}}')
        estrela += 2
    for tronco in range(tamanho//3):
        print(f'{(tamanho//4) * '*':^{tamanho*2}}')


arvore(30)
