import psycopg2

try:
    con = psycopg2.connect(
        'host={}, dbname={} user={} password={}'.format('localhost','projeto','admin','4linux')
    )
except Exception as e:
    print('Erro:{}'.format(e))
    exit()

try:
    cur = con.cursor()
    cur.execute("select * from scripts;")
    #print(cur.fetchone())
    for x in cur.fetchall():
        print('''
        ID:   {:.>15}
        Nome: {:.>15}
        Conteudo: {:.>11}
        '''.format(x[0], x[1], x[2]))
    #cur.execute("insert into scripts(nome, conteudo) values ('alexandre','teste');")

    con.commit() # no caso de uma query não necessita fazer este commit

    cur.close()
    con.close()
except Exception as e:
    print('Erro:{}'.format(e))
    con.rollback()