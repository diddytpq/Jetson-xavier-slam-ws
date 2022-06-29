// Generated by gencpp from file openrobot_vesc_msgs/VescSetCommand.msg
// DO NOT EDIT!


#ifndef OPENROBOT_VESC_MSGS_MESSAGE_VESCSETCOMMAND_H
#define OPENROBOT_VESC_MSGS_MESSAGE_VESCSETCOMMAND_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace openrobot_vesc_msgs
{
template <class ContainerAllocator>
struct VescSetCommand_
{
  typedef VescSetCommand_<ContainerAllocator> Type;

  VescSetCommand_()
    : data(0.0)
    , send_can(false)
    , can_id(0)  {
    }
  VescSetCommand_(const ContainerAllocator& _alloc)
    : data(0.0)
    , send_can(false)
    , can_id(0)  {
  (void)_alloc;
    }



   typedef double _data_type;
  _data_type data;

   typedef uint8_t _send_can_type;
  _send_can_type send_can;

   typedef uint8_t _can_id_type;
  _can_id_type can_id;





  typedef boost::shared_ptr< ::openrobot_vesc_msgs::VescSetCommand_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::openrobot_vesc_msgs::VescSetCommand_<ContainerAllocator> const> ConstPtr;

}; // struct VescSetCommand_

typedef ::openrobot_vesc_msgs::VescSetCommand_<std::allocator<void> > VescSetCommand;

typedef boost::shared_ptr< ::openrobot_vesc_msgs::VescSetCommand > VescSetCommandPtr;
typedef boost::shared_ptr< ::openrobot_vesc_msgs::VescSetCommand const> VescSetCommandConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::openrobot_vesc_msgs::VescSetCommand_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::openrobot_vesc_msgs::VescSetCommand_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::openrobot_vesc_msgs::VescSetCommand_<ContainerAllocator1> & lhs, const ::openrobot_vesc_msgs::VescSetCommand_<ContainerAllocator2> & rhs)
{
  return lhs.data == rhs.data &&
    lhs.send_can == rhs.send_can &&
    lhs.can_id == rhs.can_id;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::openrobot_vesc_msgs::VescSetCommand_<ContainerAllocator1> & lhs, const ::openrobot_vesc_msgs::VescSetCommand_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace openrobot_vesc_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::openrobot_vesc_msgs::VescSetCommand_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::openrobot_vesc_msgs::VescSetCommand_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::openrobot_vesc_msgs::VescSetCommand_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::openrobot_vesc_msgs::VescSetCommand_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::openrobot_vesc_msgs::VescSetCommand_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::openrobot_vesc_msgs::VescSetCommand_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::openrobot_vesc_msgs::VescSetCommand_<ContainerAllocator> >
{
  static const char* value()
  {
    return "9cffe44297165322576d6c2378fd0593";
  }

  static const char* value(const ::openrobot_vesc_msgs::VescSetCommand_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x9cffe44297165322ULL;
  static const uint64_t static_value2 = 0x576d6c2378fd0593ULL;
};

template<class ContainerAllocator>
struct DataType< ::openrobot_vesc_msgs::VescSetCommand_<ContainerAllocator> >
{
  static const char* value()
  {
    return "openrobot_vesc_msgs/VescSetCommand";
  }

  static const char* value(const ::openrobot_vesc_msgs::VescSetCommand_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::openrobot_vesc_msgs::VescSetCommand_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float64 data\n"
"bool  send_can\n"
"uint8 can_id\n"
;
  }

  static const char* value(const ::openrobot_vesc_msgs::VescSetCommand_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::openrobot_vesc_msgs::VescSetCommand_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.data);
      stream.next(m.send_can);
      stream.next(m.can_id);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct VescSetCommand_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::openrobot_vesc_msgs::VescSetCommand_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::openrobot_vesc_msgs::VescSetCommand_<ContainerAllocator>& v)
  {
    s << indent << "data: ";
    Printer<double>::stream(s, indent + "  ", v.data);
    s << indent << "send_can: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.send_can);
    s << indent << "can_id: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.can_id);
  }
};

} // namespace message_operations
} // namespace ros

#endif // OPENROBOT_VESC_MSGS_MESSAGE_VESCSETCOMMAND_H
