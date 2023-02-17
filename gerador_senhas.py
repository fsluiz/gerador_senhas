import random, string

tamanho = int(input('Digite o tamanho de senha que você deseja: ')) # tamanho da senha

chars = string.ascii_letters + string.digits + "!@#$%&*()_+?" #strutura da senha

rnd = random.SystemRandom() #os.urandom

print(''.join(rnd.choice(chars) for i in range(tamanho))) # retorna uma lista com caracter randomico