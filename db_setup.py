import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    port = 3306,
    password="new_password",
)

cursor = conexao.cursor()

cursor.execute('create database if not exists movie_ctalog')
cursor.execute('use movie_catalog')
cursor.execute("""create table if not exists movie(
                id int(11) not null auto_increment,
                title varchar(100) not null,
                year int not null,
                sinopsis varchar(1000) not null,
                primary key (id)
                )"""
            )

# inserindo jogos
cursor.executemany(
    'INSERT INTO movie_catalog.movie (title, year, sinopse) VALUES (%s, %s, %s)',
    [
        ('Clube da Luta', 1999, 'Um homem deprimido que sofre de insônia conhece um estranho vendedor chamado Tyler Durden e se vê morando em uma casa suja depois que seu perfeito apartamento é destruído. A dupla forma um clube com regras rígidas onde homens lutam. A parceria perfeita é comprometida quando uma mulher, Marla, atrai a atenção de Tyler.'),
        ('Mad Max: Estrada da Fúria', 2015, 'Mad Max é uma franquia multi-media australiana do gênero ficção científica, contendo elementos de ação baseada em um futuro pós-apocalíptico, criada por James McCausland e George Miller. Começou em 1979 com o filme Mad Max, seguido por Mad Max 2: The Road Warrior e Mad Max Beyond Thunderdome.'),
        ('Jumanji', 1995, 'Alan Parrish desapareceu quando era menino e ninguém acredita na história de seu amigo de que ele foi sugado por um jogo de tabuleiro. Vinte e seis anos depois, duas crianças acham o jogo no sótão e, quando começam a jogar, Alan é libertado. Mas a disputa ainda não acabou e Alan precisa terminar antes de ser realmente solto.'),
        ('Pulp Fiction: Tempo de Violência', 1994, 'Os caminhos de vários criminosos se cruzam nestas três histórias de Quentin Tarantino. Um pistoleiro se apaixona pela mulher de seu chefe, um boxeador não se sai bem em uma luta e um casal tenta executar um plano de roubo que foge do controle.'),
        ('Meninas Malvadas', 2004, 'A adolescente Cady Heron foi educada na África pelos seus pais cientistas. Quando sua família se muda para o subúrbio, nos Estados Unidos, Cady começa a frequentar a escola pública e recebe uma rápida introdução às leis de popularidade que dividem seus colegas. Sem querer, ela acaba no meio de um grupo de elite de estudantes apelidadas "as poderosas".'),
        ('Frozen', 2014, 'Acompanhada por um vendedor de gelo, a jovem e destemida princesa Anna parte em uma jornada por perigosas montanhas de gelo na esperança de encontrar sua irmã, a rainha Elsa, e acabar com a terrível maldição de inverno eterno, que está provocando o congelamento do reino.'),
    ])

cursor.execute('select * from movie_catalog.movie')
print(' -------------  Filmes:  -------------')
for movie in cursor.fetchall():
    print(movie[1])

# commitando senão nada tem efeito
conexao.commit()
conexao.close()