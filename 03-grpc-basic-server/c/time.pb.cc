// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: time.proto

#include "time.pb.h"

#include <algorithm>

#include <google/protobuf/io/coded_stream.h>
#include <google/protobuf/extension_set.h>
#include <google/protobuf/wire_format_lite.h>
#include <google/protobuf/descriptor.h>
#include <google/protobuf/generated_message_reflection.h>
#include <google/protobuf/reflection_ops.h>
#include <google/protobuf/wire_format.h>
// @@protoc_insertion_point(includes)
#include <google/protobuf/port_def.inc>
namespace time_message {
class TimeMessageDefaultTypeInternal {
 public:
  ::PROTOBUF_NAMESPACE_ID::internal::ExplicitlyConstructed<TimeMessage> _instance;
} _TimeMessage_default_instance_;
class TimeRequestDefaultTypeInternal {
 public:
  ::PROTOBUF_NAMESPACE_ID::internal::ExplicitlyConstructed<TimeRequest> _instance;
} _TimeRequest_default_instance_;
}  // namespace time_message
static void InitDefaultsscc_info_TimeMessage_time_2eproto() {
  GOOGLE_PROTOBUF_VERIFY_VERSION;

  {
    void* ptr = &::time_message::_TimeMessage_default_instance_;
    new (ptr) ::time_message::TimeMessage();
    ::PROTOBUF_NAMESPACE_ID::internal::OnShutdownDestroyMessage(ptr);
  }
  ::time_message::TimeMessage::InitAsDefaultInstance();
}

::PROTOBUF_NAMESPACE_ID::internal::SCCInfo<0> scc_info_TimeMessage_time_2eproto =
    {{ATOMIC_VAR_INIT(::PROTOBUF_NAMESPACE_ID::internal::SCCInfoBase::kUninitialized), 0, 0, InitDefaultsscc_info_TimeMessage_time_2eproto}, {}};

static void InitDefaultsscc_info_TimeRequest_time_2eproto() {
  GOOGLE_PROTOBUF_VERIFY_VERSION;

  {
    void* ptr = &::time_message::_TimeRequest_default_instance_;
    new (ptr) ::time_message::TimeRequest();
    ::PROTOBUF_NAMESPACE_ID::internal::OnShutdownDestroyMessage(ptr);
  }
  ::time_message::TimeRequest::InitAsDefaultInstance();
}

::PROTOBUF_NAMESPACE_ID::internal::SCCInfo<0> scc_info_TimeRequest_time_2eproto =
    {{ATOMIC_VAR_INIT(::PROTOBUF_NAMESPACE_ID::internal::SCCInfoBase::kUninitialized), 0, 0, InitDefaultsscc_info_TimeRequest_time_2eproto}, {}};

static ::PROTOBUF_NAMESPACE_ID::Metadata file_level_metadata_time_2eproto[2];
static constexpr ::PROTOBUF_NAMESPACE_ID::EnumDescriptor const** file_level_enum_descriptors_time_2eproto = nullptr;
static constexpr ::PROTOBUF_NAMESPACE_ID::ServiceDescriptor const** file_level_service_descriptors_time_2eproto = nullptr;

const ::PROTOBUF_NAMESPACE_ID::uint32 TableStruct_time_2eproto::offsets[] PROTOBUF_SECTION_VARIABLE(protodesc_cold) = {
  ~0u,  // no _has_bits_
  PROTOBUF_FIELD_OFFSET(::time_message::TimeMessage, _internal_metadata_),
  ~0u,  // no _extensions_
  ~0u,  // no _oneof_case_
  ~0u,  // no _weak_field_map_
  PROTOBUF_FIELD_OFFSET(::time_message::TimeMessage, seconds_),
  PROTOBUF_FIELD_OFFSET(::time_message::TimeMessage, minutes_),
  PROTOBUF_FIELD_OFFSET(::time_message::TimeMessage, hours_),
  PROTOBUF_FIELD_OFFSET(::time_message::TimeMessage, mday_),
  PROTOBUF_FIELD_OFFSET(::time_message::TimeMessage, month_),
  PROTOBUF_FIELD_OFFSET(::time_message::TimeMessage, year_),
  PROTOBUF_FIELD_OFFSET(::time_message::TimeMessage, wday_),
  PROTOBUF_FIELD_OFFSET(::time_message::TimeMessage, yday_),
  PROTOBUF_FIELD_OFFSET(::time_message::TimeMessage, isdst_),
  ~0u,  // no _has_bits_
  PROTOBUF_FIELD_OFFSET(::time_message::TimeRequest, _internal_metadata_),
  ~0u,  // no _extensions_
  ~0u,  // no _oneof_case_
  ~0u,  // no _weak_field_map_
  PROTOBUF_FIELD_OFFSET(::time_message::TimeRequest, seconds_),
  PROTOBUF_FIELD_OFFSET(::time_message::TimeRequest, minutes_),
  PROTOBUF_FIELD_OFFSET(::time_message::TimeRequest, hours_),
  PROTOBUF_FIELD_OFFSET(::time_message::TimeRequest, mday_),
  PROTOBUF_FIELD_OFFSET(::time_message::TimeRequest, month_),
  PROTOBUF_FIELD_OFFSET(::time_message::TimeRequest, year_),
  PROTOBUF_FIELD_OFFSET(::time_message::TimeRequest, wday_),
  PROTOBUF_FIELD_OFFSET(::time_message::TimeRequest, yday_),
  PROTOBUF_FIELD_OFFSET(::time_message::TimeRequest, isdst_),
};
static const ::PROTOBUF_NAMESPACE_ID::internal::MigrationSchema schemas[] PROTOBUF_SECTION_VARIABLE(protodesc_cold) = {
  { 0, -1, sizeof(::time_message::TimeMessage)},
  { 14, -1, sizeof(::time_message::TimeRequest)},
};

