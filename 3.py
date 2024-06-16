class Model(object):
    services = {
        'email': {'number': 1000, 'price': 2,},
        'sms': {'number': 1000, 'price': 10,},
        'voice': {'number': 1000, 'price': 15,},
    }

class View(object):
    def list_services(self, services):
        for svc in services:
            print(svc)

    def list_pricing(self, services):
        for svc in services:
            print(f"For {Model.services[svc]['number']} {svc} message, you pay ${Model.services[svc]['price']}")

class View2(object):
    def list_services(self, services):
        for svc in services:
            print(svc)

    def list_pricing(self, services):
        for svc in services:
            print(f"Untuk setiap {Model.services[svc]['number']} {svc}, Anda membayar ${Model.services[svc]['price']}")

class Controller(object):
    def __init__(self):
        self.model = Model()
        self.view = View()
        self.view2 = View2()

    def get_services(self, language):
        services = self.model.services.keys()
        if language == 'English':
            return self.view.list_services(services)
        elif language == 'Indonesia':
            return self.view2.list_services(services)

    def get_pricing(self, language):
        services = self.model.services.keys()
        if language == 'English':
            return self.view.list_pricing(services)
        elif language == 'Indonesia':
            return self.view2.list_pricing(services)

    def bid_price(self):
        service_name = input("Masukan nama layanan: ")
        bid_price = float(input("Masukan harga penawaran Anda: "))

        self.model.services[service_name] = {'number': 1000, 'price': bid_price}

        print("Harga sesuai dengan penawaran Anda!")
        self.get_pricing(language)

# Instansiasi objek
controller = Controller()
language = input("What language do you choose? [1]English [2]Indonesia: ")
if language == '1':
    language = 'English'
elif language == '2':
    language = 'Indonesia'
print("Services Provided:")
controller.get_services(language)
print("Pricing for Services:")
controller.get_pricing(language)
controller.bid_price()
