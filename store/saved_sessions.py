
from dashboard.models import Product

class RecentlyViewed(object):
    def __init__(self, request):
        self.session = request.session
        recently_viewed = self.session.get("recently_viewed")

        if not recently_viewed:
            recently_viewed = self.session["recently_viewed"] = []
        
        self.recently_viewed = recently_viewed
        

    def __iter__(self):
        for pk in self.recently_viewed:
            product = Product.objects.get(pk=pk)

            yield product

    def add(self, pk):
        if pk not in self.recently_viewed:
            self.recently_viewed.insert(0, pk)
            self.delete()
            self.save()

        else:
            self.recently_viewed.remove(pk)
            self.recently_viewed.insert(0, pk)
            self.save()


    def delete(self):
        if len(self.recently_viewed) > 20:
            self.recently_viewed.pop()

    def save(self):
        self.session["recently_viewed"] = self.recently_viewed
        self.session.modified = True