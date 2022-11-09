from email import message
from django.shortcuts import render, redirect
from signup.models import *
import hashlib
from django.core.exceptions import ObjectDoesNotExist
from signup.models import *
from upload.models import *
import os
from django.conf import settings
from django.http import HttpResponse
from django.core import serializers
import json
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.

def index(request):
    if not 'user_id' in request.session.keys():
        return redirect('')
    user_id = request.session['user_id']
    user = User.objects.get(user_id = user_id)
    documents = Document.objects.filter(file_user=user)
    content = {'documents': documents}
    return render(request, 'main/index.html', content)

def loginView(request):
    return render(request, 'main/login.html')

def login(request):
    user_input_id = request.POST['loginID']
    user_input_pw = request.POST['loginPW']
    try:
        user = User.objects.get(user_id = user_input_id)
        encoded_userPW = user_input_pw.encode()
        encrypted_userPW = hashlib.sha256(encoded_userPW).hexdigest()

        if encrypted_userPW == user.user_pw:
            request.session['user_id'] = user.user_id
            request.session['user_name'] = user.user_name
            return redirect('main_index')
        else:
            return redirect('main_loginView')
    
    except ObjectDoesNotExist:
        message = 'Email does not exist.'
        return render(request, 'main/error.html', {"message": message})

    except:
        message = 'An unknown error occurred.'
        return render(request, 'main/error.html', {"message": message})

def logout(request):
    del request.session['user_id']
    del request.session['user_name']
    return redirect('main_loginView')

def download(request):
    path = request.GET['path']
    file_path = os.path.join(settings.MEDIA_ROOT, path)

    if os.path.exists(file_path):
        binary_file = open(file_path, 'rb')
        response = HttpResponse(binary_file.read(), content_type = "application/liquid; charset=utf-8")
        response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
        return response

    else:
        message = " An anknown error occured."
        return render(request, 'main/error.html',{"message": message})

def result(request):
    if 'user_name' in request.session.keys():
        content = {}
        content['grade_calculate_dic'] = request.session['grade_calculate_dic']
        content['email_domain_dic'] = request.session['email_domain_dic']
        del request.session['grade_calculate_dic']
        del request.session['email_domain_dic']
        return render(request, 'main/result.html', content)
    else:
        return redirect('main_login')

def showDaily(request):

    if 'show_daily_contents' in request.session.keys():
        contents = serializers.deserialize("json", request.session['show_daily_contents'],cls=DjangoJSONEncoder)
        del request.session['show_daily_contents']

        return render(request, 'main/show_daily.html', {'contents': contents})
    else:
        return redirect('main_login')

def resultDaily(request):

    if 'calculate_daily_contents' in request.session.keys():
        contents = serializers.deserialize("json", request.session['calculate_daily_contents'],cls=DjangoJSONEncoder)
        # contents_json = request.session['calculate_daily_contents']
        # contents = json.loads(contents_json)
        # print("contents dejson",contents )
        del request.session['calculate_daily_contents']

        return render(request, 'main/result_daily.html', {'contents': contents})
    else:
        return redirect('main_login')

