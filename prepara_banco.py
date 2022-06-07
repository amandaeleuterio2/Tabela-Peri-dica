import MySQLdb
print('Conectando...')
conn = MySQLdb.connect(user='root', passwd='123456',
                       host='127.0.0.1', port=3306, charset='utf8')

# Descomente se quiser desfazer o banco
conn.cursor().execute("DROP DATABASE `tabelaperiodica`;")
conn.commit()

criar_tabelas = '''SET NAMES utf8;
    CREATE DATABASE `tabelaperiodica` DEFAULT CHARSET=utf8;
    USE `tabelaperiodica`;

CREATE TABLE IF NOT EXISTS `tabelaperiodica`.`classe` (
  `id_classe` INT NOT NULL AUTO_INCREMENT,
  `nome_classe` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_classe`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `tabelaperiodica`.`elemento` (
  `id_elemento` INT NOT NULL AUTO_INCREMENT,
  `nome_elemento` VARCHAR(45) NOT NULL,
  `num_atomico` INT NOT NULL,
  `massa_atomica` DOUBLE NOT NULL,
  `estado_fisico` VARCHAR(20) NOT NULL,
  `simbolo` VARCHAR(2) NOT NULL,
  `distribuicao_eletronica` VARCHAR(20) NOT NULL,
  `classe` INT NOT NULL,
  PRIMARY KEY (`id_elemento`),
  INDEX `fk_elemento_classe_idx` (`classe` ASC) VISIBLE,
  CONSTRAINT `fk_elemento_classe`
    FOREIGN KEY (`classe`)
    REFERENCES `tabelaperiodica`.`classe` (`id_classe`)
    ON DELETE CASCADE 
    ON UPDATE CASCADE)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `tabelaperiodica`.`curiosidade` (
  `id_curiosidade` INT NOT NULL AUTO_INCREMENT,
  `tipo` VARCHAR(45) NOT NULL,
  `descricao` TEXT NOT NULL,
  `elemento` INT NOT NULL,
  PRIMARY KEY (`id_curiosidade`),
  INDEX `fk_curiosidade_elemento1_idx` (`elemento` ASC) VISIBLE,
  CONSTRAINT `fk_curiosidade_elemento1`
    FOREIGN KEY (`elemento`)
    REFERENCES `tabelaperiodica`.`elemento` (`id_elemento`)
    ON DELETE CASCADE 
    ON UPDATE CASCADE)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `tipo_usuario` (
  `id_tipo_usuario` int NOT NULL,
  `descricao_tipo_usuario` varchar(45) NOT NULL,
  KEY `FK_tipo_usuario_usuario` (`id_tipo_usuario`),
  CONSTRAINT `FK_tipo_usuario_usuario` FOREIGN KEY (`id_tipo_usuario`) REFERENCES `usuario` (`id_usuario`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;


CREATE TABLE IF NOT EXISTS `usuario` (
  `id_usuario` int NOT NULL AUTO_INCREMENT,
  `usuario` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `nome_usuario` varchar(55) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `email_usuario` varchar(45) NOT NULL,
  `senha` varchar(45) NOT NULL,
  PRIMARY KEY (`id_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

CREATE TABLE IF NOT EXISTS `tabelaperiodica`.`nivel` (
  `id_nivel` INT NOT NULL AUTO_INCREMENT,
  `nome_nivel` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_nivel`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `tabelaperiodica`.`desafio` (
  `id_desafio` INT NOT NULL AUTO_INCREMENT,
  `quanidade_perguntas` VARCHAR(45) NOT NULL,
  `nivel` INT NOT NULL,
  PRIMARY KEY (`id_desafio`),
  INDEX `fk_desafio_nivel1_idx` (`nivel` ASC) VISIBLE,
  CONSTRAINT `fk_desafio_nivel1`
    FOREIGN KEY (`nivel`)
    REFERENCES `tabelaperiodica`.`nivel` (`id_nivel`)
    ON DELETE CASCADE 
    ON UPDATE CASCADE)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `tabelaperiodica`.`perguntas` (
  `id_perguntas` INT NOT NULL AUTO_INCREMENT,
  `nome_pergunta` VARCHAR(20) NOT NULL,
  `descricao` TEXT NOT NULL,
  `resposta` TEXT NOT NULL,
  `desafio` INT NOT NULL,
  PRIMARY KEY (`id_perguntas`),
  INDEX `fk_perguntas_desafio1_idx` (`desafio` ASC) VISIBLE,
  CONSTRAINT `fk_perguntas_desafio1`
    FOREIGN KEY (`desafio`)
    REFERENCES `tabelaperiodica`.`desafio` (`id_desafio`)
    ON DELETE CASCADE 
    ON UPDATE CASCADE)
ENGINE = InnoDB;

'''

