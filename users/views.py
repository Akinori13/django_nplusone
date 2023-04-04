from django.contrib.auth import get_user_model
from django.views.generic import ListView

User = get_user_model()


class UserListView(ListView):
    model = User
    template_name = "users/user_list.html"
    context_object_name = "users"
