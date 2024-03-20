class Human:
    info_list = ('name', 'birthday', 'phone', 'city', 'country', 'address')

    def __init__(self, name='default', birthday='newer', phone='+380000000000',
                 city='nowhere Town', country='Czechoslovakia', address='nowhere'):
        self.name = name
        self.birthday = birthday
        self.phone = phone
        self.city = city
        self.country = country
        self.address = address

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getBirthday(self):
        return self.birthday

    def setBirthday(self, birthday):
        self.birthday = birthday

    def getPhone(self):
        return self.phone

    def setPhone(self, phone):
        self.phone = phone

    def getCity(self):
        return self.city

    def setCity(self, city):
        self.city = city

    def getCountry(self):
        return self.country

    def setCountry(self, country):
        self.country = country

    def getAddress(self):
        return self.address

    def setAddress(self, address):
        self.address = address

    def def_list(self, link: str, key):
        match link:
            case 'name':
                if key == 'get':
                    return self.getName
                return self.setName
            case 'birthday':
                if key == 'get':
                    return self.getBirthday
                return self.setBirthday
            case 'phone':
                if key == 'get':
                    return self.getPhone
                return self.setPhone
            case 'city':
                if key == 'get':
                    return self.getCity
                return self.setCity
            case 'country':
                if key == 'get':
                    return self.getCountry
                return self.setCountry
            case 'address':
                if key == 'get':
                    return self.getAddress
                return self.setAddress

    def info(self, key='get', change_list: dict = {}):
        if key == 'get':
            for link in self.info_list:
                print(f'{link.title()} - {self.def_list(link, key)()}')
        else:
            for link in change_list:
                self.def_list(link, key)(change_list[link])


obj_dict = {'default': Human()}
while True:
    choice = input('''
    Read info   - 1
    Change info - 2
    Add info    - 3
    
    End the program - 0
    
    Enter a num of function: ''')
    print()
    change_list = {}
    match choice:

        case '0':
            break

        case '1':
            for obj in obj_dict.keys():
                print(obj)
            obj_name = input('Enter a name of object: ')
            obj_dict[obj_name].info()

        case '2':
            for obj in obj_dict.keys():
                print(obj)
            obj_name = input('Enter a name of object: ')
            print(Human.info_list)

            information = input('Enter an info to change separated by comma: ').split(',')
            for info in information:
                change_list[info.strip().lower()] = input(f'Enter a new {info}: ')
            obj_dict[obj_name].info('set', change_list)
            if 'name' in change_list:
                obj_dict[change_list['name']] = obj_dict[obj_name]
                obj_dict.pop(obj_name)

        case '3':
            for data in Human.info_list:
                change_list[data] = input(f'Enter a {data}')
            obj_dict[change_list['name']] = Human(change_list['name'], change_list['birthday'],
                                                  change_list['phone'], change_list['city'],
                                                  change_list['country'], change_list['address'])
