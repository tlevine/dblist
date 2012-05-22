import unittest
from dblist import dblist

class CompareLists(unittest.TestCase):
  def setUp(self):
    self.list=[0,"five", {}, [{"foo": "bar"}]] + range(30)
    self.dblist=dblist(self.list, dbname = ":memory:")

  def test_manipulation(self):
    return1 = self.manipulate(self.list)
    return2 = self.manipulate(self.dblist)

    if isinstance(return2, dblist):
      return2 = self.dblist.tolist()

    self.assertEqual(return1, return2)
    self.assertListEqual(self.list, self.dblist.tolist())

class TestToList(CompareLists):
  @staticmethod
  def manipulate(l):
    return l

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
    raise NotImplementedError("Test not yet implemented.")

class TestGetItem(CompareLists):
  @staticmethod
  def manipulate(l):
    return l[-1], l[3]

class TestHash(CompareLists):
  @staticmethod
  def manipulate(l):
    raise NotImplementedError("Test not yet implemented.")

class TestIAdd(CompareLists):
  @staticmethod
  def manipulate(l):
    raise NotImplementedError("Test not yet implemented.")

class TestImul(CompareLists):
  @staticmethod
  def manipulate(l):
    raise NotImplementedError("Test not yet implemented.")

class TestIter(CompareLists):
  @staticmethod
  def manipulate(l):
    raise NotImplementedError("Test not yet implemented.")

class TestLen(CompareLists):
  @staticmethod
  def manipulate(l):
    return len(l)

class TestMul(CompareLists):
  @staticmethod
  def manipulate(l):
    return l*3

class TestNew(CompareLists):
  @staticmethod
  def manipulate(l):
    raise NotImplementedError("Test not yet implemented.")

class TestReduce(CompareLists):
  @staticmethod
  def manipulate(l):
    raise NotImplementedError("Test not yet implemented.")

class TestReduceEx(CompareLists):
  @staticmethod
  def manipulate(l):
    raise NotImplementedError("Test not yet implemented.")

class TestRepr(CompareLists):
  @staticmethod
  def manipulate(l):
    raise NotImplementedError("Test not yet implemented.")

class TestReversed(CompareLists):
  @staticmethod
  def manipulate(l):
    raise NotImplementedError("Test not yet implemented.")

class TestRmul(CompareLists):
  @staticmethod
  def manipulate(l):
    raise NotImplementedError("Test not yet implemented.")

class TestSetAttr(CompareLists):
  @staticmethod
  def manipulate(l):
    raise NotImplementedError("Test not yet implemented.")

class TestSetItem(CompareLists):
  @staticmethod
  def manipulate(l):
    return l[5] == l[-3]

class TestSetSlice(CompareLists):
  @staticmethod
  def manipulate(l):
    return l[3:5] == l[-5:-3]

class TestStr(CompareLists):
  @staticmethod
  def manipulate(l):
    return str(l)

class TestSubClassHook(CompareLists):
  @staticmethod
  def manipulate(l):
    raise NotImplementedError("Test not yet implemented.")

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
    return l.insert(3, "9fouear8aoeus")

class TestPop(CompareLists):
  @staticmethod
  def manipulate(l):
    return l.pop(9)

class TestRemove(CompareLists):
  @staticmethod
  def manipulate(l):
    return l.remove(24) #The value 24, not the index

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

class TestNe(CompareLists):
  @staticmethod
  def manipulate(l):
    raise NotImplementedError("Test not yet implemented.")

class TestGe(CompareLists):
  @staticmethod
  def manipulate(l):
    raise NotImplementedError("Test not yet implemented.")

class TestLe(CompareLists):
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

# Type casting
class TestInit(CompareLists):
  @staticmethod
  def manipulate(l):
    raise NotImplementedError("Test not yet implemented.")

# These should not be equal between the two types.
class TestSizeOf(CompareLists):
  @staticmethod
  def manipulate(l):
    raise NotImplementedError("Test not yet implemented.")

if __name__ == '__main__':
  unittest.main()
