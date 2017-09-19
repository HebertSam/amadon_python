from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if 'item_price' and 'total' and 'count' not in request.session:
        request.session['item_price'] = 0
        request.session['total'] = 0
        request.session['count'] = 0
    return render(request, 'shop/index.html')

def buy(request):
    
    price = {
        '10': 20,
        '11': 30,
        '12': 5,
        '13': 50
    }

    thing = request.POST['item']

    amount = int(request.POST['quantity'])
    print thing
    print amount

    request.session['item_price'] = price[thing] * amount

    request.session['total'] += request.session['item_price']

    request.session['count'] += amount

    print request.session['item_price']
    print request.session['total']
    print request.session['count']

    return redirect('/checkout')

def checkout(request):
    return render(request, 'shop/checkout.html')

def clear(request):
    request.session.clear()
    return redirect('/')