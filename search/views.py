from itertools import chain
from django.views.generic import ListView

from django.db.models import Q

from baptisms.models import Baptisms
from churchs.models import Churchs
from members.models import Members
from ministries.models import Ministries
from sacraments.models import Sacraments

# search views
class SearchView(ListView):
    template_name = 'search/search_view.html'
    paginate_by = 20
    count = 0
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['count'] = self.count or 0
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)
        
        if query is not None:
            baptisms_results  = Baptisms.objects.search(query)
            churchs_results = Churchs.objects.search(query)
            members_results = Members.objects.search(query)
            ministries_results = Ministries.objects.search(query)
            sacraments_results = Sacraments.objects.search(query)
            
            # combine querysets 
            queryset_chain = chain(
                    baptisms_results,
                    members_results,
                    ministries_results,
                    sacraments_results,
                    churchs_results
            )        
            qs = sorted(queryset_chain, 
                        key=lambda instance: instance.pk, 
                        reverse=True)
            self.count = len(qs) # since qs is actually a list
            return qs
        return Churchs.objects.none() # just an empty queryset as default
