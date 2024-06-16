class Model(object):
    services = {
        'email': {'number': 1000, 'price': 2},
        'sms': {'number': 1000, 'price': 10},
        'voice': {'number': 1000, 'price': 15},
    }

class View:
    def list_services(self, services):
        print("Services Provided:")
        for svc in services:
            print(svc, '')

    def list_pricing(self, services):
        print("Pricing for Services:")
        for svc in services:
            print("For", Model.services[svc]['number'], svc, "message you pay $", Model.services[svc]['price'])

class View2:
    def list_services(self, services):
        print("Layanan yang disediakan:")
        for svc in services:
            print(svc)

    def list_pricing(self, services):
        print("Tarif tiap layanan:")
        for svc in services:
            print("Untuk setiap", Model.services[svc]['number'], "pesan", svc, "Anda membayar $", Model.services[svc]['price'])

class Controller:
    def __init__(self):
        while True:
            language_choice = input("What language do you choose? [1]English [2]Indonesia: ")
            if language_choice in ('1', '2'):
                break
            else:
                print("Error, choose the language number!")
                print("Error, choose the language number!")
                exit()
        if language_choice == '1':
            self.view = View()
        else:
            self.view = View2()

    def get_services(self):
        services = Model.services.keys()
        self.view.list_services(services)

    def get_pricing(self):
        services = Model.services.keys()
        self.view.list_pricing(services)

controller = Controller()
controller.get_services()
controller.get_pricing()