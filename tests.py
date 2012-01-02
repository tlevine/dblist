import unittest
from dblist import dblist

def compare(func,init=[]):
  foo=dblist(init)
  bar=list(init)
  for baz in (foo,bar):
    func(baz)
  return foo.tolist(),bar

class TestDbList(unittest.TestCase):
  #List methods
  def test_append(self):
    foo,bar=compare(lambda baz:baz.append('u'))
    self.assertEqual(foo,bar)
    del(foo)
    del(bar)
    
  def test_count(self):
    foo,bar=compare(lambda baz:baz.count(3),[3,4,3])
    self.assertEqual(foo,bar)
    del(foo)
    del(bar)

  def test_extend(self):
    foo,bar=compare(lambda baz:baz.extend([3,2]))
    self.assertEqual(foo,bar)
    del(foo)
    del(bar)

  def test_index(self):
    foo,bar=compare(lambda baz:baz.index(2),[38,5,2,3])
    self.assertEqual(foo,bar)
    del(foo)
    del(bar)

  def test_insert(self):
   pass

  def test_pop(self):
    foo,bar=compare(lambda baz:baz.pop(2),[38,5,2,3])
    self.assertEqual(foo,bar)
    foo,bar=compare(lambda baz:baz.pop(),[38,5,2,3])
    self.assertEqual(foo,bar)

  def test_remove(self):
    foo,bar=compare(lambda baz:baz.remove(2),[38,5,2,3])
    self.assertEqual(foo,bar)

# def test_reverse(self):
#   foo,bar=compare(lambda baz:baz.reverse(),[38,5,2,3])
#   self.assertEqual(foo,bar)

# def test_sort(self):
#   foo,bar=compare(lambda baz:baz.sort(),[38,5,2,10,3])
#   self.assertEqual(foo,bar)

# #Special list methods
# def test___init__(self):
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
