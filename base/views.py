from django.shortcuts import render
from .models import User,Profile,Author,Book,BlogPost,Tag
from django.core.exceptions import ObjectDoesNotExist


def Home(request):
    return render(request,'base/index.html')
    
def users(request):
    allUsers = User.objects.all()
    print(str(allUsers.query))
    context = {'allUsers':allUsers}
    return render(request,'base/users.html',context)
    
def UserProfile(request,pk):
    error =""
    try:
        users = User.objects.select_related('profile').get(id=pk)
        print(users)
    except User._meta.model.related.ObjectDoesNotExist:
        print("The profile related to this user does not exist.")
    context = {'error':error,'users':users}
    return render(request,'base/profile.html',context)

def author(request):
    authors = Author.objects.all()
    context = {'authors':authors}
    return render(request,'base/author.html',context)

def book(request,pk):
    authors = Author.objects.get(id=pk)
    print(authors)
    books = Book.objects.filter(author=authors)
    print(books)
    context = {'books':books}
    return render(request,'base/books.html',context)

def tags(request,pk):
    post = BlogPost.objects.get(id=pk)
    print(post)
    Tagss = Tag.objects.filter()
    return render(request,'base/tags.html')


def Posts(request):
    posts = BlogPost.objects.all()
    context = {'posts':posts}
    return render(request,'base/posts.html',context)


