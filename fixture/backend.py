import requests
from data.document_data import document_name_be


class BackendHelper:

    def __init__(self, res):
        self.res = res

    def get_token(self):
        url = 'http://test.def.k8s.dev.bi.zone/api/public/auth/connect/token'
        data = {"grant_type": "password", "client_id": "portal", "clinet_secret": "s0KL3w5MxzPy02E",
                "username": "admin", "password": "Default!1"}
        r = requests.post(url, data)
        access_token = r.json()['access_token']
        assert (r.status_code == 200), True
        return access_token

    def create_document(self):
        url = 'http://test.def.k8s.dev.bi.zone/api/public/defdocs/document'
        head = {"Authorization": "Bearer " + self.get_token(),
                "X-OID": "838dd131-0c06-456d-8455-03493318b25a"}
        data = {"name": document_name_be,
                "number": "123",
                "description": "123",
                "date": "2020-12-11T21:00:00.000Z",
                "fileObjectId": "fbac6141-5562-4d2a-b7dd-59b92da35a17",
                "fileName": "File_test-1 (1) (1).txt",
                "templateCode": "Default_v1",
                "organizationId": "838dd131-0c06-456d-8455-03493318b25a"}
        r = requests.post(url, headers=head, json=data)
        assert (r.status_code == 200), True
        # document_id = r.json()['id']
        # return document_id

    def get_bad_token(self):
        url = 'http://test.def.k8s.dev.bi.zone/api/public/auth/connect/token'
        data = {"grant_type": "password", "client_id": "portal", "clinet_secret": "s0KL3w5MxzPy02E",
                "username": "admin", "password": "qwe"}
        r = requests.post(url, data)
        assert (r.status_code == 200), True

    def get_document_statistic(self):
        url = 'http://test.def.k8s.dev.bi.zone/api/public/defdocs/document-statistic'
        head = {"Authorization": "Bearer " + self.get_token(),
                "X-OID": "838dd131-0c06-456d-8455-03493318b25a"}
        r = requests.get(url, headers=head)
        documents_list = r.json()
        print(documents_list)
        assert (r.status_code == 200), True

    def get_last_document_name(self):
        url = 'http://test.def.k8s.dev.bi.zone/api/public/defdocs/document-statistic'
        head = {"Authorization": "Bearer " + self.get_token(),
                "X-OID": "838dd131-0c06-456d-8455-03493318b25a"}
        r = requests.get(url, headers=head)
        assert (r.status_code == 200), True
        print(r.json()[0]['name'])




