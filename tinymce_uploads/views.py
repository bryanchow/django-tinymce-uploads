import json
from os.path import splitext
from uuid import uuid4
from base64 import b64decode
from django.http import HttpResponse, HttpResponseBadRequest, Http404
from django.core.files.base import ContentFile
from django.views.decorators.csrf import csrf_exempt
from .models import Upload


@csrf_exempt
def upload_file(request):
    """
    Handle an AJAX upload request from TinyMCE, and return the URL of the
    uploaded file.
    """

    if not request.user.is_authenticated() and request.user.is_staff:
        raise Http404

    if request.method == 'POST':

        try:
            original_filename = request.POST['filename']
            data = b64decode(request.POST['base64'])
        except KeyError:
            return HttpResponseBadRequest

        ext = splitext(original_filename)[1]
        filename = "{}{}".format(uuid4().hex, ext)
        content = ContentFile(data)

        upload = Upload(filename=filename)
        upload.file.save(filename, content)
        upload.size = content.size
        upload.save()

        return HttpResponse(json.dumps({
            'location': upload.file.url,
        }), content_type="application/json")

    raise Http404
