from django.contrib import admin
from core.models import Publisher,Category,Book,Author,Reviewer,Review
# Register your models here.
admin.site.register(Publisher)
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Review)
admin.site.register(Reviewer)