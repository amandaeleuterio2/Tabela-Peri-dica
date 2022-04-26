from models import usuario, tipo_usuario, elemento, classe, curiosidades, perguntas, desafio, nivel
'''e um padrão para aplicações que utilizam persistência de dados, onde tem a separação
ddas regras de negócio das regras de acesso a banco de dados, implementda em linguagem OO'''

SQL_DELETA_ELEMENTO = 'delete from elemento where id_elemento = %s'
SQL_CRIA_ELEMENTO = 'INSERT into elemento (nome_elemento, num_atomico, massa_atomica, estado_fisico, simbolo, distribuicao_eletronica, classe) values (%s, %s, %s, %s, %s, %s, %s)'
SQL_ATUALIZA_ELEMENTO = 'UPDATE elemento SET nome_elemento = %s, num_atomico = %s, massa_atomica = %s, estado_fisico = %s, simbolo = %s, distribuicao_eletronica = %s, classe = %s where id_elemento = %s'
SQL_BUSCA_ELEMENTO = 'SELECT E.id_elemento, E.nome_elemento, E.num_atomico, E.massa_atomica, E.estado_fisico, E.simbolo, E.distribuicao_eletronica, E.classe, C.nome_classe as classe from classe C inner join classe C on E.classe = C.id_classe'
SQL_ELEMENTO_POR_ID = ' SELECT E.id_elemento, E.nome_elemento, E.num_atomico, E.massa_atomica, E.estado_fisico, E.simbolo, E.distribuicao_eletronica, E.classe, C.nome_classe as classe from classe C inner join classe C on E.classe = C.id_classe where E.id_elemento = %s'

SQL_BUSCA_USUARIO_POR_ID = 'SELECT id, nome, senha from usuario where id=%s'

SQL_ATUALIZA_CLASSE = 'UPDATE classe SET nome_classe = %s where id_classe = %s'
SQL_CRIA_CLASSE = 'INSERT into classe (nome_classe) values (%s)'
SQL_BUSCA_CLASSE = 'SELECT id_classe, nome_classe from classe'
SQL_DELETA_CLASSE  = 'delete from classe where id_classe = %s'
SQL_CLASSE_POR_ID = 'SELECT id_classe, nome_classe from classe where id_clase = %s'

SQL_ATUALIZA_CURIOSIDADE = 'UPDATE curiosidade SET tipo = %s, descricao = %s, elemento = %s where id_curiosidade = %s'
SQL_CRIA_CURIOSIDADE = 'INSERT into curiosidade (tipo, descricao, elemento) values (%s, %s, %s)'
SQL_BUSCA_CURIOSIDADE = 'SELECT CS.id_curiosidade, CS.tipo, CS.descricao, CS.elemento, E.nome_elemento as elemento from curiosidade CS inner join elemento E on CS.elemento = E.id_elemento'
SQL_DELETA_CURIOSIDADE = 'delete from curiosidade where id_curiosidade = %s'
SQL_CURIOSIDADE_POR_ID = 'SELECT CS.id_curiosidade, CS.tipo, CS.descricao, CS.elemento, E.nome_elemento as elemento from curiosidade CS inner join elemento E on CS.elemento = E.id_elemento where CS.id_curiosidade=%s'

class ElementoDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, elemento):
        cursor = self.__db.connection.cursor()

        if (elemento._id_elemento):
            cursor.execute(SQL_ATUALIZA_ELEMENTO, (elemento._nome_elemento, elemento.git._especie, animal._sexo, animal._raca, animal._porte, animal._cliente_id, animal._id))
        else:
            cursor.execute(SQL_CRIA_ANIMAL, (animal._nome_animal, animal._especie, animal._sexo, animal._raca, animal._porte, animal._cliente_id))
            cursor._id = cursor.lastrowid

        self.__db.connection.commit()
        return animal

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_ANIMAIS)
        animais = traduz_animais(cursor.fetchall())
        return animais

    def busca_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_ANIMAL_POR_ID, (id,))
        tupla = cursor.fetchone()
        return Animal(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6], tupla[7], id=tupla[0])

    def deletar(self, id):
        self.__db.connection.cursor().execute(SQL_DELETA_ANIMAL, (id,))
        self.__db.connection.commit()

