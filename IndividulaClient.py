from  client import Client

class IndividulClient (Client):

    def getClosingbalanace(self,amount):
        return 2*10000

ind = IndividulClient()
ind.getClosingbalanace(1)

print('Get Closing Balance Of Client :', ind.getClosingbalanace(1))