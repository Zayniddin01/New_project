from modeltranslation.translator import register, TranslationOptions, translator
from .models import News, Category

class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'body',)

translator.register(News, NewsTranslationOptions)

class CategoryTranslationOption(TranslationOptions):
    fields = ('name',)

translator.register(Category, CategoryTranslationOption)