# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: object.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='object.proto',
  package='ObjectDetection',
  syntax='proto3',
  serialized_options=b'\200\001\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0cobject.proto\x12\x0fObjectDetection\"\x1e\n\rObjectRequest\x12\r\n\x05image\x18\x01 \x01(\x0c\"@\n\x04Rect\x12\x0c\n\x04left\x18\x01 \x01(\x02\x12\r\n\x05right\x18\x02 \x01(\x02\x12\x0b\n\x03top\x18\x03 \x01(\x02\x12\x0e\n\x06\x62ottom\x18\x04 \x01(\x02\"K\n\x06Object\x12\r\n\x05label\x18\x01 \x01(\t\x12\r\n\x05score\x18\x02 \x01(\x02\x12#\n\x04rect\x18\x03 \x01(\x0b\x32\x15.ObjectDetection.Rect\"<\n\x0eObjectResponse\x12*\n\tresponses\x18\x01 \x03(\x0b\x32\x17.ObjectDetection.Object2]\n\rObjectService\x12L\n\x07predict\x12\x1e.ObjectDetection.ObjectRequest\x1a\x1f.ObjectDetection.ObjectResponse\"\x00\x42\x03\x80\x01\x01\x62\x06proto3'
)




_OBJECTREQUEST = _descriptor.Descriptor(
  name='ObjectRequest',
  full_name='ObjectDetection.ObjectRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='image', full_name='ObjectDetection.ObjectRequest.image', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=33,
  serialized_end=63,
)


_RECT = _descriptor.Descriptor(
  name='Rect',
  full_name='ObjectDetection.Rect',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='left', full_name='ObjectDetection.Rect.left', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='right', full_name='ObjectDetection.Rect.right', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='top', full_name='ObjectDetection.Rect.top', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bottom', full_name='ObjectDetection.Rect.bottom', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=65,
  serialized_end=129,
)


_OBJECT = _descriptor.Descriptor(
  name='Object',
  full_name='ObjectDetection.Object',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='label', full_name='ObjectDetection.Object.label', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='score', full_name='ObjectDetection.Object.score', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rect', full_name='ObjectDetection.Object.rect', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=131,
  serialized_end=206,
)


_OBJECTRESPONSE = _descriptor.Descriptor(
  name='ObjectResponse',
  full_name='ObjectDetection.ObjectResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='responses', full_name='ObjectDetection.ObjectResponse.responses', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=208,
  serialized_end=268,
)

_OBJECT.fields_by_name['rect'].message_type = _RECT
_OBJECTRESPONSE.fields_by_name['responses'].message_type = _OBJECT
DESCRIPTOR.message_types_by_name['ObjectRequest'] = _OBJECTREQUEST
DESCRIPTOR.message_types_by_name['Rect'] = _RECT
DESCRIPTOR.message_types_by_name['Object'] = _OBJECT
DESCRIPTOR.message_types_by_name['ObjectResponse'] = _OBJECTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ObjectRequest = _reflection.GeneratedProtocolMessageType('ObjectRequest', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTREQUEST,
  '__module__' : 'object_pb2'
  # @@protoc_insertion_point(class_scope:ObjectDetection.ObjectRequest)
  })
_sym_db.RegisterMessage(ObjectRequest)

Rect = _reflection.GeneratedProtocolMessageType('Rect', (_message.Message,), {
  'DESCRIPTOR' : _RECT,
  '__module__' : 'object_pb2'
  # @@protoc_insertion_point(class_scope:ObjectDetection.Rect)
  })
_sym_db.RegisterMessage(Rect)

Object = _reflection.GeneratedProtocolMessageType('Object', (_message.Message,), {
  'DESCRIPTOR' : _OBJECT,
  '__module__' : 'object_pb2'
  # @@protoc_insertion_point(class_scope:ObjectDetection.Object)
  })
_sym_db.RegisterMessage(Object)

ObjectResponse = _reflection.GeneratedProtocolMessageType('ObjectResponse', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTRESPONSE,
  '__module__' : 'object_pb2'
  # @@protoc_insertion_point(class_scope:ObjectDetection.ObjectResponse)
  })
_sym_db.RegisterMessage(ObjectResponse)


DESCRIPTOR._options = None

_OBJECTSERVICE = _descriptor.ServiceDescriptor(
  name='ObjectService',
  full_name='ObjectDetection.ObjectService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=270,
  serialized_end=363,
  methods=[
  _descriptor.MethodDescriptor(
    name='predict',
    full_name='ObjectDetection.ObjectService.predict',
    index=0,
    containing_service=None,
    input_type=_OBJECTREQUEST,
    output_type=_OBJECTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_OBJECTSERVICE)

DESCRIPTOR.services_by_name['ObjectService'] = _OBJECTSERVICE

# @@protoc_insertion_point(module_scope)
