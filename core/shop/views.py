from django.shortcuts import render
from django.views import generic
from .models import Item, Category
from .filters import ItemFilter
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator
from cart.cart import Cart


def search(request):
    q = request.POST.get('search')
    q = q if q else '01234567890'
    items = Item.objects.filter(name__iregex=q)[:10]
    return render(request, 'search_box.html',{'s_items':items})

def filter(request):
    catg = request.POST.get('category_slug')
    qs = Item.objects.filter(category__slug=catg) if catg != '' else Item.objects.all()
    items = ItemFilter(request.POST, queryset=qs).qs

    paginator = Paginator(items, 20) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'item_list.html',{'items':items, 'page_obj': page_obj})

def messages(request):
    return render(request,'message.html')


class BaseItemsList(generic.ListView):
    model = Item
    context_object_name = 'items'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home | WaveMarket"
        context["categories"] = Category.objects.all() 
        context["filter"] = ItemFilter()
        return context
    
    def get_template_names(self):
        if self.request.htmx:
            return 'item_list.html'
            
        return 'items.html'


class ItemListView(BaseItemsList):
    pass

class CategoryListView(BaseItemsList):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = " ".join(self.kwargs['slug'].split("-")).capitalize() +" | WaveMarket"
        return context
     
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(category__slug=self.kwargs['slug'])

class TagsListView(BaseItemsList):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "#" + " ".join(self.kwargs['slug'].split("-")).capitalize() +" | WaveMarket"
        return context
    
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(tags__slug=self.kwargs['slug'])
    
    
class ItemDetailView(generic.DetailView):
    model = Item
    template_name = 'items_detail.html'
    context_object_name = 'items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = f" | WaveMarket"
        return context