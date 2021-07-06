from orders.models import Order
from django.shortcuts import redirect, render, get_object_or_404
from django.urls.base import reverse
from main.models import Vehicle
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def order_summary(request, slug):
    vehicle = get_object_or_404(Vehicle, slug=slug)
    if request.method=="POST":
        full_name = request.POST['fullname']
        source_addr = request.POST['address']
        source_state = request.POST['state']
        source_pincode = request.POST['pincode']
        dest_addr = request.POST['dest_address']
        dest_state = request.POST['dest_state']
        dest_pincode = request.POST['dest_pincode']
        phone = request.POST['phone']
        ord = Order.objects.create(user=request.user,full_name=full_name, 
                                    address1=source_addr, city=source_state, 
                                    post_code=source_pincode, dest_address1=dest_addr, 
                                    dest_city=dest_state, dest_post_code=dest_pincode, phone=phone,
                                    total_paid=0.0, order_key="COD")
        ord.save()
        return redirect('basket:confirmation', slug= slug)
    return render(request, 'basket/summary.html', {'vehicle': vehicle})

def confirmation(request, slug):
    return render(request, 'basket/confirmation.html')