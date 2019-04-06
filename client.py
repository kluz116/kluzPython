from abc import abstractmethod


class Client:
    @abstractmethod
    def getClosingbalanace(self,amount):
        pass


cli1 = Client()
cli1.firstname = 'Allan Musembya'

print('The Client Name is :',cli1.getClosingbalanace(10000))