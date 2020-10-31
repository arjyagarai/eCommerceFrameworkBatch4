import configparser

config = configparser.RawConfigParser()
config.read("C://Users//Admin//PycharmProjects//eCommerceFramework//Configurations//config.ini")

class Readconfig:
    @staticmethod
    def getApplicationUrl():
        url = config.get('application info','baseURL')
        return url

    @staticmethod
    def getUsername():
        username = config.get('application info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('application info', 'password')
        return password

    @staticmethod
    def getConfigforPayementDetails(param):
        cname = config.get('payment details', param)
        return cname
