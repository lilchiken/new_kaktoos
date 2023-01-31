from recension.models import Recension


def last_rec_film_title(request):
    rec = Recension.objects.first()
    try:
        if rec.film.title:
            return {'last_rec_film_title': rec.film.title}
    except:
        return {'last_rec_film_title': 'здесь типа фильм ну название ево'}


def last_rec_pub_date(request):
    rec = Recension.objects.first()
    return {'last_rec_pub_date': rec.pub_date}


def last_rec_id(request):
    rec = Recension.objects.first()
    return {'last_rec_id': rec.id}


def last_rec_small_text(request):
    rec = Recension.objects.first()
    return {'last_rec_small_text': rec.small_text}
