import unittest
from dblist import dblist

class TestDbList(unittest.TestCase):
  def setUp(self):
    self.list=[3,5,1]
    self.dblist=dblist(self.list)
    self.dblist.commit()

  #List methods
  def test_append(self):
    self.list.append(8)
    self.dblist.append(8)
    self.assertEqual(self.list.count(5),self.dblist.count(5))
    
  def test_count(self):
    self.assertEqual(self.list.count(5),self.dblist.count(5))

# def test_extend(self):
#   foo,bar=compare(lambda baz:baz.extend([3,2]))
#   self.assertEqual(foo,bar)
#   del(foo)
#   del(bar)

  def test_index(self):
    self.assertEqual(self.list.index(5),self.dblist.index(5))

  def test_insert(self):
   pass

# def test_pop(self):
#   foo,bar=compare(lambda baz:baz.pop(2),[38,5,2,3])
#   self.assertEqual(foo,bar)
#   foo,bar=compare(lambda baz:baz.pop(),[38,5,2,3])
#   self.assertEqual(foo,bar)

# def test_remove(self):
#   foo,bar=compare(lambda baz:baz.remove(2),[38,5,2,3])
#   self.assertEqual(foo,bar)

# def test_reverse(self):
#   foo,bar=compare(lambda baz:baz.reverse(),[38,5,2,3])
#   self.assertEqual(foo,bar)

# def test_sort(self):
#   foo,bar=compare(lambda baz:baz.sort(),[38,5,2,10,3])
#   self.assertEqual(foo,bar)

# #Special list methods
  def test___init__(self):
    self.assertEqual(self.dblist.tolist(),self.list)

# def test___del__(self):
# def test___str__(self):
# def test___unicode__(self):

# #Item (index) operators
# def test___getitem__(self,index):
#   return
# def test___setitem__(self,index):
#   return
# def test___getslice__(self,index):
#   return

# #Non-list methods
# def test_commit(self): 


if __name__ == '__main__':
  unittest.main()
