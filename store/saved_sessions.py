
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

    def __len__(self):
        return (len(self.recently_viewed))

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



class SavedProduct(object):
    def __init__(self, request):
        self.session = request.session
        saved_product = self.session.get("saved_product")

        if not saved_product:
            saved_product = self.session["saved_product"] = []
        
        self.saved_product = saved_product
        

    def items(self):
        return self.saved_product

    def add(self, pk):
        if pk not in self.saved_product:
            self.saved_product.insert(0, pk)
            self.save()


    def delete(self, pk):
        self.saved_product.remove(pk)
        self.save()

    def save(self):
        self.session["saved_product"] = self.saved_product
        self.session.modified = True