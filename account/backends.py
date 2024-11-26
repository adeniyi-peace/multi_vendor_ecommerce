from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):

        UserModel = get_user_model()

        try:
            user = UserModel.objects.get(email=username)

        except UserModel.DoesNotExist:
            try:
                UserModel = get_user_model()
                user = UserModel.objects.get(username=username)
                print(user)

            except UserModel.DoesNotExist:
                return None
        
        
        if user.check_password(password) and self.user_can_authenticate(user):
            return user
            
        return None
