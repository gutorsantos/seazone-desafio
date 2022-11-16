from rest_framework.test import APITestCase
from imoveis.models import Imovel
from anuncios.models import Anuncio
from reservas.models import Reserva
from rest_framework.reverse import reverse

class ReservaTests(APITestCase):

    def setUp(self):
        self.url = reverse('reservas-list')
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

        self.reserva_test = Reserva.objects.create(
            checkin='2022-12-15T19:25:00Z',
            checkout='2022-12-30T19:25:00Z',
            total=2000.00,
            comentario='Observações sobre a reserva',
            hospedes=10,
            anuncio_id=self.anuncio_test
        )

    def test_create_reserva(self):
        data = {
            "checkin": '2022-12-15T19:25:00Z',
            "checkout": '2022-12-17T19:25:00Z',
            "total": 200.00,
            "comentario": "Observações sobre a reserva",
            "hospedes": 10,
            "anuncio_id": self.anuncio_test.id
        }
        response = self.client.post(self.url, data)
        assert response.status_code == 201

    def test_invalid_checkin_checkout_reserva(self):
        data = {
            "checkin": '2022-12-17T19:25:00Z',
            "checkout": '2022-12-15T19:25:00Z',
            "total": 200.00,
            "comentario": "Observações sobre a reserva",
            "hospedes": 10,
            "anuncio_id": self.anuncio_test.id
        }
        response = self.client.post(self.url, data)
        assert response.status_code == 400 and 'O check-out não pode ocorrer antes do check-in' in response.data['non_field_errors']

    def test_invalid_checkin_reserva(self):
        data = {
            "checkin": '2022-10-17T19:25:00Z',
            "checkout": '2022-12-15T19:25:00Z',
            "total": 200.00,
            "comentario": "Observações sobre a reserva",
            "hospedes": 10,
            "anuncio_id": self.anuncio_test.id
        }
        response = self.client.post(self.url, data)
        assert response.status_code == 400 and 'Você não pode fazer uma reserva para o passado' in response.data['non_field_errors']

    def test_invalid_hospedes_reserva(self):
        data = {
            "checkin": '2022-12-15T19:25:00Z',
            "checkout": '2022-12-17T19:25:00Z',
            "total": 200.00,
            "comentario": "Observações sobre a reserva",
            "hospedes": 11,
            "anuncio_id": self.anuncio_test.id
        }
        response = self.client.post(self.url, data)
        assert response.status_code == 400 and 'Limite máximo de hospedes excedido' in response.data['non_field_errors']

    def test_list_reserva(self):
        response = self.client.get(self.url)
        assert response.status_code == 200 and len(response.data) >= 1

    def test_retrieve_reserva(self):
        response = self.client.get(self.url+f'{self.reserva_test.id}/')
        assert response.status_code == 200

    def test_put_reserva(self):
        data = {
            "checkin": '2022-12-15T19:25:00Z',
            "checkout": '2022-12-30T19:25:00Z',
            "total": 2500.00,
            "comentario": "Observações sobre a reserva",
            "hospedes": 10,
            "anuncio_id": self.anuncio_test.id
        }
        response = self.client.put(self.url+f'{self.reserva_test.id}/', data)
        assert response.status_code == 405

    def test_patch_reserva(self):
        data = { "hospedes": 8 }
        response = self.client.patch(self.url+f'{self.reserva_test.id}/', data)
        assert response.status_code == 405

    def test_delete_reserva(self):
        response = self.client.delete(self.url+f'{self.reserva_test.id}/')
        assert response.status_code == 204
