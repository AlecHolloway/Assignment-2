from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.views.generic import TemplateView

from .models import Post
from .forms import HomeForm, BMIForm


class HomeView(TemplateView):
    template_name = 'home.html'


    def get(self, request):
        form = HomeForm()
        posts = Post.objects.all()

        args = {'form': form, 'posts': posts}
        return render(request, self.template_name, args)

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            text = form.cleaned_data['name']
            text1 = form.cleaned_data['age']
            text2 = form.cleaned_data['income']
            text3 = form.cleaned_data['years']
            form = HomeForm()

            return redirect('home')

        args = {'form': form, 'text': text, 'text1': text1, 'text2': text2, 'text3': text3}
        return render(request, self.template_name, args)


class BMIView(TemplateView):
    template_name = 'BMI.html'

    def get(self, request):
        form = BMIForm()
        posts = Post.objects.all()
        ##posts = Post.objects.filter(published=True).order_by('name')[0:1]
        args = {'form': form, 'posts': posts}
        return render(request, self.template_name, args)

    def post(self, request):
        form = BMIForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            text = form.cleaned_data['name']
            text1 = form.cleaned_data['weight']
            text2 = form.cleaned_data['feet']
            text3 = form.cleaned_data['inches']
            form = HomeForm()

            return redirect('BMI')

        args = {'form': form, 'text': text, 'text1': text1, 'text2': text2, 'text3': text3}
        return render(request, self.template_name, args)


def calculate(self, text, text1, text2):
    text3 = text + text1 + text2
