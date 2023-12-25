from django.shortcuts import render
from .models import emp

def home(request):
    return render(request, 'home.html')

def get_staff_details(request):
    if request.method == 'POST':
        staff_id = request.POST.get('staffId')  # Use get() instead of indexing

        try:
            staff_details = emp.objects.get(staffid=staff_id)
            return render(request, 'staff_detail.html', {'staff_details': [staff_details]})
        except emp.DoesNotExist:
            return render(request, 'staff_detail.html', {'staff_details': None})
    else:
        return render(request, 'staff_detail.html', {'staff_details': None})
