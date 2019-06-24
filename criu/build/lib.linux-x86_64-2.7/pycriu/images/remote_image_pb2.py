# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: remote-image.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='remote-image.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x12remote-image.proto\"I\n\x11local_image_entry\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x13\n\x0bsnapshot_id\x18\x02 \x02(\t\x12\x11\n\topen_mode\x18\x03 \x02(\r\"X\n\x12remote_image_entry\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x13\n\x0bsnapshot_id\x18\x02 \x02(\t\x12\x11\n\topen_mode\x18\x03 \x02(\r\x12\x0c\n\x04size\x18\x04 \x02(\x04\"(\n\x17local_image_reply_entry\x12\r\n\x05\x65rror\x18\x01 \x02(\r\"(\n\x11snapshot_id_entry\x12\x13\n\x0bsnapshot_id\x18\x01 \x02(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_LOCAL_IMAGE_ENTRY = _descriptor.Descriptor(
  name='local_image_entry',
  full_name='local_image_entry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='local_image_entry.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='snapshot_id', full_name='local_image_entry.snapshot_id', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='open_mode', full_name='local_image_entry.open_mode', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
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
  serialized_start=22,
  serialized_end=95,
)


_REMOTE_IMAGE_ENTRY = _descriptor.Descriptor(
  name='remote_image_entry',
  full_name='remote_image_entry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='remote_image_entry.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='snapshot_id', full_name='remote_image_entry.snapshot_id', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='open_mode', full_name='remote_image_entry.open_mode', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='size', full_name='remote_image_entry.size', index=3,
      number=4, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
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
  serialized_start=97,
  serialized_end=185,
)


_LOCAL_IMAGE_REPLY_ENTRY = _descriptor.Descriptor(
  name='local_image_reply_entry',
  full_name='local_image_reply_entry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='local_image_reply_entry.error', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
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
  serialized_start=187,
  serialized_end=227,
)


_SNAPSHOT_ID_ENTRY = _descriptor.Descriptor(
  name='snapshot_id_entry',
  full_name='snapshot_id_entry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='snapshot_id', full_name='snapshot_id_entry.snapshot_id', index=0,
      number=1, type=9, cpp_type=9, label=2,
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
  serialized_start=229,
  serialized_end=269,
)

DESCRIPTOR.message_types_by_name['local_image_entry'] = _LOCAL_IMAGE_ENTRY
DESCRIPTOR.message_types_by_name['remote_image_entry'] = _REMOTE_IMAGE_ENTRY
DESCRIPTOR.message_types_by_name['local_image_reply_entry'] = _LOCAL_IMAGE_REPLY_ENTRY
DESCRIPTOR.message_types_by_name['snapshot_id_entry'] = _SNAPSHOT_ID_ENTRY

local_image_entry = _reflection.GeneratedProtocolMessageType('local_image_entry', (_message.Message,), dict(
  DESCRIPTOR = _LOCAL_IMAGE_ENTRY,
  __module__ = 'remote_image_pb2'
  # @@protoc_insertion_point(class_scope:local_image_entry)
  ))
_sym_db.RegisterMessage(local_image_entry)

remote_image_entry = _reflection.GeneratedProtocolMessageType('remote_image_entry', (_message.Message,), dict(
  DESCRIPTOR = _REMOTE_IMAGE_ENTRY,
  __module__ = 'remote_image_pb2'
  # @@protoc_insertion_point(class_scope:remote_image_entry)
  ))
_sym_db.RegisterMessage(remote_image_entry)

local_image_reply_entry = _reflection.GeneratedProtocolMessageType('local_image_reply_entry', (_message.Message,), dict(
  DESCRIPTOR = _LOCAL_IMAGE_REPLY_ENTRY,
  __module__ = 'remote_image_pb2'
  # @@protoc_insertion_point(class_scope:local_image_reply_entry)
  ))
_sym_db.RegisterMessage(local_image_reply_entry)

snapshot_id_entry = _reflection.GeneratedProtocolMessageType('snapshot_id_entry', (_message.Message,), dict(
  DESCRIPTOR = _SNAPSHOT_ID_ENTRY,
  __module__ = 'remote_image_pb2'
  # @@protoc_insertion_point(class_scope:snapshot_id_entry)
  ))
_sym_db.RegisterMessage(snapshot_id_entry)


# @@protoc_insertion_point(module_scope)