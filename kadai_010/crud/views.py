
from django.views.generic import DetailView
from .models import Product


#DetailViewクラスを継承したクラスを定義
class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
