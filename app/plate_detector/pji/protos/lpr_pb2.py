# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pji/protos/lpr.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14pji/protos/lpr.proto\x12\x12LicenseRecognition\"\x18\n\x07Request\x12\r\n\x05image\x18\x01 \x01(\x0c\"@\n\x04Rect\x12\x0c\n\x04left\x18\x01 \x01(\x02\x12\r\n\x05right\x18\x02 \x01(\x02\x12\x0b\n\x03top\x18\x03 \x01(\x02\x12\x0e\n\x06\x62ottom\x18\x04 \x01(\x02\"O\n\x05Plate\x12\x0f\n\x07license\x18\x01 \x01(\t\x12\r\n\x05score\x18\x02 \x01(\x01\x12&\n\x04rect\x18\x03 \x01(\x0b\x32\x18.LicenseRecognition.Rect\"5\n\x08Response\x12)\n\x06plates\x18\x01 \x03(\x0b\x32\x19.LicenseRecognition.Plate2d\n\x18LicenseRecognitionEngine\x12H\n\x0bRecognition\x12\x1b.LicenseRecognition.Request\x1a\x1c.LicenseRecognition.ResponseBB\n*com.pji.cloud.research.license.recognitionB\x12LicenseRecognitionP\x01\x62\x06proto3')



_REQUEST = DESCRIPTOR.message_types_by_name['Request']
_RECT = DESCRIPTOR.message_types_by_name['Rect']
_PLATE = DESCRIPTOR.message_types_by_name['Plate']
_RESPONSE = DESCRIPTOR.message_types_by_name['Response']
Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'pji.protos.lpr_pb2'
  # @@protoc_insertion_point(class_scope:LicenseRecognition.Request)
  })
_sym_db.RegisterMessage(Request)

Rect = _reflection.GeneratedProtocolMessageType('Rect', (_message.Message,), {
  'DESCRIPTOR' : _RECT,
  '__module__' : 'pji.protos.lpr_pb2'
  # @@protoc_insertion_point(class_scope:LicenseRecognition.Rect)
  })
_sym_db.RegisterMessage(Rect)

Plate = _reflection.GeneratedProtocolMessageType('Plate', (_message.Message,), {
  'DESCRIPTOR' : _PLATE,
  '__module__' : 'pji.protos.lpr_pb2'
  # @@protoc_insertion_point(class_scope:LicenseRecognition.Plate)
  })
_sym_db.RegisterMessage(Plate)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'pji.protos.lpr_pb2'
  # @@protoc_insertion_point(class_scope:LicenseRecognition.Response)
  })
_sym_db.RegisterMessage(Response)

_LICENSERECOGNITIONENGINE = DESCRIPTOR.services_by_name['LicenseRecognitionEngine']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n*com.pji.cloud.research.license.recognitionB\022LicenseRecognitionP\001'
  _REQUEST._serialized_start=44
  _REQUEST._serialized_end=68
  _RECT._serialized_start=70
  _RECT._serialized_end=134
  _PLATE._serialized_start=136
  _PLATE._serialized_end=215
  _RESPONSE._serialized_start=217
  _RESPONSE._serialized_end=270
  _LICENSERECOGNITIONENGINE._serialized_start=272
  _LICENSERECOGNITIONENGINE._serialized_end=372
# @@protoc_insertion_point(module_scope)
