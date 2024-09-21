from django.contrib import admin
from .models import CustomUser, AdminHOD, Staffs, Students, Courses, Subjects, SessionYearModel, Attendance, AttendanceReport, LeaveReportStudent, LeaveReportStaff, FeedBackStudent, FeedBackStaffs, NotificationStudent, NotificationStaffs, StudentResult

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(AdminHOD)
admin.site.register(Staffs)
admin.site.register(Students)
admin.site.register(Courses)
admin.site.register(Subjects)
admin.site.register(SessionYearModel)
admin.site.register(Attendance)
admin.site.register(AttendanceReport)
admin.site.register(LeaveReportStudent)
admin.site.register(LeaveReportStaff)
admin.site.register(FeedBackStudent)
admin.site.register(FeedBackStaffs)
admin.site.register(NotificationStudent)
admin.site.register(NotificationStaffs)
admin.site.register(StudentResult)
