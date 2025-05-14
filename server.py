import rpyc
from constRPYC import * #-
from rpyc.utils.server import ThreadedServer

class DBList(rpyc.Service):
  value = []

  def exposed_append(self, data):
    self.value = self.value + [data]
    return self.value

  def exposed_value(self):
    return self.value
  
  def exposed_sum(self):
    sum = 0
    for i in self.value:
      sum += i
    return sum
  
  def exposed_showElement(self, index):
    if index >= len(self.value):
      return "Error! Index out of bounds."
    else:
      return self.value[index]
  

if __name__ == "__main__":
  server = ThreadedServer(DBList(), port = PORT)
  server.start()

