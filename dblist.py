"Database-backed list-like type"
#http://en.wikibooks.org/wiki/Python_Programming/Classes
from time import time
import sqlite3

#from pickle import dumps,loads
from json import dumps,loads

class dblist:
  #List methods
  def append(self,value):
    "Add a row"
    pickle=dumps(value)
    self.cursor.execute('INSERT INTO `%s`(pickle) VALUES(?);'%self._table_name,[pickle])
    if self.auto_commit:
      self.commit()

  def count(self,value):
    self.cursor.execute('SELECT count(`pickle`) FROM `%s` WHERE `pickle`=?;'%self._table_name,[dumps(value)])
    rows=self.cursor.fetchall()
    return rows[0][0]

#  def extend(self):
  def index(self,value):
    self.cursor.execute('SELECT `rowid` FROM `%s` WHERE `pickle`=? ORDER BY `rowid` ASC LIMIT 1;'%self._table_name,[dumps(value)])
    rows=self.cursor.fetchall()
    return rows[0][0]

#  def insert(self):
    
  def pop(self,index=None,commit=False):
    #Get
    self.cursor.execute('SELECT `pickle` FROM `%s` ORDER BY `rowid` DESC LIMIT 1'%self._table_name)
    rows=self.cursor.fetchall()
    if len(rows)==0:
      raise IndexError("pop from empty list")
    else:
      value=loads(rows[0][0])

      #Delete
      if index==None:
        self.cursor.execute('DELETE FROM `%s` WHERE `rowid`=(SELECT max(`rowid`) from `%s`);'%(self._table_name,self._table_name))
      else:
        self.cursor.execute('DELETE FROM `%s` WHERE `rowid`=?;'%(self._table_name),[index])
        
      #Commit
      if self.auto_commit:
        self.commit()

      return value

  def remove(self,value):
    rowid=self.index(value)
    self.cursor.execute('DELETE FROM `%s` WHERE `rowid`=?;'%(self._table_name),[rowid])

# def reverse(self):
# def sort(self):

  def __init__(self, base_list = [], dbname = "dblist.py", table_name = "_dblist", auto_commit = True):
    pass
    # Should database changes be committed automatically after each command?
    if type(auto_commit) != bool:
      raise TypeError("auto_commit must be True or False.")
    else:
      self.auto_commit = auto_commit

    # Database connection
    if type(dbname) not in [unicode, str]:
      raise TypeError("dbname must be a string")
    else:
      #self.connection=sqlite3.connect(dbname, detect_types = sqlite3.PARSE_DECLTYPES)
      self.connection=sqlite3.connect(db_name)
      self.cursor=self.connection.cursor()

    # Make sure it's a good table name
    if type(table_name) not in [unicode, str]:
      raise TypeError("table_name must be a string")
    else:
      self.__table_name = table_name


    self.cursor=self.connection.cursor()
    self.cursor.execute("SELECT name FROM sqlite_master WHERE TYPE='table'")
    table_names=[row[0] for row in self.cursor.fetchall()]
    if table_name in table_names:
      self.cursor.execute("PRAGMA table_info(%s)" % table_name)
      print self.cursor.fetchall()

    else:
      "Create the table and set the base stack."
      self.cursor.execute("CREATE TABLE %s ( pickle BLOB )" % self._table_name)

      #Initial contents
      for value in base_list:
        pickle=dumps(value)
        self.cursor.execute('INSERT INTO `%s`(pickle) VALUES(?)' % self._table_name,[pickle])

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
      WHERE `rowid` >= ? AND `rowid` < ? ASC;
    """%self._table_name,[index])
    rows=self.cursor.fetchall()
    return [loads(row[0]) for row in rows]

  def __setslice__(self,start,end,values,commit=True):
    for value in values:
      pickle=dumps(value)
      self.cursor.execute("""
        INSERT INTO `%s`(pickle) VALUES(?)
        WHERE `rowid` >= ? AND `rowid` < ? ASC;
      """ % self._table_name,[pickle,start,end])
    if commit:
      self.commit()

  #Non-list methods
  def commit(self): 
    self.connection.commit()
#    self.cursor.close()

  def tolist(self):
    self.cursor.execute('SELECT `pickle` FROM `%s` ORDER BY `rowid` ASC'%self._table_name)
    thestack=[loads(row[0]) for row in self.cursor.fetchall()]
    return thestack
