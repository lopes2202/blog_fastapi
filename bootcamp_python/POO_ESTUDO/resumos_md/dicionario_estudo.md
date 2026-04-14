# Criando Dicionários 

conjunto não ordenado de pares chave:valor OU
usar a função dict

exemplo:

variavel = {"chave_1": "oi}
print(variavel)

pessoa = dict(nome="gabriel")

para adicionar uma informação ao dicionário é:
pessoa["telefone"] = '8394-4834'

para acessar o valor
pessoa["nome"]
variavel["chave_1"]

Dicionários aninhados -> pode armazenar qualquer tipo de objeto python como valor
exemplo:
st.session_state["lista_mensagens"][st.session_state["chat_selecionado"]].append(mensagem_waynebot)

# Iterar dicionários 

for coluna in tabela:
    print(coluna, tabela[coluna])


# Metódos da classe Dict

.clear -> serve pra apagar os dados do dicionário
.copy -> tira uma cópia do dicionário 
.fromkeys -> cria chaves com o valor none ou da pra criar um conjunto de chaves e atribuir um valor pra elas (poder ser um dicionário existente ou ñ)
.get -> acessar os valores do dicionário (contatos.get("chave"))
.itens -> retorna uma lista de tuplas
.keys -> retorna só as chaves do dicionário 
.pop -> remove chave e retorna o valor que removeu
.popitem -> remove os itens em sequencia
.setdefault ->  serve para adicionar um valor que ñ existe
.update -> atualiza o dicionário 
.values -> metódos que retorna somente os valores

metódo IN ->
exemplo: resultado = "x" in "y"
print(resultado)
procura se x existe em y

Metódo del -> serve pra remover um valor
exemplo: 
del X["teste"]["objeto_removido"]
seleciona a chave que quer tenha algo removido e depois aninha ela