from django.shortcuts import render, redirect
from blog.models import *
from blog.forms import Link
from django.conf import settings
from django.core.mail import send_mail

def products_list(request):
    form = Link()
    products = Product.objects.all()
    return render(request, 'blog/index.html', context={'products': products,'form': form})

def send_message(request):
    def Mail():
        if request.method == 'POST':
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            message = request.POST.get('message', '')
            send_mail(name,name + ' ' + email + ' ' + message + ' ', settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER],fail_silently=False)

    m = Mail()
    return redirect('thanks_url')

def product_detail(request,slug):
    product = Product.objects.get(slug__iexact=slug)
    return render(request,'blog/product_detail.html',context={'product': product})

def thanks(request):
    return render(request,'blog/thanks.html')

def gallery(request):
    images = Image.objects.all()
    img_list = []
    for image in images:
        img_list.append(image.pic.url)
    return render(request,'blog/gallery.html',context={'images': img_list})

def about(request):
    about = About.objects.first()
    return render(request,'blog/about.html',context={'about': about})












# def tags_list(request):
#     tags = Tag.objects.all()
#     return render(request,'blog/thanks.html', context={'tags': tags})
#
# # def tag_detail(request, slug):
# #     tag = Tag.objects.get(slug__iexact=slug)
# #     return render(request,'blog/tag_detail.html',context={'tag': tag})
#
# class TagDetail(View):
#     def get(self, request, slug):
#         # tag = Tag.objects.get(slug__iexact=slug)
#         tag = get_object_or_404(Tag, slug__iexact=slug)
#         return render(request, 'blog/tag_detail.html', context={'tag': tag})
#
# # def post_detail(request, slug):
# #     post = Post.objects.get(slug__iexact=slug)
# #     return render(request, 'blog/product_detail.html', context={'post': post})
#
# class PostDetail(View):
#     def get(self,request,slug):
#         # post = Post.objects.get(slug__iexact=slug)
#         post = get_object_or_404(Post,slug__iexact=slug)
#         return render(request, 'blog/product_detail.html', context={'post': post})
