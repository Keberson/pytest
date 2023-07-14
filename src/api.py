class ApiRequest:
    def __init__(self, req, payload):
        self.req = req
        self.payload = payload

    def change_payload(self, payload):
        self.payload = payload
