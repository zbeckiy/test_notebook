import uuid

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Note
from .forms import NoteForm


@login_required
def note_list(request):
    notes = Note.objects.filter(author=request.user)
    return render(request, 'notes/note_list.html', {'notes': notes})


@login_required
def note_detail(request, pk):
    note = Note.objects.get(id=pk)
    return render(request, 'notes/note_detail.html', {'note': note})


@login_required
def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'notes/note_create.html', {'form': form})


@login_required
def note_delete(request, pk):
    note = Note.objects.get(pk=pk)
    note.delete()
    return redirect('note_list')


@login_required
def note_edit(request, pk):
    note = get_object_or_404(Note, pk=pk, author=request.user)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_detail', pk=pk)
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_edit.html', {'form': form})


@login_required
def generate_uuid(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.note_uuid = uuid.uuid4()
    note.is_accessible_by_uuid = True
    note.save()
    return redirect('note_detail_uuid', note_uuid=note.note_uuid)


@login_required
def delete_uuid(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.note_uuid = None
    note.save()
    return redirect('note_detail', pk=pk)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def note_detail_uuid(request, note_uuid):
    notes = get_object_or_404(Note, note_uuid=note_uuid)
    current_url = request.build_absolute_uri()
    if notes.is_accessible_by_uuid:
        return render(request, "notes/note_detail.html", {"note": notes, "current_url": current_url})
    return render(request, 'registration/register.html')
