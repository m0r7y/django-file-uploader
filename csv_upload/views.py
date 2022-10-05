import csv
import io
from typing import Dict, List, Union

from django.http import (
    Http404,
    HttpRequest,
    HttpResponse,
    HttpResponseRedirect,
    JsonResponse,
)
from django.shortcuts import render
from django.views.decorators.http import require_GET

from .forms import UploadFileForm
from .models import Document


def mapdict(values: Dict[str, Union[str, float]]):
    """
    convert dict value to Document object
    convert etape fields to float"""
    try:
        values['etape'] = float(values['etape'])
    except ValueError:
        pass
    values['file_format'] = values['file_format'] or None
    return Document(**values)


def upload_file(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form: UploadFileForm = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # avoid re-mapping when using models
            fieldnames: List[str] = Document.document_fields()
            string_io: io.StringIO = io.StringIO(
                request.FILES['file'].read().decode('ISO-8859-1')
            )
            reader: csv.DictReader = csv.DictReader(
                string_io, fieldnames=fieldnames, delimiter='|', quotechar='"'
            )
            # skip first row
            next(reader)
            Document.objects.all().delete()
            Document.objects.bulk_create(list(map(mapdict, [row for row in reader])))
            return HttpResponseRedirect('success/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


@require_GET
def upload_file_success(request: HttpRequest) -> HttpResponse:
    return render(request, 'sucess.html')


@require_GET
def get_document(request: HttpRequest, numdos: str = '') -> HttpResponse:
    documents = Document.objects.filter(numdos=numdos)
    if not documents.exists():
        raise Http404
    return JsonResponse(list(documents.values()), safe=False)
