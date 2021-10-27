import csv
from datetime import datetime

from django.contrib import admin
from django.http import HttpResponse

from .models import Local, Produto

MDATA = datetime.now().strftime('%Y-%m-%d')


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'estoque',
        'estoque_minimo',
        'local',
    )
    search_fields = ('produto',)
    actions = ('export_as_csv', 'export_as_xlsx')

    class Media:
        js = (
            'https://code.jquery.com/jquery-3.3.1.min.js',
            '/static/js/estoque_admin.js'
        )

    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response[
            'Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field)
                                   for field in field_names])

        return response

  
@admin.register(Local)
class LocalAdmin(admin.ModelAdmin):
    list_display = ('__str__', )
    search_fields = ('local',)
