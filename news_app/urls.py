from django.urls import path
from .views import news_list, news_detail, ContactPageView, HomePageView, \
    CountryNewsView, WorldNewsView, EconomyNewsView, SoceityNewsView, \
    TexnologyNewsView, SportNewsView, PointNewsView, NewsDeleteView, \
    NewsUpdateView, NewsCreateView, admin_page_view, SearchResultsList


urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('news/', news_list, name='all_news_list'),
    path('news/create/', NewsCreateView.as_view(), name='news_create'),
    path('news/<slug:news>/', news_detail, name='news_detail_page'),
    path('news/<slug>/edit/', NewsUpdateView.as_view(), name='news_update'),
    path('news/<slug>/delete', NewsDeleteView.as_view(), name='news_delete'),
    path('contact-us/', ContactPageView.as_view(), name='contact_page'),
    path('country/', CountryNewsView.as_view(), name='country_news_page'),
    path('world/', WorldNewsView.as_view(), name='world_news_page'),
    path('economy/', EconomyNewsView.as_view(), name='economy_news_page'),
    path('soceity/', SoceityNewsView.as_view(), name='soceity_news_page'),
    path('texnology/', TexnologyNewsView.as_view(), name='texnology_news_page'),
    path('sport/', SportNewsView.as_view(), name='sport_news_page'),
    path('point/', PointNewsView.as_view(), name='point_news_page'),
    path('adminpage/', admin_page_view, name='admin_page'),
    path('searchresult/', SearchResultsList.as_view(), name='search_results'),
]