static ::PROTOBUF_NAMESPACE_ID::Message const * const file_default_instances[] = {
  reinterpret_cast<const ::PROTOBUF_NAMESPACE_ID::Message*>(&::time_message::_TimeMessage_default_instance_),
  reinterpret_cast<const ::PROTOBUF_NAMESPACE_ID::Message*>(&::time_message::_TimeRequest_default_instance_),
};

const char descriptor_table_protodef_time_2eproto[] PROTOBUF_SECTION_VARIABLE(protodesc_cold) =
  "\n\ntime.proto\022\014time_message\"\224\001\n\013TimeMessa"
  "ge\022\017\n\007seconds\030\001 \001(\r\022\017\n\007minutes\030\002 \001(\r\022\r\n\005"
  "hours\030\003 \001(\r\022\014\n\004mday\030\004 \001(\r\022\r\n\005month\030\005 \001(\r"
  "\022\014\n\004year\030\006 \001(\r\022\014\n\004wday\030\007 \001(\r\022\014\n\004yday\030\010 \001"
  "(\r\022\r\n\005isdst\030\t \001(\r\"\224\001\n\013TimeRequest\022\017\n\007sec"
  "onds\030\001 \001(\010\022\017\n\007minutes\030\002 \001(\010\022\r\n\005hours\030\003 \001"
  "(\010\022\014\n\004mday\030\004 \001(\010\022\r\n\005month\030\005 \001(\010\022\014\n\004year\030"
  "\006 \001(\010\022\014\n\004wday\030\007 \001(\010\022\014\n\004yday\030\010 \001(\010\022\r\n\005isd"
  "st\030\t \001(\0102P\n\013TimeService\022A\n\007GetTime\022\031.tim"
  "e_message.TimeRequest\032\031.time_message.Tim"
  "eMessage\"\000b\006proto3"
  ;
static const ::PROTOBUF_NAMESPACE_ID::internal::DescriptorTable*const descriptor_table_time_2eproto_deps[1] = {
};
static ::PROTOBUF_NAMESPACE_ID::internal::SCCInfoBase*const descriptor_table_time_2eproto_sccs[2] = {
  &scc_info_TimeMessage_time_2eproto.base,
  &scc_info_TimeRequest_time_2eproto.base,
};
static ::PROTOBUF_NAMESPACE_ID::internal::once_flag descriptor_table_time_2eproto_once;
static bool descriptor_table_time_2eproto_initialized = false;
const ::PROTOBUF_NAMESPACE_ID::internal::DescriptorTable descriptor_table_time_2eproto = {
  &descriptor_table_time_2eproto_initialized, descriptor_table_protodef_time_2eproto, "time.proto", 418,
  &descriptor_table_time_2eproto_once, descriptor_table_time_2eproto_sccs, descriptor_table_time_2eproto_deps, 2, 0,
  schemas, file_default_instances, TableStruct_time_2eproto::offsets,
  file_level_metadata_time_2eproto, 2, file_level_enum_descriptors_time_2eproto, file_level_service_descriptors_time_2eproto,
};

