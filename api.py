from flask import Flask, render_template, request,  redirect, session, flash, url_for

app = Flask(__name__)
app.secret_key = 'matrix'

#Classe filme
class Filme:
    def __init__(self, title, year, sinopsis):
        self.title = title
        self.year = year
        self.sinopsis = sinopsis


filme1 = Filme('Godzilla', '1999', 'filme de monstro')
filme2 = Filme('Pulp Fiction', '1987', 'Escrito e dirigido por Quentin tarantino')
filme3 = Filme('Mad Max', '2017', 'Witness me')
lista = [filme1, filme2, filme3]

#Main page: exhibits movies
@app.route('/')
def index():
    return render_template('movies.html', titulo='Filmes', filmes=lista)

#Form for adding new movies to inventory
@app.route('/add_movie')
def add_movie():
    if 'logged_user' not in session or session['logged_user'] == None:
        return redirect(url_for('login', next=url_for('add_movie')))
    return render_template('add_movie.html', titulo='Adicionar novo filme')

#Adds movie from the form to movie inventory and returns to main 
@app.route('/create', methods=['POST',])
def create():
    title = request.form['title']
    year = request.form['year']
    sinopsis = request.form['sinopsis']
    filme = Filme(title, year, sinopsis)
    lista.append(filme)
    return redirect(url_for('index'))

@app.route('/login')
def login():
    next = request.args.get('next')
    return render_template('login.html', next=next)

@app.route('/authenticate', methods=['POST', ])
def authenticate():
    if 'enter' == request.form['pass']:
        session['logged_user'] = request.form['user']
        flash(request.form['user'] + ' logou com sucesso!')
        next_page = request.form['next']
        return redirect(next_page)
    else:
        flash('Senha incorreta')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['logged_user'] = None
    flash('Logout realizado com sucesso!')
    return redirect(url_for('index'))

app.run(debug=True)