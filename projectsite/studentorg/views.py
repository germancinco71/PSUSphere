from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from studentorg.models import Organization, OrgMember, Student, College, Program
from studentorg.forms import OrganizationForm, OrgMemberForm, StudentForm, CollegeForm, ProgramForm
from django.urls import reverse_lazy

class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = 'home.html'
    
class OrganizationList(ListView):
    model = Organization
    context_object_name = 'organization'
    template_name = 'org_list.html'
    paginate_by = 5
    
class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('organization-list')
    
class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('organization-list')
    
class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = 'org_del.html'
    success_url = reverse_lazy('organization-list')

class OrgMemberList(ListView):
    model = OrgMember
    context_object_name = 'orgmember'
    template_name = 'orgmember_list.html'
    paginate_by = 5
    
class OrgMemberCreateView(CreateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'orgmember_form.html'
    success_url = reverse_lazy('orgmember-list')
    
class OrgMemberUpdateView(UpdateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'orgmember_form.html'
    success_url = reverse_lazy('orgmember-list')

class OrgMemberDeleteView(DeleteView):
    model = OrgMember
    template_name = 'orgmember_del.html'
    success_url = reverse_lazy('orgmember-list')
    
class StudentList(ListView):
    model = Student
    context_object_name = 'student'
    template_name = 'stud_list.html'
    paginate_by = 5
    
class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'stud_form.html'
    success_url = reverse_lazy('student-list')
    
class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'stud_form.html'
    success_url = reverse_lazy('student-list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'stud_del.html'
    success_url = reverse_lazy('student-list')
    
class CollegeList(ListView):
    model = College
    context_object_name = 'college'
    template_name = 'col_list.html'
    paginate_by = 5
    
class CollegeCreateView(CreateView):
    model = College
    form_class = CollegeForm
    template_name = 'col_form.html'
    success_url = reverse_lazy('college-list')
    
class CollegeUpdateView(UpdateView):
    model = College
    form_class = CollegeForm
    template_name = 'col_form.html'
    success_url = reverse_lazy('college-list')
    
class CollegeDeleteView(DeleteView):
    model = College
    template_name = 'col_del.html'
    success_url = reverse_lazy('college-list')
    
class ProgramList(ListView):
    model = Program
    context_object_name = 'program'
    template_name = 'prog_list.html'
    paginate_by = 5
    
class ProgramCreateView(CreateView):
    model = Program
    form_class = ProgramForm
    template_name = 'prog_form.html'
    success_url = reverse_lazy('program-list')
    
class ProgramUpdateView(UpdateView):
    model = Program
    form_class = ProgramForm
    template_name = 'prog_form.html'
    success_url = reverse_lazy('program-list')
    
class ProgramDeleteView(DeleteView):
    model = Program
    template_name = 'prog_del.html'
    success_url = reverse_lazy('program-list')