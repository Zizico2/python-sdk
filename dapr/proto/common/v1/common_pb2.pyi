"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

# HTTPExtension includes HTTP verb and querystring
# when Dapr runtime delivers HTTP content.
# 
# For example, when callers calls http invoke api
# POST http://localhost:3500/v1.0/invoke/<app_id>/method/<method>?query1=value1&query2=value2
# 
# Dapr runtime will parse POST as a verb and extract querystring to quersytring map.
class HTTPExtension(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    # Type of HTTP 1.1 Methods
    # RFC 7231: https://tools.ietf.org/html/rfc7231#page-24
    class Verb(_Verb, metaclass=_VerbEnumTypeWrapper):
        pass
    class _Verb:
        V = typing.NewType('V', builtins.int)
    class _VerbEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Verb.V], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        NONE = HTTPExtension.Verb.V(0)
        GET = HTTPExtension.Verb.V(1)
        HEAD = HTTPExtension.Verb.V(2)
        POST = HTTPExtension.Verb.V(3)
        PUT = HTTPExtension.Verb.V(4)
        DELETE = HTTPExtension.Verb.V(5)
        CONNECT = HTTPExtension.Verb.V(6)
        OPTIONS = HTTPExtension.Verb.V(7)
        TRACE = HTTPExtension.Verb.V(8)

    NONE = HTTPExtension.Verb.V(0)
    GET = HTTPExtension.Verb.V(1)
    HEAD = HTTPExtension.Verb.V(2)
    POST = HTTPExtension.Verb.V(3)
    PUT = HTTPExtension.Verb.V(4)
    DELETE = HTTPExtension.Verb.V(5)
    CONNECT = HTTPExtension.Verb.V(6)
    OPTIONS = HTTPExtension.Verb.V(7)
    TRACE = HTTPExtension.Verb.V(8)

    VERB_FIELD_NUMBER: builtins.int
    QUERYSTRING_FIELD_NUMBER: builtins.int
    # Required. HTTP verb.
    verb: global___HTTPExtension.Verb.V = ...
    # Optional. querystring represents an encoded HTTP url query string in the following format: name=value&name2=value2
    querystring: typing.Text = ...
    def __init__(self,
        *,
        verb : global___HTTPExtension.Verb.V = ...,
        querystring : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"querystring",b"querystring",u"verb",b"verb"]) -> None: ...
global___HTTPExtension = HTTPExtension

# InvokeRequest is the message to invoke a method with the data.
# This message is used in InvokeService of Dapr gRPC Service and OnInvoke
# of AppCallback gRPC service.
class InvokeRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    METHOD_FIELD_NUMBER: builtins.int
    DATA_FIELD_NUMBER: builtins.int
    CONTENT_TYPE_FIELD_NUMBER: builtins.int
    HTTP_EXTENSION_FIELD_NUMBER: builtins.int
    # Required. method is a method name which will be invoked by caller.
    method: typing.Text = ...
    # Required. Bytes value or Protobuf message which caller sent.
    # Dapr treats Any.value as bytes type if Any.type_url is unset.
    @property
    def data(self) -> google.protobuf.any_pb2.Any: ...
    # The type of data content.
    #
    # This field is required if data delivers http request body
    # Otherwise, this is optional.
    content_type: typing.Text = ...
    # HTTP specific fields if request conveys http-compatible request.
    #
    # This field is required for http-compatible request. Otherwise,
    # this field is optional.
    @property
    def http_extension(self) -> global___HTTPExtension: ...
    def __init__(self,
        *,
        method : typing.Text = ...,
        data : typing.Optional[google.protobuf.any_pb2.Any] = ...,
        content_type : typing.Text = ...,
        http_extension : typing.Optional[global___HTTPExtension] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"data",b"data",u"http_extension",b"http_extension"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"content_type",b"content_type",u"data",b"data",u"http_extension",b"http_extension",u"method",b"method"]) -> None: ...
global___InvokeRequest = InvokeRequest

