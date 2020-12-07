import csv

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .filters import SampleFilter
from .forms import CommentForm
from .models import Sample


# Create your views here.
def index(request):
    context = {}
    if request.user:
        context['user'] = request.user

    return render(request, 'malsearch/landing.html', context)


@login_required
def dashboard(request):
    context = {}
    return render(request, 'malsearch/dash_home.html', context)


@login_required
def search(request):
    context = {}

    q = request.GET.get('q', '')
    matches = Sample.objects.filter(Q(hash_md5__startswith=q) | Q(hash_sha1__startswith=q) | Q(hash_sha256__startswith=q))

    paginator = Paginator(matches, 25)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)

    context['result_page'] = page_obj

    return render(request, 'malsearch/dash_search.html', context)


@login_required
def sample_detail(request, sample_id):
    sample = get_object_or_404(Sample, sample_id=sample_id)
    try:
        latest_comment = sample.comments.order_by('-datetime_created')[0]
        comment = latest_comment.comment
    except IndexError as e:
        comment = ""

    # comment_form = CommentForm(initial={'user_id': request.user.id, 'comment': comment})
    return render(request, 'malsearch/sample_detail.html', {'sample': sample, 'scans': sample.scan_results.all(), 'comment': comment})


@login_required
def sample_detail_comment_update(request, sample_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(status=201)

    return


@login_required
def sample_detail_export(request, sample_id):
    sample = get_object_or_404(Sample, sample_id=sample_id)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{sample.sample_id}-report.csv"'

    fields = ['sample_id', 'file_name', 'file_path', 'hash_md5', 'hash_sha1', 'hash_sha256', 'date_added', 'last_scanned', 'file_size']
    values = [sample.__getattribute__(fn) for fn in fields]

    writer = csv.writer(response)
    writer.writerow(fields)
    writer.writerow(values)

    return response


@login_required
def advanced_search(request):
    f = SampleFilter(request.GET, queryset=Sample.objects.all())

    paginator = Paginator(f.qs, 25)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)

    return render(request, 'malsearch/advanced_search.html', {'filter': f, 'results': page_obj})
