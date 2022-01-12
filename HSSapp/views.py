from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from .models import State, District, Order, RequestWork, JobCategory, Profile, Area, Feedback, Notification, Location, \
    Chat
from django.contrib.auth.models import User
from .forms import locationform, loginform, profileform, searchform, phoneform, jobform, workform, Chatform,registerform
from django.contrib.auth import authenticate, login,logout
from itertools import chain
from django import forms
from django.contrib.auth.forms import AuthenticationForm



class Register(CreateView):
    model = User
    form_class = registerform
    template_name = ('HSSapp/registration.html')
    success_url = reverse_lazy('login')



def loginview(request):
    if request.method == 'GET':
        form = loginform()
        print("inside get")
        return render(request, 'HSSapp/login.html', {'form': form})
    if request.method == 'POST':
        form = loginform(request.POST)
        print('inside post')
        name = request.POST['username']
        pwd = request.POST['password']
        user = User.objects.filter(username=name)
        print('user', user)
        print('name: ', name)
        print('pwd: ', pwd)
        l1 = len(user)
        print('l1:',l1)
        flag=0
        if l1 == 1:
            if user[0].password == pwd:
                flag = 1
        # print('user: ', user)
        if flag==1:
            request.session['user'] = user[0].id
            print('userid:', user[0].id)
            login(request, user[0])
            print("login successfull")
            # print(request.session['user'])
            return redirect('mypage')
        else:
            print('not satisfied')
            return render(request, 'HSSapp/login.html', {'form': form})
    return render(request, 'home.html')


def logoutview(request):

    logout(request)
    # del request.session['user']
    return redirect('login')


def profileview(request):
    if request.method == 'GET':
        form = profileform()
        return render(request, 'HSSapp/profile.html', {'form': form})
    if request.method == 'POST':
        form = profileform(request.POST)
        if form.is_valid():
            phone = request.POST['phone']
            job = request.POST['job']
            print(job)
            print(request.session['user'])
            user = User.objects.get(id=request.session['user'])
            print(user)
            job1 = JobCategory.objects.get(id=job)
            print(job1)
            u = Profile(name=user, phone=phone, job=job1)
            print(u)
            u.save()
            return redirect('mypage')


def locationview(request):
    if request.method == 'GET':
        form = locationform()
        return render(request, 'HSSapp/location.html', {'form': form})
    if request.method == 'POST':
        form = locationform(request.POST)
        if form.is_valid():
            user = User.objects.get(id=request.session['user'])
            state = request.POST['state']
            state1 = State.objects.get(id=state)
            district = request.POST['district']
            district1 = District.objects.get(id=district)
            area = request.POST['area']
            area1 = Area.objects.get(id=area)
            place = request.POST['place']
            u = Location(name=user, state=state1, district=district1, area=area1, place=place)
            u.save()
            return render(request, 'HSSapp/mypage.html', {'form': form})


def Locationview(request):
    user = User.objects.get(id=request.session['user'])
    loc = Location.objects.filter(name=user)
    print('location view')
    l1 = len(loc)
    print('length: ', l1)
    if l1 == 0:
        print('inside if xcondition')
        return redirect('location')
    print('location: ', loc)
    print(loc[0].id)
    return render(request, 'HSSapp/locationview.html', {'object_list': loc})


def Profileview(request):
    user = User.objects.get(id=request.session['user'])
    prof = Profile.objects.filter(name=user)
    return render(request, 'HSSapp/profileview.html', {'object_list': prof})


def search(request):
    if request.method == 'GET':
        print('inside search get')
        form = searchform()
        return render(request, 'HSSapp/search.html', {'form': form})
    if request.method == 'POST':
        form = searchform(request.POST)
        job = request.POST['job']
        user = Profile.objects.filter(job=job)
        return render(request, 'HSSapp/search2.html', {'form': form, 'object_list': user})


