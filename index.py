from flask import Flask, render_template, request, redirect, session, flash
import os

from dao import ElementoDao, ClasseDao, CuriosidadesDao, UsuarioDao
from flask_mysqldb import MySQL

from models import Usuario, Tipo_usuario, Elemento, Classe, Curiosidades, Perguntas, Desafio, Nivel

app = Flask(__name__)
app.secret_key = 'LP2'
app.config['UPLOAD_PATH'] = os.path.dirname(
    os.path.abspath(__file__))+'/uploads'
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'tabelaperiodica'
app.config['MYSQL_PORT'] = 3306
db = MySQL(app)

elemento_dao = ElementoDao(db)
usuario_dao = UsuarioDao(db)
classe_dao = ClasseDao(db)
curiosidades_dao = CuriosidadesDao(db)


@app.route('/')
def index():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login')
    return render_template('index.html')


@app.route('/lista_elementos')
def lista_elementos():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=lista_elementos')
    lista = elemento_dao.listar()
    return render_template('lista.html', titulo="Elementos Cadastrados", elementos=lista)


@app.route('/lista_classes')
def lista_classes():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=lista_classes')
    lista = classe_dao.listar()
    return render_template('lista_classes.html', titulo="Classes Cadastradas", classes=lista)


@app.route('/lista_curiosidades')
def lista_curiosidades():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=lista_curiosidades')
    lista = curiosidades_dao.listar()
    return render_template('lista_curiosidades.html', titulo="Curiosidades Cadastradas", curiosidades=lista)


@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=novo')
    lista = classe_dao.listar()
    return render_template('novo.html', titulo="Cadastrando novo elemento", classes=lista)


@app.route('/nova_classe')
def novaclasse():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=nova_classe')
    return render_template('nova_classe.html', titulo="Cadastrando nova classe")


@app.route('/nova_curiosidade')
def nova_curiosidade():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=nova_curiosidade')
    lista = elemento_dao.listar()
    return render_template('nova_curiosidade.html', titulo="Cadastrando nova curiosidade", elementos=lista)


@app.route('/criar', methods=['POST', ])
def criar():
    nome_elemento = request.form['nome_elemento']
    num_atomico = request.form['num_atomico']
    massa_atomica = request.form['massa_atomica']
    estado_fisico = request.form['estado_fisico']
    simbolo = request.form['simbolo']
    distribuicao_eletronica = request.form['distribuicao_eletronica']
    classe_id = request.form['classe']
    elemento = Elemento(nome_elemento, num_atomico, massa_atomica,
                        estado_fisico, simbolo, distribuicao_eletronica, classe_id, None)

    # lista.append(pet)
    elemento_dao.salvar(elemento)
    return redirect('/lista_elementos')


@app.route('/criarclasse', methods=['POST', ])
def criarclasse():
    nome_classe = request.form['nome_classe']
    classe = Classe(nome_classe)

    classe_dao.salvar(classe)
    return redirect('/lista_classes')


@app.route('/criarcuriosidades', methods=['POST', ])
def criarcuriosidades():
    tipo = request.form['tipo']
    descricao = request.form['descricao']
    elemento_id = request.form['elemento']

    curiosidades = Curiosidades(tipo, descricao, elemento_id)
    curiosidades_dao.salvar(curiosidades)
    return redirect('/lista_curiosidades')


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    if proxima == None:
        proxima = ''
    return render_template('login.html', proxima=proxima)


@app.route('/autenticar', methods=['POST', ])
def autenticar():
    usuario = usuario_dao.busca_por_id(request.form['usuario'])
    if usuario:
        if usuario._senha == request.form['senha']:
            session['usuario_logado'] = request.form['usuario']
            flash(request.form['usuario'] + ' logou com sucesso!')
            proxima_pagina = request.form['proxima']
            if proxima_pagina == '':
                return redirect('/')
            else:
                return redirect('/{}'.format(proxima_pagina))
    flash('Não logado, tente novamente!')
    return redirect('/login')


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado!')
    return redirect('/login')


@app.route('/editar/<int:id>')
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('editar')))
    elementos = elemento_dao.busca_por_id(id)
    lista = classe_dao.listar()
    return render_template('editar.html', titulo="Editando Dados dos Elementos", elemento=elementos, classes=lista)


@app.route('/editar_classes/<int:id>')
def editar_classes(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('editar_classes')))
    classe = classe_dao.busca_por_id(id)
    return render_template('editarclientes.html', titulo="Editando Dados das Classes", classes=classe)


@app.route('/editar_curiosidades/<int:id>')
def editar_curiosidades(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('editar_curiosidades')))
    curiosidade = curiosidades_dao.busca_por_id(id)
    return render_template('editar_curiosidades.html', titulo="Editando Dados das Curiosidades", curiosidades=curiosidade)


@app.route('/atualizar', methods=['POST', ])
def atualizar():
    nome_elemento = request.form['nome_elemento']
    num_atomico = request.form['num_atomico']
    massa_atomica = request.form['massa_atomica']
    estado_fisico = request.form['estado_fisico']
    simbolo = request.form['simbolo']
    distribuicao_eletronica = request.form['distribuicao_eletronica']
    classe_id = request.form['classe']
    id = request.form['id']

    elemento = Elemento(nome_elemento, num_atomico, massa_atomica,
                        estado_fisico, simbolo, distribuicao_eletronica, classe_id, None, id)
    elemento_dao.salvar(elemento)
    return redirect('/lista_elementos')


@app.route('/atualizarclasse', methods=['POST', ])
def atualizarclasse():
    nome_classe = request.form['nome_classe']
    id = request.form['id']
    classe = Classe(nome_classe, id)

    classe_dao.salvar(classe)
    return redirect('/lista_classes')


@app.route('/atualizarcuriosidades', methods=['POST', ])
def atualizarcuriosidades():
    tipo = request.form['tipo']
    descricao = request.form['descricao']
    elemento_id = request.form['elemento']
    id = request.form['id']

    curiosidades = Curiosidades(tipo, descricao, elemento_id, id)
    curiosidades_dao.salvar(curiosidades)
    return redirect('/lista_curiosidades')


@app.route('/deletar/<int:id>')
def deletar(id):
    elemento_dao.deletar(id)
    return redirect('/lista_elementos')


@app.route('/deletarclasses/<int:id>')
def deletarfinanceiro(id):
    classe_dao.deletar(id)
    return redirect('/lista_classes')


@app.route('/deletarcuriosidades/<int:id>')
def deletarcuriosidades(id):
    curiosidades_dao.deletar(id)
    return redirect('/lista_curiosidades')


@app.route('/uploads/<nome_arquivo>')
def upload_file(nome_arquivo):
    return send_from_directory(app.config['UPLOAD_PATH'], nome_arquivo)


if __name__ == '__main__':
    app.run(debug=True)
