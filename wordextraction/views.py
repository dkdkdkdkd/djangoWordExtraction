from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from .extract import extract_word
from .translate import makeWordDic
from django.views.generic import ListView
from .models import WordDb

from rest_framework.views import APIView
from .serializers import WordSerializer
from rest_framework.response import Response

# Create your views here.

class AddressForm(forms.Form):
    input_address = forms.CharField(label="address", max_length=300)


def index(request):
    return render(request, 'wordextraction/index.html')


def add(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)

        if form.is_valid():
            address = form.cleaned_data['input_address']  #주소 받아오기

            words = extract_word(address)       # 주소에서 단어 추출
            makeWordDic((words[:30]))  #  추출한 단어 한글뜻 구해서 저장

            form = AddressForm()
            return render(request, 'wordextraction/add.html'
                          , {'form': form})

    else:
        form = AddressForm()
        return render(request, 'wordextraction/add.html'
                      , {'form': form})


class Show(ListView):
    model = WordDb
    template_name = 'wordextraction/show.html'
    paginate_by = 30
    ordering = "?"

# def show(request):
#     global address
#     # words = extract_word(address)
#     # words = makeWordDic(words[:30])
#
#     return render(request, 'wordextraction/show.html'
#                   , {'words': words})

class WordListAPI(APIView):
    def get(self, request):
        queryset = WordDb.objects.order_by('?').all()[:30]
        print(len(queryset))
        serializer = WordSerializer(queryset, many=True)
        return Response(serializer.data)


