from django.shortcuts import render,redirect
from music_app.models import Song, Video,RelatedSimilar,Mostwatch
from music_app.forms import LoginForm
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.db import transaction

from django.contrib.auth import login as auth_login

from music_app.forms import SongForm,VideoForm



from django.http import HttpResponse,JsonResponse
# Create your views here.


def landing_page(request, template_name='music_temp/play_music.html'):
    data = 'listpage'
    music = Song.objects.all()



    return render(request, template_name, locals()) 


def play_video(request,template_name='music_temp/video_list.html'):
    video =  Video.objects.all()

    video = Video.objects.all()
    relatedsimilar = RelatedSimilar.objects.all()
    mostwatch = Mostwatch.objects.all()

    return render(request,template_name,locals())




def play_music(request, pk, template_name="music_temp/play_music.html"):
    data = 'playsong'
    music = Song.objects.get(id=pk)
    music_list = Song.objects.all()

    return render(request, template_name, locals())




def login_page(request,template_name="login/login_input.html"):
    if request.method == "POST":
        print(request.POST)
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        print(user_name,password,"views")

        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=user_name, password=password)
            if user is not None:
                login(request, user)
                if user.is_superuser:
                    print('it is super user')
                    success_url = reverse('admin_all_list')
                    return HttpResponseRedirect(success_url)

    else:    
        form = LoginForm()

    return render(request, template_name, locals())    


def second_login_(request,template_name="login/none.html"):
    # if request.is_ajax and request.method == 'GET':
    user_name = request.GET.get('username')
    password = request.GET.get('password')

    if user_name and password:
        user = authenticate(username=user_name, password=password)
        if user:
            result = login(request, user)
            # if user.is_superuser:
            #     # print(request.user.is_authenticated)
            #     # print(request.user)
            #     # print(user.is_superuser,'is_superuser')
            #     success_url = reverse('success_login')
            #     return HttpResponseRedirect(success_url)
            print(user,"oooo")
            data = result
    return render(request, template_name, locals())      
     


def logout_view(request):
    logout(request)
    success_url = reverse('landing_page')
    return HttpResponseRedirect(success_url)



       
def admin_all_list(request, template_name="admin/admin_list_page.html"):
    if not request.user.is_superuser == True:
        print(request.user.is_superuser)
        return render(request, '404.html')
    music = Song.objects.all()

    return render(request, template_name, locals())



def add_song(request,template_name='admin/add_song.html'):

    if not request.user.is_superuser == True:
        print(request.user.is_superuser)
        return render(request, '404.html')
    success_url = reverse('admin_all_list')
    song_qs = Song.objects.all()
    # cat_slug_list=[]
    # for cat in song_qs:
    #     cat_slug_list.append(cat.slug)
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        form = SongForm(request.POST,request.FILES)
        if form.is_valid():
            with transaction.atomic():
                form.save()
                # else:
                #     messages.error(request,"Category Already Exist ")
            return HttpResponseRedirect(success_url)
      
    else:
        form = SongForm()
    context = {'song_qs':song_qs,'form':form,'title':"Add Song"}
    return render(request, template_name,context )




def edit_song(request,pk,template_name='admin/add_song.html'):
    if not request.user.is_superuser == True:
        return render(request, '404.html')

    success_url = reverse('admin_all_list')
    instance = Song.objects.get(pk=pk)
    if request.method == "POST":
        form = SongForm(request.POST,request.FILES, instance=instance)
        if form.is_valid():
            with transaction.atomic():
                form.save()
            return HttpResponseRedirect(success_url)
    else:
        form = SongForm(instance=instance)
    context = {'form':form,'title':"Update Song"}
    return render(request, template_name,context )


def initial_delete(request, pk,template_name="admin/confirm_delete.html"):
    if not request.user.is_superuser == True:
        return render(request, '404.html')

    data = Song.objects.get(pk=pk)  
    return render(request,template_name, locals())



def delete_song(request,pk):
    if not request.user.is_superuser == True:
        return render(request, '404.html')

    success_url = reverse('admin_all_list')
    instance = Song.objects.get(pk=pk)
    instance.delete()


    return HttpResponseRedirect(success_url)




def video_player(request,pk,template_name="video/video_player.html"):
    video = Video.objects.get(pk=pk)
    all_video = Video.objects.all()


    return render(request, template_name, locals())



