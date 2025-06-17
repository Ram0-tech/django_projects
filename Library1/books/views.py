from django.shortcuts import render, redirect

from books.forms import AddbookForm


def home(request):
    return render(request, 'home.html')


def add_books(request):
    if request.method == 'POST':
        # print(request.POST)
        # print(request.FILES)
        form_instance = AddbookForm(request.POST, request.FILES)

        if form_instance.is_valid():
            #     # data=form_instance.cleaned_data
            #     # print(data)
            #     # t=data['title']
            #     # a=data['author']
            #     # p = data['price']
            #     # pa = data['pages']
            #     # l=data['language']
            #     # b = Book.objects.create(title=t, author=a, price=p, pages=pa, language=l)
            # b = Book.objects.create(title=form_instance.cleaned_data['title'],
            #                         author=form_instance.cleaned_data['author'],
            #                         price=form_instance.cleaned_data['price'],
            #                         pages=form_instance.cleaned_data['pages'],
            #                         language=form_instance.cleaned_data['language'],
            #                         image=form_instance.cleaned_data['image'])
            # b.save()
            form_instance.save()
        return redirect('books:view')
        # return render(request,'add_books.html')

    form_instance = AddbookForm()
    return render(request, 'add_books.html', {'forms': form_instance})


from books.models import Book


# user defined form
def add_books1(request):
    if request.method == 'POST':
        # print(request.POST)
        # print(request.FILES)
        t = request.POST['t']
        a = request.POST['a']
        p = request.POST['p']
        pa = request.POST['pa']
        l = request.POST['l']
        i = request.FILES['i']
        b = Book.objects.create(title=t, author=a, price=p, pages=pa, language=l, image=i)
        b.save()
        # return render(request,'add_books1.html')
        return redirect('books:view')
    return render(request, 'add_books1.html')


def view_book(request):
    b = Book.objects.all()
    print(b)
    return render(request, 'view_book.html', {'book': b})


def detail(request, i):
    b = Book.objects.get(id=i)
    return render(request, 'detail.html', {'book': b})


def edit(request, i):
    b = Book.objects.get(id=i)
    if request.method == 'POST':
        form_instance = AddbookForm(request.POST, request.FILES, instance=b)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('books:view')
    form_instance = AddbookForm(instance=b)
    return render(request, 'edit.html', {'forms': form_instance})


def delete(request, i):
    Book.objects.get(id=i).delete()
    return redirect('books:view')


from django.db.models import Q


def search(request):
    if request.method == 'POST':
        data = request.POST['s']
        print(data)
        b = Book.objects.filter(Q(title__icontains=data) | Q(author__icontains=data) | Q(language__icontains=data))
        #lookups--> (filename__lookup)
        print(b)
    return render(request, 'search.html',{'book':b})
