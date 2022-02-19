# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: feast/serving/ServingService.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from connector_python import Value_pb2 as feast_dot_types_dot_Value__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='feast/serving/ServingService.proto',
  package='feast.serving',
  syntax='proto3',
  serialized_options=b'\n\023feast.proto.servingB\017ServingAPIProtoZ2github.com/feast-dev/feast/go/protos/feast/serving',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\"feast/serving/ServingService.proto\x12\rfeast.serving\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17\x66\x65\x61st/types/Value.proto\"\x1c\n\x1aGetFeastServingInfoRequest\".\n\x1bGetFeastServingInfoResponse\x12\x0f\n\x07version\x18\x01 \x01(\t\"E\n\x12\x46\x65\x61tureReferenceV2\x12\x19\n\x11\x66\x65\x61ture_view_name\x18\x01 \x01(\t\x12\x14\n\x0c\x66\x65\x61ture_name\x18\x02 \x01(\t\"\xfd\x02\n\x1aGetOnlineFeaturesRequestV2\x12\x33\n\x08\x66\x65\x61tures\x18\x04 \x03(\x0b\x32!.feast.serving.FeatureReferenceV2\x12H\n\x0b\x65ntity_rows\x18\x02 \x03(\x0b\x32\x33.feast.serving.GetOnlineFeaturesRequestV2.EntityRow\x12\x0f\n\x07project\x18\x05 \x01(\t\x1a\xce\x01\n\tEntityRow\x12-\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12O\n\x06\x66ields\x18\x02 \x03(\x0b\x32?.feast.serving.GetOnlineFeaturesRequestV2.EntityRow.FieldsEntry\x1a\x41\n\x0b\x46ieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12!\n\x05value\x18\x02 \x01(\x0b\x32\x12.feast.types.Value:\x02\x38\x01\"\x1a\n\x0b\x46\x65\x61tureList\x12\x0b\n\x03val\x18\x01 \x03(\t\"\xc8\x03\n\x18GetOnlineFeaturesRequest\x12\x19\n\x0f\x66\x65\x61ture_service\x18\x01 \x01(\tH\x00\x12.\n\x08\x66\x65\x61tures\x18\x02 \x01(\x0b\x32\x1a.feast.serving.FeatureListH\x00\x12G\n\x08\x65ntities\x18\x03 \x03(\x0b\x32\x35.feast.serving.GetOnlineFeaturesRequest.EntitiesEntry\x12\x1a\n\x12\x66ull_feature_names\x18\x04 \x01(\x08\x12T\n\x0frequest_context\x18\x05 \x03(\x0b\x32;.feast.serving.GetOnlineFeaturesRequest.RequestContextEntry\x1aK\n\rEntitiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12)\n\x05value\x18\x02 \x01(\x0b\x32\x1a.feast.types.RepeatedValue:\x02\x38\x01\x1aQ\n\x13RequestContextEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12)\n\x05value\x18\x02 \x01(\x0b\x32\x1a.feast.types.RepeatedValue:\x02\x38\x01\x42\x06\n\x04kind\"\xc2\x02\n\x19GetOnlineFeaturesResponse\x12\x42\n\x08metadata\x18\x01 \x01(\x0b\x32\x30.feast.serving.GetOnlineFeaturesResponseMetadata\x12G\n\x07results\x18\x02 \x03(\x0b\x32\x36.feast.serving.GetOnlineFeaturesResponse.FeatureVector\x1a\x97\x01\n\rFeatureVector\x12\"\n\x06values\x18\x01 \x03(\x0b\x32\x12.feast.types.Value\x12,\n\x08statuses\x18\x02 \x03(\x0e\x32\x1a.feast.serving.FieldStatus\x12\x34\n\x10\x65vent_timestamps\x18\x03 \x03(\x0b\x32\x1a.google.protobuf.Timestamp\"V\n!GetOnlineFeaturesResponseMetadata\x12\x31\n\rfeature_names\x18\x01 \x01(\x0b\x32\x1a.feast.serving.FeatureList*[\n\x0b\x46ieldStatus\x12\x0b\n\x07INVALID\x10\x00\x12\x0b\n\x07PRESENT\x10\x01\x12\x0e\n\nNULL_VALUE\x10\x02\x12\r\n\tNOT_FOUND\x10\x03\x12\x13\n\x0fOUTSIDE_MAX_AGE\x10\x04\x32\xe6\x01\n\x0eServingService\x12l\n\x13GetFeastServingInfo\x12).feast.serving.GetFeastServingInfoRequest\x1a*.feast.serving.GetFeastServingInfoResponse\x12\x66\n\x11GetOnlineFeatures\x12\'.feast.serving.GetOnlineFeaturesRequest\x1a(.feast.serving.GetOnlineFeaturesResponseBZ\n\x13\x66\x65\x61st.proto.servingB\x0fServingAPIProtoZ2github.com/feast-dev/feast/go/protos/feast/servingb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,feast_dot_types_dot_Value__pb2.DESCRIPTOR,])

