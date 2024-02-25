from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView

from .models import News, Category
from .forms import ContactForm

def news_list(request):
    # news_list =  News.objects.filter(status=News.Status.Published)
    news_list = News.published.all()
    context = {
        'news_list':news_list
    }
    return render(request, "news/news_list.html", context)

def news_detail(request, news):
    news = get_object_or_404(News, slug=news, status=News.Status.Published)
    context = {
        'news':news
    }

    return render(request, 'news/news_detail.html', context)

# def homePageView(request):
#     categories = Category.objects.all()
#     news_list = News.published.all().order_by('-publish_time')[:15]
#     local_news = News.published.all().filter(category__name="O'ZBEKISTON").order_by('-publish_time')[:5]
#     economy_news = News.published.all().filter(category__name="IQTISODIYOT").order_by('-publish_time')[:5]
#     texnology_news = News.published.filter(category__name="FAN-TEXNIKA").order_by('-publish_time')[:5]
#     sport_news = News.published.filter(category__name='SPORT').order_by('-publish_time')[:5]
#     context = {
#         'news_list':news_list,
#         'categories':categories,
#         'local_news':local_news,
#         'economy_news':economy_news,
#         'texnology_news':texnology_news,
#         'sport_news':sport_news
#     }
#
#     return render(request, 'news/home.html', context)

class HomePageView(ListView):
    model = News
    template_name = 'news/home.html'
    context_object_name = 'name'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['news_list'] = News.published.all().order_by('-publish_time')[:15]
        context['local_news'] = News.published.all().filter(category__name="JAMIYAT").order_by('-publish_time')[:5]
        context['economy_news'] = News.published.all().filter(category__name="IQTISODIYOT").order_by('-publish_time')[:5]
        context['texnology_news'] = News.published.filter(category__name="FAN-TEXNIKA").order_by('-publish_time')[:5]
        context['sport_news'] = News.published.filter(category__name='SPORT').order_by('-publish_time')[:5]

        return context


# def contactPageView(request):
#     form = ContactForm(request.POST)
#     if request.method == "POST" and form.is_valid():
#         form.save()
#         return HttpResponse("<h2> Biz bilan bilan bog'langaningiz uchun tashakkur!")
#     context = {
#         "form": form
#     }
#     return render(request, 'news/contact.html', context)

class ContactPageView(TemplateView):
    template_name = 'news/contact.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            'form': form
        }

        return render(request, 'news/contact.html', context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return HttpResponse("<h2> Biz bilan bog'langaningiz uchun rahmat!</h2>")
        context = {
            'form':form
        }
        return render(request, 'news/contact.html', context)

class CountryNewsView(ListView):
    model = News
    template_name = "news/country.html"
    context_object_name = "country_news"

    def get_queryset(self):
        news = self.model.published.all().filter(category__name="O'ZBEKISTON")
        return news

class WorldNewsView(ListView):
    model = News
    template_name = 'news/jahon.html'
    context_object_name = "jahon_yangiliklar"

    def get_queryset(self):
        news = self.model.published.all().filter(category__name="JOHON")
        return news

class EconomyNewsView(ListView):
    model = News
    template_name = 'news/iqtisodiyot.html'
    context_object_name = "iqtisodiyot_yangiliklar"

    def get_queryset(self):
        news = self.model.published.all().filter(category__name="IQTISODIYOT")
        return news

class SoceityNewsView(ListView):
    model = News
    template_name = 'news/jamiyat.html'
    context_object_name = "jamiyat_yangiliklar"

    def get_queryset(self):
        news = self.model.published.all().filter(category__name="JAMIYAT")
        return news

class TexnologyNewsView(ListView):
    model = News
    template_name = 'news/texnika.html'
    context_object_name = "texnologiya_yangiliklar"

    def get_queryset(self):
        news = self.model.published.all().filter(category__name="FAN-TEXNIKA")
        return news

class SportNewsView(ListView):
    model = News
    template_name = 'news/sport.html'
    context_object_name = "sport_yangiliklar"

    def get_queryset(self):
        news = self.model.published.all().filter(category__name="SPORT")
        return news

class PointNewsView(ListView):
    model = News
    template_name = 'news/nazar.html'
    context_object_name = "nazar_yangiliklar"

    def get_queryset(self):
        news = self.model.published.all().filter(category__name="NUQTAI NAZAR")
        return news
