from django.contrib import admin
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType

from .models import Booking, Contact, Album, Artist

class AdminURLMinxin(object):

    def get_admin_url(self, obj):
        content_type = ContentType.objects.get_for_model(obj.__class__)
        return reverse("admin:store_%s_change" %
            (content_type.model),
            args=(obj.id,))

class BookingInline(admin.TabularInline, AdminURLMinxin):
    readonly_fields = ["created_at", "album_link", "contacted"]
    model = Booking
    fieldsets = [
        (None, {'fields': ['album_link', 'contacted']})
        ] #list columns
    extra = 0
    verbose_name = "Reservation"
    verbose_name_plural = "Reservation"

    def album_link(self, booking):
        url = self.get_admin_url(booking.album)
        return mark_safe("<a href='{}'>{}</a>".format(url, booking.album.title))

    album_link.short_description = "Album"

    def has_add_permission(self, request, a):
        return False

class AlbumArtistInline(admin.TabularInline):
    model = Album.artists.through
    extra = 1
    verbose_name = "Disque"
    verbose_name_plural = "Disques"

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    inlines = [BookingInline, ]


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    inlines = [AlbumArtistInline, ]

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    search_fields = ['reference' , 'title']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin, AdminURLMinxin):
    readonly_fields = ["created_at", "contact_link", "album_link"]
    fields = ["created_at", "album_link", "contacted"]
    # list_filter = ['created_at' , 'contacted']

    def contact_link(self, booking):
        url = self.get_admin_url(booking.contact)
        return mark_safe("<a href='{}'>{}</a>".format(url, booking.contact.name))

    def has_add_permission(self, request):
        return False

    def album_link(self, obj):
        # path = "admin:store_album_change"
        url = self.get_admin_url(obj.album)
        return mark_safe("<a href='{}'>{}</a>".format(url, obj.album.title))
