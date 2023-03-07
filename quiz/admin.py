from django.contrib import admin

from .models import SingleChoiceQuestion, MultiChoiceQuestion, TrueOrFalseQuestion, TextQuestion

# Register your models here.
admin.site.register(SingleChoiceQuestion)
admin.site.register(MultiChoiceQuestion)
admin.site.register(TrueOrFalseQuestion)
admin.site.register(TextQuestion)