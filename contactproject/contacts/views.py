from django.shortcuts import render
from .forms import ContactForm


def contact(request):

    if request.method == 'POST':

        form = ContactForm(request.POST)

        if form.is_valid():

            contact = form.save()

            return render(
                request,
                'contacts/thank_you.html',
                {'name': contact.full_name}
            )

    else:
        form = ContactForm()

    return render(
        request,
        'contacts/contact.html',
        {'form': form}
    )