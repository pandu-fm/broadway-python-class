from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay_via_bank(self):
        pass

    @abstractmethod
    def pay_via_QR(self):
        pass

    def download_receipt(self):
        return {
            "name": "abc",
            "total": 200
        }


class LocalShop(Payment):
    def pay_via_bank(self):
        pass

    def pay_via_QR(self):
        pass

class Bhatbheteni(Payment):
    def pay_via_bank(self):
        pass

    def pay_via_QR(self):
        pass


class BigMart(Payment):
    def pay_via_bank(self):
        pass

    def pay_via_QR(self):
        pass

local_shop = LocalShop()
bhatbhateni = Bhatbheteni()

# payment = Payment()