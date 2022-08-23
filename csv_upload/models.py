from typing import List

from django.db import models


class Document(models.Model):
    class FileFormat(models.TextChoices):
        COUV_JPEG_BQ = 'COUV_JPEG_BQ'
        COUV_JPEG_HQ = 'COUV_JPEG_HQ'
        PDF_POD = 'PDF_POD'
        PDFC = 'PDFC'
        PDFI = 'PDFI'
        PDFRL = 'PDFRL'
        XML = 'XML'
        XMLRL = 'XMLRL'
        NO_FORMAT = ''

    numdos = models.CharField(max_length=10, db_index=True)
    numdosverling = models.CharField(max_length=10)
    ancart = models.CharField(max_length=20)
    filiere = models.CharField(max_length=5)
    etape = models.FloatField()
    verling = models.CharField(max_length=8)
    file_format = models.CharField(max_length=15, choices=FileFormat.choices)

    def __str__(self) -> str:
        return f'{self.numdos}.{self.file_format}'

    @staticmethod
    def document_fields() -> List[str]:
        """
        return Document fields'name
        """
        return [
            'numdos',
            'numdosverling',
            'ancart',
            'filiere',
            'etape',
            'verling',
            'file_format',
        ]
