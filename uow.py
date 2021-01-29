import sqlite3

from collections.abc import MutableMapping
from operator import itemgetter


class SQLDict(MutableMapping):

    """SQLDict repository. Abstracts over data persistance."""

    def __init__(self, context):
        # self.context = context?
        # cur = self.context.conn.cursor()
        # the context that this exists in IS the connection
        self.context = context
        self.create_table()

    def create_table(self):
        cur = self.context.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS Dict(key text, value text)')

    def __setitem__(self, key, value):
        if key in self: 
            del self[key]
        cur = self.context.cursor()
        cur.execute('INSERT INTO Dict VALUES (?, ?)', (key, value))

    def __getitem__(self, key):
        cur = self.context.cursor()
        cur.execute('SELECT value FROM Dict WHERE key=?', (key,))
        row = cur.fetchone()
        if not row: 
            raise KeyError(key)
        return row[0]

    def __delitem__(self, key):
        cur = self.context.cursor()
        cur.execute('DELETE FROM Dict WHERE key=?', (key,))

    def __len__(self):
        cur = self.context.cursor()
        return next(cur.execute('SELECT COUNT(*) FROM Dict'))[0]

    def __iter__(self):
        cur = self.context.cursor()
        cur.execute('SELECT key FROM Dict')
        return map(itemgetter(0), cur.fetchall())

    def __repr__(self):
        return f'{type(self).__name__}(items={list(self.items())}'


class UnitOfWork:

    """UOW. 
    
    Abstracts an atomic operation.
    
    Make a connection on instantiation
    Manage the lifecycle of the conn for the atomic operation
    Inject the connection into the repo so the repo can be used (or passed) like a dict

    Sort of like strategy?
    """

    def __init__(self, dbname):
        self.context = sqlite3.connect(dbname)
        self.sqldict = SQLDict

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.context.rollback()
        self.context.close()

    def commit(self):
        self.context.commit()

    @property
    def repository(self):
        return self.sqldict(context=self.context)


if __name__ == '__main__':
    
    import os

    dbname = 'uow.test.db'
    
    with UnitOfWork(dbname=dbname) as uow:
        repo = uow.repository
        repo["I would do anything for love"] = "but I won't do that"
        uow.commit()

    with UnitOfWork(dbname=dbname) as uow:
        repo = uow.repository
        key = "I would do anything for love"
        line = f'{key}, {repo[key]}!'
        print(line, "Noooooo I won't do that.")

    os.remove(dbname)
