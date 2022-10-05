from django.test import TestCase

from csv_upload.models import Document


class DocumentTestCase(TestCase):
    def setUp(self):
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

        Document.objects.create(
            **{
                'numdos': 'DD352055',
                'numdosverling': 'DD352055',
                'ancart': 'LNEN50266-2-1',
                'filiere': 'ETR',
                'etape': 75.60,
                'verling': 'E',
            }
        )

    def test_documents_created(self):
        document = Document.objects.get(numdos='DD352051')
        self.assertEqual(str(document), 'DD352051.PDFC')

        document = Document.objects.get(numdos='DD352055')
        self.assertEqual(str(document), 'DD352055')
