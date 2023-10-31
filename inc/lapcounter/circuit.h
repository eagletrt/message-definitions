#ifndef CIRCUIT_H
#define CIRCUIT_H

#include "circuit.pb.h"

#include <cstdint>
#include <string>
#include <vector>
#include <unordered_map>

namespace Serializers
{
namespace LapCounter
{
struct Vector
{
    double x;
    double y;
    
    Vector() = default;
    Vector(const PbLapCounter::Vector& protobuf);
    operator PbLapCounter::Vector() const;

    std::string serializeAsJsonString() const;
    std::string serializeAsProtobufString() const;
    bool deserializeFromJsonString(const std::string& str);
    bool deserializeFromProtobufString(const std::string& str);
};

struct Line
{
    Vector position;
    Vector direction;
    
    Line() = default;
    Line(const PbLapCounter::Line& protobuf);
    operator PbLapCounter::Line() const;

    std::string serializeAsJsonString() const;
    std::string serializeAsProtobufString() const;
    bool deserializeFromJsonString(const std::string& str);
    bool deserializeFromProtobufString(const std::string& str);
};

struct Circuit
{
    std::string circuitId;
    std::vector<Line> checksLines;
    std::vector<Line> sectorsLines;
    
    Circuit() = default;
    Circuit(const PbLapCounter::Circuit& protobuf);
    operator PbLapCounter::Circuit() const;

    std::string serializeAsJsonString() const;
    std::string serializeAsProtobufString() const;
    bool deserializeFromJsonString(const std::string& str);
    bool deserializeFromProtobufString(const std::string& str);
};
}
}

#endif