from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
import os
from django.urls import reverse
from .forms import image_form
from .Neural_Style_Transfer.style_transfer import style_transfer
from .models import image_container


def show_main_page(request):
    form = image_form()
    return render(request, 'Style_Transfer_Application/main_page.html',
                  {'form': form})


def upload_img(request):
    if request.method == 'POST':
        form = image_form(request.POST, request.FILES)
        if form.is_valid():
            image_container(img_content=request.FILES.get('img_content'),
                            img_style=request.FILES.get('img_style'))
            form.save()
            content_path = './media/images/' + str(request.FILES.get('img_content'))
            style_path = './media/images/' + str(request.FILES.get('img_style'))

            style_transfer(content_path,
                           style_path, 10)
            os.remove(content_path)
            os.remove(style_path)
            return HttpResponseRedirect(reverse('show_main_page', ))
        else:
            raise Http404("Wrong file format!!!")
    else:
        raise Http404("Wrong way!!!")


def download_img(request):
    FILE_PATH = './media/images/stylized-image.png'

    file = open(FILE_PATH, 'rb')
    response = HttpResponse(file.read(), content_type='Image')
    response['Content-Disposition'] = 'inline; filename=' + os.path.basename(FILE_PATH)
    return response
