# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: options.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='options.proto',
  package='v1',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\roptions.proto\x12\x02v1\x1a google/protobuf/descriptor.proto\"6\n\x0c\x46ieldOptions\x12\x0e\n\x04name\x18\xb4\xbev \x01(\t\x12\x16\n\x0csql_nullable\x18\xb5\xbev \x01(\x08\" \n\x0eMessageOptions\x12\x0e\n\x04name\x18\xb4\xbev \x01(\t\"$\n\x0cOneofOptions\x12\x14\n\nmodel_name\x18\x84\xbfv \x01(\t:H\n\rfield_options\x12\x1d.google.protobuf.FieldOptions\x18\x8e\xbfv \x01(\x0b\x32\x10.v1.FieldOptions:N\n\x0fmessage_options\x12\x1f.google.protobuf.MessageOptions\x18\x8f\xbfv \x01(\x0b\x32\x12.v1.MessageOptions:H\n\roneof_options\x12\x1d.google.protobuf.OneofOptions\x18\x85\xbfv \x01(\x0b\x32\x10.v1.OneofOptionsb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,])


FIELD_OPTIONS_FIELD_NUMBER = 1941390
field_options = _descriptor.FieldDescriptor(
  name='field_options', full_name='v1.field_options', index=0,
  number=1941390, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
MESSAGE_OPTIONS_FIELD_NUMBER = 1941391
message_options = _descriptor.FieldDescriptor(
  name='message_options', full_name='v1.message_options', index=1,
  number=1941391, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
ONEOF_OPTIONS_FIELD_NUMBER = 1941381
oneof_options = _descriptor.FieldDescriptor(
  name='oneof_options', full_name='v1.oneof_options', index=2,
  number=1941381, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)


_FIELDOPTIONS = _descriptor.Descriptor(
  name='FieldOptions',
  full_name='v1.FieldOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='v1.FieldOptions.name', index=0,
      number=1941300, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sql_nullable', full_name='v1.FieldOptions.sql_nullable', index=1,
      number=1941301, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=55,
  serialized_end=109,
)


_MESSAGEOPTIONS = _descriptor.Descriptor(
  name='MessageOptions',
  full_name='v1.MessageOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='v1.MessageOptions.name', index=0,
      number=1941300, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_end=143,
)


_ONEOFOPTIONS = _descriptor.Descriptor(
  name='OneofOptions',
  full_name='v1.OneofOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='model_name', full_name='v1.OneofOptions.model_name', index=0,
      number=1941380, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=145,
  serialized_end=181,
)

DESCRIPTOR.message_types_by_name['FieldOptions'] = _FIELDOPTIONS
DESCRIPTOR.message_types_by_name['MessageOptions'] = _MESSAGEOPTIONS
DESCRIPTOR.message_types_by_name['OneofOptions'] = _ONEOFOPTIONS
DESCRIPTOR.extensions_by_name['field_options'] = field_options
DESCRIPTOR.extensions_by_name['message_options'] = message_options
DESCRIPTOR.extensions_by_name['oneof_options'] = oneof_options
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FieldOptions = _reflection.GeneratedProtocolMessageType('FieldOptions', (_message.Message,), {
  'DESCRIPTOR' : _FIELDOPTIONS,
  '__module__' : 'options_pb2'
  # @@protoc_insertion_point(class_scope:v1.FieldOptions)
  })
_sym_db.RegisterMessage(FieldOptions)

MessageOptions = _reflection.GeneratedProtocolMessageType('MessageOptions', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGEOPTIONS,
  '__module__' : 'options_pb2'
  # @@protoc_insertion_point(class_scope:v1.MessageOptions)
  })
_sym_db.RegisterMessage(MessageOptions)

OneofOptions = _reflection.GeneratedProtocolMessageType('OneofOptions', (_message.Message,), {
  'DESCRIPTOR' : _ONEOFOPTIONS,
  '__module__' : 'options_pb2'
  # @@protoc_insertion_point(class_scope:v1.OneofOptions)
  })
_sym_db.RegisterMessage(OneofOptions)

field_options.message_type = _FIELDOPTIONS
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(field_options)
message_options.message_type = _MESSAGEOPTIONS
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(message_options)
oneof_options.message_type = _ONEOFOPTIONS
google_dot_protobuf_dot_descriptor__pb2.OneofOptions.RegisterExtension(oneof_options)

# @@protoc_insertion_point(module_scope)
