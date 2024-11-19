# myapp/views.py
from django.shortcuts import render
from .forms import StringForm

def string_input_view(request):
    result = None
    if request.method == 'POST':
        form = StringForm(request.POST)
        if form.is_valid():
            result = form.cleaned_data['input_string']  # รับค่าที่ผู้ใช้ป้อน
    else:
        form = StringForm()

    return render(request, 'string_input.html', {'form': form, 'result': result})

