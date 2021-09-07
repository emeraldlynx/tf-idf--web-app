from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser

from .forms import UploadFileForm
from .utils import TFIDF


@method_decorator(csrf_exempt, name='dispatch')
class TFIDFView(View):
    def get(self, request):
        form = UploadFileForm()
        context = {
            'form': form,
            'result': None,
            'error': '',
        }
        return render(request, 'words/tf_idf.html', context)
    
    def post(self, request):
        result = None
        error = ''

        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                uploaded_file = request.FILES['file']
                text = ''
                
                for line in uploaded_file:
                    text = text + line.decode()

                result = TFIDF.apply(text)        
            except:
                error = 'Wrong file'
        else:
            error = 'Wrong form'

        context = {
            'form': form,
            'result': result,
            'error': error,
        }
        return render(request, 'words/tf_idf.html', context)

class FileUploadView(APIView):
    parser_classes = (FileUploadParser,)

    def post(self, request, filename, format=None):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                uploaded_file = request.FILES['file']
                text = ''
                for line in uploaded_file:
                    text = text + line.decode()

                data = TFIDF.apply(text)
                return JsonResponse(data, status=200)
            except:
                return JsonResponse({'errors': {'Internal Server Error': True}}, status=500)
        else:
            errors = form.errors.as_json()
            return JsonResponse({'errors': errors}, status=400)
