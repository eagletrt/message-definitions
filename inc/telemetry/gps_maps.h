#ifndef SERIALIZERS_GPS_MAPS_H
#define SERIALIZERS_GPS_MAPS_H

#include "gps_maps.pb.h"

#include <cstdint>
#include <string>
#include <vector>
#include <unordered_map>

namespace Serializers
{
namespace Telemetry
{
struct GPSMapOrigin
{
    double latitude;
    double longitude;
    double ecefX;
    double ecefY;
    double ecefZ;
    
    GPSMapOrigin() = default;
    GPSMapOrigin(const PbTelemetry::GPSMapOrigin& protobuf);
    operator PbTelemetry::GPSMapOrigin() const;

    std::string serializeAsJsonString() const;
    std::string serializeAsProtobufString() const;
    bool deserializeFromJsonString(const std::string& str);
    bool deserializeFromProtobufString(const std::string& str);
};

struct GPSMapOrigins
{
    std::string selectedMap;
    std::unordered_map<std::string, GPSMapOrigin> origins;
    
    GPSMapOrigins() = default;
    GPSMapOrigins(const PbTelemetry::GPSMapOrigins& protobuf);
    operator PbTelemetry::GPSMapOrigins() const;

    std::string serializeAsJsonString() const;
    std::string serializeAsProtobufString() const;
    bool deserializeFromJsonString(const std::string& str);
    bool deserializeFromProtobufString(const std::string& str);
};
}
}

#endif