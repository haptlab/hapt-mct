# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fpv_image.proto

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
  name='fpv_image.proto',
  package='hapt',
  syntax='proto3',
  serialized_pb=_b('\n\x0f\x66pv_image.proto\x12\x04hapt\"8\n\x08\x46pvImage\x12\r\n\x05width\x18\x01 \x01(\x05\x12\x0e\n\x06height\x18\x02 \x01(\x05\x12\r\n\x05image\x18\x03 \x01(\x0c\x62\x06proto3')
)




_FPVIMAGE = _descriptor.Descriptor(
  name='FpvImage',
  full_name='hapt.FpvImage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='width', full_name='hapt.FpvImage.width', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='height', full_name='hapt.FpvImage.height', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='image', full_name='hapt.FpvImage.image', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=81,
)

DESCRIPTOR.message_types_by_name['FpvImage'] = _FPVIMAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FpvImage = _reflection.GeneratedProtocolMessageType('FpvImage', (_message.Message,), dict(
  DESCRIPTOR = _FPVIMAGE,
  __module__ = 'fpv_image_pb2'
  # @@protoc_insertion_point(class_scope:hapt.FpvImage)
  ))
_sym_db.RegisterMessage(FpvImage)


# @@protoc_insertion_point(module_scope)
