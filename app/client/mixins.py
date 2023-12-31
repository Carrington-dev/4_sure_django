from rest_framework import mixins, viewsets 

class ClientMixin(
    mixins.ListModelMixin, \
        mixins.RetrieveModelMixin, \
        mixins.CreateModelMixin, \
        mixins.UpdateModelMixin, \
        viewsets.GenericViewSet, ):
    pass