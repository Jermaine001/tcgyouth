from django.shortcuts import render, redirect, get_object_or_404
from .models import Member, AttendanceRecord
from django.utils import timezone

# Create your views here.
def member_list(request):
    members = Member.objects.filter(active=True)
    date = timezone.now().date()

    if request.method == 'POST':
        for member in members:
            status = request.POST.get(f'status_{member.id}')
            AttendanceRecord.objects.update_or_create(
                member=member,
                date=date,
                defaults={'status': status}
            )
        return redirect('attendance_report', date=date)

    return render(request, 'attendance/member_list.html', {'members': members, 'date': date})

def attendance_report(request, date):
    date = timezone.datetime.strptime(date, '%Y-%m-%d').date()
    attendance_records = AttendanceRecord.objects.filter(date=date)
    return render(request, 'attendance/attendance_report.html', {'attendance_records': attendance_records, 'date': date})