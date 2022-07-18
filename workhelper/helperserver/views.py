from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from django.db.models import F

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'helperserver/order_list.html', {'orders': orders})


def order_detail(request, pk):

    order = get_object_or_404(Order, pk=pk)
    work = Work.objects.filter(order__pk=pk)
    parts = Spare_parts.objects.filter(order__pk=pk)
    F_work_form = False
    F_parts_form = False
    work_form = Work_form()
    parts_form = Spare_parts_form()
    if request.method == 'POST':

        if request.POST.get('delete_button'):
            return delete_order(request, pk)

        if request.POST.get('add_work_button'):
            F_work_form = True

        if request.POST.get('save_work_button'):
            print('work!')
            work_form = Work_form(request.POST)
            if work_form.is_valid():
                new_work = work_form.save(commit=False)
                new_work.order = order
                new_work.save()
                F_work_form = False

        if request.POST.get('add_parts_button'):
            F_parts_form = True

        if request.POST.get('save_part_button'):
            parts_form = Spare_parts_form(request.POST)
            if parts_form.is_valid():
                new_part = parts_form.save(commit=False)
                new_part.order = order
                new_part.save()
                F_parts_form = False

    return render(request, 'helperserver/order_details.html',
                  {
                    'order': order,
                    'work': work,
                    'parts': parts,
                    'F_work_form': F_work_form,
                    'work_form': work_form,
                    'F_parts_form': F_parts_form,
                    'parts_form': parts_form

                   }
                  )


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


def delete_order(request, pk):
    order = Order.objects.get(pk=pk)
    order.delete()
    return render(request, 'helperserver/has_deleted_page.html')