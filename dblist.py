"Database-backed list-like type"
#http://en.wikibooks.org/wiki/Python_Programming/Classes
from time import time
import sqlite3

#from pickle import dumps,loads
from json import dumps,loads

#Check types
# if type(index)!=type(42):
#   raise TypeError('list indices must be integers, not ??')
# if type(start)!=type(42) or type(end)!=type(42):
#   raise TypeError('slice indices must be integers or None or have an __index__ method')

class dblist:
  #List methods
  def append(self,commit=True):
    "Add a row"
    pickle=dumps(row)
    self.cursor.execute('INSERT INTO `%s`(pickle) VALUES(?);'%self._table_name,[pickle])
    if commit:
      self.commit()


  def pop(self,commit=False):
    self.cursor.execute('SELECT `pickle` FROM `%s` ORDER BY `pk` DESC LIMIT 1'%self._table_name)
    rows=self.cursor.fetchall()

    if len(rows)==0:
      raise IndexError("pop from empty list")
    else:
      state=loads(rows[0][0])
      self.cursor.execute('DELETE FROM `%s` WHERE `pk`=(SELECT max(pk) from `%s`);'%(self._table_name,self._table_name))
      if commit:
        self.connection.commit()
      return out

  def count(self):
  def extend(self):
  def index(self):
  def insert(self):
  def pop(self):
  def remove(self):
  def reverse(self):
  def sort(self):

  #Special list methods
  def __init__(self,base_stack=[],table_name="_stack",db_name="stack.db",commit=True):
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
      if commit:
        self.commit()

  def __del__(self,commit=True):
    "Delete the stack"
    self.cursor.execute('DELETE FROM `%s`'%self._table_name)
    if commit:
      self.commit()

# def __str__(self):
# def __unicode__(self):


  #Unary operators
  def __len__(self):
    self.cursor.execute('select count(*) from %s'%self._table_name)
    rows=self.cursor.fetchall()
    if len(rows)==0:
      count=0
    else:
      count=rows[0][0]
    return count

  #Item (index) operators
  def __getitem__(self,index):
    return self.__getslice__(index,index+1)

  def __setitem__(self,index,value):
    self.__setslice__(index,index+1,[value])

  def __getslice__(self,start,end):
    self.cursor.execute("""
      SELECT `pickle` FROM `%s`
      WHERE pk >= ? AND pk < ? ASC;
    """%self._table_name,[index])
    rows=self.cursor.fetchall()
    return [loads(row[0]) for row in rows]

  def __setslice__(self,start,end,values,commit=True):
    for value in values:
      pickle=dumps(value)
      self.cursor.execute("""
        INSERT INTO `%s`(pickle) VALUES(?)
        WHERE pk >= ? AND pk < ? ASC;
      """, % self._table_name,[pickle,start,end])
    if commit:
      self.commit()

  #Non-list methods
  def commit(self): 
    self.connection.commit()

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

  stack=property(_getstack,_setstack,_delstack,"The stack list")

  def len(self):

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
