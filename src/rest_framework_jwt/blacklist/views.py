from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from rest_framework_jwt.blacklist.models import BlacklistedToken

from ..utils import get_jwt_value
from .serializers import BlacklistTokenSerializer


class BlacklistView(ModelViewSet):
    queryset = BlacklistedToken.objects.all()
    serializer_class = BlacklistTokenSerializer
    permission_classes = (IsAuthenticated, )

    def create(self, request, *args, **kwargs):
        if 'token' not in request.data:
            request.data.update({'token': get_jwt_value(request)})

        return super(BlacklistView, self).create(request, *args, **kwargs)
