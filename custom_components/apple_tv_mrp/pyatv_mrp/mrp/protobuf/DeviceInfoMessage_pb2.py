# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyatv/mrp/protobuf/DeviceInfoMessage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import ProtocolMessage_pb2 as pyatv_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pyatv/mrp/protobuf/DeviceInfoMessage.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n*pyatv/mrp/protobuf/DeviceInfoMessage.proto\x1a(pyatv/mrp/protobuf/ProtocolMessage.proto\"\x8c\x04\n\x11\x44\x65viceInfoMessage\x12\x18\n\x10uniqueIdentifier\x18\x01 \x02(\t\x12\x0c\n\x04name\x18\x02 \x02(\t\x12\x1a\n\x12localizedModelName\x18\x03 \x01(\t\x12\x1a\n\x12systemBuildVersion\x18\x04 \x02(\t\x12#\n\x1b\x61pplicationBundleIdentifier\x18\x05 \x02(\t\x12 \n\x18\x61pplicationBundleVersion\x18\x06 \x01(\t\x12\x17\n\x0fprotocolVersion\x18\x07 \x02(\x05\x12 \n\x18lastSupportedMessageType\x18\x08 \x01(\r\x12\x1d\n\x15supportsSystemPairing\x18\t \x01(\x08\x12\x15\n\rallowsPairing\x18\n \x01(\x08\x12\x11\n\tconnected\x18\x0b \x01(\x08\x12\x1e\n\x16systemMediaApplication\x18\x0c \x01(\t\x12\x13\n\x0bsupportsACL\x18\r \x01(\x08\x12\x1b\n\x13supportsSharedQueue\x18\x0e \x01(\x08\x12\x1e\n\x16supportsExtendedMotion\x18\x0f \x01(\x08\x12\x18\n\x10\x62luetoothAddress\x18\x10 \x01(\x0c\x12\x1a\n\x12sharedQueueVersion\x18\x11 \x01(\r\x12$\n\x1clocalReceiverPairingIdentity\x18\x13 \x01(\t:?\n\x11\x64\x65viceInfoMessage\x12\x10.ProtocolMessage\x18\x14 \x01(\x0b\x32\x12.DeviceInfoMessage')
  ,
  dependencies=[pyatv_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2.DESCRIPTOR,])


DEVICEINFOMESSAGE_FIELD_NUMBER = 20
deviceInfoMessage = _descriptor.FieldDescriptor(
  name='deviceInfoMessage', full_name='deviceInfoMessage', index=0,
  number=20, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None, file=DESCRIPTOR)


_DEVICEINFOMESSAGE = _descriptor.Descriptor(
  name='DeviceInfoMessage',
  full_name='DeviceInfoMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uniqueIdentifier', full_name='DeviceInfoMessage.uniqueIdentifier', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='DeviceInfoMessage.name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='localizedModelName', full_name='DeviceInfoMessage.localizedModelName', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='systemBuildVersion', full_name='DeviceInfoMessage.systemBuildVersion', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='applicationBundleIdentifier', full_name='DeviceInfoMessage.applicationBundleIdentifier', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='applicationBundleVersion', full_name='DeviceInfoMessage.applicationBundleVersion', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='protocolVersion', full_name='DeviceInfoMessage.protocolVersion', index=6,
      number=7, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lastSupportedMessageType', full_name='DeviceInfoMessage.lastSupportedMessageType', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='supportsSystemPairing', full_name='DeviceInfoMessage.supportsSystemPairing', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='allowsPairing', full_name='DeviceInfoMessage.allowsPairing', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connected', full_name='DeviceInfoMessage.connected', index=10,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='systemMediaApplication', full_name='DeviceInfoMessage.systemMediaApplication', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='supportsACL', full_name='DeviceInfoMessage.supportsACL', index=12,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='supportsSharedQueue', full_name='DeviceInfoMessage.supportsSharedQueue', index=13,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='supportsExtendedMotion', full_name='DeviceInfoMessage.supportsExtendedMotion', index=14,
      number=15, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bluetoothAddress', full_name='DeviceInfoMessage.bluetoothAddress', index=15,
      number=16, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sharedQueueVersion', full_name='DeviceInfoMessage.sharedQueueVersion', index=16,
      number=17, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='localReceiverPairingIdentity', full_name='DeviceInfoMessage.localReceiverPairingIdentity', index=17,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=89,
  serialized_end=613,
)

DESCRIPTOR.message_types_by_name['DeviceInfoMessage'] = _DEVICEINFOMESSAGE
DESCRIPTOR.extensions_by_name['deviceInfoMessage'] = deviceInfoMessage
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DeviceInfoMessage = _reflection.GeneratedProtocolMessageType('DeviceInfoMessage', (_message.Message,), dict(
  DESCRIPTOR = _DEVICEINFOMESSAGE,
  __module__ = 'pyatv.mrp.protobuf.DeviceInfoMessage_pb2'
  # @@protoc_insertion_point(class_scope:DeviceInfoMessage)
  ))
_sym_db.RegisterMessage(DeviceInfoMessage)

deviceInfoMessage.message_type = _DEVICEINFOMESSAGE
pyatv_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2.ProtocolMessage.RegisterExtension(deviceInfoMessage)

# @@protoc_insertion_point(module_scope)
