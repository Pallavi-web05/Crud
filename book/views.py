from turtle import title
from urllib import request
from django.shortcuts import redirect, render
from book.models import Book

# Create your views here.
def Login(request):
    return render(request,'login.html')

def Select(request):
    return render(request,'select.html')

def Showbook(request):
    a = Book.objects.all()
    return render(request,'view.html',{'user':a})

def Add(request):
    return render(request,'add.html')

def Addbook(request):
    if request.method == 'POST':

        Book_id = request.POST['book_id']
        Tittle = request.POST['tittle']
        Author = request.POST['author']
        Price = request.POST['price']
        Edition = request.POST['edition']
        Publication = request.POST['publication']

        bk = Book.objects.create(book_id = Book_id,
                                tittle = Tittle,
                                author = Author,
                                price = Price,
                                edition = Edition,
                                publication = Publication
        )
    return redirect ("add")

def Deletebook(request):
     a = Book.objects.all()
     return render(request,'delete.html',{'user':a})

def Delete(request,id):
    b = Book.objects.get(id=id)
    b.delete()
    return redirect("deletebook")

def Edit(request):
    d = Book.objects.all()
    return render(request,'update.html',{'user':d})

def Editpage(request,pk):
    c = Book.objects.get(id=pk)
    return render(request,'update.html',{'user':c})
    #return redirect('editbook')

# def Update(request,id):
#     udata = Book.objects.get(id=id)
#     udata.book_id = request.POST['book_id']
#     udata.tittle = request.POST['tittle']
#     udata.author = request.POST['author']
#     udata.price = request.POST['price']
#     udata.edition = request.POST['edition']
#     udata.publication = request.POST['publication']
#     udata.save()
#     return redirect('editbook')


def Update(request,id):
    e = Book.objects.filter(id=id)
    if e.count() > 0:
        e.update(
            book_id = request.POST['book_id'], 
            tittle = request.POST['tittle'], 
            author = request.POST['author'], 
            price = request.POST['price'], 
            edition = request.POST['edition'], 
            publication = request.POST['publication'],  
        )
    return redirect('editbook')




     

    