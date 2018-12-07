from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views import View


class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        return HttpResponse('TO DO')