conn.cursor().execute(criar_tabelas)

cursor = conn.cursor()
cursor.executemany(
    'INSERT INTO `classe` (`id_classe`, `nome_classe`) VALUES (%s, %s)',
    [
        (1, 'Metais Alcalinos'),
        (2, 'Metais Alcalinos Terrosos'),
        (3, 'Metais de Transição'),
        (4, 'Lantanídeos'),
        (5, 'Actinídeos'),
        (6, 'Gases Nobres'),
        (7, 'Semimetais'),
        (8, 'Não metais'),
        (9, 'Halogênios'),
        (10, 'Outros metais'),
    ])

cursor.execute('select * from tabelaperiodica.classe')
print(' ------------ Classes: ------------ ')
for classe in cursor.fetchall():
    print(classe[1])

cursor.executemany(
    'INSERT INTO `elemento` (`id_elemento`, `nome_elemento`, `num_atomico`, `massa_atomica`, `estado_fisico`, `simbolo`, `distribuicao_eletronica`, `classe`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
    [
        (1, 'Hidrogênio', 1, '1', 'Gasoso', 'H', '1s¹', 8),
        (2, 'Hélio', 2, '4', 'Gasoso', 'He', '1s²', 6),
        (4, 'Lítio', 3, '7', 'Sólido', 'Li', '[He]2s¹', 1),
        (5, 'Berílio', 4, '9', 'Sólido', 'Be', '[He]2s²', 2),
        (6, 'Boro', 5, '11', 'Sólido', 'B', '[He]2s²2p¹', 7),
        (7, 'Carbono', 6, '12', 'Sólido', 'C', '[He]2s²2p²', 8),
        (8, 'Nitrogênio', 7, '14', 'Gasoso', 'N', '[He]2s²2p³', 8),
        (9, 'Oxigênio', 8, '16', 'Gasoso', 'O', '[He]2s²2p⁴', 8),
        (10, 'Flúor', 9, '19', 'Gasoso', 'F', '[He]2s²2p⁵', 9),
        (11, 'Neônio', 10, '20', 'Gasoso', 'Ne', '[He]2s²2p⁶', 6),
        (12, 'Sódio', 11, '23', 'Sólido', 'Na', '[Ne]3s¹', 1),
        (13, 'Magnésio', 12, '24', 'Sólido', 'Mg', '[Ne]3s²', 2),
        (14, 'Alumínio', 13, '27', 'Sólido', 'Al', '[Ne]3s²3p¹', 10),
        (15, 'Silício', 14, '28', 'Sólido', 'Si', '[Ne]3s²3p²', 7),
        (16, 'Fósforo', 15, '31', 'Sólido', 'P', '[Ne]3s²3p³', 8),
        (17, 'Enxofre', 16, '32', 'Sólido', 'S', '[Ne]3s²3p⁴', 8),
        (18, 'Cloro', 17, '35', 'Sólido', 'Cl', '[Ne]3s²3p⁵', 9),
        (19, 'Argônio', 18, '40', 'Gasoso', 'Ar', '[Ne]3s²3p⁶', 6),
        (20, 'Potássio', 19, '39', 'Sólido', 'K', '[Ar]4s¹', 1),
        (21, 'Cálcio', 20, '40', 'Sólido', 'Ca', '[Ar]4s²', 2),
        (22, 'Escândio', 21, '45', 'Sólido', 'Sc', '[Ar]3d¹4s²', 3),
        (23, 'Titânio', 22, '48', 'Sólido', 'Ti', '[Ar]3d²4s²', 3),
        (24, 'Vanádio', 23, '51', 'Sólido', 'V', '[Ar]3d³4s²', 3),
        (25, 'Crômio', 24, '52', 'Sólido', 'Cr', '[Ar]3d⁵4s¹', 3)
    ])

