from django.shortcuts import render
from django.db import models
from django.db.models import Count
from django.db import connection
from django.core.cache import cache
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache


from members.models import Members
from churchs.models import Churchs
from baptisms.models import Baptisms
from sacraments.models import Sacraments
from ministries.models import Ministries

# Create your views here.
@login_required
@never_cache
def home(request):
    context = {
        'title': "Gestion de l'Eglise Lutherien Malgache",
    }
    return render(request, 'statistic/index.html', context)
    
@login_required
@never_cache
def homepage(request):
    members_count = Members.objects.count()
    
    pastor_count = Ministries.objects.filter(service='Pasteur').count()
    deacon_count = Ministries.objects.filter(service='Diacre').count()
    catechists_count = Ministries.objects.filter(service='Catéchiste').count()
    evangelists_count = Ministries.objects.filter(service="Evangeliste").count()
    theologians_count = Ministries.objects.filter(service="Théologien").count()
    servants_count =  Ministries.objects.filter(service='Berger').count()
    
#    with connection.cursor() as cursor:
#        cursor.execute("""
#            SELECT church_synod, COUNT(*) AS count
#            FROM churchs_churchs
#            GROUP BY church_synod
#        """)
#        synod_count = cursor.fetchall()

    def get_counts():
        synod_counts = cache.get('church_synod')
        if synod_counts is None:
            synod_counts = Churchs.objects.values('church_synod').annotate(count=Count('id'))
            cache.set('synod_count', synod_counts)
        return synod_counts
    
    synod_count = get_counts()
    
#   synod_count = Churchs.objects.values('church_synod').annotate(count=models.Count('id')).values('church_synod', 'count')
#   synod_count = Churchs.get_synod_counts()

    employees_count = Ministries.objects.count()
    sacraments_count = Sacraments.objects.count()
    baptisms_count = Baptisms.objects.count()
    
    churchs_count = Churchs.objects.filter(type_of='Eglise').count()
    schools_count = Churchs.objects.filter(type_of='Ecole').count()
    hospitals_count = Churchs.objects.filter(type_of='Hôpital').count()
    centers_count = Churchs.objects.filter(type_of='Centre').count()
    
    context = {
        'title': "Fiangonana Loterana Malagasy",
        'members_count': members_count,
        'pastor_count': pastor_count,
        'deacon_count': deacon_count,
        'synod_count': synod_count,
        'sacraments_count': sacraments_count,
        'baptisms_count': baptisms_count,
        'catechists_count': catechists_count,
        'evangelists_count': evangelists_count,
        'theologians_count': theologians_count,
        'servants_count': servants_count,
        'churchs_count': churchs_count,
        'schools_count': schools_count,
        'hospitals_count': hospitals_count,
        'centers_count': centers_count,
        'employees_count': employees_count
    }
    
    return render(request, 'statistic/home.html', context) 