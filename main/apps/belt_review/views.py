from django.shortcuts import render, redirect
from django.contrib import messages
from models import *
import bcrypt

# views fo login
def index(request):
    if 'current_user' not in request.session:
        request.session['current_user'] = 0
    if 'current_book' not in request.session:
        request.session['current_book'] = 0
    if 'current_id' not in request.session:
            request.session['current_id'] = 0
    return render(request, "book/index.html")


def register(request):
    errors = user.objects.registration_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
            print errors.iteritems()
        return redirect('/')
    else:
        #print request.POST['name']
        password = request.POST['password']
        pwd = bcrypt.hashpw(password.encode(), bcrypt.gensalt(8))
        user.objects.create(
            name=request.POST['name'], alias=request.POST['alias'], email=request.POST['email'], password=pwd)
        user_email = request.POST['email']
        request.session['current_user'] = request.POST['email']
        query = user.objects.get(email=user_email)
        #print query
        return redirect('/books')


def signIn(request):
    errors = user.objects.login_validator(request.POST)
    if len(errors):
        # print errors
        for tag, error in errors.iteritems():
            #print errors.iteritems()
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        user_email = request.POST['email']
        password = request.POST['password']
        query = user.objects.get(email=user_email)
        print query.id
        pwd = bcrypt.hashpw(password.encode(), query.password.encode())
        #checks password
        if pwd == query.password:
            request.session['current_user'] = request.POST['email']
            return redirect("/books")
        else:
            messages.error(request, 'Invalid email or password')
    return redirect("/")


def books(request):
    print "hello"
    count = book.objects.count()
    count
    books = book.objects.get(id=count)
    books1 = book.objects.get(id=count - 1)
    books2 = book.objects.get(id= count - 2)
    print books.review_id
   
    context = {
        "user": user.objects.get(email=request.session['current_user']),
        "books": book.objects.all(),
        "count": book.objects.count(),
        "recent": books,
        "recent1": books1,
        "recent2": books2,
    }
    return render(request, 'book/books.html', context)


def signOut(request):
    request.session.clear()
    return redirect('/')


#views for adding books
def add_books(request, num):
    print num
    context = {
        "num": num,
        "authors": author.objects.all(),
    }
    return render(request, "book/books_add.html", context)

def add(request, num):
    print "hello"
    if request.POST['authorDD'] == '':
        author_pick = request.POST['author']
    else: 
        author_pick = request.POST['authorDD']

    current_u = user.objects.get(id=num)
    current_a = author.objects.create(author=author_pick)
    current_b = book.objects.create(title=request.POST['title'], author_id=current_a)
    request.session['current_book'] = current_b.id
    review.objects.create(rating=int(request.POST['rating']), review=request.POST['review'], users_id=current_u, books_id=current_b)

    return redirect("/books/display")

def current_book(request, num):
    request.session['current_book'] = num
    return redirect("/books/display")

#views for editing books
def display_book(request):
    print request.session['current_user']
    current_book = request.session['current_book']
    current_b = book.objects.get(id=current_book)
    print current_b.title

    current_book = book.objects.filter(title=current_b.title)
    #print cool[3].id
    # current_r = review.objects.get(books_id=current_b)
    #print review.objects.all()

    context = {
        "user": user.objects.get(email=request.session['current_user']),
        "books": book.objects.get(id=current_book),
        "author": current_b.author_id,
        "reviews": review.objects.all(),
        "current_books": current_book,
    }
    return render(request, "book/books_review.html", context)


def add_review(request, uid, bid):
    print uid
    print bid
    current_u = user.objects.get(id=uid)
    current_b = book.objects.get(id=bid)
    # current_b = book.objects.create(title=bid.title, author_id=author.objects.get(id=bid))
    print current_b.title
    review.objects.create(rating=int(request.POST['rating']), review=request.POST['review'], users_id=current_u, books_id=current_b)

    return redirect("/books/display")

#views for user books
def user_info(request, num):
    print "hello"
    print num
    count = review.objects.count()
    user_reviews = review.objects.all()
    print user_reviews
    context = {
        "user": user.objects.get(id=num),
        "reviews": user_reviews,
        "count": count,
    }
    return render(request, "book/user.html", context)