def sort(request):
    if request.method == 'GET':
        print('inside sort get')
        form = locationform()
        return render(request, 'HSSapp/filter.html', {'form': form})
    if request.method == 'POST':
        form = locationform(request.POST)
        if form.is_valid():
            state = request.POST['state']
            district = request.POST['district']
            area = request.POST['area']
            place = request.POST['place']
            print('place', place)
            if place == '':
                print('place none')
                loc = Location.objects.filter(state=state).filter(district=district).filter(area=area)
            else:
                loc = Location.objects.filter(state=state).filter(district=district).filter(area=area).filter(
                    place=place)

            print('location:', loc)
            l1 = len(loc)
            print('l1= ', l1)
            user = list()
            for i in range(0, l1):
                user1 = Profile.objects.filter(name=loc[i].name)
                user = list(chain(user, user1))
            print('user: ', user)
            return render(request, 'HSSapp/search3.html', {'form': form, 'object_list': user})


def phoneedit(request, pk, template_name='HSSapp/profile.html'):
    book = get_object_or_404(Profile, pk=pk)
    form = phoneform(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('profileview')
    return render(request, template_name, {'form': form})


def jobedit(request, pk, template_name='HSSapp/profile.html'):
    book = get_object_or_404(Profile, pk=pk)
    form = jobform(request.POST or None, instance=book)
    print('inside phoneedit')
    if form.is_valid():
        form.save()
        return redirect('profileview')
    return render(request, template_name, {'form': form})


def chat(request, pk,template_name='HSSapp/chat.html'):
    user = get_object_or_404(Notification, pk=pk)
    form = Chatform(request.POST or None, instance=user)
    # customername = user.customername
    # name = user.name
       
    if form.is_valid():
        form.save()
        # message = request.POST['message']
        # Chat(name=name, customername=customername, message=message)
        return redirect('chat')
    # return render(request, template_name, {'form': form})


class Profiledelete(DeleteView):
    model = Profile
    template_name = 'HSSapp/delete.html'
    success_url = reverse_lazy('profileview')


def userview(request, pk, template_name='HSSapp/searchuserview.html'):
    book = get_object_or_404(Profile, pk=pk)
    user = Profile.objects.get(id=pk)
    return render(request, template_name, {'object_list': user})


class Locationupdate(DeleteView):
    model = Location
    template_name = 'HSSapp/update.html'
    success_url = reverse_lazy('location')


def notificationview(request):
    print('inside notification')
    print(request.session['user'])
    user = User.objects.get(id=request.session['user'])
    note = Notification.objects.filter(name=user)
    return render(request, 'HSSapp/notification.html', {'object_list': note})


class Notice(DetailView):
    model = Notification
    template_name = 'HSSapp/notice.html'


def workrequest(request):
    if request.method == 'GET':
        print('inside workrequest get')
        form = workform()
        return render(request, 'HSSapp/work.html', {'form': form})
    if request.method == 'POST':
        form = workform(request.POST)
        if form.is_valid():
            name = User.objects.get(id=request.session['user'])
            print('name', name)
            notice = request.POST['notice']
            category = request.POST['category']
            print('user: ', request.session['user'])
            cat = JobCategory.objects.get(id=category)
            print('category: ', category)
            r = RequestWork(name=name, notice=notice, category=cat)
            p = Profile.objects.filter(job=category)
            l1 = len(p)
            for i in range(0, l1):
                if p[i].name != name:
                    n = Notification(name=p[i].name, customername=name, notice=notice, category=cat)
                    print(p[i].name)
                    n.save()
            r.save()

            return redirect('mypage')


def mypagenotice(request):
    print('inside notification')
    # print(request.session['user'])
    user = User.objects.get(id=request.session['user'])
    print('login: ', user.last_login)
    date = user.last_login
    print('date:', date)
    note = Notification.objects.filter(name=user)
    print('note none')
    return render(request, 'HSSapp/mypage.html', {'object_list': note})


def workposted(request):
    print('inside work post')
    user = User.objects.get(id=request.session['user'])
    note = RequestWork.objects.filter(name=user)
    print(note)
    return render(request, 'HSSapp/workpost.html', {'object_list': note})


class Noticedelete(DeleteView):
    model = RequestWork
    template_name = 'HSSapp/deletenotice.html'
    success_url = reverse_lazy('noticedelete')


def noticedelete(request, pk):
    work = get_object_or_404(RequestWork, pk=pk)
    note = Notification.objects.filter(customername=work.name).filter(category=work.category)
    note.delete()
    return reverse_lazy('workposted')
