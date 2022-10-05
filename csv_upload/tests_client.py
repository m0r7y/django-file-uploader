import csv
import io
import unittest

from django.test import Client

from .models import Document


class ClientTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        Document.objects.create(
            **{
                'numdos': 'DD352051',
                'numdosverling': 'DD352051',
                'ancart': 'LNEN50266-2-1',
                'filiere': 'ETR',
                'etape': 99.60,
                'verling': 'E',
                'file_format': 'PDFC',
            }
        )

    def test_document_get(self):
        # document exist
        response = self.client.get('/document/get/DD352051/')
        self.assertEqual(response.status_code, 200)

        # document !exist
        response = self.client.get('/document/get/DD3520/')
        self.assertEqual(response.status_code, 404)

        # not allowed method
        response = self.client.post('/document/get/DD352051/')
        self.assertEqual(response.status_code, 405)

    def test_document_upload(self):
        # get request
        response = self.client.get('/document/upload/')
        self.assertEqual(response.status_code, 200)

        # valid form, true CSV
        io_string = io.StringIO()
        fieldnames = Document.document_fields()
        writer = csv.DictWriter(io_string, fieldnames=fieldnames, delimiter='|')
        writer.writeheader()
        writer.writerow(
            {
                'numdos': 'DD353051',
                'numdosverling': 'DD353051',
                'ancart': 'LNEN50266-2-1',
                'filiere': 'ETR',
                'etape': 99.60,
                'verling': 'E',
                'file_format': 'PDFC',
            }
        )
        writer.writerow(
            {
                'numdos': 'DD353055',
                'numdosverling': 'DD353055',
                'ancart': 'LNEN50266-2-1',
                'filiere': 'ETR',
                'etape': 99.60,
                'verling': 'E',
                'file_format': '',
            }
        )
        response = self.client.post(
            '/document/upload/',
            {'file': io.StringIO(io_string.getvalue())},  # weird
            follow=True,
        )
        self.assertEqual(response.redirect_chain, [('success/', 302)])
        document = Document.objects.filter(numdos='DD353051')
        self.assertTrue(document.exists())

        document = Document.objects.get(numdos='DD353055')
        self.assertIsNone(document.file_format)

        # invalid form, plain test
        response = self.client.post(
            '/document/upload/',
            {'file': ''},
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
