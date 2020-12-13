import os

from django.http import FileResponse, HttpResponse
from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse

from DjangoDemo.settings import FileSave_DIR
from .models import filetb
from login.models import userLogin
from Utils.tools import save_file
# Create your views here.

def index(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = userLogin.objects.get(username=username, password=password)
        except userLogin.DoesNotExist:
            return render(request, "login.html", {'error_message': '登录失败！'})
        else:
            request.session['username'] = username
            return render(request, "index.html")
    return render(request, "index.html")
def searchfile(request):
    if request.POST:
        fname = request.POST.get('filename')
        if fname is None:
            files = filetb.objects.all()
        else:
            files = filetb.objects.filter(filename__contains = fname)
        pageCount = 10
        return render(request,"index.html",{'files':files,'pageCount':pageCount})
    return render(request,'index.html')

def addPage(request):
    return render(request, "house_edit.html")

def insertfile(request):        # 新增不能重名 ，更新直接替换重名
    if request.POST:
        file = request.FILES.get('addfile')
        fname = file.name
        username = request.session['username']
        user = userLogin.objects.get(username=username)
        if user is None:
            return render(request, 'login.html', {
                'error_message': '请先登录'
            })
        filepath = FileSave_DIR
        if filetb.objects.filter(filename=fname):
            return render(request, 'house_edit.html', {
                'error_message': '文件上传失败!,已有重名文件'
            })
        if file:
            filetb.objects.create(filename=fname,username=user,filepath=filepath)
            save_file(file, filepath)
            return HttpResponseRedirect(reverse('handlerfile:index'),{'successFlag':True})
        return render(request, 'house_edit.html', {
            'error_message': '文件上传失败!'
        })
    return render(request,'index.html')

def deletefile(request):        # 新增不能重名 ，更新直接替换重名
    if request.POST:
        filename = request.POST.get('filename')
        file = filetb.objects.get(filename=filename)
        if file:
            file.delete()
            if os.path.exists(os.path.join(FileSave_DIR, filename)):
                os.remove(os.path.join(FileSave_DIR, filename))
    return render(request,'index.html')

def downloadfile(request):
    if request.POST:
        filename = request.POST.get('filename')
        file = open(FileSave_DIR+"/"+filename, 'rb')
        response = FileResponse(file)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="'+filename+'"'
        return response
