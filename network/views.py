from django.http import HttpResponse


def my_view(request):
	if request.method == 'GET':
		param1 = request.GET.get('param1')
		param2 = request.GET.get('param2')

		return HttpResponse('Вы ввели: param1={}, param2={}'.format(param1, param2))
