import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V2beta2CrossVersionObjectReference:
    api_version: typing.Optional[str]
    kind: str
    name: str
    
    def __init__(self, *, api_version: typing.Optional[str] = ..., kind: str, name: str) -> None:
        ...
    def to_dict(self) -> V2beta2CrossVersionObjectReferenceDict:
        ...
class V2beta2CrossVersionObjectReferenceDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: str
    name: str
