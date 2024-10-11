from django.contrib import admin

from .models import Article, Tag, Scope



from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            if form.cleaned_data != {}:
                if form.cleaned_data['is_main'] == True:
                    count += 1
        if count == 0:
            raise ValidationError('Нет ни одной галочки')
        elif count > 1:
            raise ValidationError('Галочек больше чем одна')
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
            # raise ValidationError('Тут всегда ошибка')
        return super().clean()  # вызываем базовый код переопределяемого метода


# class RelationshipInline(admin.TabularInline):
#     model = Relationship
#     formset = RelationshipInlineFormset


# @admin.register(Object)
# class ObjectAdmin(admin.ModelAdmin):
#     inlines = [RelationshipInline]





class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 3
    formset = ScopeInlineFormset # 1


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'published_at', 'image']
    inlines = [ScopeInline,]





