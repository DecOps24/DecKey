from django.shortcuts import render

# Create your views here.


from django.shortcuts import render
from django.http import HttpResponse
from xhtml2pdf import pisa
from io import BytesIO
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect




# Create your views here.
from .forms import Staff_form, WorkDetailsForm, Party_form
from .models import Work_Details, Staff, Party


def homepage(request):
    return render(request, 'index.html')


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('userpage')
        else:
            messages.info(request, 'Invalid Credentials')
    return render(request, 'Login.html')


@login_required(login_url='loginpage')
def userpage(request):
    return render(request, 'userpage.html')


@login_required(login_url='loginpage')
def add_details(request):
    form = WorkDetailsForm()
    if request.method == 'POST':
        form = WorkDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('userpage')
    return render(request, 'add_details.html', {'form': form})


@login_required(login_url='loginpage')
def view_details(request):
    data = Work_Details.objects.all()
    return render(request, 'view_details.html', {'data': data})

# add staff

@login_required(login_url='loginpage')
def add_staff(request):
    form = Staff_form()
    if request.method == 'POST':
        form = Staff_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('userpage')
    return render(request, 'add_staff.html', {'form': form})

# view staff
@login_required(login_url='loginpage')
def view_staff(request):
    data = Staff.objects.all()
    return render(request, 'views_staff.html', {'data': data})






# ///////////   party   //////////////////////////////\/\/\/\/\/\/\/\/\/\
@login_required(login_url='loginpage')
def add_party(request):
    form = Party_form()
    if request.method == 'POST':
        form = Party_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_party')
    return render(request, 'add_party.html', {'form': form})

# view staff
@login_required(login_url='loginpage')
def view_party(request):
    data = Party.objects.all()
    return render(request, 'views_party.html', {'data': data})


@login_required(login_url='loginpage')
def download_bill(request, id):
    try:
        row = Work_Details.objects.get(id=id)
    except Work_Details.DoesNotExist:
        return HttpResponse("Record not found", status=404)

    # Render HTML page as a string with context
    html_content = render(request, 'bill_template.html', {'row': row})

    # Convert the rendered HTML to PDF using xhtml2pdf
    pdf_output = BytesIO()
    pisa_status = pisa.CreatePDF(html_content.content.decode('utf-8'), dest=pdf_output)

    # Return PDF as HTTP response
    if pisa_status.err:
        return HttpResponse("Error generating PDF", status=500)

    pdf_output.seek(0)
    response = HttpResponse(pdf_output, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="Bill_{row.id}.pdf"'
    return response


def logout_view(request):
    logout(request)
    return redirect('homepage')