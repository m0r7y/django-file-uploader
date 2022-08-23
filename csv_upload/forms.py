import csv

from django import forms


class UploadFileForm(forms.Form):
    file = forms.FileField()

    def clean_file(self):
        file: bytes = self.cleaned_data['file']
        try:
            csv.Sniffer().sniff(file.read(1024).decode('ISO-8859-1'))
            file.seek(0)
        except csv.Error:
            raise forms.ValidationError('CSV format expected !!')
        return file
