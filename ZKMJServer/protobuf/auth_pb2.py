# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: auth.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import assets_pb2 as assets__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='auth.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\nauth.proto\x1a\x0c\x61ssets.proto\"/\n\x0cVCodeRequest\x12\x0f\n\x07nUserID\x18\x01 \x02(\x05\x12\x0e\n\x06sPhone\x18\x02 \x02(\t\"3\n\rVCodeResponse\x12\x12\n\nnErrorCode\x18\x01 \x02(\x05\x12\x0e\n\x06sVCode\x18\x02 \x02(\t\"_\n\x0b\x41uthRequest\x12\x0f\n\x07nUserID\x18\x01 \x02(\x05\x12\x0e\n\x06sPhone\x18\x02 \x02(\t\x12\x0e\n\x06sVCode\x18\x03 \x02(\t\x12\x11\n\tsRealName\x18\x04 \x02(\t\x12\x0c\n\x04sSFZ\x18\x05 \x02(\t\"B\n\x0c\x41uthResponse\x12\x12\n\nnErrorCode\x18\x01 \x02(\x05\x12\x1e\n\x08newasset\x18\x02 \x01(\x0b\x32\x0c.AssetUpdate')
  ,
  dependencies=[assets__pb2.DESCRIPTOR,])




_VCODEREQUEST = _descriptor.Descriptor(
  name='VCodeRequest',
  full_name='VCodeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nUserID', full_name='VCodeRequest.nUserID', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sPhone', full_name='VCodeRequest.sPhone', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=75,
)


_VCODERESPONSE = _descriptor.Descriptor(
  name='VCodeResponse',
  full_name='VCodeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nErrorCode', full_name='VCodeResponse.nErrorCode', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sVCode', full_name='VCodeResponse.sVCode', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=77,
  serialized_end=128,
)


_AUTHREQUEST = _descriptor.Descriptor(
  name='AuthRequest',
  full_name='AuthRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nUserID', full_name='AuthRequest.nUserID', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sPhone', full_name='AuthRequest.sPhone', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sVCode', full_name='AuthRequest.sVCode', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sRealName', full_name='AuthRequest.sRealName', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sSFZ', full_name='AuthRequest.sSFZ', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=130,
  serialized_end=225,
)


_AUTHRESPONSE = _descriptor.Descriptor(
  name='AuthResponse',
  full_name='AuthResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nErrorCode', full_name='AuthResponse.nErrorCode', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='newasset', full_name='AuthResponse.newasset', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=227,
  serialized_end=293,
)

_AUTHRESPONSE.fields_by_name['newasset'].message_type = assets__pb2._ASSETUPDATE
DESCRIPTOR.message_types_by_name['VCodeRequest'] = _VCODEREQUEST
DESCRIPTOR.message_types_by_name['VCodeResponse'] = _VCODERESPONSE
DESCRIPTOR.message_types_by_name['AuthRequest'] = _AUTHREQUEST
DESCRIPTOR.message_types_by_name['AuthResponse'] = _AUTHRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VCodeRequest = _reflection.GeneratedProtocolMessageType('VCodeRequest', (_message.Message,), dict(
  DESCRIPTOR = _VCODEREQUEST,
  __module__ = 'auth_pb2'
  # @@protoc_insertion_point(class_scope:VCodeRequest)
  ))
_sym_db.RegisterMessage(VCodeRequest)

VCodeResponse = _reflection.GeneratedProtocolMessageType('VCodeResponse', (_message.Message,), dict(
  DESCRIPTOR = _VCODERESPONSE,
  __module__ = 'auth_pb2'
  # @@protoc_insertion_point(class_scope:VCodeResponse)
  ))
_sym_db.RegisterMessage(VCodeResponse)

AuthRequest = _reflection.GeneratedProtocolMessageType('AuthRequest', (_message.Message,), dict(
  DESCRIPTOR = _AUTHREQUEST,
  __module__ = 'auth_pb2'
  # @@protoc_insertion_point(class_scope:AuthRequest)
  ))
_sym_db.RegisterMessage(AuthRequest)

AuthResponse = _reflection.GeneratedProtocolMessageType('AuthResponse', (_message.Message,), dict(
  DESCRIPTOR = _AUTHRESPONSE,
  __module__ = 'auth_pb2'
  # @@protoc_insertion_point(class_scope:AuthResponse)
  ))
_sym_db.RegisterMessage(AuthResponse)


# @@protoc_insertion_point(module_scope)
