from django.shortcuts import render
from contact.models import Contact
from contact.forms import ContactInput
# Create your views here.
def contact(request):
    contact = Contact.objects.all()
    info = {
        "contact":contact,
    }
    return render(request, 'contact/contact.html', context=info)


def input_form(request):
    if request.method == 'POST':
        contact_input = ContactInput(request.POST)
        if contact_input.is_valid():
            print("This is post statement")
            print(contact_input.cleaned_data['password'])
            print(contact_input.cleaned_data['repassword'])
    contact_input = ContactInput()
    contact_input.order_fields(field_order=["name", 'email', 'phone', 'address'])
    return render(request, 'contact/form.html', {"contact_input": contact_input})