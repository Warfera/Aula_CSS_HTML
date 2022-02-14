def save(mensagem):
    arquivo = open('mensagem.txt', 'w')
    arquivo.write(mensagem)
    arquivo.close()




idade = int(input('Digite sua idade: '))
def status_voto(idade):
    if idade >= 18 and idade < 70:
        return 'obrigatório'
    elif idade >= 16:
        return 'facultativo'
    else:
        return 'proibido'

resposta = status_voto(idade)
save(f'Com {idade} anos, o seu voto é {resposta}!')
