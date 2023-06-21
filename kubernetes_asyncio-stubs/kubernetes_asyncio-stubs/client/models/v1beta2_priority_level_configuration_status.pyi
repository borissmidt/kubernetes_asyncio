import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta2PriorityLevelConfigurationStatus:
    conditions: typing.Optional[list[kubernetes_asyncio.client.V1beta2PriorityLevelConfigurationCondition]]
    
    def __init__(self, *, conditions: typing.Optional[list[kubernetes_asyncio.client.V1beta2PriorityLevelConfigurationCondition]] = ...) -> None:
        ...
    def to_dict(self) -> V1beta2PriorityLevelConfigurationStatusDict:
        ...
class V1beta2PriorityLevelConfigurationStatusDict(typing.TypedDict, total=False):
    conditions: typing.Optional[list[kubernetes_asyncio.client.V1beta2PriorityLevelConfigurationConditionDict]]