from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from . models import Human


class IndexTemplate(View):
    template_name = 'index_orm.html'

    def get(self, request):
        humans = Human.objects.all()
        context = {
            'humans': humans
        }
        return render(request, self.template_name, context)


def delete_record(request, id):
    print(id)
    obj_list = Human.objects.filter(id=id)
    if not obj_list:
        return HttpResponse('Удаляемые данные не найдены')
    obj_list.delete()
    return redirect('/')
