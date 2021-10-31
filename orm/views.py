from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from . models import Human


class IndexTemplate(View):
    template_name = 'index_orm.html'

    def get(self, request):
        humans = Human.objects.all()
        context = {
            'humans': humans
        }
        return render(request, self.template_name, context)