_FIELDSTATUS = _descriptor.EnumDescriptor(
  name='FieldStatus',
  full_name='feast.serving.FieldStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INVALID', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PRESENT', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NULL_VALUE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NOT_FOUND', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OUTSIDE_MAX_AGE', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1544,
  serialized_end=1635,
)
_sym_db.RegisterEnumDescriptor(_FIELDSTATUS)

FieldStatus = enum_type_wrapper.EnumTypeWrapper(_FIELDSTATUS)
INVALID = 0
PRESENT = 1
NULL_VALUE = 2
NOT_FOUND = 3
OUTSIDE_MAX_AGE = 4



_GETFEASTSERVINGINFOREQUEST = _descriptor.Descriptor(
  name='GetFeastServingInfoRequest',
  full_name='feast.serving.GetFeastServingInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=111,
  serialized_end=139,
)


_GETFEASTSERVINGINFORESPONSE = _descriptor.Descriptor(
  name='GetFeastServingInfoResponse',
  full_name='feast.serving.GetFeastServingInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='feast.serving.GetFeastServingInfoResponse.version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=141,
  serialized_end=187,
)


_FEATUREREFERENCEV2 = _descriptor.Descriptor(
  name='FeatureReferenceV2',
  full_name='feast.serving.FeatureReferenceV2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='feature_view_name', full_name='feast.serving.FeatureReferenceV2.feature_view_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='feature_name', full_name='feast.serving.FeatureReferenceV2.feature_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=189,
  serialized_end=258,
)


_GETONLINEFEATURESREQUESTV2_ENTITYROW_FIELDSENTRY = _descriptor.Descriptor(
  name='FieldsEntry',
  full_name='feast.serving.GetOnlineFeaturesRequestV2.EntityRow.FieldsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='feast.serving.GetOnlineFeaturesRequestV2.EntityRow.FieldsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='feast.serving.GetOnlineFeaturesRequestV2.EntityRow.FieldsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=577,
  serialized_end=642,
)

_GETONLINEFEATURESREQUESTV2_ENTITYROW = _descriptor.Descriptor(
  name='EntityRow',
  full_name='feast.serving.GetOnlineFeaturesRequestV2.EntityRow',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='feast.serving.GetOnlineFeaturesRequestV2.EntityRow.timestamp', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fields', full_name='feast.serving.GetOnlineFeaturesRequestV2.EntityRow.fields', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_GETONLINEFEATURESREQUESTV2_ENTITYROW_FIELDSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=436,
  serialized_end=642,
)

_GETONLINEFEATURESREQUESTV2 = _descriptor.Descriptor(
  name='GetOnlineFeaturesRequestV2',
  full_name='feast.serving.GetOnlineFeaturesRequestV2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='features', full_name='feast.serving.GetOnlineFeaturesRequestV2.features', index=0,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='entity_rows', full_name='feast.serving.GetOnlineFeaturesRequestV2.entity_rows', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='project', full_name='feast.serving.GetOnlineFeaturesRequestV2.project', index=2,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_GETONLINEFEATURESREQUESTV2_ENTITYROW, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=261,
  serialized_end=642,
)


