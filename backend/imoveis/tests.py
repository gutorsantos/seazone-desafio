from rest_framework.test import APITestCase
from imoveis.models import Imovel
from rest_framework.reverse import reverse

class ImovelTests(APITestCase):

    def setUp(self):
        self.url = reverse('imoveis-list')
        self.imovel_test = Imovel.objects.create(
            hospedes=10,
            banheiros=5,
            pet=True,
            valor_limpeza=150,
            data_ativacao='2015-07-05'
        )


    def test_create_imovel(self):
        data = {
            "hospedes": 2,
            "banheiros": 1,
            "pet": False,
            "valor_limpeza": 30,
            "data_ativacao": '2013-04-10'
        }
        response = self.client.post(self.url, data)
        assert response.status_code == 201

    def test_list_imovel(self):
        response = self.client.get(self.url)
        assert response.status_code == 200 and len(response.data) >= 1

    def test_retrieve_imovel(self):
        response = self.client.get(self.url+f'{self.imovel_test.id}/')
        assert response.status_code == 200

    def test_put_imovel(self):
        data = {
            "hospedes": 10,
            "banheiros": 4,
            "pet": True,
            "valor_limpeza": 150,
            "data_ativacao": '2015-07-05'
        }
        response = self.client.put(self.url+f'{self.imovel_test.id}/', data)
        assert response.status_code == 200

    def test_patch_imovel(self):
        data = { "banheiros": 5 }
        response = self.client.patch(self.url+f'{self.imovel_test.id}/', data)
        assert response.status_code == 200

    def test_delete_imovel(self):
        response = self.client.delete(self.url+f'{self.imovel_test.id}/')
        assert response.status_code == 204
