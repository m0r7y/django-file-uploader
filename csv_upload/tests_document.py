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

    def test_documents_created(self):
        document = Document.objects.get(numdos='DD352051')
        self.assertEqual(str(document), 'DD352051.PDFC')
