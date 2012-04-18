import unittest
from dblist import dblist

class CompareLists(unittest.TestCase):
  def setUp(self):
    self.list=[0,"five", {}, [{"foo": "bar"}]] + range(30)
    self.dblist=dblist(self.list, dbname = ":memory:")

  def test_manipulation(self):
    return1 = self.manipulate(self.list)
    return2 = self.manipulate(self.dblist)
    self.assertEqual(return1, return2)
    self.assertEqual(self.list, self.dblist)

class TestAdd(CompareLists):
  @staticmethod
  def manipulate(l):
    return l + l

class TestContains(CompareLists):
  @staticmethod
  def manipulate(l):
    return [l.__contains__(item) for item in l]

class TestDelAttr(CompareLists):
  @staticmethod
  def manipulate(l):
    raise NotImplementedError("Test not yet implemented.")

class TestDelItem(CompareLists):
  @staticmethod
  def manipulate(l):
    del(l[int(len(l/2))])

class TestDelSlice(CompareLists):
  @staticmethod
  def manipulate(l):
    del(l[2:-2])

class TestDoc(CompareLists):
  @staticmethod
  def manipulate(l):
    raise NotImplementedError("Test not yet implemented.")

class TestFormat(CompareLists):
  @staticmethod
  def manipulate(l):
    raise NotImplementedError("Test not yet implemented.")

class TestGetAttribute(CompareLists):
  @staticmethod
  def manipulate(l):

class TestGetItem(CompareLists):
  @staticmethod
  def manipulate(l):

class TestHash(CompareLists):
  @staticmethod
  def manipulate(l):

class TestIAdd(CompareLists):
  @staticmethod
  def manipulate(l):

class TestImul(CompareLists):
  @staticmethod
  def manipulate(l):

class TestInit(CompareLists):
  @staticmethod
  def manipulate(l):

class TestIter(CompareLists):
  @staticmethod
  def manipulate(l):

class TestLe(CompareLists):
  @staticmethod
  def manipulate(l):

class TestLen(CompareLists):
  @staticmethod
  def manipulate(l):
    return len(l)

class TestMul(CompareLists):
  @staticmethod
  def manipulate(l):

class TestNe(CompareLists):
  @staticmethod
  def manipulate(l):

class TestNew(CompareLists):
  @staticmethod
  def manipulate(l):

class TestReduce(CompareLists):
  @staticmethod
  def manipulate(l):

class TestReduceEx(CompareLists):
  @staticmethod
  def manipulate(l):

class TestRepr(CompareLists):
  @staticmethod
  def manipulate(l):

class TestReversed(CompareLists):
  @staticmethod
  def manipulate(l):

class TestRmul(CompareLists):
  @staticmethod
  def manipulate(l):

class TestSetAttr(CompareLists):
  @staticmethod
  def manipulate(l):

class TestSetItem(CompareLists):
  @staticmethod
  def manipulate(l):

class TestSetSlice(CompareLists):
  @staticmethod
  def manipulate(l):

class TestSizeOf(CompareLists):
  @staticmethod
  def manipulate(l):

class TestStr(CompareLists):
  @staticmethod
  def manipulate(l):

class TestSubClassHook(CompareLists):
  @staticmethod
  def manipulate(l):

class TestAppend(CompareLists):
  @staticmethod
  def manipulate(l):
    return l.append(l[3])

class TestCount(CompareLists):
  @staticmethod
  def manipulate(l):
    return [l.count(i) for i in l]

class TestExtend(CompareLists):
  @staticmethod
  def manipulate(l):
    return l.extend(l)

class TestIndex(CompareLists):
  @staticmethod
  def manipulate(l):
    return l.index(5) 

class TestInsert(CompareLists):
  @staticmethod
  def manipulate(l):
    return l.insert(3, l[8])

class TestPop(CompareLists):
  @staticmethod
  def manipulate(l):
    return l.pop(int(len(l/2)))

class TestRemove(CompareLists):
  @staticmethod
  def manipulate(l):
    return l.remove(l[-3])

class TestReverse(CompareLists):
  @staticmethod
  def manipulate(l):
    return l.reverse()

class TestSort(CompareLists):
  @staticmethod
  def manipulate(l):
    return l.sort()

# Comparison operators
class TestEq(CompareLists):
  @staticmethod
  def manipulate(l):
    return l == l

class TestGe(CompareLists):
  @staticmethod
  def manipulate(l):
    raise NotImplementedError("Test not yet implemented.")

class TestGt(CompareLists):
  @staticmethod
  def manipulate(l):
    raise NotImplementedError("Test not yet implemented.")

class TestLt(CompareLists):
  @staticmethod
  def manipulate(l):
    raise NotImplementedError("Test not yet implemented.")

if __name__ == '__main__':
  unittest.main()
