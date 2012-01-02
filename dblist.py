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


  def count(self,value):
    self.cursor.execute('SELECT count(`pickle`) FROM `%s` WHERE `pickle`=?;'%self._table_name,[dumps(value)])
    rows=self.cursor.fetchall()
    return rows[0][0]

#  def extend(self):
  def index(self,value):
    self.cursor.execute('SELECT `pk` FROM `%s` WHERE `pickle`=? ORDER BY `pk` ASC LIMIT 1;'%self._table_name,[dumps(value)])
    rows=self.cursor.fetchall()
    return rows[0][0]

#  def insert(self):
    
  def pop(self,index=None,commit=False):
    #Get
    self.cursor.execute('SELECT `pickle` FROM `%s` ORDER BY `pk` DESC LIMIT 1'%self._table_name)
    rows=self.cursor.fetchall()
    if len(rows)==0:
      raise IndexError("pop from empty list")
    else:
      state=loads(rows[0][0])

      #Delete
      if index==None:
        self.cursor.execute('DELETE FROM `%s` WHERE `pk`=(SELECT max(pk) from `%s`);'%(self._table_name,self._table_name))
      else:
        self.cursor.execute('DELETE FROM `%s` WHERE `pk`=?;'%(self._table_name),[index])
        
      #Commit
      if commit:
        self.connection.commit()
      return out

  def remove(self,value):
    pk=self.index(value)
    self.cursor.execute('DELETE FROM `%s` WHERE `pk`=?;'%(self._table_name),[pk])

# def reverse(self):
# def sort(self):

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
      """ % self._table_name,[pickle,start,end])
    if commit:
      self.commit()

  #Non-list methods
  def commit(self): 
    self.connection.commit()

  def tolist(self):
    self.cursor.execute('SELECT `pickle` FROM `%s` ORDER BY `pk` ASC'%self._table_name)
    thestack=[loads(row[0]) for row in self.cursor.fetchall()]
    return thestack
