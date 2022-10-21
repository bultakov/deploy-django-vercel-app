from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    DeleteModelMixin
)
from djangochannelsrestframework.observer import model_observer
from djangochannelsrestframework.observer.generics import ObserverModelInstanceMixin

from .serializers import NewsSerializers
from .models import News


class NewsConsumer(ListModelMixin, ObserverModelInstanceMixin, GenericAsyncAPIConsumer):
    queryset = News.objects.all()
    serializer_class = NewsSerializers

    async def connect(self):
        await self.accept()

    async def disconnect(self, code):
        await super().disconnect(code=code)

    @model_observer(News)
    async def post_activity(
            self,
            message: NewsSerializers,
            **kwargs
    ):
        await self.send_json(dict(message.data))

    @post_activity.serializer
    def post_activity(self, instance: News, action, **kwargs) -> NewsSerializers:
        print(action)
        return NewsSerializers(instance)