# InvokeResponse is the response message inclduing data and its content type
# from app callback.
# This message is used in InvokeService of Dapr gRPC Service and OnInvoke
# of AppCallback gRPC service.
class InvokeResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DATA_FIELD_NUMBER: builtins.int
    CONTENT_TYPE_FIELD_NUMBER: builtins.int
    # Required. The content body of InvokeService response.
    @property
    def data(self) -> google.protobuf.any_pb2.Any: ...
    # Required. The type of data content.
    content_type: typing.Text = ...
    def __init__(self,
        *,
        data : typing.Optional[google.protobuf.any_pb2.Any] = ...,
        content_type : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"data",b"data"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"content_type",b"content_type",u"data",b"data"]) -> None: ...
global___InvokeResponse = InvokeResponse

# StateItem represents state key, value, and additional options to save state.
class StateItem(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class MetadataEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        value: typing.Text = ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    KEY_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    ETAG_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    OPTIONS_FIELD_NUMBER: builtins.int
    # Required. The state key
    key: typing.Text = ...
    # Required. The state data for key
    value: builtins.bytes = ...
    # The entity tag which represents the specific version of data.
    # The exact ETag format is defined by the corresponding data store.
    @property
    def etag(self) -> global___Etag: ...
    # The metadata which will be passed to state store component.
    @property
    def metadata(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]: ...
    # Options for concurrency and consistency to save the state.
    @property
    def options(self) -> global___StateOptions: ...
    def __init__(self,
        *,
        key : typing.Text = ...,
        value : builtins.bytes = ...,
        etag : typing.Optional[global___Etag] = ...,
        metadata : typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        options : typing.Optional[global___StateOptions] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"etag",b"etag",u"options",b"options"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"etag",b"etag",u"key",b"key",u"metadata",b"metadata",u"options",b"options",u"value",b"value"]) -> None: ...
global___StateItem = StateItem

# Etag represents a state item version
class Etag(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    VALUE_FIELD_NUMBER: builtins.int
    # value sets the etag value
    value: typing.Text = ...
    def __init__(self,
        *,
        value : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"value",b"value"]) -> None: ...
global___Etag = Etag

# StateOptions configures concurrency and consistency for state operations
class StateOptions(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    # Enum describing the supported concurrency for state.
    class StateConcurrency(_StateConcurrency, metaclass=_StateConcurrencyEnumTypeWrapper):
        pass
    class _StateConcurrency:
        V = typing.NewType('V', builtins.int)
    class _StateConcurrencyEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_StateConcurrency.V], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        CONCURRENCY_UNSPECIFIED = StateOptions.StateConcurrency.V(0)
        CONCURRENCY_FIRST_WRITE = StateOptions.StateConcurrency.V(1)
        CONCURRENCY_LAST_WRITE = StateOptions.StateConcurrency.V(2)

    CONCURRENCY_UNSPECIFIED = StateOptions.StateConcurrency.V(0)
    CONCURRENCY_FIRST_WRITE = StateOptions.StateConcurrency.V(1)
    CONCURRENCY_LAST_WRITE = StateOptions.StateConcurrency.V(2)

    # Enum describing the supported consistency for state.
    class StateConsistency(_StateConsistency, metaclass=_StateConsistencyEnumTypeWrapper):
        pass
    class _StateConsistency:
        V = typing.NewType('V', builtins.int)
    class _StateConsistencyEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_StateConsistency.V], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        CONSISTENCY_UNSPECIFIED = StateOptions.StateConsistency.V(0)
        CONSISTENCY_EVENTUAL = StateOptions.StateConsistency.V(1)
        CONSISTENCY_STRONG = StateOptions.StateConsistency.V(2)

    CONSISTENCY_UNSPECIFIED = StateOptions.StateConsistency.V(0)
    CONSISTENCY_EVENTUAL = StateOptions.StateConsistency.V(1)
    CONSISTENCY_STRONG = StateOptions.StateConsistency.V(2)

    CONCURRENCY_FIELD_NUMBER: builtins.int
    CONSISTENCY_FIELD_NUMBER: builtins.int
    concurrency: global___StateOptions.StateConcurrency.V = ...
    consistency: global___StateOptions.StateConsistency.V = ...
    def __init__(self,
        *,
        concurrency : global___StateOptions.StateConcurrency.V = ...,
        consistency : global___StateOptions.StateConsistency.V = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"concurrency",b"concurrency",u"consistency",b"consistency"]) -> None: ...
global___StateOptions = StateOptions