_FEATURELIST = _descriptor.Descriptor(
  name='FeatureList',
  full_name='feast.serving.FeatureList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='val', full_name='feast.serving.FeatureList.val', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=644,
  serialized_end=670,
)


_GETONLINEFEATURESREQUEST_ENTITIESENTRY = _descriptor.Descriptor(
  name='EntitiesEntry',
  full_name='feast.serving.GetOnlineFeaturesRequest.EntitiesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='feast.serving.GetOnlineFeaturesRequest.EntitiesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='feast.serving.GetOnlineFeaturesRequest.EntitiesEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=963,
  serialized_end=1038,
)

_GETONLINEFEATURESREQUEST_REQUESTCONTEXTENTRY = _descriptor.Descriptor(
  name='RequestContextEntry',
  full_name='feast.serving.GetOnlineFeaturesRequest.RequestContextEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='feast.serving.GetOnlineFeaturesRequest.RequestContextEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='feast.serving.GetOnlineFeaturesRequest.RequestContextEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1040,
  serialized_end=1121,
)

_GETONLINEFEATURESREQUEST = _descriptor.Descriptor(
  name='GetOnlineFeaturesRequest',
  full_name='feast.serving.GetOnlineFeaturesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='feature_service', full_name='feast.serving.GetOnlineFeaturesRequest.feature_service', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='features', full_name='feast.serving.GetOnlineFeaturesRequest.features', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='entities', full_name='feast.serving.GetOnlineFeaturesRequest.entities', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='full_feature_names', full_name='feast.serving.GetOnlineFeaturesRequest.full_feature_names', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='request_context', full_name='feast.serving.GetOnlineFeaturesRequest.request_context', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_GETONLINEFEATURESREQUEST_ENTITIESENTRY, _GETONLINEFEATURESREQUEST_REQUESTCONTEXTENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='kind', full_name='feast.serving.GetOnlineFeaturesRequest.kind',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=673,
  serialized_end=1129,
)


_GETONLINEFEATURESRESPONSE_FEATUREVECTOR = _descriptor.Descriptor(
  name='FeatureVector',
  full_name='feast.serving.GetOnlineFeaturesResponse.FeatureVector',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='feast.serving.GetOnlineFeaturesResponse.FeatureVector.values', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='statuses', full_name='feast.serving.GetOnlineFeaturesResponse.FeatureVector.statuses', index=1,
      number=2, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='event_timestamps', full_name='feast.serving.GetOnlineFeaturesResponse.FeatureVector.event_timestamps', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1303,
  serialized_end=1454,
)

_GETONLINEFEATURESRESPONSE = _descriptor.Descriptor(
  name='GetOnlineFeaturesResponse',
  full_name='feast.serving.GetOnlineFeaturesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='metadata', full_name='feast.serving.GetOnlineFeaturesResponse.metadata', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='results', full_name='feast.serving.GetOnlineFeaturesResponse.results', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_GETONLINEFEATURESRESPONSE_FEATUREVECTOR, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1132,
  serialized_end=1454,
)


_GETONLINEFEATURESRESPONSEMETADATA = _descriptor.Descriptor(
  name='GetOnlineFeaturesResponseMetadata',
  full_name='feast.serving.GetOnlineFeaturesResponseMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='feature_names', full_name='feast.serving.GetOnlineFeaturesResponseMetadata.feature_names', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1456,
  serialized_end=1542,
)

