from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import GuessNumbers
from .forms import PostForm

# Create your views here.
def index(request):

    lottos = GuessNumbers.objects.all()

    return render(request, 'lotto/default.html', {'lottos' : lottos}) # context-dict

# 중요한 부분 ********************************************
def post(request):

    if request.method == 'POST':

        form = PostForm(request.POST)

        if form.is_valid():
            lotto = form.save(commit=False)
            lotto.generate()

            # 특정 url로 이동하세요 > redirect 
            return redirect('index')
        # form.save()
    else:
        form = PostForm()
        return render(request, 'lotto/form.html', {'form' : form})
# *********************************************************

def hello(request):

    return HttpResponse("<h1 style='color:blue;'>Hello, World</h1>")


def detail(request, lottokey):

    lotto = GuessNumbers.objects.get(pk=lottokey)

    return render(request, 'lotto/detail.html', {'lotto':lotto})



# #HTML에서 name이 'name'인 input tag에 대해 USER가 입력한 값 
#request.POST['name'] 