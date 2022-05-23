# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: plate.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='plate.proto',
  package='PlateDetection',
  syntax='proto3',
  serialized_options=b'\200\001\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0bplate.proto\x12\x0ePlateDetection\"\x1d\n\x0cPlateRequest\x12\r\n\x05image\x18\x01 \x01(\x0c\"@\n\x04Rect\x12\x0c\n\x04left\x18\x01 \x01(\x02\x12\r\n\x05right\x18\x02 \x01(\x02\x12\x0b\n\x03top\x18\x03 \x01(\x02\x12\x0e\n\x06\x62ottom\x18\x04 \x01(\x02\"\x1d\n\x05Point\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\"\xb5\x01\n\x0bPlate4Point\x12&\n\x07topleft\x18\x01 \x01(\x0b\x32\x15.PlateDetection.Point\x12\'\n\x08topright\x18\x02 \x01(\x0b\x32\x15.PlateDetection.Point\x12)\n\nbottomleft\x18\x03 \x01(\x0b\x32\x15.PlateDetection.Point\x12*\n\x0b\x62ottomright\x18\x04 \x01(\x0b\x32\x15.PlateDetection.Point\"g\n\x05Plate\x12\r\n\x05score\x18\x01 \x01(\x02\x12\"\n\x04rect\x18\x02 \x01(\x0b\x32\x14.PlateDetection.Rect\x12+\n\x06points\x18\x03 \x01(\x0b\x32\x1b.PlateDetection.Plate4Point\"6\n\rPlateResponse\x12%\n\x06Plates\x18\x01 \x03(\x0b\x32\x15.PlateDetection.Plate2X\n\x0cPlateService\x12H\n\x07predict\x12\x1c.PlateDetection.PlateRequest\x1a\x1d.PlateDetection.PlateResponse\"\x00\x42\x03\x80\x01\x01\x62\x06proto3'
)




_PLATEREQUEST = _descriptor.Descriptor(
  name='PlateRequest',
  full_name='PlateDetection.PlateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='image', full_name='PlateDetection.PlateRequest.image', index=0,
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
  serialized_start=31,
  serialized_end=60,
)


_RECT = _descriptor.Descriptor(
  name='Rect',
  full_name='PlateDetection.Rect',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='left', full_name='PlateDetection.Rect.left', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='right', full_name='PlateDetection.Rect.right', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='top', full_name='PlateDetection.Rect.top', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bottom', full_name='PlateDetection.Rect.bottom', index=3,
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
  serialized_start=62,
  serialized_end=126,
)


_POINT = _descriptor.Descriptor(
  name='Point',
  full_name='PlateDetection.Point',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='PlateDetection.Point.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y', full_name='PlateDetection.Point.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
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
  serialized_start=128,
  serialized_end=157,
)


_PLATE4POINT = _descriptor.Descriptor(
  name='Plate4Point',
  full_name='PlateDetection.Plate4Point',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='topleft', full_name='PlateDetection.Plate4Point.topleft', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='topright', full_name='PlateDetection.Plate4Point.topright', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bottomleft', full_name='PlateDetection.Plate4Point.bottomleft', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bottomright', full_name='PlateDetection.Plate4Point.bottomright', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=160,
  serialized_end=341,
)


_PLATE = _descriptor.Descriptor(
  name='Plate',
  full_name='PlateDetection.Plate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='score', full_name='PlateDetection.Plate.score', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rect', full_name='PlateDetection.Plate.rect', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='points', full_name='PlateDetection.Plate.points', index=2,
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
  serialized_start=343,
  serialized_end=446,
)


_PLATERESPONSE = _descriptor.Descriptor(
  name='PlateResponse',
  full_name='PlateDetection.PlateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Plates', full_name='PlateDetection.PlateResponse.Plates', index=0,
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
  serialized_start=448,
  serialized_end=502,
)

_PLATE4POINT.fields_by_name['topleft'].message_type = _POINT
_PLATE4POINT.fields_by_name['topright'].message_type = _POINT
_PLATE4POINT.fields_by_name['bottomleft'].message_type = _POINT
_PLATE4POINT.fields_by_name['bottomright'].message_type = _POINT
_PLATE.fields_by_name['rect'].message_type = _RECT
_PLATE.fields_by_name['points'].message_type = _PLATE4POINT
_PLATERESPONSE.fields_by_name['Plates'].message_type = _PLATE
DESCRIPTOR.message_types_by_name['PlateRequest'] = _PLATEREQUEST
DESCRIPTOR.message_types_by_name['Rect'] = _RECT
DESCRIPTOR.message_types_by_name['Point'] = _POINT
DESCRIPTOR.message_types_by_name['Plate4Point'] = _PLATE4POINT
DESCRIPTOR.message_types_by_name['Plate'] = _PLATE
DESCRIPTOR.message_types_by_name['PlateResponse'] = _PLATERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PlateRequest = _reflection.GeneratedProtocolMessageType('PlateRequest', (_message.Message,), {
  'DESCRIPTOR' : _PLATEREQUEST,
  '__module__' : 'plate_pb2'
  # @@protoc_insertion_point(class_scope:PlateDetection.PlateRequest)
  })
_sym_db.RegisterMessage(PlateRequest)

Rect = _reflection.GeneratedProtocolMessageType('Rect', (_message.Message,), {
  'DESCRIPTOR' : _RECT,
  '__module__' : 'plate_pb2'
  # @@protoc_insertion_point(class_scope:PlateDetection.Rect)
  })
_sym_db.RegisterMessage(Rect)

Point = _reflection.GeneratedProtocolMessageType('Point', (_message.Message,), {
  'DESCRIPTOR' : _POINT,
  '__module__' : 'plate_pb2'
  # @@protoc_insertion_point(class_scope:PlateDetection.Point)
  })
_sym_db.RegisterMessage(Point)

Plate4Point = _reflection.GeneratedProtocolMessageType('Plate4Point', (_message.Message,), {
  'DESCRIPTOR' : _PLATE4POINT,
  '__module__' : 'plate_pb2'
  # @@protoc_insertion_point(class_scope:PlateDetection.Plate4Point)
  })
_sym_db.RegisterMessage(Plate4Point)

Plate = _reflection.GeneratedProtocolMessageType('Plate', (_message.Message,), {
  'DESCRIPTOR' : _PLATE,
  '__module__' : 'plate_pb2'
  # @@protoc_insertion_point(class_scope:PlateDetection.Plate)
  })
_sym_db.RegisterMessage(Plate)

PlateResponse = _reflection.GeneratedProtocolMessageType('PlateResponse', (_message.Message,), {
  'DESCRIPTOR' : _PLATERESPONSE,
  '__module__' : 'plate_pb2'
  # @@protoc_insertion_point(class_scope:PlateDetection.PlateResponse)
  })
_sym_db.RegisterMessage(PlateResponse)


DESCRIPTOR._options = None

_PLATESERVICE = _descriptor.ServiceDescriptor(
  name='PlateService',
  full_name='PlateDetection.PlateService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=504,
  serialized_end=592,
  methods=[
  _descriptor.MethodDescriptor(
    name='predict',
    full_name='PlateDetection.PlateService.predict',
    index=0,
    containing_service=None,
    input_type=_PLATEREQUEST,
    output_type=_PLATERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PLATESERVICE)

DESCRIPTOR.services_by_name['PlateService'] = _PLATESERVICE

# @@protoc_insertion_point(module_scope)