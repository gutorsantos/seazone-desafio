from rest_framework.test import APITestCase
from imoveis.models import Imovel
from anuncios.models import Anuncio
from rest_framework.reverse import reverse

class AnuncioTests(APITestCase):

    def setUp(self):
        self.url = reverse('anuncios-list')
        self.imovel_test = Imovel.objects.create(
            hospedes=10,
            banheiros=5,
            pet=True,
            valor_limpeza=150,
            data_ativacao='2015-07-05'
        )

        self.anuncio_test = Anuncio.objects.create(
            plataforma='AirBnB',
            taxa=20,
            imovel_id=self.imovel_test
        )

    def test_create_anuncio(self):
        data = {
            "plataforma": "AirBnB",
            "taxa": 20,
            "imovel_id": self.imovel_test.id
        }
        response = self.client.post(self.url, data)
        assert response.status_code == 201

    def test_list_anuncio(self):
        response = self.client.get(self.url)
        assert response.status_code == 200 and len(response.data) >= 1

    def test_retrieve_anuncio(self):
        response = self.client.get(self.url+f'{self.anuncio_test.id}/')
        assert response.status_code == 200

    def test_put_anuncio(self):
        data = {
            "plataforma": "AirBnB",
            "taxa": 22,
            "imovel_id": self.imovel_test.id
        }
        response = self.client.put(self.url+f'{self.anuncio_test.id}/', data)
        assert response.status_code == 200

    def test_patch_anuncio(self):
        data = { "plataforma": 'Vrbo' }
        response = self.client.patch(self.url+f'{self.anuncio_test.id}/', data)
        assert response.status_code == 200

    def test_delete_anuncio(self):
        response = self.client.delete(self.url+f'{self.anuncio_test.id}/')
        assert response.status_code == 405
