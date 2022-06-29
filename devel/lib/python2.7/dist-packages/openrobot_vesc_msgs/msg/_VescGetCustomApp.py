# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from openrobot_vesc_msgs/VescGetCustomApp.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg

class VescGetCustomApp(genpy.Message):
  _md5sum = "1e8f9cfbe1d9f55788965982c55ee433"
  _type = "openrobot_vesc_msgs/VescGetCustomApp"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """# VESCuino CDI CUSTOM_APP RX Messages

Header  header
int32 can_devs_num

# Common Data
int32[] can_id
float64[] voltage_input        # input voltage (volt)
float64[] temperature_pcb      # temperature of printed circuit board (degrees Celsius)
float64[] temperature_motor    # temperature of printed circuit board (degrees Celsius)
float64[] current_motor        # motor current (ampere)
float64[] current_input        # input current (ampere)
float64[] duty_cycle           # duty cycle (0 to 1)
float64[] watt_hours           # watt hours
float64[] watt_hours_charged   # watt hours charged
float64[] accum_deg_now        # accumulated degree now
float64[] diff_deg_now	       # degreee difference in 0.1ms(10kHz)
================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id
"""
  __slots__ = ['header','can_devs_num','can_id','voltage_input','temperature_pcb','temperature_motor','current_motor','current_input','duty_cycle','watt_hours','watt_hours_charged','accum_deg_now','diff_deg_now']
  _slot_types = ['std_msgs/Header','int32','int32[]','float64[]','float64[]','float64[]','float64[]','float64[]','float64[]','float64[]','float64[]','float64[]','float64[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,can_devs_num,can_id,voltage_input,temperature_pcb,temperature_motor,current_motor,current_input,duty_cycle,watt_hours,watt_hours_charged,accum_deg_now,diff_deg_now

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(VescGetCustomApp, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.can_devs_num is None:
        self.can_devs_num = 0
      if self.can_id is None:
        self.can_id = []
      if self.voltage_input is None:
        self.voltage_input = []
      if self.temperature_pcb is None:
        self.temperature_pcb = []
      if self.temperature_motor is None:
        self.temperature_motor = []
      if self.current_motor is None:
        self.current_motor = []
      if self.current_input is None:
        self.current_input = []
      if self.duty_cycle is None:
        self.duty_cycle = []
      if self.watt_hours is None:
        self.watt_hours = []
      if self.watt_hours_charged is None:
        self.watt_hours_charged = []
      if self.accum_deg_now is None:
        self.accum_deg_now = []
      if self.diff_deg_now is None:
        self.diff_deg_now = []
    else:
      self.header = std_msgs.msg.Header()
      self.can_devs_num = 0
      self.can_id = []
      self.voltage_input = []
      self.temperature_pcb = []
      self.temperature_motor = []
      self.current_motor = []
      self.current_input = []
      self.duty_cycle = []
      self.watt_hours = []
      self.watt_hours_charged = []
      self.accum_deg_now = []
      self.diff_deg_now = []

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
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.can_devs_num
      buff.write(_get_struct_i().pack(_x))
      length = len(self.can_id)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(struct.Struct(pattern).pack(*self.can_id))
      length = len(self.voltage_input)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.voltage_input))
      length = len(self.temperature_pcb)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.temperature_pcb))
      length = len(self.temperature_motor)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.temperature_motor))
      length = len(self.current_motor)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.current_motor))
      length = len(self.current_input)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.current_input))
      length = len(self.duty_cycle)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.duty_cycle))
      length = len(self.watt_hours)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.watt_hours))
      length = len(self.watt_hours_charged)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.watt_hours_charged))
      length = len(self.accum_deg_now)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.accum_deg_now))
      length = len(self.diff_deg_now)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.diff_deg_now))
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
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 4
      (self.can_devs_num,) = _get_struct_i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.can_id = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.voltage_input = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.temperature_pcb = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.temperature_motor = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.current_motor = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.current_input = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.duty_cycle = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.watt_hours = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.watt_hours_charged = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.accum_deg_now = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.diff_deg_now = s.unpack(str[start:end])
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
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.can_devs_num
      buff.write(_get_struct_i().pack(_x))
      length = len(self.can_id)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(self.can_id.tostring())
      length = len(self.voltage_input)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.voltage_input.tostring())
      length = len(self.temperature_pcb)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.temperature_pcb.tostring())
      length = len(self.temperature_motor)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.temperature_motor.tostring())
      length = len(self.current_motor)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.current_motor.tostring())
      length = len(self.current_input)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.current_input.tostring())
      length = len(self.duty_cycle)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.duty_cycle.tostring())
      length = len(self.watt_hours)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.watt_hours.tostring())
      length = len(self.watt_hours_charged)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.watt_hours_charged.tostring())
      length = len(self.accum_deg_now)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.accum_deg_now.tostring())
      length = len(self.diff_deg_now)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.diff_deg_now.tostring())
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
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 4
      (self.can_devs_num,) = _get_struct_i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.can_id = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.voltage_input = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.temperature_pcb = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.temperature_motor = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.current_motor = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.current_input = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.duty_cycle = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.watt_hours = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.watt_hours_charged = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.accum_deg_now = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.diff_deg_now = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_i = None
def _get_struct_i():
    global _struct_i
    if _struct_i is None:
        _struct_i = struct.Struct("<i")
    return _struct_i