// Force running AddDescriptors() at dynamic initialization time.
static bool dynamic_init_dummy_time_2eproto = (  ::PROTOBUF_NAMESPACE_ID::internal::AddDescriptors(&descriptor_table_time_2eproto), true);
namespace time_message {

// ===================================================================

void TimeMessage::InitAsDefaultInstance() {
}
class TimeMessage::_Internal {
 public:
};

TimeMessage::TimeMessage()
  : ::PROTOBUF_NAMESPACE_ID::Message(), _internal_metadata_(nullptr) {
  SharedCtor();
  // @@protoc_insertion_point(constructor:time_message.TimeMessage)
}
TimeMessage::TimeMessage(const TimeMessage& from)
  : ::PROTOBUF_NAMESPACE_ID::Message(),
      _internal_metadata_(nullptr) {
  _internal_metadata_.MergeFrom(from._internal_metadata_);
  ::memcpy(&seconds_, &from.seconds_,
    static_cast<size_t>(reinterpret_cast<char*>(&isdst_) -
    reinterpret_cast<char*>(&seconds_)) + sizeof(isdst_));
  // @@protoc_insertion_point(copy_constructor:time_message.TimeMessage)
}

void TimeMessage::SharedCtor() {
  ::memset(&seconds_, 0, static_cast<size_t>(
      reinterpret_cast<char*>(&isdst_) -
      reinterpret_cast<char*>(&seconds_)) + sizeof(isdst_));
}

TimeMessage::~TimeMessage() {
  // @@protoc_insertion_point(destructor:time_message.TimeMessage)
  SharedDtor();
}

void TimeMessage::SharedDtor() {
}

void TimeMessage::SetCachedSize(int size) const {
  _cached_size_.Set(size);
}
const TimeMessage& TimeMessage::default_instance() {
  ::PROTOBUF_NAMESPACE_ID::internal::InitSCC(&::scc_info_TimeMessage_time_2eproto.base);
  return *internal_default_instance();
}


void TimeMessage::Clear() {
// @@protoc_insertion_point(message_clear_start:time_message.TimeMessage)
  ::PROTOBUF_NAMESPACE_ID::uint32 cached_has_bits = 0;
  // Prevent compiler warnings about cached_has_bits being unused
  (void) cached_has_bits;

  ::memset(&seconds_, 0, static_cast<size_t>(
      reinterpret_cast<char*>(&isdst_) -
      reinterpret_cast<char*>(&seconds_)) + sizeof(isdst_));
  _internal_metadata_.Clear();
}

const char* TimeMessage::_InternalParse(const char* ptr, ::PROTOBUF_NAMESPACE_ID::internal::ParseContext* ctx) {
#define CHK_(x) if (PROTOBUF_PREDICT_FALSE(!(x))) goto failure
  while (!ctx->Done(&ptr)) {
    ::PROTOBUF_NAMESPACE_ID::uint32 tag;
    ptr = ::PROTOBUF_NAMESPACE_ID::internal::ReadTag(ptr, &tag);
    CHK_(ptr);
    switch (tag >> 3) {
      // uint32 seconds = 1;
      case 1:
        if (PROTOBUF_PREDICT_TRUE(static_cast<::PROTOBUF_NAMESPACE_ID::uint8>(tag) == 8)) {
          seconds_ = ::PROTOBUF_NAMESPACE_ID::internal::ReadVarint(&ptr);
          CHK_(ptr);
        } else goto handle_unusual;
        continue;
      // uint32 minutes = 2;
      case 2:
        if (PROTOBUF_PREDICT_TRUE(static_cast<::PROTOBUF_NAMESPACE_ID::uint8>(tag) == 16)) {
          minutes_ = ::PROTOBUF_NAMESPACE_ID::internal::ReadVarint(&ptr);
          CHK_(ptr);
        } else goto handle_unusual;
        continue;
      // uint32 hours = 3;
      case 3:
        if (PROTOBUF_PREDICT_TRUE(static_cast<::PROTOBUF_NAMESPACE_ID::uint8>(tag) == 24)) {
          hours_ = ::PROTOBUF_NAMESPACE_ID::internal::ReadVarint(&ptr);
          CHK_(ptr);
        } else goto handle_unusual;
        continue;
      // uint32 mday = 4;
      case 4:
        if (PROTOBUF_PREDICT_TRUE(static_cast<::PROTOBUF_NAMESPACE_ID::uint8>(tag) == 32)) {
          mday_ = ::PROTOBUF_NAMESPACE_ID::internal::ReadVarint(&ptr);
          CHK_(ptr);
        } else goto handle_unusual;
        continue;
      // uint32 month = 5;
      case 5:
        if (PROTOBUF_PREDICT_TRUE(static_cast<::PROTOBUF_NAMESPACE_ID::uint8>(tag) == 40)) {
          month_ = ::PROTOBUF_NAMESPACE_ID::internal::ReadVarint(&ptr);
          CHK_(ptr);
        } else goto handle_unusual;
        continue;
      // uint32 year = 6;
      case 6:
        if (PROTOBUF_PREDICT_TRUE(static_cast<::PROTOBUF_NAMESPACE_ID::uint8>(tag) == 48)) {
          year_ = ::PROTOBUF_NAMESPACE_ID::internal::ReadVarint(&ptr);
          CHK_(ptr);
        } else goto handle_unusual;
        continue;
      // uint32 wday = 7;
      case 7:
        if (PROTOBUF_PREDICT_TRUE(static_cast<::PROTOBUF_NAMESPACE_ID::uint8>(tag) == 56)) {
          wday_ = ::PROTOBUF_NAMESPACE_ID::internal::ReadVarint(&ptr);
          CHK_(ptr);
        } else goto handle_unusual;
        continue;
      // uint32 yday = 8;
      case 8:
        if (PROTOBUF_PREDICT_TRUE(static_cast<::PROTOBUF_NAMESPACE_ID::uint8>(tag) == 64)) {
          yday_ = ::PROTOBUF_NAMESPACE_ID::internal::ReadVarint(&ptr);
          CHK_(ptr);
        } else goto handle_unusual;
        continue;
      // uint32 isdst = 9;
      case 9:
        if (PROTOBUF_PREDICT_TRUE(static_cast<::PROTOBUF_NAMESPACE_ID::uint8>(tag) == 72)) {
          isdst_ = ::PROTOBUF_NAMESPACE_ID::internal::ReadVarint(&ptr);
          CHK_(ptr);
        } else goto handle_unusual;
        continue;
      default: {
      handle_unusual:
        if ((tag & 7) == 4 || tag == 0) {
          ctx->SetLastTag(tag);
          goto success;
        }
        ptr = UnknownFieldParse(tag, &_internal_metadata_, ptr, ctx);
        CHK_(ptr != nullptr);
        continue;
      }
    }  // switch
  }  // while
success:
  return ptr;
failure:
  ptr = nullptr;
  goto success;
#undef CHK_
}

::PROTOBUF_NAMESPACE_ID::uint8* TimeMessage::InternalSerializeWithCachedSizesToArray(
    ::PROTOBUF_NAMESPACE_ID::uint8* target, ::PROTOBUF_NAMESPACE_ID::io::EpsCopyOutputStream* stream) const {
  // @@protoc_insertion_point(serialize_to_array_start:time_message.TimeMessage)
  ::PROTOBUF_NAMESPACE_ID::uint32 cached_has_bits = 0;
  (void) cached_has_bits;

  // uint32 seconds = 1;
  if (this->seconds() != 0) {
    stream->EnsureSpace(&target);
    target = ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::WriteUInt32ToArray(1, this->_internal_seconds(), target);
  }

  // uint32 minutes = 2;
  if (this->minutes() != 0) {
    stream->EnsureSpace(&target);
    target = ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::WriteUInt32ToArray(2, this->_internal_minutes(), target);
  }

  // uint32 hours = 3;
  if (this->hours() != 0) {
    stream->EnsureSpace(&target);
    target = ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::WriteUInt32ToArray(3, this->_internal_hours(), target);
  }

  // uint32 mday = 4;
  if (this->mday() != 0) {
    stream->EnsureSpace(&target);
    target = ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::WriteUInt32ToArray(4, this->_internal_mday(), target);
  }

  // uint32 month = 5;
  if (this->month() != 0) {
    stream->EnsureSpace(&target);
    target = ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::WriteUInt32ToArray(5, this->_internal_month(), target);
  }

  // uint32 year = 6;
  if (this->year() != 0) {
    stream->EnsureSpace(&target);
    target = ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::WriteUInt32ToArray(6, this->_internal_year(), target);
  }

  // uint32 wday = 7;
  if (this->wday() != 0) {
    stream->EnsureSpace(&target);
    target = ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::WriteUInt32ToArray(7, this->_internal_wday(), target);
  }

  // uint32 yday = 8;
  if (this->yday() != 0) {
    stream->EnsureSpace(&target);
    target = ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::WriteUInt32ToArray(8, this->_internal_yday(), target);
  }

  // uint32 isdst = 9;
  if (this->isdst() != 0) {
    stream->EnsureSpace(&target);
    target = ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::WriteUInt32ToArray(9, this->_internal_isdst(), target);
  }

  if (PROTOBUF_PREDICT_FALSE(_internal_metadata_.have_unknown_fields())) {
    target = ::PROTOBUF_NAMESPACE_ID::internal::WireFormat::InternalSerializeUnknownFieldsToArray(
        _internal_metadata_.unknown_fields(), target, stream);
  }
  // @@protoc_insertion_point(serialize_to_array_end:time_message.TimeMessage)
  return target;
}

size_t TimeMessage::ByteSizeLong() const {
// @@protoc_insertion_point(message_byte_size_start:time_message.TimeMessage)
  size_t total_size = 0;

  ::PROTOBUF_NAMESPACE_ID::uint32 cached_has_bits = 0;
  // Prevent compiler warnings about cached_has_bits being unused
  (void) cached_has_bits;

  // uint32 seconds = 1;
  if (this->seconds() != 0) {
    total_size += 1 +
      ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::UInt32Size(
        this->_internal_seconds());
  }

  // uint32 minutes = 2;
  if (this->minutes() != 0) {
    total_size += 1 +
      ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::UInt32Size(
        this->_internal_minutes());
  }

  // uint32 hours = 3;
  if (this->hours() != 0) {
    total_size += 1 +
      ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::UInt32Size(
        this->_internal_hours());
  }

  // uint32 mday = 4;
  if (this->mday() != 0) {
    total_size += 1 +
      ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::UInt32Size(
        this->_internal_mday());
  }

  // uint32 month = 5;
  if (this->month() != 0) {
    total_size += 1 +
      ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::UInt32Size(
        this->_internal_month());
  }

  // uint32 year = 6;
  if (this->year() != 0) {
    total_size += 1 +
      ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::UInt32Size(
        this->_internal_year());
  }

  // uint32 wday = 7;
  if (this->wday() != 0) {
    total_size += 1 +
      ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::UInt32Size(
        this->_internal_wday());
  }

  // uint32 yday = 8;
  if (this->yday() != 0) {
    total_size += 1 +
      ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::UInt32Size(
        this->_internal_yday());
  }

  // uint32 isdst = 9;
  if (this->isdst() != 0) {
    total_size += 1 +
      ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::UInt32Size(
        this->_internal_isdst());
  }

  if (PROTOBUF_PREDICT_FALSE(_internal_metadata_.have_unknown_fields())) {
    return ::PROTOBUF_NAMESPACE_ID::internal::ComputeUnknownFieldsSize(
        _internal_metadata_, total_size, &_cached_size_);
  }
  int cached_size = ::PROTOBUF_NAMESPACE_ID::internal::ToCachedSize(total_size);
  SetCachedSize(cached_size);
  return total_size;
}

void TimeMessage::MergeFrom(const ::PROTOBUF_NAMESPACE_ID::Message& from) {
// @@protoc_insertion_point(generalized_merge_from_start:time_message.TimeMessage)
  GOOGLE_DCHECK_NE(&from, this);
  const TimeMessage* source =
      ::PROTOBUF_NAMESPACE_ID::DynamicCastToGenerated<TimeMessage>(
          &from);
  if (source == nullptr) {
  // @@protoc_insertion_point(generalized_merge_from_cast_fail:time_message.TimeMessage)
    ::PROTOBUF_NAMESPACE_ID::internal::ReflectionOps::Merge(from, this);
  } else {
  // @@protoc_insertion_point(generalized_merge_from_cast_success:time_message.TimeMessage)
    MergeFrom(*source);
  }
}

void TimeMessage::MergeFrom(const TimeMessage& from) {
// @@protoc_insertion_point(class_specific_merge_from_start:time_message.TimeMessage)
  GOOGLE_DCHECK_NE(&from, this);
  _internal_metadata_.MergeFrom(from._internal_metadata_);
  ::PROTOBUF_NAMESPACE_ID::uint32 cached_has_bits = 0;
  (void) cached_has_bits;

  if (from.seconds() != 0) {
    _internal_set_seconds(from._internal_seconds());
  }
  if (from.minutes() != 0) {
    _internal_set_minutes(from._internal_minutes());
  }
  if (from.hours() != 0) {
    _internal_set_hours(from._internal_hours());
  }
  if (from.mday() != 0) {
    _internal_set_mday(from._internal_mday());
  }
  if (from.month() != 0) {
    _internal_set_month(from._internal_month());
  }
  if (from.year() != 0) {
    _internal_set_year(from._internal_year());
  }
  if (from.wday() != 0) {
    _internal_set_wday(from._internal_wday());
  }
  if (from.yday() != 0) {
    _internal_set_yday(from._internal_yday());
  }
  if (from.isdst() != 0) {
    _internal_set_isdst(from._internal_isdst());
  }
}

void TimeMessage::CopyFrom(const ::PROTOBUF_NAMESPACE_ID::Message& from) {
// @@protoc_insertion_point(generalized_copy_from_start:time_message.TimeMessage)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

void TimeMessage::CopyFrom(const TimeMessage& from) {
// @@protoc_insertion_point(class_specific_copy_from_start:time_message.TimeMessage)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

bool TimeMessage::IsInitialized() const {
  return true;
}

void TimeMessage::InternalSwap(TimeMessage* other) {
  using std::swap;
  _internal_metadata_.Swap(&other->_internal_metadata_);
  swap(seconds_, other->seconds_);
  swap(minutes_, other->minutes_);
  swap(hours_, other->hours_);
  swap(mday_, other->mday_);
  swap(month_, other->month_);
  swap(year_, other->year_);
  swap(wday_, other->wday_);
  swap(yday_, other->yday_);
  swap(isdst_, other->isdst_);
}

::PROTOBUF_NAMESPACE_ID::Metadata TimeMessage::GetMetadata() const {
  return GetMetadataStatic();
}


// ===================================================================

void TimeRequest::InitAsDefaultInstance() {
}
class TimeRequest::_Internal {
 public:
};

TimeRequest::TimeRequest()
  : ::PROTOBUF_NAMESPACE_ID::Message(), _internal_metadata_(nullptr) {
  SharedCtor();
  // @@protoc_insertion_point(constructor:time_message.TimeRequest)
}
TimeRequest::TimeRequest(const TimeRequest& from)
  : ::PROTOBUF_NAMESPACE_ID::Message(),
      _internal_metadata_(nullptr) {
  _internal_metadata_.MergeFrom(from._internal_metadata_);
  ::memcpy(&seconds_, &from.seconds_,
    static_cast<size_t>(reinterpret_cast<char*>(&isdst_) -
    reinterpret_cast<char*>(&seconds_)) + sizeof(isdst_));
  // @@protoc_insertion_point(copy_constructor:time_message.TimeRequest)
}

void TimeRequest::SharedCtor() {
  ::memset(&seconds_, 0, static_cast<size_t>(
      reinterpret_cast<char*>(&isdst_) -
      reinterpret_cast<char*>(&seconds_)) + sizeof(isdst_));
}

TimeRequest::~TimeRequest() {
  // @@protoc_insertion_point(destructor:time_message.TimeRequest)
  SharedDtor();
}

void TimeRequest::SharedDtor() {
}

void TimeRequest::SetCachedSize(int size) const {
  _cached_size_.Set(size);
}
const TimeRequest& TimeRequest::default_instance() {
  ::PROTOBUF_NAMESPACE_ID::internal::InitSCC(&::scc_info_TimeRequest_time_2eproto.base);
  return *internal_default_instance();
}


void TimeRequest::Clear() {
// @@protoc_insertion_point(message_clear_start:time_message.TimeRequest)
  ::PROTOBUF_NAMESPACE_ID::uint32 cached_has_bits = 0;
  // Prevent compiler warnings about cached_has_bits being unused
  (void) cached_has_bits;

  ::memset(&seconds_, 0, static_cast<size_t>(
      reinterpret_cast<char*>(&isdst_) -
      reinterpret_cast<char*>(&seconds_)) + sizeof(isdst_));
  _internal_metadata_.Clear();
}

const char* TimeRequest::_InternalParse(const char* ptr, ::PROTOBUF_NAMESPACE_ID::internal::ParseContext* ctx) {
#define CHK_(x) if (PROTOBUF_PREDICT_FALSE(!(x))) goto failure
  while (!ctx->Done(&ptr)) {
    ::PROTOBUF_NAMESPACE_ID::uint32 tag;
    ptr = ::PROTOBUF_NAMESPACE_ID::internal::ReadTag(ptr, &tag);
    CHK_(ptr);
    switch (tag >> 3) {
      // bool seconds = 1;
      case 1:
        if (PROTOBUF_PREDICT_TRUE(static_cast<::PROTOBUF_NAMESPACE_ID::uint8>(tag) == 8)) {
          seconds_ = ::PROTOBUF_NAMESPACE_ID::internal::ReadVarint(&ptr);
          CHK_(ptr);
        } else goto handle_unusual;
        continue;
      // bool minutes = 2;
      case 2:
        if (PROTOBUF_PREDICT_TRUE(static_cast<::PROTOBUF_NAMESPACE_ID::uint8>(tag) == 16)) {
          minutes_ = ::PROTOBUF_NAMESPACE_ID::internal::ReadVarint(&ptr);
          CHK_(ptr);
        } else goto handle_unusual;
        continue;
      // bool hours = 3;
      case 3:
        if (PROTOBUF_PREDICT_TRUE(static_cast<::PROTOBUF_NAMESPACE_ID::uint8>(tag) == 24)) {
          hours_ = ::PROTOBUF_NAMESPACE_ID::internal::ReadVarint(&ptr);
          CHK_(ptr);
        } else goto handle_unusual;
        continue;
      // bool mday = 4;
      case 4:
        if (PROTOBUF_PREDICT_TRUE(static_cast<::PROTOBUF_NAMESPACE_ID::uint8>(tag) == 32)) {
          mday_ = ::PROTOBUF_NAMESPACE_ID::internal::ReadVarint(&ptr);
          CHK_(ptr);
        } else goto handle_unusual;
        continue;
      // bool month = 5;
      case 5:
        if (PROTOBUF_PREDICT_TRUE(static_cast<::PROTOBUF_NAMESPACE_ID::uint8>(tag) == 40)) {
          month_ = ::PROTOBUF_NAMESPACE_ID::internal::ReadVarint(&ptr);
          CHK_(ptr);
        } else goto handle_unusual;
        continue;
      // bool year = 6;
      case 6:
        if (PROTOBUF_PREDICT_TRUE(static_cast<::PROTOBUF_NAMESPACE_ID::uint8>(tag) == 48)) {
          year_ = ::PROTOBUF_NAMESPACE_ID::internal::ReadVarint(&ptr);
          CHK_(ptr);
        } else goto handle_unusual;
        continue;
      // bool wday = 7;
      case 7:
        if (PROTOBUF_PREDICT_TRUE(static_cast<::PROTOBUF_NAMESPACE_ID::uint8>(tag) == 56)) {
          wday_ = ::PROTOBUF_NAMESPACE_ID::internal::ReadVarint(&ptr);
          CHK_(ptr);
        } else goto handle_unusual;
        continue;
      // bool yday = 8;
      case 8:
        if (PROTOBUF_PREDICT_TRUE(static_cast<::PROTOBUF_NAMESPACE_ID::uint8>(tag) == 64)) {
          yday_ = ::PROTOBUF_NAMESPACE_ID::internal::ReadVarint(&ptr);
          CHK_(ptr);
        } else goto handle_unusual;
        continue;
      // bool isdst = 9;
      case 9:
        if (PROTOBUF_PREDICT_TRUE(static_cast<::PROTOBUF_NAMESPACE_ID::uint8>(tag) == 72)) {
          isdst_ = ::PROTOBUF_NAMESPACE_ID::internal::ReadVarint(&ptr);
          CHK_(ptr);
        } else goto handle_unusual;
        continue;
      default: {
      handle_unusual:
        if ((tag & 7) == 4 || tag == 0) {
          ctx->SetLastTag(tag);
          goto success;
        }
        ptr = UnknownFieldParse(tag, &_internal_metadata_, ptr, ctx);
        CHK_(ptr != nullptr);
        continue;
      }
    }  // switch
  }  // while
success:
  return ptr;
failure:
  ptr = nullptr;
  goto success;
#undef CHK_
}

::PROTOBUF_NAMESPACE_ID::uint8* TimeRequest::InternalSerializeWithCachedSizesToArray(
    ::PROTOBUF_NAMESPACE_ID::uint8* target, ::PROTOBUF_NAMESPACE_ID::io::EpsCopyOutputStream* stream) const {
  // @@protoc_insertion_point(serialize_to_array_start:time_message.TimeRequest)
  ::PROTOBUF_NAMESPACE_ID::uint32 cached_has_bits = 0;
  (void) cached_has_bits;

  // bool seconds = 1;
  if (this->seconds() != 0) {
    stream->EnsureSpace(&target);
    target = ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::WriteBoolToArray(1, this->_internal_seconds(), target);
  }

  // bool minutes = 2;
  if (this->minutes() != 0) {
    stream->EnsureSpace(&target);
    target = ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::WriteBoolToArray(2, this->_internal_minutes(), target);
  }

  // bool hours = 3;
  if (this->hours() != 0) {
    stream->EnsureSpace(&target);
    target = ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::WriteBoolToArray(3, this->_internal_hours(), target);
  }

  // bool mday = 4;
  if (this->mday() != 0) {
    stream->EnsureSpace(&target);
    target = ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::WriteBoolToArray(4, this->_internal_mday(), target);
  }

  // bool month = 5;
  if (this->month() != 0) {
    stream->EnsureSpace(&target);
    target = ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::WriteBoolToArray(5, this->_internal_month(), target);
  }

  // bool year = 6;
  if (this->year() != 0) {
    stream->EnsureSpace(&target);
    target = ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::WriteBoolToArray(6, this->_internal_year(), target);
  }

  // bool wday = 7;
  if (this->wday() != 0) {
    stream->EnsureSpace(&target);
    target = ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::WriteBoolToArray(7, this->_internal_wday(), target);
  }

  // bool yday = 8;
  if (this->yday() != 0) {
    stream->EnsureSpace(&target);
    target = ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::WriteBoolToArray(8, this->_internal_yday(), target);
  }

  // bool isdst = 9;
  if (this->isdst() != 0) {
    stream->EnsureSpace(&target);
    target = ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::WriteBoolToArray(9, this->_internal_isdst(), target);
  }

  if (PROTOBUF_PREDICT_FALSE(_internal_metadata_.have_unknown_fields())) {
    target = ::PROTOBUF_NAMESPACE_ID::internal::WireFormat::InternalSerializeUnknownFieldsToArray(
        _internal_metadata_.unknown_fields(), target, stream);
  }
  // @@protoc_insertion_point(serialize_to_array_end:time_message.TimeRequest)
  return target;
}

size_t TimeRequest::ByteSizeLong() const {
// @@protoc_insertion_point(message_byte_size_start:time_message.TimeRequest)
  size_t total_size = 0;

  ::PROTOBUF_NAMESPACE_ID::uint32 cached_has_bits = 0;
  // Prevent compiler warnings about cached_has_bits being unused
  (void) cached_has_bits;

  // bool seconds = 1;
  if (this->seconds() != 0) {
    total_size += 1 + 1;
  }

  // bool minutes = 2;
  if (this->minutes() != 0) {
    total_size += 1 + 1;
  }

  // bool hours = 3;
  if (this->hours() != 0) {
    total_size += 1 + 1;
  }

  // bool mday = 4;
  if (this->mday() != 0) {
    total_size += 1 + 1;
  }

  // bool month = 5;
  if (this->month() != 0) {
    total_size += 1 + 1;
  }

  // bool year = 6;
  if (this->year() != 0) {
    total_size += 1 + 1;
  }

  // bool wday = 7;
  if (this->wday() != 0) {
    total_size += 1 + 1;
  }

  // bool yday = 8;
  if (this->yday() != 0) {
    total_size += 1 + 1;
  }

  // bool isdst = 9;
  if (this->isdst() != 0) {
    total_size += 1 + 1;
  }

  if (PROTOBUF_PREDICT_FALSE(_internal_metadata_.have_unknown_fields())) {
    return ::PROTOBUF_NAMESPACE_ID::internal::ComputeUnknownFieldsSize(
        _internal_metadata_, total_size, &_cached_size_);
  }
  int cached_size = ::PROTOBUF_NAMESPACE_ID::internal::ToCachedSize(total_size);
  SetCachedSize(cached_size);
  return total_size;
}

void TimeRequest::MergeFrom(const ::PROTOBUF_NAMESPACE_ID::Message& from) {
// @@protoc_insertion_point(generalized_merge_from_start:time_message.TimeRequest)
  GOOGLE_DCHECK_NE(&from, this);
  const TimeRequest* source =
      ::PROTOBUF_NAMESPACE_ID::DynamicCastToGenerated<TimeRequest>(
          &from);
  if (source == nullptr) {
  // @@protoc_insertion_point(generalized_merge_from_cast_fail:time_message.TimeRequest)
    ::PROTOBUF_NAMESPACE_ID::internal::ReflectionOps::Merge(from, this);
  } else {
  // @@protoc_insertion_point(generalized_merge_from_cast_success:time_message.TimeRequest)
    MergeFrom(*source);
  }
}

void TimeRequest::MergeFrom(const TimeRequest& from) {
// @@protoc_insertion_point(class_specific_merge_from_start:time_message.TimeRequest)
  GOOGLE_DCHECK_NE(&from, this);
  _internal_metadata_.MergeFrom(from._internal_metadata_);
  ::PROTOBUF_NAMESPACE_ID::uint32 cached_has_bits = 0;
  (void) cached_has_bits;

  if (from.seconds() != 0) {
    _internal_set_seconds(from._internal_seconds());
  }
  if (from.minutes() != 0) {
    _internal_set_minutes(from._internal_minutes());
  }
  if (from.hours() != 0) {
    _internal_set_hours(from._internal_hours());
  }
  if (from.mday() != 0) {
    _internal_set_mday(from._internal_mday());
  }
  if (from.month() != 0) {
    _internal_set_month(from._internal_month());
  }
  if (from.year() != 0) {
    _internal_set_year(from._internal_year());
  }
  if (from.wday() != 0) {
    _internal_set_wday(from._internal_wday());
  }
  if (from.yday() != 0) {
    _internal_set_yday(from._internal_yday());
  }
  if (from.isdst() != 0) {
    _internal_set_isdst(from._internal_isdst());
  }
}

void TimeRequest::CopyFrom(const ::PROTOBUF_NAMESPACE_ID::Message& from) {
// @@protoc_insertion_point(generalized_copy_from_start:time_message.TimeRequest)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

void TimeRequest::CopyFrom(const TimeRequest& from) {
// @@protoc_insertion_point(class_specific_copy_from_start:time_message.TimeRequest)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

bool TimeRequest::IsInitialized() const {
  return true;
}

void TimeRequest::InternalSwap(TimeRequest* other) {
  using std::swap;
  _internal_metadata_.Swap(&other->_internal_metadata_);
  swap(seconds_, other->seconds_);
  swap(minutes_, other->minutes_);
  swap(hours_, other->hours_);
  swap(mday_, other->mday_);
  swap(month_, other->month_);
  swap(year_, other->year_);
  swap(wday_, other->wday_);
  swap(yday_, other->yday_);
  swap(isdst_, other->isdst_);
}

::PROTOBUF_NAMESPACE_ID::Metadata TimeRequest::GetMetadata() const {
  return GetMetadataStatic();
}


// @@protoc_insertion_point(namespace_scope)
}  // namespace time_message
PROTOBUF_NAMESPACE_OPEN
template<> PROTOBUF_NOINLINE ::time_message::TimeMessage* Arena::CreateMaybeMessage< ::time_message::TimeMessage >(Arena* arena) {
  return Arena::CreateInternal< ::time_message::TimeMessage >(arena);
}
template<> PROTOBUF_NOINLINE ::time_message::TimeRequest* Arena::CreateMaybeMessage< ::time_message::TimeRequest >(Arena* arena) {
  return Arena::CreateInternal< ::time_message::TimeRequest >(arena);
}
PROTOBUF_NAMESPACE_CLOSE

// @@protoc_insertion_point(global_scope)
#include <google/protobuf/port_undef.inc>
