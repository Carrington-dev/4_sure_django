from rest_framework import mixins, viewsets 

class TroupeMixin(
    mixins.ListModelMixin, \
        mixins.RetrieveModelMixin, \
        mixins.CreateModelMixin, \
        mixins.UpdateModelMixin, \
        viewsets.GenericViewSet, ):
    pass