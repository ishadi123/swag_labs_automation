import configparser
config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class ReadConfig:
    @staticmethod
    def get_application_url():
        url = config.get('common data', 'base_url')
        return url

    @staticmethod
    def get_username_standard():
        username = config.get('common data', 'username_standard_user')
        return username

    @staticmethod
    def get_username_locked_out_user():
        username = config.get('common data', 'username_locked_out_user')
        return username

    @staticmethod
    def get_username_problem_user():
        username = config.get('common data', 'username_problem_user')
        return username

    @staticmethod
    def get_username_visual_user():
        username = config.get('common data', 'username_visual_user')
        return username

    @staticmethod
    def get_username_error_user():
        username = config.get('common data', 'username_error_user')
        return username

    @staticmethod
    def get_password():
        password = config.get('common data', 'password')
        return password

    @staticmethod
    def get_invalid_username():
        invalid_username = config.get('common data', 'invalid_username')
        return invalid_username

