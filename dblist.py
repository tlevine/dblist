"Database-backed list-like type"
#http://en.wikibooks.org/wiki/Python_Programming/Classes
from time import time
import sqlite3

#from pickle import dumps,loads
from json import dumps,loads

class dblist:
  #List methods
  def append(self):
  def count(self):
  def extend(self):
  def index(self):
  def insert(self):
  def pop(self):
  def remove(self):
  def reverse(self):
  def sort(self):

  #Special list methods
  def __init__(self,table_name="_stack",db_name="stack.db",base_stack=[]):
    self._table_name=table_name
    self.connection=sqlite3.connect(db_name)
    self.cursor=self.connection.cursor()
    self.cursor.execute("SELECT name FROM sqlite_master WHERE TYPE='table'")
    table_names=[row[0] for row in self.cursor.fetchall()]
    if table_name in table_names:
      "Check the schema"
    else:
      "Create the table and set the base stack."
      self.cursor.execute("""
        CREATE TABLE %s(
          pk INTEGER PRIMARY KEY,
          pickle BLOB
        );
      """%self._table_name)
      self._setstack(base_stack)
      self.connection.commit()

  def __del__(self):
    "Delete the stack"
    self.cursor.execute('DELETE FROM `%s`'%self._table_name)
    self.connection.commit()

  def __str__(self):
  def __unicode__(self):

  #Item (index) operators
  def __getitem__(self,index):
    return
  def __setitem__(self,index):
    return
  def __getslice__(self,index):
    return

  #Non-list methods
  def commit(self): 
  def tolist(self):
    self.cursor.execute('SELECT `pickle` FROM `%s` ORDER BY `pk` ASC'%self._table_name)
    thestack=[loads(row[0]) for row in self.cursor.fetchall()]
    return thestack

class SqliteStack():
  "Stack backed by an sqlite3 database datastore"

  class EmptyStack(Exception):
    pass

  def _getstack(self):

  def _delstack(self):

  def _setstack(self,newstack):
    "Replace the stack table with a new one. This is slow."
    self._delstack()
    for state in newstack:
      pickle=dumps(state)
      self.cursor.execute('INSERT INTO `%s`(pickle) VALUES(?)' % self._table_name,[pickle])
    self.connection.commit()

  stack=property(_getstack,_setstack,_delstack,"The stack list")

  def len(self):
    self.cursor.execute('select count(*) from %s'%self._table_name)
    rows=self.cursor.fetchall()
    if len(rows)==0:
      count=0
    else:
      count=rows[0][0]
    return count

  def first(self):
    self.cursor.execute('SELECT `pickle` FROM `%s` ORDER BY `pk` ASC LIMIT 1'%self._table_name)
    rows=self.cursor.fetchall()
    if len(rows)==0:
      raise self.EmptyStack
    else:
      state=loads(rows[0][0])
      return state

  def last(self):
    self.cursor.execute('SELECT `pickle` FROM `%s` ORDER BY `pk` DESC LIMIT 1'%self._table_name)
    rows=self.cursor.fetchall()
    if len(rows)==0:
      raise self.EmptyStack
    else:
      state=loads(rows[0][0])
      return state

  def head(self):
    stack=self.stack
    if len(stack)==0:
      return []
    else:
      return stack[0:-1]

  def tail(self):
    stack=self.stack
    if len(stack)==0:
      return []
    else:
      return stack[1:len(stack)]

  def append(self,row):
    "Add a row"
    pickle=dumps(row)
    self.cursor.execute('INSERT INTO `%s`(pickle) VALUES(?);'%self._table_name,[pickle])
    self.connection.commit()

  def pop(self,commit=False):
    out=self.last()
    #Delete the row
    self.cursor.execute('DELETE FROM `%s` WHERE `pk`=(SELECT max(pk) from `%s`);'%(self._table_name,self._table_name))
    if commit:
      self.connection.commit()
    return out

class SWStack():
  "Stack backed by the ScraperWiki datastore"
  def __init__(self,stack,table_name="_stack"):
    self._table_name=table_name

  class EmptyStack(Exception):
    pass

  @property
  def stack(self):
    rows=sw.execute('SELECT `pickle` FROM `%s` ORDER BY `_timestamp` ASC',self._table_name)
    stack=[loads(row['pickle']) for row in rows]
    return stack

  @stack.setter
  def stack(self,newstack):
    "Replace the stack table with a new one. This is slow."
    sw.execute('DELETE FROM `%s`' % self._table_name)

    prevtime=None
    while len(newstack)>0:
      state=newstack.pop(0)
      currenttime=time()
      if currenttime==prevtime:
        currenttime+=0.00001
      state['_timestamp']=currenttime
      sw.save([],state,self._table_name)
      prevtime=currenttime

  def len(self):
    rows=sw.select('count(*) as c from %s' % self._table_name)
    if len(rows)==0:
      count=0
    else:
      count=rows[0]['c']
    return count

  def first(self):
    rows=sw.execute('SELECT `pickle` FROM `%s` ORDER BY `_timestamp` ASC LIMIT 1',self._table_name)
    if len(rows)==0:
      raise self.EmptyStack
    else:
      state=loads(rows[0]['pickle'])
      return state

  def last(self):
    rows=sw.execute('SELECT `pickle` FROM `%s` ORDER BY `_timestamp` DESC LIMIT 1',self._table_name)
    if len(rows)==0:
      raise self.EmptyStack
    else:
      state=loads(rows[0]['pickle'])
      return state

  def head(self):
    stack=self.stack
    if len(stack)==0:
      return []
    else:
      return stack[0:-1]

  def tail(self):
    stack=self.stack
    if len(stack)==0:
      return []
    else:
      return stack[1:len(stack)]

  def append(self,row):
    "Add a row"
    row["_timestamp"]=time()
    sw.save([],row,self._table_name)

  def pop(self):
    out=self.last()
    #Delete the row
    sw.execute('DELETE FROM `%s` ORDER BY `_timestamp` DESC LIMIT 1' % self._table_name)
    return out
  
    
class ListStack(list):
  def __init__(self,stack=[]):
    self._stack=stack

  class EmptyStack(Exception):
    pass

  @property
  def stack(self):
    return self._stack

  @stack.setter
  def stack(self,value):
    self._stack=value

  def len(self):
    return len(self._stack)

  def pop(self):
    return self._stack.pop()

  def append(self,state):
    return self._stack.append(state)

  def first(self):
    if len(self._stack)==0:
      raise self.EmptyStack
    else:
      return self._stack[0]

  def last(self):
    if len(self._stack)==0:
      raise self.EmptyStack
    else:
      return self._stack[-1]

  def head(self):
    return self._stack[0:-1]

  def tail(self):
    if len(self._stack)==0:
      return []
    else:
      return self._stack[1:len(self._stack)]
