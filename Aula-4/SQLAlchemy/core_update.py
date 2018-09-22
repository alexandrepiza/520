#!/usr/bin/python3

from sqlalchemy import update
from core import user_table, engine

con = engine.connect()

atualizar = update(user_table).where(user_table.c.nome == 'daniel')

atualizar = atualizar.values(nome='daniel prata')
result = con.execute(atualizar)
print('linhas afetas: {}'.format(result.rowcount))