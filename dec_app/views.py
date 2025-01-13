import logging
from django.shortcuts import render
from django.core.paginator import Paginator
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

from .filters import WorkFilter
# Create your views here.
from .forms import Staff_form, WorkDetailsForm, Party_form
from .models import Work_Details, Staff, Party


logger = logging.getLogger('django')

def homepage(request):
    return render(request, 'index.html')


def loginpage(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('uname')
            password = request.POST.get('pass')
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_staff:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.info(request, 'Invalid Credentials')
    except Exception as e:
        # Log the error with traceback information
        logger.error(f"An error occurred in loginpage: {str(e)}", exc_info=True)
        messages.error(request, f"An error occurred: {str(e)}")
    return render(request, 'auth/authentication-login.html')

def userpage(request):
    return render(request, 'admintemp/index.html')

def view_details(request):
    try:
        data = Work_Details.objects.all().order_by('id')
        workfilter = WorkFilter(request.GET, queryset=data)
        data = workfilter.qs

        # Pagination
        paginator = Paginator(data, 10)  # Show 10 items per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'admintemp/details.html', {'data': page_obj,'workfilter':workfilter})
    except Exception as e:
        logger.error(f"An error occurred while fetching work details: {e}")
        return render(request, 'admintemp/error.html', {'message': 'Unable to fetch work details at this time.'})

def single_detials(request,id):
    try:
        data = Work_Details.objects.get(id=id)
        return render(request, 'admintemp/single-details.html',{'data':data})
    except Exception as e:
        logger.error(f"An error occurred while fetching work details by Id: {e}")
        return render(request, 'admintemp/error.html', {'message': 'Unable to fetch work details by Id at this time.'})


@login_required(login_url='loginpage')
def add_details(request):
    form = WorkDetailsForm()
    if request.method == 'POST':
        form = WorkDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_details')
    return render(request, 'admintemp/add_details.html', {'form': form})



def details_edit(request,id):
    data = Work_Details.objects.get(id=id)
    form = WorkDetailsForm(instance = data)
    if request.method == 'POST':
        form1 = WorkDetailsForm(request.POST,instance =data)
        if form1.is_valid():
            form1.save()
            return redirect('view_details')
    return render(request, 'add_details_update.html', {'form': form})


# add staff

@login_required(login_url='loginpage')
def add_staff(request):
    form = Staff_form()
    if request.method == 'POST':
        form = Staff_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_staff')
    return render(request, 'admintemp/add_staff.html', {'form': form})

# view staff
def view_staff(request):
    try:
        # raise Exception("Testing error handling")
        data = Staff.objects.all()
        return render(request, 'admintemp/staffs.html', {'data': data})
    except Exception as e:
        logger.error(f"An error occurred while fetching staff data: {e}")
        return render(request, 'admintemp/error.html', {'message': 'Unable to fetch staff data at this time.'})


def delete_staff(request,id):
    data = Staff.objects.get(id=id)
    data.delete()
    return redirect("view_staff")




# ///////////   party   //////////////////////////////\/\/\/\/\/\/\/\/\/\
def add_party(request):
    form = Party_form()
    try:
        if request.method == 'POST':
            form = Party_form(request.POST)
            if form.is_valid():
                form.save()
                return redirect('parties')
        return render(request, 'admintemp/add_party.html', {'form': form})
    except Exception as e:
        logger.error(f"An error occurred while adding party: {e}")
        return render(request, 'admintemp/add_party.html', {'form': form,'error_message': 'An error occurred while adding the party. Please try again later.'})

# view staff
@login_required(login_url='loginpage')
def view_party(request):
    try:
        data = Party.objects.all().order_by('id')
        # Pagination
        paginator = Paginator(data, 10)  # Show 10 items per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'admintemp/parties.html', {'data': page_obj})
    except Exception as e:
        logger.error(f"An error occurred while fetching party data: {e}")
        return render(request, 'admintemp/error.html', {'message': 'Unable to fetch party data at this time.'})


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