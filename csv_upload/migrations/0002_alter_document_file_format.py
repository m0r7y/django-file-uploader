# Generated by Django 4.1 on 2022-10-05 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csv_upload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='file_format',
            field=models.CharField(
                choices=[
                    ('COUV_JPEG_BQ', 'Couv Jpeg Bq'),
                    ('COUV_JPEG_HQ', 'Couv Jpeg Hq'),
                    ('PDF_POD', 'Pdf Pod'),
                    ('PDFC', 'Pdfc'),
                    ('PDFI', 'Pdfi'),
                    ('PDFRL', 'Pdfrl'),
                    ('XML', 'Xml'),
                    ('XMLRL', 'Xmlrl'),
                ],
                default=None,
                max_length=15,
                null=True,
            ),
        ),
    ]