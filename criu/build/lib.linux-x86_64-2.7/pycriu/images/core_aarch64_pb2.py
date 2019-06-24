# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: core-aarch64.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import opts_pb2 as opts__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='core-aarch64.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x12\x63ore-aarch64.proto\x1a\nopts.proto\"O\n\x17user_aarch64_regs_entry\x12\x0c\n\x04regs\x18\x01 \x03(\x04\x12\n\n\x02sp\x18\x02 \x02(\x04\x12\n\n\x02pc\x18\x03 \x02(\x04\x12\x0e\n\x06pstate\x18\x04 \x02(\x04\"N\n!user_aarch64_fpsimd_context_entry\x12\r\n\x05vregs\x18\x01 \x03(\x04\x12\x0c\n\x04\x66psr\x18\x02 \x02(\r\x12\x0c\n\x04\x66pcr\x18\x03 \x02(\r\"\xa6\x01\n\x13thread_info_aarch64\x12\x1d\n\x0e\x63lear_tid_addr\x18\x01 \x02(\x04\x42\x05\xd2?\x02\x08\x01\x12\x0b\n\x03tls\x18\x02 \x02(\x04\x12/\n\x06gpregs\x18\x03 \x02(\x0b\x32\x18.user_aarch64_regs_entryB\x05\xd2?\x02\x08\x01\x12\x32\n\x06\x66psimd\x18\x04 \x02(\x0b\x32\".user_aarch64_fpsimd_context_entry')
  ,
  dependencies=[opts__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_USER_AARCH64_REGS_ENTRY = _descriptor.Descriptor(
  name='user_aarch64_regs_entry',
  full_name='user_aarch64_regs_entry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='regs', full_name='user_aarch64_regs_entry.regs', index=0,
      number=1, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sp', full_name='user_aarch64_regs_entry.sp', index=1,
      number=2, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pc', full_name='user_aarch64_regs_entry.pc', index=2,
      number=3, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pstate', full_name='user_aarch64_regs_entry.pstate', index=3,
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
  serialized_start=34,
  serialized_end=113,
)


_USER_AARCH64_FPSIMD_CONTEXT_ENTRY = _descriptor.Descriptor(
  name='user_aarch64_fpsimd_context_entry',
  full_name='user_aarch64_fpsimd_context_entry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vregs', full_name='user_aarch64_fpsimd_context_entry.vregs', index=0,
      number=1, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fpsr', full_name='user_aarch64_fpsimd_context_entry.fpsr', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fpcr', full_name='user_aarch64_fpsimd_context_entry.fpcr', index=2,
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
  serialized_start=115,
  serialized_end=193,
)


_THREAD_INFO_AARCH64 = _descriptor.Descriptor(
  name='thread_info_aarch64',
  full_name='thread_info_aarch64',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='clear_tid_addr', full_name='thread_info_aarch64.clear_tid_addr', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322?\002\010\001'))),
    _descriptor.FieldDescriptor(
      name='tls', full_name='thread_info_aarch64.tls', index=1,
      number=2, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gpregs', full_name='thread_info_aarch64.gpregs', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322?\002\010\001'))),
    _descriptor.FieldDescriptor(
      name='fpsimd', full_name='thread_info_aarch64.fpsimd', index=3,
      number=4, type=11, cpp_type=10, label=2,
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
  serialized_start=196,
  serialized_end=362,
)

_THREAD_INFO_AARCH64.fields_by_name['gpregs'].message_type = _USER_AARCH64_REGS_ENTRY
_THREAD_INFO_AARCH64.fields_by_name['fpsimd'].message_type = _USER_AARCH64_FPSIMD_CONTEXT_ENTRY
DESCRIPTOR.message_types_by_name['user_aarch64_regs_entry'] = _USER_AARCH64_REGS_ENTRY
DESCRIPTOR.message_types_by_name['user_aarch64_fpsimd_context_entry'] = _USER_AARCH64_FPSIMD_CONTEXT_ENTRY
DESCRIPTOR.message_types_by_name['thread_info_aarch64'] = _THREAD_INFO_AARCH64

user_aarch64_regs_entry = _reflection.GeneratedProtocolMessageType('user_aarch64_regs_entry', (_message.Message,), dict(
  DESCRIPTOR = _USER_AARCH64_REGS_ENTRY,
  __module__ = 'core_aarch64_pb2'
  # @@protoc_insertion_point(class_scope:user_aarch64_regs_entry)
  ))
_sym_db.RegisterMessage(user_aarch64_regs_entry)

user_aarch64_fpsimd_context_entry = _reflection.GeneratedProtocolMessageType('user_aarch64_fpsimd_context_entry', (_message.Message,), dict(
  DESCRIPTOR = _USER_AARCH64_FPSIMD_CONTEXT_ENTRY,
  __module__ = 'core_aarch64_pb2'
  # @@protoc_insertion_point(class_scope:user_aarch64_fpsimd_context_entry)
  ))
_sym_db.RegisterMessage(user_aarch64_fpsimd_context_entry)

thread_info_aarch64 = _reflection.GeneratedProtocolMessageType('thread_info_aarch64', (_message.Message,), dict(
  DESCRIPTOR = _THREAD_INFO_AARCH64,
  __module__ = 'core_aarch64_pb2'
  # @@protoc_insertion_point(class_scope:thread_info_aarch64)
  ))
_sym_db.RegisterMessage(thread_info_aarch64)


_THREAD_INFO_AARCH64.fields_by_name['clear_tid_addr'].has_options = True
_THREAD_INFO_AARCH64.fields_by_name['clear_tid_addr']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322?\002\010\001'))
_THREAD_INFO_AARCH64.fields_by_name['gpregs'].has_options = True
_THREAD_INFO_AARCH64.fields_by_name['gpregs']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322?\002\010\001'))
# @@protoc_insertion_point(module_scope)
