class usuario():
    def __init__(self, nome, email, senha, tipo_usuario_id, tipo_usuario, id=None):
        self._id=id
        self._nome=nome
        self._email=email
        self._senha=senha
        self._tipo_usuario_id = tipo_usuario_id
        self._tipo_usuario=tipo_usuario

class tipo_usuario():
    def __init__(self, descricao_tipo_usuario, id=None):
        self._id=id
        self._descricao_tipo_usuario=descricao_tipo_usuario

class elemento():
    def __init__(self, nome_elemento, num_atomico, massa_atomica, estado_fisico, simbolo, distribuicao_eletronica, classe_id, nome_classe, id=None):
        self._id=id
        self._nome_elemento=nome_elemento
        self._num_atomico=num_atomico
        self._massa_atomica=massa_atomica
        self._estado_fisico=estado_fisico
        self._simbolo=simbolo
        self._distribuicao_eletronica=distribuicao_eletronica
        self._classe_id=classe_id
        self.nome_classe=nome_classe

class classe():
    def __init__(self, nome_classe, id=None):
        self._id=id
        self._nome_classe=nome_classe

class curiosidades():
    def __init__(self, tipo, descricao, elemento, id=None):
        self._id=id
        self._tipo=tipo
        self._descricao=descricao
        self._elemento=elemento

class perguntas():
    def __init__(self, nome_pergunta, descricao, resposta, desafio_id, id=None):
        self._id=id
        self._nome_pergunta=nome_pergunta
        self._descricao=descricao
        self._resposta=resposta
        self._desafio_id=desafio_id

class desafio():
    def __init__(self, quantidade_perguntas, nivel_id, id=None):
        self._id=id
        self._quantidade_perguntas=quantidade_perguntas
        self._nivel_id=nivel_id

class nivel():
    def __init__(self, nome_nivel, id=None):
        self._id=id
        Self._nome_nivel=nome_nivel
