from django.shortcuts import render, redirect, get_object_or_404

from .models import StudentInfo

from .forms import StudentInfoForm


# Create your views here.


def student_list(request):
    queryset = StudentInfo.objects.all()
    context = {
        'queryset': queryset
    }
    return render(request, 'student_list.html', context)


def create_student(request):
    if request.method == "POST":
        form = StudentInfoForm(request.POST or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect("student_list")
    else:
        form = StudentInfoForm()
    return render(request, 'student_form.html', {'form': form})


def update_student(request, id):
    obj = get_object_or_404(StudentInfo, pk=id)
    form = StudentInfoForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'student_form.html', {'form': form})


def delete_student(request, id):
    student = get_object_or_404(StudentInfo, pk=id)
    student.delete()
    return redirect("student_list")



