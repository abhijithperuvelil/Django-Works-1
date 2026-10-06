from django.http import JsonResponse
from django.views import View

class About(View):
    def get(self, request):
        data = [{
            'id': 1,
            'full name': 'Arun',
            'Title': 'Engineer',
            'Dob': '01/10/2000',
            'Email': 'arun@gmail.com',
            'Contact': '93437384793',
            'Location': 'Kochi',
            'Github Url': 'https://github.com/abhijithperuvelil',
            'Linkedin Url': 'https://github.com/abhijithperuvelil'
        }]
        return JsonResponse(data, safe=False)
class Education(View):
    def get(self, request):
        data = {
            'id': 1,
            'institution': 'Sngce',
            'Course': 'B.Tech',
            'University': 'KTU',
            'Location': 'Kochi',
            'Start Year': '2022',
            'End Year': '2026',
            'Garde': 'A',
            'Description': 'Nill'
        }
        return JsonResponse(data, safe=False)
class Project(View):
    def get(self, request):
        data = [
            {
                'id': 1,
                'Project Name': 'Smart Energy Meter',
                'Description': 'For Reading Electrical Measurements Through Dashboard',
                'Technologies': 'Iot',
                'Duration': '1 Year',
                'Live Url': ''
            },
            {
                'id': 2,
                'Project Name': 'Smart Dustbin',
                'Description': 'Automatic Lid Opening and Closing',
                'Technologies': 'Arduino Nano',
                'Duration': '6 Months',
                'Live Url': ''
            }
        ]
        return JsonResponse(data, safe=False)