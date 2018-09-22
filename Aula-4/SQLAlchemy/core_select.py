#!/usr/bin/python3

from sqlalchemy import select
from core import user_table

result = select([user_table])
result2 = select([user_table]).where(user_table.c.nome == 'daniel')





print([x for x in result2.execute()])