_GETONLINEFEATURESREQUESTV2_ENTITYROW_FIELDSENTRY.fields_by_name['value'].message_type = feast_dot_types_dot_Value__pb2._VALUE
_GETONLINEFEATURESREQUESTV2_ENTITYROW_FIELDSENTRY.containing_type = _GETONLINEFEATURESREQUESTV2_ENTITYROW
_GETONLINEFEATURESREQUESTV2_ENTITYROW.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_GETONLINEFEATURESREQUESTV2_ENTITYROW.fields_by_name['fields'].message_type = _GETONLINEFEATURESREQUESTV2_ENTITYROW_FIELDSENTRY
_GETONLINEFEATURESREQUESTV2_ENTITYROW.containing_type = _GETONLINEFEATURESREQUESTV2
_GETONLINEFEATURESREQUESTV2.fields_by_name['features'].message_type = _FEATUREREFERENCEV2
_GETONLINEFEATURESREQUESTV2.fields_by_name['entity_rows'].message_type = _GETONLINEFEATURESREQUESTV2_ENTITYROW
_GETONLINEFEATURESREQUEST_ENTITIESENTRY.fields_by_name['value'].message_type = feast_dot_types_dot_Value__pb2._REPEATEDVALUE
_GETONLINEFEATURESREQUEST_ENTITIESENTRY.containing_type = _GETONLINEFEATURESREQUEST
_GETONLINEFEATURESREQUEST_REQUESTCONTEXTENTRY.fields_by_name['value'].message_type = feast_dot_types_dot_Value__pb2._REPEATEDVALUE
_GETONLINEFEATURESREQUEST_REQUESTCONTEXTENTRY.containing_type = _GETONLINEFEATURESREQUEST
_GETONLINEFEATURESREQUEST.fields_by_name['features'].message_type = _FEATURELIST
_GETONLINEFEATURESREQUEST.fields_by_name['entities'].message_type = _GETONLINEFEATURESREQUEST_ENTITIESENTRY
_GETONLINEFEATURESREQUEST.fields_by_name['request_context'].message_type = _GETONLINEFEATURESREQUEST_REQUESTCONTEXTENTRY
_GETONLINEFEATURESREQUEST.oneofs_by_name['kind'].fields.append(
  _GETONLINEFEATURESREQUEST.fields_by_name['feature_service'])
_GETONLINEFEATURESREQUEST.fields_by_name['feature_service'].containing_oneof = _GETONLINEFEATURESREQUEST.oneofs_by_name['kind']
_GETONLINEFEATURESREQUEST.oneofs_by_name['kind'].fields.append(
  _GETONLINEFEATURESREQUEST.fields_by_name['features'])
_GETONLINEFEATURESREQUEST.fields_by_name['features'].containing_oneof = _GETONLINEFEATURESREQUEST.oneofs_by_name['kind']
_GETONLINEFEATURESRESPONSE_FEATUREVECTOR.fields_by_name['values'].message_type = feast_dot_types_dot_Value__pb2._VALUE
_GETONLINEFEATURESRESPONSE_FEATUREVECTOR.fields_by_name['statuses'].enum_type = _FIELDSTATUS
_GETONLINEFEATURESRESPONSE_FEATUREVECTOR.fields_by_name['event_timestamps'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_GETONLINEFEATURESRESPONSE_FEATUREVECTOR.containing_type = _GETONLINEFEATURESRESPONSE
_GETONLINEFEATURESRESPONSE.fields_by_name['metadata'].message_type = _GETONLINEFEATURESRESPONSEMETADATA
_GETONLINEFEATURESRESPONSE.fields_by_name['results'].message_type = _GETONLINEFEATURESRESPONSE_FEATUREVECTOR
_GETONLINEFEATURESRESPONSEMETADATA.fields_by_name['feature_names'].message_type = _FEATURELIST
DESCRIPTOR.message_types_by_name['GetFeastServingInfoRequest'] = _GETFEASTSERVINGINFOREQUEST
DESCRIPTOR.message_types_by_name['GetFeastServingInfoResponse'] = _GETFEASTSERVINGINFORESPONSE
DESCRIPTOR.message_types_by_name['FeatureReferenceV2'] = _FEATUREREFERENCEV2
DESCRIPTOR.message_types_by_name['GetOnlineFeaturesRequestV2'] = _GETONLINEFEATURESREQUESTV2
DESCRIPTOR.message_types_by_name['FeatureList'] = _FEATURELIST
DESCRIPTOR.message_types_by_name['GetOnlineFeaturesRequest'] = _GETONLINEFEATURESREQUEST
DESCRIPTOR.message_types_by_name['GetOnlineFeaturesResponse'] = _GETONLINEFEATURESRESPONSE
DESCRIPTOR.message_types_by_name['GetOnlineFeaturesResponseMetadata'] = _GETONLINEFEATURESRESPONSEMETADATA
DESCRIPTOR.enum_types_by_name['FieldStatus'] = _FIELDSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetFeastServingInfoRequest = _reflection.GeneratedProtocolMessageType('GetFeastServingInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETFEASTSERVINGINFOREQUEST,
  '__module__' : 'feast.serving.ServingService_pb2'
  # @@protoc_insertion_point(class_scope:feast.serving.GetFeastServingInfoRequest)
  })
