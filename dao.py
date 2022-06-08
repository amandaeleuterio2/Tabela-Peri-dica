from models import Usuario, Tipo_usuario, Elemento, Classe, Curiosidades, Perguntas, Desafio, Nivel
'''e um padrão para aplicações que utilizam persistência de dados, onde tem a separação
ddas regras de negócio das regras de acesso a banco de dados, implementda em linguagem OO'''

SQL_DELETA_ELEMENTO = 'delete from elemento where id_elemento = %s'
SQL_CRIA_ELEMENTO = 'INSERT into elemento (nome_elemento, num_atomico, massa_atomica, estado_fisico, simbolo, distribuicao_eletronica, classe) values (%s, %s, %s, %s, %s, %s, %s)'
SQL_ATUALIZA_ELEMENTO = 'UPDATE elemento SET nome_elemento = %s, num_atomico = %s, massa_atomica = %s, estado_fisico = %s, simbolo = %s, distribuicao_eletronica = %s, classe = %s where id_elemento = %s'
SQL_BUSCA_ELEMENTO = 'SELECT E.id_elemento, E.nome_elemento, E.num_atomico, E.massa_atomica, E.estado_fisico, E.simbolo, E.distribuicao_eletronica, C.nome_classe as classe from elemento E inner join classe C on E.classe = C.id_classe;'
SQL_ELEMENTO_POR_ID = ' SELECT E.id_elemento, E.nome_elemento, E.num_atomico, E.massa_atomica, E.estado_fisico, E.simbolo, E.distribuicao_eletronica, E.classe, C.nome_classe as classe from classe C inner join classe C on E.classe = C.id_classe where E.id_elemento = %s'

SQL_BUSCA_USUARIO_POR_ID = 'SELECT id_usuario, usuario, nome_usuario, email_usuario, senha FROM usuario where usuario=%s'

SQL_ATUALIZA_CLASSE = 'UPDATE classe SET nome_classe = %s where id_classe = %s'
SQL_CRIA_CLASSE = 'INSERT into classe (nome_classe) values (%s)'
SQL_BUSCA_CLASSE = 'SELECT id_classe, nome_classe from classe'
SQL_DELETA_CLASSE = 'delete from classe where id_classe = %s'
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
            cursor.execute(SQL_ATUALIZA_ELEMENTO, (elemento._nome_elemento, elemento._num_atomico, elemento._massa_atomica,
                           elemento._estado_fisico, elemento._simbolo, elemento._distribuicao_eletronica, elemento._classe, elemento._id_elemento))
        else:
            cursor.execute(SQL_CRIA_ELEMENTO, (elemento._nome_elemento, elemento._num_atomico, elemento._massa_atomica,
                           elemento._estado_fisico, elemento._simbolo, elemento._distribuicao_eletronica, elemento._classe))
            cursor._id = cursor.lastrowid

        self.__db.connection.commit()
        return elemento

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_ELEMENTO)
        elementos = traduz_elementos(cursor.fetchall())
        return elementos

    def busca_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_ELEMENTO_POR_ID, (id,))
        tupla = cursor.fetchone()
        return Elemento(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6], tupla[7], id=tupla[0])

    def deletar(self, id):
        self.__db.connection.cursor().execute(SQL_DELETA_ELEMENTO, (id,))
        self.__db.connection.commit()


def traduz_elementos(Elementos):
    def cria_elemento_com_tupla(tupla):
        return Elemento(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6], tupla[7], id=tupla[0])
    return list(map(cria_elemento_com_tupla, Elementos))


class ClasseDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, classe):
        cursor = self.__db.connection.cursor()

        if (classe._id_classe):
            cursor.execute(SQL_ATUALIZA_CLASSE, (
                classe._nome_classe, classe._id_classe))

        else:
            cursor.execute(SQL_CRIA_CLASSE, (
                classe._nome_classe))
            cursor._id = cursor.lastrowid

        self.__db.connection.commit()
        return classe

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_CLASSE)
        classes = traduz_classes(cursor.fetchall())
        return classes

    def busca_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_CLASSE_POR_ID, (id,))
        tupla = cursor.fetchone()
        return Classe(tupla[1], id=tupla[0])

    def deletar(self, id):
        self.__db.connection.cursor().execute(SQL_DELETA_CLASSE, (id,))
        self.__db.connection.commit()


def traduz_classes(classes):
    def cria_classe_com_tupla(tupla):
        return classes(tupla[1], id=tupla[0])
    return list(map(cria_classe_com_tupla, classes))


class CuriosidadesDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, curiosidade):
        cursor = self.__db.connection.cursor()

        if (curiosidade._id):
            cursor.execute(SQL_ATUALIZA_CURIOSIDADE, (curiosidade._tipo,
                           curiosidade._descricao, curiosidade._elemento, curiosidade._id))
        else:
            cursor.execute(SQL_CRIA_CURIOSIDADE, (curiosidade._tipo,
                           curiosidade._descricao, curiosidade._elemento))
            cursor._id = cursor.lastrowid

        self.__db.connection.commit()
        return curiosidade

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_CURIOSIDADE)
        curiosidades = traduz_curiosidades(cursor.fetchall())
        return curiosidades

    def busca_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_CURIOSIDADE_POR_ID, (id,))
        tupla = cursor.fetchone()
        return Curiosidades(tupla[1], tupla[2], tupla[3], id=tupla[0])

    def deletar(self, id):
        self.__db.connection.cursor().execute(SQL_DELETA_CURIOSIDADE, (id,))
        self.__db.connection.commit()


def traduz_curiosidades(curiosidades):
    def cria_curiosidade_com_tupla(tupla):
        return curiosidades(tupla[1], tupla[2], tupla[3], id=tupla[0])
    return list(map(cria_curiosidade_com_tupla, curiosidades))


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
    return Usuario(tupla[0], tupla[1], tupla[2],tupla[3], tupla[4])
