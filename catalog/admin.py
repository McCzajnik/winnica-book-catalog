from django.contrib import admin

from .models import Book, Author, Translator, Category, Language, BookInstance
from .models import Regal


#----------------------------------------
#BOOK
#----------------------------------------

#admin.site.register(Book)

class BookAdmin(admin.ModelAdmin):
	list_display=('title', 'display_author', 'display_category', 'display_language')

admin.site.register(Book,BookAdmin)


#---------------------------------------
#BOOK INSTANCE
#---------------------------------------

admin.site.register(BookInstance)

#------------------------------------
#AUTHOR
#-----------------------------------

admin.site.register(Author)
admin.site.register(Regal)
admin.site.register(Category)
admin.site.register(Translator)
admin.site.register(Language)
# Register your models here.
