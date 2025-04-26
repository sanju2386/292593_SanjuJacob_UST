from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import IncidentForm
from .models import Incident
from django.db.models import Count
 
# Create your views here.
 
def categorize_age(age):
    if age is None:
        return None
    elif age <= 12:
        return 'Children'
    elif age <= 25:
        return 'Young Adults'
    elif age <= 59:
        return 'Adults'
    else:
        return 'Seniors'
 
@login_required
def dashboard(request):
    # Incident type chart data
    data = Incident.objects.values('incident_type').annotate(count=Count('id'))
    labels = [d['incident_type'].capitalize() for d in data]
    counts = [d['count'] for d in data]
 
    # Age group pie chart data
    incidents = Incident.objects.all()
    age_groups = {'Children': 0, 'Young Adults': 0, 'Adults': 0, 'Seniors': 0}
 
    for incident in incidents:
        category = categorize_age(incident.age)
        if category:
            age_groups[category] += 1
 
    age_labels = list(age_groups.keys())
    age_counts = list(age_groups.values())
 
    context = {
        'labels': labels,
        'counts': counts,
        'age_labels': age_labels,
        'age_counts': age_counts,
    }
 
    return render(request, 'Navmain/dashboard.html', context=context)
 
@login_required
def incidents(request):
    if request.method == 'POST':
        form = IncidentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('incidents')
    else:
        form = IncidentForm()
    context = {
        'form': form
    }
    return render(request, 'Navmain/incidents.html', context=context)
 
@login_required
def customers(request):
    incidents = Incident.objects.all().order_by('timestamp')
    context = {
        "incidents": incidents
    }
    return render(request, 'Navmain/customers.html', context=context)
 
 
def about(request):
    return render(request, 'Navmain/about.html')