from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django import views
import pandas

from .forms import UploadFileForm
from .utils import compute_tf_idf, separate_text


@method_decorator(csrf_exempt, name='dispatch')
class FileView(views.View):
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

                words = separate_text(text)
                words_stats: pandas.Dataframe = compute_tf_idf(words)[:50].to_dict()
                indecies = range(len(words_stats['Word']))

                result = {'words_stats': words_stats, 'indecies': indecies}
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
