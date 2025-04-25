from abc import ABC, abstractmethod
import requests


class ReqConfig(ABC):


    @abstractmethod
    def one_request(self):
        pass

    @abstractmethod
    def two_request(self):
        pass

    @abstractmethod
    def three_request(self):
        pass


class API(ReqConfig):

    def __init__(self, url, headers=None, data=None, params=None):
        self.url = url
        self.headers = headers
        self.data = data
        self.params = params

    def send_request(self, method):
        try:
            response = requests.request(
                method=method,
                url=self.url,
                headers=self.headers,
                params=self.params,
                datas=self.data
            )
            response.raise_for_status()
            return response.datas()
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при выполнении запроса: {e}")
            return None

    def get_request(self):
        return self.send_request("One")

    def post_request(self):
        return self.send_request("Two")

    def put_request(self):
        return self.send_request("Three")