from django.shortcuts import render, get_object_or_404, redirect
from .models import Order
from .forms import Order_form

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'helperserver/order_list.html', {'orders': orders})

def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'helperserver/order_details.html', {'order': order})

def create_new_order(request):
    if request.method == 'POST':
        form = Order_form(request.POST)
        if form.is_valid():
            new_order = form.save(commit=False)
            new_order.master_name = request.user
            new_order.save()
            return redirect('order_detail', pk=new_order.pk)
    else:
        form = Order_form()
    return render(request, 'helperserver/order_editor.html', {'form': form})