def traduz_animais(animais):
    def cria_animal_com_tupla(tupla):
        return Animal(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6], tupla[7], id=tupla[0])
    return list(map(cria_animal_com_tupla, animais))

class ClienteDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, cliente):
        cursor = self.__db.connection.cursor()

        if (cliente._id):
            cursor.execute(SQL_ATUALIZA_CLIENTE, (
            cliente._nome, cliente._cpf, cliente._rua, cliente._numero, cliente._bairro, cliente._cidade, cliente._telefone, cliente._id))

        else:
            cursor.execute(SQL_CRIA_CLIENTE, (
            cliente._nome, cliente._cpf, cliente._rua, cliente._numero, cliente._bairro, cliente._cidade, cliente._telefone))
            cursor._id = cursor.lastrowid

        self.__db.connection.commit()
        return cliente

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_CLIENTES)
        clientes = traduz_clientes(cursor.fetchall())
        return clientes

    def busca_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_CLIENTE_POR_ID, (id,))
        tupla = cursor.fetchone()
        return Cliente(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6], tupla[7], id=tupla[0])

    def deletar(self, id):
        self.__db.connection.cursor().execute(SQL_DELETA_CLIENTE, (id,))
        self.__db.connection.commit()

def traduz_clientes(clientes):
    def cria_cliente_com_tupla(tupla):
        return Cliente(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5],tupla[6],tupla[7], id=tupla[0])
    return list(map(cria_cliente_com_tupla, clientes))

class UsuarioDao:
    def __init__(self, db):
        self.__db = db

    def busca_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_USUARIO_POR_ID, (id,))
        dados = cursor.fetchone()
        usuario = traduz_usuario(dados) if dados else None
        return usuario

def traduz_usuario(tupla):
    return Usuario(tupla[0], tupla[1], tupla[2])

class AgendamentoDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, agendamento):
        cursor = self.__db.connection.cursor()

        if (agendamento._id):
            cursor.execute(SQL_ATUALIZA_AGENDAMENTO, (agendamento._data_agendamento, agendamento._animal_id, agendamento._id))
        else:
            cursor.execute(SQL_CRIA_AGENDAMENTO, (agendamento._data_agendamento, agendamento._animal_id))
            cursor._id = cursor.lastrowid

        self.__db.connection.commit()
        return agendamento

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_AGENDAMENTO)
        agendamentos = traduz_agendamentos(cursor.fetchall())
        return agendamentos

    def busca_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_AGENDAMENTO_POR_ID, (id,))
        tupla = cursor.fetchone()
        return Agendamento(tupla[1], tupla[2], tupla[3], id=tupla[0])

    def deletar(self, id):
        self.__db.connection.cursor().execute(SQL_DELETA_AGENDAMENTO, (id,))
        self.__db.connection.commit()

def traduz_agendamentos(agendamentos):
    def cria_agendamento_com_tupla(tupla):
        return Agendamento(tupla[1], tupla[2], tupla[3], id=tupla[0])
    return list(map(cria_agendamento_com_tupla, agendamentos))


class AtendimentoDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, atendimento):
        cursor = self.__db.connection.cursor()
        if (atendimento._id):
            cursor.execute(SQL_ATUALIZA_ATENDIMENTO, (atendimento._descricao, atendimento._subtotal, atendimento._adicional, atendimento._desconto, atendimento._total,
                                                      atendimento._funcionario_id, atendimento._agenda_id, atendimento._id))
        else:
            cursor.execute(SQL_CRIA_ATENDIMENTO, (atendimento._descricao, atendimento._subtotal, atendimento._adicional, atendimento._desconto, atendimento._total,
                                                  atendimento._funcionario_id, atendimento._agenda_id))
            cursor._id = cursor.lastrowid

        self.__db.connection.commit()
        return atendimento

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_ATENDIMENTO)
        atendimentos = traduz_atendimentos(cursor.fetchall())
        return atendimentos

    def busca_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_ATENDIMENTO_POR_ID, (id,))
        tupla = cursor.fetchone()
        return Atendimento(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6], tupla[7], tupla[8], tupla[9], id=tupla[0])

    def deletar(self, id):
        self.__db.connection.cursor().execute(SQL_DELETA_ATENDIMENTO, (id,))
        self.__db.connection.commit()

