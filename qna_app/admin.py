from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import *
# Register your models here.

class QnAAdmin(SummernoteModelAdmin):
    summernote_fields = ('question_text')

class AnswerAdmin(SummernoteModelAdmin):
    summernote_fields= ('solution')

admin.site.register(Questions, QnAAdmin)
admin.site.register(Answers, AnswerAdmin)



