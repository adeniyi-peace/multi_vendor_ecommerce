from .saved_sessions import RecentlyViewed


def recently_viewed(request):
    return {"recently_viewed":RecentlyViewed(request)}
