data_escrita = open("Dados",'a')
data_leitura = open("Dados",'r')
ask = 0
t = 0 

def check(tentativas,data_escrita,data_leitura):
    if ask == 1:
        enter_name = input('Nome de usuario:')
        enter_pass = input('Senha:')
        data_escrita.writelines('Usuario:{}|Senha:{}\n'.format(enter_name,enter_pass))
        print('Cadastro concluido com sucesso!')
    if ask == 2 :
        enter_name = input('Nome de usuario:')
        enter_pass = input('Senha:') 
        if enter_name and enter_name in data_leitura.readlines():
            print('Entrou')
        elif enter_name or enter_pass not in data_leitura.readlines() and tentativas < 3 :
            tentativas += 1
            print('Nome de usuario ou senha incorreto')
            return tentativas 
    enter_name,enter_pass = ('','')
while ask != 3:
    ask = int(input('1-Cadastrar\n2-Entrar\n3-Sair\nResposta:'))
    check(t,data_escrita,data_leitura)