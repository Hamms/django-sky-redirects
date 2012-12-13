
from django.contrib import admin
from sky_redirects.models import DomainRedirect, RegexPathRedirect


class DomainRedirectAdmin(admin.ModelAdmin):
    list_display = ('redirect_from','redirect_to', 'redirect_type')

    def redirect_from(self, obj):
        return obj.fqdn

admin.site.register(DomainRedirect, DomainRedirectAdmin)


class RegexPathRedirectAdmin(admin.ModelAdmin):
    list_display = ('redirect_from','to','redirect_type','ordering')
    ordering = ('ordering',)

    def to(self, obj):
        return '%s...' % obj.redirect_to[:63] if len(obj.redirect_to) > 63 else obj.redirect_to

admin.site.register(RegexPathRedirect, RegexPathRedirectAdmin)
