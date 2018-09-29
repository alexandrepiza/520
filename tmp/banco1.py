def cadastrar(name, mensagem):
    date = {
        'nome': name,
        'mensagem1: mensagem,
        'hora': time.strftime('%d-%m-%Y %H:%M:%S')
    }
    db.chat.insert(date)