from stores import models


def stores(request):
    store = models.Store.objects.order_by('-id').first()

    return {
        'store': store
    }
