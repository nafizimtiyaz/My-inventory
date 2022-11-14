from django.shortcuts import render,redirect
from django.http import HttpResponse
from  django.contrib import messages
from .models import invent,billing


def home(request):
    obj=invent.objects.all()
    return render(request,'product-list.html',{'obj':obj})

def addqn(request,id):
    if request.method=='POST':
        qn=float(request.POST['addhml'])
        a=invent.objects.get(id=id)
        a.qutity=float(a.qutity)+qn
        a.save()
        return redirect('/')
    else:
        obj = invent.objects.get(id=id)
        return render(request, 'add-quantity.html', {'obj': obj})

def delete_record(request,id):
    remove=invent.objects.get(id=id)
    remove.delete()
    return redirect('/')

def create_product(request):
    if request.method=="POST":
        name=request.POST['pname']
        buying_price=request.POST['buying_price']
        qutity=request.POST['qutity']
        selling_price = request.POST['selling_price']
        id=None
        obj=invent(id,name=name,buying_price=buying_price,qutity=qutity,selling_price=selling_price)
        obj.save()
        return redirect('/')
    else:
        return render(request,'add-product.html')

def product_sale(request,id):
    a = invent.objects.get(id=id)
    if request.method=='POST':
        product_name=request.POST["product_name"]
        customer_name=request.POST["customer_name"]
        customer_mobile=request.POST["customer_mobile"]
        selling_price=eval(request.POST["selling_price"])
        buying_price=request.POST["buying_price"]
        amount=eval(request.POST["amount"])
        discount=eval(request.POST["discount"])
        total=request.POST["total"]
        if a.qutity>=amount:
            a.qutity=a.qutity-amount
            a.save()
            if a.qutity==0:
                a.delete()
            if discount == 0:
                total = selling_price * amount
                sale = billing(product_name=product_name, customer_name=customer_name, customer_mobile=customer_mobile,
                               selling_price=selling_price, buying_price=buying_price, amount=amount, discount=discount,
                               total=total)
                sale.save()
                return redirect('/')
            elif discount > 0:
                total1 = selling_price * amount
                total2 = total1* discount
                total3=total1-total2
                total="{:.2f}".format(total3)
                sale = billing(product_name=product_name, customer_name=customer_name, customer_mobile=customer_mobile,
                        selling_price=selling_price, buying_price=buying_price, amount=amount, discount=discount,total=total)
                sale.save()
                return redirect('/')
        else:
            return HttpResponse('<h1>Mother Fucker Out Of range!!</h1>')
    else:
        return render(request,'add-sale.html',{'a':a})

def sale_list(request):
    bill=billing.objects.all()
    return render(request,'sale-list.html',{'bill':bill})

def edit_product(request,id):
    if request.method == "POST":
        name = request.POST['pname']
        buying_price = request.POST['buying_price']
        qutity = request.POST['qutity']
        selling_price = request.POST['selling_price']
        x=invent.objects.get(id=id)
        x.name=name
        x.buying_price=buying_price
        x.qutity=qutity
        x.selling_price=selling_price
        x.save()
        return redirect('/')
    else:
        obj = invent.objects.get(id=id)
        return render(request, 'edit.html', {'obj': obj})