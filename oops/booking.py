from abc import ABC,abstractmethod

class Booking(ABC):
    @abstractmethod
    def makePayment(self):
        pass


class FlightBooking(Booking):
    def __init__(self,amount):
        self.__amount=amount

    def makePayment(self):
        print("Pay the amount %d by any payment mode"
              %(self.__amount))


flightBookimg=FlightBooking(150000)
flightBookimg.makePayment()