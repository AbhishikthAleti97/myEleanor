from django.views.generic import TemplateView
from home.forms import HomeForm
from django.shortcuts import render, redirect
from home.models import Post
import json
from chatterbot import ChatBot
import os
from django import forms

class HomeView(TemplateView):
    template_name = 'home/home.html'


    def get(self, request):
        form = HomeForm()
        posts = Post.objects.all().order_by('-created')
        print(posts)

        args = {'form':form, 'posts':posts}
        return render(request, self.template_name, args)

    def post(self, request):
        form = HomeForm(request.POST)
        dbpath = os.path.join(os.path.dirname(__file__),"Database","db.sqlite3")

        if form.is_valid():
            post = form.save(commit=False)
            resp = ChatBot("reply",database=dbpath, logic_adapters=["chatterbot.logic.BestMatch"] )
            response_text = resp.get_response(str(post.post))
            post.reply = "Bot replied: "+str(response_text)
            post.user = request.user
            post.save()


            text = form.cleaned_data['post']


            form = HomeForm()
            return redirect('home:home')

        

        args = {'form':form, 'text': text}
        return render(request, self.template_name, args)
