usuarios = [
    {
        'nome' : "alex machado",
        'idade' : 41,
            'email' : "alex@gmail.com"
    },
    {
         'nome' : "joana da silva",
          'idade' : 18,
          'email' : "joana@gmail.com",
    },
    {
         'nome' : "karoiyne de souza",
         'idade' : 28,
          'email' : "karol@gmail.com",
    },
]

for usuario in usuarios:
    for chave, valor in usuario.items():
        print(f"{chave.capitalize()}: {valor}")
    print(f"{'.'*40}")