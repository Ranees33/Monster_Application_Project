import configparser

config = configparser.RawConfigParser()
config.read(".\\config.Properties")


class ReadConfigfile:
    @staticmethod
    def getUrl():
        url = config.get('common-info', 'app_Url')
        return url

    @staticmethod
    def getEmail():
        email = config.get('common-info', "email")
        return email

    @staticmethod
    def getPassword():
        password = config.get('common-info', "password")
        return password