cursor.execute('select * from tabelaperiodica.elemento')
print(' ------------ Elementos: ------------ ')
for elemento in cursor.fetchall():
    print(elemento[1])

cursor.executemany(
    'INSERT INTO `curiosidade` (`id_curiosidade`, `tipo`, `descricao`, `elemento`) VALUES (%s, %s, %s, %s)',
    [
        (1, 'Propriedades', 'Ocorre como um gás incolor, inodoro e altamente inflamável. É o elemento de menor densidade da Tabela Periódica e por este motivo era utilizado no enchimento de dirigíveis, mas teve seu uso abolido devido à elevada inflamabilidade.', 1),
        (2, 'Abundância', 'O hidrogênio é o elemento mais abundante do universo. Sendo encontrado no sol, na maioria das estrelas e o principal constituinte do planeta Júpiter.', 1),
        (3, 'Usos', 'O gás hidrogênio (H2) é considerado\no combustível limpo do futuro, uma vez que sua combustão produz água. A eletrólise da água constitui um dos principais métodos de obtenção do gás hidrogênio.', 1),
        (4, 'Propriedades', 'O hélio é o segundo elemento menos denso da Tabela Periódica, e por este motivo é comumente usado no enchimento de balões decorativos, bem como de balões meteorológicos ou dirigíveis.', 2),
        (5, 'Origem do nome', 'O nome hélio vem da palavra grega “helios” que significa “SOL”. O hélio é o principal componente do sol, onde é formado pela fusão nuclear de átomos de hidrogênio, processo que libera uma quantidade altíssima de energia.', 2),
        (6, 'Usos', 'Devido ao seu baixíssimo ponto de congelamento, o hélio é usado em\r\ncrioscopia como meio de resfriamento de equipamentos diversos como os espectrômetros de RMN e para resfriar o combustível de veículos espaciais.', 2),
    ])

cursor.execute('select * from tabelaperiodica.curiosidade')
print(' ------------ Curiosidades: ------------ ')
for curiosidade in cursor.fetchall():
    print(curiosidade[1])

cursor.executemany(
    'INSERT INTO `tipo_usuario` (`id_tipo_usuario`, `descricao_tipo_usuario`) VALUES (%s, %s)',
    [
        (1, 'Professor'),
        (2, 'Aluno'),
        (3, 'Professor'),
    ])

cursor.execute('select * from tabelaperiodica.tipo_usuario')
print(' ------------ Tipo de Usuário: ------------ ')
for tipo_usuario in cursor.fetchall():
    print(tipo_usuario[1])

cursor.executemany(
    'INSERT INTO `usuario` (`id_usuario`, `usuario`,`nome_usuario`, `email_usuario`, `senha`) VALUES (%s, %s, %s, %s, %s)',
    [
        (1,'amanda', 'Amanda Eleutério', 'amanda2@gmail.com', '54321'),
        (2,'daiane', 'Daiane Cristina', 'daiane@gmail.com', '54321'),
        (3,'tiago', 'Tiago Carlos', 'tiago@gmail.com', '54321'),
    ])

cursor.execute('select * from tabelaperiodica.usuario')
print(' ------------ Usuário: ------------ ')
for usuario in cursor.fetchall():
    print(usuario[1])

cursor.executemany(
    'INSERT INTO `nivel` (`id_nivel`, `nome_nivel`) VALUES(%s, %s)',
    [
        (1, 'Fácil'),
        (2, 'Médio'),
        (3, 'Difícil'),
    ])

cursor.execute('select * from tabelaperiodica.nivel')
print(' ------------ Nível: ------------ ')
for nivel in cursor.fetchall():
    print(nivel[1])
conn.commit()
cursor.close()
