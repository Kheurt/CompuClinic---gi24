from rest_framework import filters


class QuittanceFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        if request.query_params.get('patient') and request.query_params.get("est_consommee"):
            return ['patient', 'est_consommee']
        elif request.query_params.get('patient'):
            return ['patient', ]
        elif request.query_params.get('est_consommee'):
            return ['est_consommee', ]
        return super().get_search_fields(view, request)