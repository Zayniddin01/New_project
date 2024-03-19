from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView, CreateView
from hitcount.utils import get_hitcount_model
from hitcount.views import HitCountMixin

from news_project.custom_permissions import OnlyLoggedSuperUser
from .models import News, Category
from .forms import ContactForm, CommentForm

def news_list(request):
    # news_list =  News.objects.filter(status=News.Status.Published)
    news_list = News.published.all()
    context = {
        'news_list':news_list
    }
    return render(request, "news/news_list.html", context)

def news_detail(request, news):
    news = get_object_or_404(News, slug=news, status=News.Status.Published)
    context = {}
    #HitCount logikasi
    hit_count = get_hitcount_model().objects.get_for_object(news)
    hits = hit_count.hits
    hitcontext = context['hitcount'] = {'pk': hit_count.pk}
    hit_count_response = HitCountMixin.hit_count(request, hit_count)
    if hit_count_response.hit_counted:
        hits = hits + 1
        hitcontext['hit_counted'] = hit_count_response.hit_counted
        hitcontext['hit_message'] = hit_count_response.hit_message
        hitcontext['total_hits'] = hits



    comments = news.comments.filter(active=True)
    comment_count = comments.count()
    new_comment = None
    if request.method == 'POST':
        if request.user.is_authenticated:
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.news = news
                new_comment.user = request.user
                new_comment.save()
                comment_form = CommentForm
        else:
            return redirect('login')
    else:
        comment_form = CommentForm()
    context = {
        'news':news,
        'comments': comments,
        'comment_count': comment_count,
        'new_comment': new_comment,
        'comment_form': comment_form
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
        news = self.model.published.all().filter(category__name="JAHON")
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

class NewsUpdateView(OnlyLoggedSuperUser, UpdateView):
    model = News
    fields = ("title", "body", "image", "category", "status")
    template_name = 'crud/news_edit.html'

class NewsDeleteView(OnlyLoggedSuperUser, DeleteView):
    model = News
    template_name = "crud/news_delete.html"
    success_url = reverse_lazy('home_page')

class NewsCreateView(OnlyLoggedSuperUser, CreateView):
    model = News
    template_name = 'crud/news_create.html'
    fields = ('title', 'slug', 'body', 'image','category', 'status')
@login_required
@user_passes_test(lambda u:u.is_superuser)
def admin_page_view(request):
    admin_users = User.objects.filter(is_superuser=True)
    context = {
        'admin_users': admin_users
    }
    return render(request, 'pages/admin_page.html', context)

class SearchResultsList(ListView):
    model = News
    template_name = 'news/search_result.html'
    context_object_name = 'barcha_yangiliklar'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return News.objects.filter(
            Q(title__icontains=query) | Q(body__icontains=query)
        )
