from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect

from accounts.models import User
from lists.forms import ItemForm, ExistingListItemForm, NewListForm

from lists.models import Item, List


def home_page(request):
    return render(request, 'home.html', {'form': ItemForm()})


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    form = ExistingListItemForm(for_list=list_)
    if request.method == 'POST':
        form = ExistingListItemForm(for_list=list_, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_)
    return render(request, 'list.html', {
        'list': list_, 'form': form
    })


def new_list(request):
    form = NewListForm(data=request.POST)
    if form.is_valid():
        list_ = form.save(owner=request.user)
        return redirect(list_)
    return render(request, 'home.html', {'form': form})


def my_lists(request, user_email):
    owner = User.objects.get(email=user_email)

    return render(
        request,
        'my_lists.html',
        {'owner': owner}
    )


def share(request, list_id):
    user = User.objects.get(pk=request.POST.get('sharee'))
    list_ = List.objects.get(id=list_id)
    list_.shared_with.add(user)
    list_.save()
    return redirect(list_)
