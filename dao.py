from models import Movie

SQL_DELETA_FILME = 'delete from movies where id = %s'
SQL_FILME_POR_ID = 'SELECT id, title, year, sinopsis from movies where id = %s'
SQL_ATUALIZA_FILME = 'UPDATE movies SET title=%s, year=%s, sinopsis=%s where id = %s'
SQL_BUSCA_FILME = 'SELECT id, title, year, sinopsis from movies'
SQL_CRIA_FILME = 'INSERT into movies (title, year, sinopsis) values (%s, %s, %s)'


class MovieDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, movie):
        cursor = self.__db.cursor()

        if (movie.id):
            cursor.execute(SQL_ATUALIZA_FILME, (movie.title, movie.year, movie.sinopsis, movie.id))
        else:
            cursor.execute(SQL_CRIA_FILME, (movie.title, movie.year, movie.sinopsis))
            movie.id = cursor.lastrowid
        self.__db.commit()
        return movie

    def listar(self):
        cursor = self.__db.cursor()
        cursor.execute(SQL_BUSCA_FILME)
        movies = traduz_filmes(cursor.fetchall())
        return movies

    def buscar_por_id(self, id):
        cursor = self.__db.cursor()
        cursor.execute(SQL_FILME_POR_ID, (id,))
        tupla = cursor.fetchone()
        return Movie(tupla[1], tupla[2], tupla[3], id=tupla[0])

    def deletar(self, id):
        self.__db.cursor().execute(SQL_DELETA_FILME, (id, ))
        self.__db.commit()



def traduz_filmes(movies):
    def cria_jogo_com_tupla(tupla):
        return Movie(tupla[1], tupla[2], tupla[3], id=tupla[0])
    return list(map(cria_jogo_com_tupla, movies))

