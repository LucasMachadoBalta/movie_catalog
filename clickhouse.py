from clickhouse_driver import Client

schema_sql = '''CREATE TABLE IF NOT EXISTS movies (`id` UUID,
`name` String,`year` int64,`sinopsis` String) 
ENGINE MergeTree() SETTINGS index_granularity=8192'''


def database_connect(host: str, port: int, user:str, password:str) -> Client:
    return Client(host=host, port=port, user=user, password=password)

def database_init(client: Client)-> None:
    print(client.execute('SHOW DATABASES'))
    print(client.execute('SHOW TABLES'))
    print(client.execute(schema_sql))
    print(client.execute('SHOW TABLES'))

def database_select_all(client: Client) -> list:
    r = client.execute('SELECT * FROM movies')
    return r

def database_insert(client: Client ) -> None:
    client.execute(
        'INSERT INTO movies (`id`,`name`, `year`,sinopsis) VALUES',
            ('Clube da Luta', 1999, 'Um homem deprimido que sofre de insônia conhece um estranho vendedor chamado Tyler Durden e se vê morando em uma casa suja depois que seu perfeito apartamento é destruído. A dupla forma um clube com regras rígidas onde homens lutam. A parceria perfeita é comprometida quando uma mulher, Marla, atrai a atenção de Tyler.'))

##use example:
client = database_connect(host='localhost', port=8123, user='default', password='88ff9b4a-5a01-4d35-abfc-769ffc69506f')  
#database_init(client)
#database_insert(client, df_short)
#database_select_all(client)
