from django import forms
from apps.appDirection.students.models import Student

class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = [
			'matricula',
			'nombre',
			'carrera',
			'especialidad',
			'cuatrimestre',
			'grupo',
		]

		labels = {
			'matricula': 'Matrícula',
			'nombre': 'Nombre',
			'carrera': 'Carrera',
			'especialidad': 'Especialidad',
			'cuatrimestre': 'Cuatrimestre',
			'grupo': 'Grupo',
		}

		widgets = {
			'matricula': forms.TextInput(attrs={'class':'form-control'}),
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'carrera': forms.TextInput(attrs={'class':'form-control'}),
			'especialidad': forms.TextInput(attrs={'class':'form-control'}),
			'cuatrimestre': forms.TextInput(attrs={'class':'form-control'}),
			'grupo': forms.TextInput(attrs={'class':'form-control'}),
		}