def select():
    ultimo = [x for x in db.chat.find().sort("_id", DESCENDING)]
    while True:
        date = [x for x in db.chat.find().sort("_id", DESCENDING)]
        if date != ultimo:
            ultimo = date
            print('[{}] {} : {> \n'.format(
                date[0][1hora'], date[0][1nome'], date[0]['mensagem']))
            time.sleep(2)