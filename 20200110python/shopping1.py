class Notebook:
  _sku = 'unknown'
  _price = 0
  _size = 'unknown'
  def __init__(self, sku, price, size):
    self._sku = sku
    self._price = price
    self._size = size
  def getSku(self):
    return self._sku
  def getPrice(self):
    return self._price
  def getSize(self):
    return self._size
  def info(self):
    return 'Notebook: {} {} {}'.format(self._sku, self._price, self._size)
  def prDetails(self):
    print(self.info())
  
class Pen:

def test():
  nb1 = Notebook('#001', 200, '4K')
  print(nb1.getSku(), nb1.getPrice(), nb1.getSize())
  print(nb1.info())
  nb1.prDetails()

  pen1 = Pen(.....)
  print(....)
  print(....)
  pen1........

test()