def admin_all_video_list(request, template_name="admin/video_list_admin.html"):
    if not request.user.is_superuser == True:
        print(request.user.is_superuser)
        return render(request, '404.html')
    video = Video.objects.all()

    return render(request, template_name, locals())




def add_video(request,template_name='admin/add_video.html'):

    if not request.user.is_superuser == True:
        print(request.user.is_superuser)
        return render(request, '404.html')
    success_url = reverse('admin_all_video_list')
    song_qs = Video.objects.all()
    # cat_slug_list=[]
    # for cat in song_qs:
    #     cat_slug_list.append(cat.slug)
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        form = VideoForm(request.POST,request.FILES)
        if form.is_valid():
            with transaction.atomic():
                form.save()
                # else:
                #     messages.error(request,"Category Already Exist ")
            return HttpResponseRedirect(success_url)
      
    else:
        form = VideoForm()
    context = {'song_qs':song_qs,'form':form,'title':"Add Video"}
    return render(request, template_name,context )






def edit_video(request,pk,template_name='admin/add_video.html'):
    if not request.user.is_superuser == True:
        return render(request, '404.html')

    success_url = reverse('admin_all_video_list')
    instance = Video.objects.get(pk=pk)
    if request.method == "POST":
        form = VideoForm(request.POST,request.FILES, instance=instance)
        if form.is_valid():
            with transaction.atomic():
                form.save()
            return HttpResponseRedirect(success_url)
    else:
        form = VideoForm(instance=instance)
    context = {'form':form,'title':"Update Video"}
    return render(request, template_name,context )




def initial_delete_video(request, pk,template_name="admin/confirm_delete.html"):
    if not request.user.is_superuser == True:
        return render(request, '404.html')
    type_d = 'video'    
    data = Video.objects.get(pk=pk)  
    return render(request,template_name, locals())



def delete_video(request,pk):
    if not request.user.is_superuser == True:
        return render(request, '404.html')

    success_url = reverse('admin_all_video_list')
    instance = Video.objects.get(pk=pk)
    instance.delete()


    return HttpResponseRedirect(success_url)








#********************* SONGS AUTOCOMPLETE METHODS *******************************
def song_autocomplete(request):
    if request.is_ajax():
        q=request.GET.get('search')
        queryset = Song.objects.filter(title__icontains=q)
        songs = list(queryset[:100])
        # vendor_ids=[]
        # for vendor in songs:
        #     vendor_ids.append(vendor.id)

        result_list = []
        for song in songs:

            result_list.append({"label":song.title, "id":song.id})
        data = {
            'result_list': result_list,
        }

        return JsonResponse(data)




def search_song_submit(request, template_name="music_temp/play_music.html"):
    
    if request.method == "POST":
        try:
            data = 'playsong'
            song_id=request.POST['song_id']
            song_name=request.POST['q']
            music = Song.objects.get(id=int(song_id))
            music_list = Song.objects.all()
        except:
            success_url = reverse('landing_page')
            return HttpResponseRedirect(success_url)    


    else:
        success_url = reverse('landing_page')
        return HttpResponseRedirect(success_url)



    return render(request, template_name, locals())

#********************* VIDEO AUTOCOMPLETE METHODS *******************************

def video_autocomplete(request):
    if request.is_ajax():
        q=request.GET.get('search')
        queryset = Video.objects.filter(title__icontains=q)
        videos = list(queryset[:100])
        # vendor_ids=[]
        # for vendor in videos:
        #     vendor_ids.append(vendor.id)

        result_list = []
        for video in videos:

            result_list.append({"label":video.title, "id":video.id})
        data = {
            'result_list': result_list,
        }

        return JsonResponse(data)


def search_video_submit(request, template_name="video/video_player.html"):
    
    if request.method == "POST":
        try:
            video_id=request.POST['video_id']
            video_name=request.POST['q']
            video = Video.objects.get(pk=int(video_id))
            all_video = Video.objects.all()
            if not video_name:
                print('no id is there')

        except:
            success_url = reverse('play_video')
            return HttpResponseRedirect(success_url)
                

    else:
        success_url = reverse('play_video')
        return HttpResponseRedirect(success_url)



    return render(request, template_name, locals())