def traduz_atendimentos(atendimentos):
    def cria_atendimento_com_tupla(tupla):
        return Atendimento(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6], tupla[7], tupla[8], tupla[9], id=tupla[0])
    return list(map(cria_atendimento_com_tupla, atendimentos))

class FuncionarioDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, funcionario):
        cursor = self.__db.connection.cursor()
        if (funcionario._id):
            cursor.execute(SQL_ATUALIZA_FUNCIONARIO, (funcionario._nome, funcionario._cpf, funcionario._rua, funcionario._numero, funcionario._bairro, funcionario._cidade, funcionario._telefone, funcionario._data_admissao, funcionario._cargo, funcionario._id))
        else:
            cursor.execute(SQL_CRIA_FUNCIONARIO, (funcionario._nome, funcionario._cpf, funcionario._rua, funcionario._numero, funcionario._bairro, funcionario._cidade, funcionario._telefone, funcionario._data_admissao, funcionario._cargo))
            cursor._id = cursor.lastrowid

        self.__db.connection.commit()
        return funcionario

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_FUNCIONARIO)
        funcionarios = traduz_funcionarios(cursor.fetchall())
        return funcionarios

    def busca_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_FUNCIONARIO_POR_ID, (id,))
        tupla = cursor.fetchone()
        return Funcionario(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6], tupla[7], tupla[8], tupla[9], id=tupla[0])

    def deletar(self, id):
        self.__db.connection.cursor().execute(SQL_DELETA_FUNCIONARIO, (id,))
        self.__db.connection.commit()

def traduz_funcionarios(funcionarios):
    def cria_funcionario_com_tupla(tupla):
        return Funcionario(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5],tupla[6],tupla[7], tupla[8], tupla[9], id=tupla[0])
    return list(map(cria_funcionario_com_tupla, funcionarios))

class FinanceiroDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, financeiro):
        cursor = self.__db.connection.cursor()
        if (financeiro._id):
            cursor.execute(SQL_ATUALIZA_FINANCEIRO, (financeiro._data_hora_chegada, financeiro._funcionario_id, financeiro._atendimento_id, financeiro._agendamento_id,
                                                     financeiro._forma_pagamento, financeiro._valor, financeiro._data_recebimento, financeiro._data_hora_saida, financeiro._id))
        else:
            cursor.execute(SQL_CRIA_FINANCEIRO, (financeiro._data_hora_chegada, financeiro._funcionario_id, financeiro._atendimento_id, financeiro._agendamento_id,
                                                     financeiro._forma_pagamento, financeiro._valor, financeiro._data_recebimento, financeiro._data_hora_saida))
            cursor._id = cursor.lastrowid

        self.__db.connection.commit()
        return financeiro

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_FINANCEIRO)
        financeiros = traduz_financeiros(cursor.fetchall())
        return financeiros

    def busca_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_FINANCEIRO_POR_ID, (id,))
        tupla = cursor.fetchone()
        return Financeiro(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6], tupla[7], tupla[8], tupla[9], tupla[10], tupla[11], id=tupla[0])

    def deletar(self, id):
        self.__db.connection.cursor().execute(SQL_DELETA_FINANCEIRO, (id,))
        self.__db.connection.commit()

def traduz_financeiros(financeiros):
    def cria_financeiro_com_tupla(tupla):
        return Financeiro(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6], tupla[7], tupla[8], tupla[9], tupla[10], tupla[11], id=tupla[0])
    return list(map(cria_financeiro_com_tupla, financeiros))