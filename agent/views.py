from api.models import File, DataFile
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import logging

LOG_FILENAME = 'error.log'
logging.basicConfig(filename=LOG_FILENAME, level=logging.WARNING)


@csrf_exempt
def get_file(request):
    if request.method == 'POST':
        file_dict = request.FILES
        file = file_dict.get('file')
        if not file:
            logging.warning("Request has error: "
                            "file should be value of name 'file'")
            return HttpResponse('', status=400)
        file_obj = File.objects.create(name=file)
        data = []
        try:
            for line in file:
                x, y, z, i = line.decode('utf-8').split()
                data.append(DataFile(x=x, y=y, z=z, i=i, file_name=file_obj))
            DataFile.objects.bulk_create(data)
        except ValueError as e:
            logging.warning(f'Error in file {file}: {e}')
            file_obj.delete()
            return HttpResponse('', status=400)
    return HttpResponse('', status=200)
