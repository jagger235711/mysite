from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Question, Choice


#
# # class QuestionAdmin(admin.ModelAdmin):
# #     fields = ["pub_date", "question_text"]
# class QuestionAdmin(admin.ModelAdmin):
#     # fieldsets元组中的第一个元素是字段集的标题
#     fieldsets = [
#         ("question", {"fields": ["question_text"]}),
#         ("Date information", {"fields": ["pub_date"]}),
#     ]
#
#
# # 创建一个模型后台类，接着将其作为第二个参数传给 admin.site.register() ——在你需要修改模型的后台管理选项时这么做。
#
# admin.site.register(Question, QuestionAdmin)

# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):  # TabularInline 放在一行里更紧凑
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]


admin.site.register(Question, QuestionAdmin)
