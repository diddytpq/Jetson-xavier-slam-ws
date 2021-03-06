# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from openrobot_vesc_msgs/VescSetCustomApp.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class VescSetCustomApp(genpy.Message):
  _md5sum = "c46f4ff65abd5670780793173869e6b9"
  _type = "openrobot_vesc_msgs/VescSetCustomApp"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# VESCuino CDI CUSTOM_APP TX Messages

int32       num_of_id
int32[]     id_set
int32[]     comm_set
bool[]      can_forward_set
float64[]   value_set
int32       data_bytes"""
  __slots__ = ['num_of_id','id_set','comm_set','can_forward_set','value_set','data_bytes']
  _slot_types = ['int32','int32[]','int32[]','bool[]','float64[]','int32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       num_of_id,id_set,comm_set,can_forward_set,value_set,data_bytes

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(VescSetCustomApp, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.num_of_id is None:
        self.num_of_id = 0
      if self.id_set is None:
        self.id_set = []
      if self.comm_set is None:
        self.comm_set = []
      if self.can_forward_set is None:
        self.can_forward_set = []
      if self.value_set is None:
        self.value_set = []
      if self.data_bytes is None:
        self.data_bytes = 0
    else:
      self.num_of_id = 0
      self.id_set = []
      self.comm_set = []
      self.can_forward_set = []
      self.value_set = []
      self.data_bytes = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.num_of_id
      buff.write(_get_struct_i().pack(_x))
      length = len(self.id_set)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(struct.Struct(pattern).pack(*self.id_set))
      length = len(self.comm_set)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(struct.Struct(pattern).pack(*self.comm_set))
      length = len(self.can_forward_set)
      buff.write(_struct_I.pack(length))
      pattern = '<%sB'%length
      buff.write(struct.Struct(pattern).pack(*self.can_forward_set))
      length = len(self.value_set)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.value_set))
      _x = self.data_bytes
      buff.write(_get_struct_i().pack(_x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 4
      (self.num_of_id,) = _get_struct_i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.id_set = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.comm_set = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sB'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.can_forward_set = s.unpack(str[start:end])
      self.can_forward_set = list(map(bool, self.can_forward_set))
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.value_set = s.unpack(str[start:end])
      start = end
      end += 4
      (self.data_bytes,) = _get_struct_i().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.num_of_id
      buff.write(_get_struct_i().pack(_x))
      length = len(self.id_set)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(self.id_set.tostring())
      length = len(self.comm_set)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(self.comm_set.tostring())
      length = len(self.can_forward_set)
      buff.write(_struct_I.pack(length))
      pattern = '<%sB'%length
      buff.write(self.can_forward_set.tostring())
      length = len(self.value_set)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.value_set.tostring())
      _x = self.data_bytes
      buff.write(_get_struct_i().pack(_x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 4
      (self.num_of_id,) = _get_struct_i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.id_set = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.comm_set = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sB'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.can_forward_set = numpy.frombuffer(str[start:end], dtype=numpy.bool, count=length)
      self.can_forward_set = list(map(bool, self.can_forward_set))
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.value_set = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (self.data_bytes,) = _get_struct_i().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_i = None
def _get_struct_i():
    global _struct_i
    if _struct_i is None:
        _struct_i = struct.Struct("<i")
    return _struct_i
