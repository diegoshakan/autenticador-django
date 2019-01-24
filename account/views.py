from django.shortcuts import render, redirect
from account.forms import UserForm
from django.views import View
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'account/index.html')

class Cadastro(View):
    def get(self, request):
        form = UserForm()
        return render(request,'account/cadastro.html',{'form': form})


    def post(self, request):
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print(form.errors)

        return render(request,'account/cadastro.html', {'form': form})

# def cadastro(request):
#     form = EstudanteModelForm(request.POST or None)
#     context = {'form': form}
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     return render(request, 'account/cadastro.html', context)