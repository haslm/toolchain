# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: core-arm.proto

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
  name='core-arm.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x0e\x63ore-arm.proto\x1a\nopts.proto\"\xf5\x01\n\x13user_arm_regs_entry\x12\n\n\x02r0\x18\x01 \x02(\r\x12\n\n\x02r1\x18\x02 \x02(\r\x12\n\n\x02r2\x18\x03 \x02(\r\x12\n\n\x02r3\x18\x04 \x02(\r\x12\n\n\x02r4\x18\x05 \x02(\r\x12\n\n\x02r5\x18\x06 \x02(\r\x12\n\n\x02r6\x18\x07 \x02(\r\x12\n\n\x02r7\x18\x08 \x02(\r\x12\n\n\x02r8\x18\t \x02(\r\x12\n\n\x02r9\x18\n \x02(\r\x12\x0b\n\x03r10\x18\x0b \x02(\r\x12\n\n\x02\x66p\x18\x0c \x02(\r\x12\n\n\x02ip\x18\r \x02(\r\x12\n\n\x02sp\x18\x0e \x02(\r\x12\n\n\x02lr\x18\x0f \x02(\r\x12\n\n\x02pc\x18\x10 \x02(\r\x12\x0c\n\x04\x63psr\x18\x11 \x02(\r\x12\x0f\n\x07orig_r0\x18\x12 \x02(\r\"j\n\x17user_arm_vfpstate_entry\x12\x10\n\x08vfp_regs\x18\x01 \x03(\x04\x12\r\n\x05\x66pscr\x18\x02 \x02(\r\x12\r\n\x05\x66pexc\x18\x03 \x02(\r\x12\x0e\n\x06\x66pinst\x18\x04 \x02(\r\x12\x0f\n\x07\x66pinst2\x18\x05 \x02(\r\"\x95\x01\n\x0fthread_info_arm\x12\x1d\n\x0e\x63lear_tid_addr\x18\x01 \x02(\x04\x42\x05\xd2?\x02\x08\x01\x12\x0b\n\x03tls\x18\x02 \x02(\r\x12+\n\x06gpregs\x18\x03 \x02(\x0b\x32\x14.user_arm_regs_entryB\x05\xd2?\x02\x08\x01\x12)\n\x07\x66pstate\x18\x04 \x02(\x0b\x32\x18.user_arm_vfpstate_entry')
  ,
  dependencies=[opts__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_USER_ARM_REGS_ENTRY = _descriptor.Descriptor(
  name='user_arm_regs_entry',
  full_name='user_arm_regs_entry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='r0', full_name='user_arm_regs_entry.r0', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='r1', full_name='user_arm_regs_entry.r1', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='r2', full_name='user_arm_regs_entry.r2', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='r3', full_name='user_arm_regs_entry.r3', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='r4', full_name='user_arm_regs_entry.r4', index=4,
      number=5, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='r5', full_name='user_arm_regs_entry.r5', index=5,
      number=6, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='r6', full_name='user_arm_regs_entry.r6', index=6,
      number=7, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='r7', full_name='user_arm_regs_entry.r7', index=7,
      number=8, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='r8', full_name='user_arm_regs_entry.r8', index=8,
      number=9, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='r9', full_name='user_arm_regs_entry.r9', index=9,
      number=10, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='r10', full_name='user_arm_regs_entry.r10', index=10,
      number=11, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fp', full_name='user_arm_regs_entry.fp', index=11,
      number=12, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ip', full_name='user_arm_regs_entry.ip', index=12,
      number=13, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sp', full_name='user_arm_regs_entry.sp', index=13,
      number=14, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lr', full_name='user_arm_regs_entry.lr', index=14,
      number=15, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pc', full_name='user_arm_regs_entry.pc', index=15,
      number=16, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cpsr', full_name='user_arm_regs_entry.cpsr', index=16,
      number=17, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='orig_r0', full_name='user_arm_regs_entry.orig_r0', index=17,
      number=18, type=13, cpp_type=3, label=2,
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
  serialized_start=31,
  serialized_end=276,
)


_USER_ARM_VFPSTATE_ENTRY = _descriptor.Descriptor(
  name='user_arm_vfpstate_entry',
  full_name='user_arm_vfpstate_entry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vfp_regs', full_name='user_arm_vfpstate_entry.vfp_regs', index=0,
      number=1, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fpscr', full_name='user_arm_vfpstate_entry.fpscr', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fpexc', full_name='user_arm_vfpstate_entry.fpexc', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fpinst', full_name='user_arm_vfpstate_entry.fpinst', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fpinst2', full_name='user_arm_vfpstate_entry.fpinst2', index=4,
      number=5, type=13, cpp_type=3, label=2,
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
  serialized_start=278,
  serialized_end=384,
)


_THREAD_INFO_ARM = _descriptor.Descriptor(
  name='thread_info_arm',
  full_name='thread_info_arm',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='clear_tid_addr', full_name='thread_info_arm.clear_tid_addr', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322?\002\010\001'))),
    _descriptor.FieldDescriptor(
      name='tls', full_name='thread_info_arm.tls', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gpregs', full_name='thread_info_arm.gpregs', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322?\002\010\001'))),
    _descriptor.FieldDescriptor(
      name='fpstate', full_name='thread_info_arm.fpstate', index=3,
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
  serialized_start=387,
  serialized_end=536,
)

_THREAD_INFO_ARM.fields_by_name['gpregs'].message_type = _USER_ARM_REGS_ENTRY
_THREAD_INFO_ARM.fields_by_name['fpstate'].message_type = _USER_ARM_VFPSTATE_ENTRY
DESCRIPTOR.message_types_by_name['user_arm_regs_entry'] = _USER_ARM_REGS_ENTRY
DESCRIPTOR.message_types_by_name['user_arm_vfpstate_entry'] = _USER_ARM_VFPSTATE_ENTRY
DESCRIPTOR.message_types_by_name['thread_info_arm'] = _THREAD_INFO_ARM

user_arm_regs_entry = _reflection.GeneratedProtocolMessageType('user_arm_regs_entry', (_message.Message,), dict(
  DESCRIPTOR = _USER_ARM_REGS_ENTRY,
  __module__ = 'core_arm_pb2'
  # @@protoc_insertion_point(class_scope:user_arm_regs_entry)
  ))
_sym_db.RegisterMessage(user_arm_regs_entry)

user_arm_vfpstate_entry = _reflection.GeneratedProtocolMessageType('user_arm_vfpstate_entry', (_message.Message,), dict(
  DESCRIPTOR = _USER_ARM_VFPSTATE_ENTRY,
  __module__ = 'core_arm_pb2'
  # @@protoc_insertion_point(class_scope:user_arm_vfpstate_entry)
  ))
_sym_db.RegisterMessage(user_arm_vfpstate_entry)

thread_info_arm = _reflection.GeneratedProtocolMessageType('thread_info_arm', (_message.Message,), dict(
  DESCRIPTOR = _THREAD_INFO_ARM,
  __module__ = 'core_arm_pb2'
  # @@protoc_insertion_point(class_scope:thread_info_arm)
  ))
_sym_db.RegisterMessage(thread_info_arm)


_THREAD_INFO_ARM.fields_by_name['clear_tid_addr'].has_options = True
_THREAD_INFO_ARM.fields_by_name['clear_tid_addr']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322?\002\010\001'))
_THREAD_INFO_ARM.fields_by_name['gpregs'].has_options = True
_THREAD_INFO_ARM.fields_by_name['gpregs']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322?\002\010\001'))
# @@protoc_insertion_point(module_scope)
