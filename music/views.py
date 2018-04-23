from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views.generic import View
from .forms import UserForm
from .models import Album


class IndexView(generic.ListView):
    template_name = "music/index.html"
    context_object_name = 'all_albums'

    # access the database and get album we want
    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = "music/detail.html"

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']

class AlbumDelete(DeleteView):
    model = Album
    # delete success, jump to what url
    success_url = reverse_lazy('music:index')

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'

    # display a blank form
    def get(self,request):
        # none context
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})


    # process form data
    def post(self,request):

        # data in the form, form already validate by form.py
        form = self.form_class(request.POST)

        if form.is_valid():

            # create a object from the form, not sending toDB yet
            user = form.save(commit=False)

            # cleaned (normalized) data, using the same format
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            # save to the database
            user.save()

            # return User objects if credentials are correct
            user = authenticate(username=username,password=password)

            if user is not None:

                if user.is_active:
                    # let user log in the website
                    login(request,user)
                    return redirect('music:index')
        # account not valid-> blank form
        return render(request,self.template_name,{'form':form})










