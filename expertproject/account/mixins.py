from rest_framework import mixins, viewsets 

class UserMixin(
    # mixins.ListModelMixin, \
        mixins.RetrieveModelMixin, \
        mixins.CreateModelMixin, \
        viewsets.GenericViewSet, ):
    pass

class UserMixinVerify(
    # mixins.ListModelMixin, \
        mixins.RetrieveModelMixin, \
        # mixins.CreateModelMixin, \
        viewsets.GenericViewSet, ):
    pass