_sym_db.RegisterMessage(GetFeastServingInfoRequest)

GetFeastServingInfoResponse = _reflection.GeneratedProtocolMessageType('GetFeastServingInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETFEASTSERVINGINFORESPONSE,
  '__module__' : 'feast.serving.ServingService_pb2'
  # @@protoc_insertion_point(class_scope:feast.serving.GetFeastServingInfoResponse)
  })
_sym_db.RegisterMessage(GetFeastServingInfoResponse)

FeatureReferenceV2 = _reflection.GeneratedProtocolMessageType('FeatureReferenceV2', (_message.Message,), {
  'DESCRIPTOR' : _FEATUREREFERENCEV2,
  '__module__' : 'feast.serving.ServingService_pb2'
  # @@protoc_insertion_point(class_scope:feast.serving.FeatureReferenceV2)
  })
_sym_db.RegisterMessage(FeatureReferenceV2)

GetOnlineFeaturesRequestV2 = _reflection.GeneratedProtocolMessageType('GetOnlineFeaturesRequestV2', (_message.Message,), {

  'EntityRow' : _reflection.GeneratedProtocolMessageType('EntityRow', (_message.Message,), {

    'FieldsEntry' : _reflection.GeneratedProtocolMessageType('FieldsEntry', (_message.Message,), {
      'DESCRIPTOR' : _GETONLINEFEATURESREQUESTV2_ENTITYROW_FIELDSENTRY,
      '__module__' : 'feast.serving.ServingService_pb2'
      # @@protoc_insertion_point(class_scope:feast.serving.GetOnlineFeaturesRequestV2.EntityRow.FieldsEntry)
      })
    ,
    'DESCRIPTOR' : _GETONLINEFEATURESREQUESTV2_ENTITYROW,
    '__module__' : 'feast.serving.ServingService_pb2'
    # @@protoc_insertion_point(class_scope:feast.serving.GetOnlineFeaturesRequestV2.EntityRow)
    })
  ,
  'DESCRIPTOR' : _GETONLINEFEATURESREQUESTV2,
  '__module__' : 'feast.serving.ServingService_pb2'
  # @@protoc_insertion_point(class_scope:feast.serving.GetOnlineFeaturesRequestV2)
  })
_sym_db.RegisterMessage(GetOnlineFeaturesRequestV2)
_sym_db.RegisterMessage(GetOnlineFeaturesRequestV2.EntityRow)
_sym_db.RegisterMessage(GetOnlineFeaturesRequestV2.EntityRow.FieldsEntry)

FeatureList = _reflection.GeneratedProtocolMessageType('FeatureList', (_message.Message,), {
  'DESCRIPTOR' : _FEATURELIST,
  '__module__' : 'feast.serving.ServingService_pb2'
  # @@protoc_insertion_point(class_scope:feast.serving.FeatureList)
  })
_sym_db.RegisterMessage(FeatureList)

