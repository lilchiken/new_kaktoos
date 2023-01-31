from django.urls import path

from recension import views

app_name = 'recension'

urlpatterns = [
    path(
        '',
        views.index,
        name='main'
    ),
    path(
        'rec/<int:rec_id>',
        views.single,
        name='single'
    )
]
