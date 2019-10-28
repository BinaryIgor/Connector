from src.presenter.presenter_response import PresenterResponse


def get_ip(ip):
    return PresenterResponse(data=ip)


def get_port(port):
    return PresenterResponse(data=port)

def get_data():
    pass