GetOnlineFeaturesRequest = _reflection.GeneratedProtocolMessageType('GetOnlineFeaturesRequest', (_message.Message,), {

  'EntitiesEntry' : _reflection.GeneratedProtocolMessageType('EntitiesEntry', (_message.Message,), {
    'DESCRIPTOR' : _GETONLINEFEATURESREQUEST_ENTITIESENTRY,
    '__module__' : 'feast.serving.ServingService_pb2'
    # @@protoc_insertion_point(class_scope:feast.serving.GetOnlineFeaturesRequest.EntitiesEntry)
    })
  ,

  'RequestContextEntry' : _reflection.GeneratedProtocolMessageType('RequestContextEntry', (_message.Message,), {
    'DESCRIPTOR' : _GETONLINEFEATURESREQUEST_REQUESTCONTEXTENTRY,
    '__module__' : 'feast.serving.ServingService_pb2'
    # @@protoc_insertion_point(class_scope:feast.serving.GetOnlineFeaturesRequest.RequestContextEntry)
    })
  ,
  'DESCRIPTOR' : _GETONLINEFEATURESREQUEST,
  '__module__' : 'feast.serving.ServingService_pb2'
  # @@protoc_insertion_point(class_scope:feast.serving.GetOnlineFeaturesRequest)
  })
_sym_db.RegisterMessage(GetOnlineFeaturesRequest)
_sym_db.RegisterMessage(GetOnlineFeaturesRequest.EntitiesEntry)
_sym_db.RegisterMessage(GetOnlineFeaturesRequest.RequestContextEntry)

GetOnlineFeaturesResponse = _reflection.GeneratedProtocolMessageType('GetOnlineFeaturesResponse', (_message.Message,), {

  'FeatureVector' : _reflection.GeneratedProtocolMessageType('FeatureVector', (_message.Message,), {
    'DESCRIPTOR' : _GETONLINEFEATURESRESPONSE_FEATUREVECTOR,
    '__module__' : 'feast.serving.ServingService_pb2'
    # @@protoc_insertion_point(class_scope:feast.serving.GetOnlineFeaturesResponse.FeatureVector)
    })
  ,
  'DESCRIPTOR' : _GETONLINEFEATURESRESPONSE,
  '__module__' : 'feast.serving.ServingService_pb2'
  # @@protoc_insertion_point(class_scope:feast.serving.GetOnlineFeaturesResponse)
  })
_sym_db.RegisterMessage(GetOnlineFeaturesResponse)
_sym_db.RegisterMessage(GetOnlineFeaturesResponse.FeatureVector)

GetOnlineFeaturesResponseMetadata = _reflection.GeneratedProtocolMessageType('GetOnlineFeaturesResponseMetadata', (_message.Message,), {
  'DESCRIPTOR' : _GETONLINEFEATURESRESPONSEMETADATA,
  '__module__' : 'feast.serving.ServingService_pb2'
  # @@protoc_insertion_point(class_scope:feast.serving.GetOnlineFeaturesResponseMetadata)
  })
_sym_db.RegisterMessage(GetOnlineFeaturesResponseMetadata)


DESCRIPTOR._options = None
_GETONLINEFEATURESREQUESTV2_ENTITYROW_FIELDSENTRY._options = None
_GETONLINEFEATURESREQUEST_ENTITIESENTRY._options = None
_GETONLINEFEATURESREQUEST_REQUESTCONTEXTENTRY._options = None

_SERVINGSERVICE = _descriptor.ServiceDescriptor(
  name='ServingService',
  full_name='feast.serving.ServingService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1638,
  serialized_end=1868,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetFeastServingInfo',
    full_name='feast.serving.ServingService.GetFeastServingInfo',
    index=0,
    containing_service=None,
    input_type=_GETFEASTSERVINGINFOREQUEST,
    output_type=_GETFEASTSERVINGINFORESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetOnlineFeatures',
    full_name='feast.serving.ServingService.GetOnlineFeatures',
    index=1,
    containing_service=None,
    input_type=_GETONLINEFEATURESREQUEST,
    output_type=_GETONLINEFEATURESRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SERVINGSERVICE)

DESCRIPTOR.services_by_name['ServingService'] = _SERVINGSERVICE

# @@protoc_insertion_point(module_scope)