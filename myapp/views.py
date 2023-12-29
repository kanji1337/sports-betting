from django.conf import settings
from django.http import JsonResponse
from django.views.generic import ListView
from .models import Item

class ItemsView(ListView):
    model = Item
    template_name = 'item_list.html'

    def get(self, request, *args, **kwargs):
        items = self.get_queryset()

        data = []
        for item in items:
            # Construct the URLs for the images
            image1_url = f"http://127.0.0.1:8000/media/{item.image1}"
            image2_url = f"http://127.0.0.1:8000/media/{item.image2}"


            # Include item in the response
            data.append({
                'id': item.id,
                'title1': item.title1,
                'title2': item.title2,
                'koef1': item.koef1,
                'koef2': item.koef2,
                'imageUrl1': image1_url,
                'imageUrl2': image2_url,
                'time': item.time,
            })

        return JsonResponse({'items': data})
