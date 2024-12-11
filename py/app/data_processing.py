from dataclasses import dataclass, field
from enum import Enum
from typing import List, Dict

from app import data_processing_pb2
from google.protobuf.json_format import MessageToJson, Parse


@dataclass
class Plugin:
    path: str = ""
    
    _proto_message: data_processing_pb2.Plugin = field(init=False, repr=False)

    def __post_init__(self):
        self._proto_message = data_processing_pb2.Plugin()

    def populate_proto(self):
        self._proto_message.path = self.path

    def serializeAsProtobufString(self) -> bytes:
        self.populate_proto()
        return self._proto_message.SerializeToString()

    @classmethod
    def deserializeFromProtobufString(cls, data: bytes) -> "Plugin":
        message = data_processing_pb2.Plugin()
        message.ParseFromString(data)
        return cls(
            path=message.path,
        )

    def serializeAsJsonString(self) -> str:
        self.populate_proto()
        return MessageToJson(self._proto_message)

    @classmethod
    def deserializeFromJsonString(cls, data: str) -> "Plugin":
        message = data_processing_pb2.Plugin()
        Parse(data, message)
        return cls.deserializeFromProtobufString(message.SerializeToString())

    def __str__(self):
        return self.serializeAsJsonString()

@dataclass
class Signal:
    msg: str = ""
    fields: List[str] = field(default_factory=list)
    
    _proto_message: data_processing_pb2.Signal = field(init=False, repr=False)

    def __post_init__(self):
        self._proto_message = data_processing_pb2.Signal()

    def populate_proto(self):
        self._proto_message.msg = self.msg
        del self._proto_message.fields[:]
        for value in self.fields:
            value.populate_proto()
            tmp = self._proto_message.fields.add()
            tmp.CopyFrom(value._proto_message)

    def serializeAsProtobufString(self) -> bytes:
        self.populate_proto()
        return self._proto_message.SerializeToString()

    @classmethod
    def deserializeFromProtobufString(cls, data: bytes) -> "Signal":
        message = data_processing_pb2.Signal()
        message.ParseFromString(data)
        return cls(
            msg=message.msg,
            fields=[str(value) for value in message.fields],
        )

    def serializeAsJsonString(self) -> str:
        self.populate_proto()
        return MessageToJson(self._proto_message)

    @classmethod
    def deserializeFromJsonString(cls, data: str) -> "Signal":
        message = data_processing_pb2.Signal()
        Parse(data, message)
        return cls.deserializeFromProtobufString(message.SerializeToString())

    def __str__(self):
        return self.serializeAsJsonString()

@dataclass
class DataProcessing:
    plugins: List[Plugin] = field(default_factory=list)
    resampledSignals: List[Signal] = field(default_factory=list)
    
    _proto_message: data_processing_pb2.DataProcessing = field(init=False, repr=False)

    def __post_init__(self):
        self._proto_message = data_processing_pb2.DataProcessing()

    def populate_proto(self):
        del self._proto_message.plugins[:]
        for value in self.plugins:
            value.populate_proto()
            tmp = self._proto_message.plugins.add()
            tmp.CopyFrom(value._proto_message)
        del self._proto_message.resampledSignals[:]
        for value in self.resampledSignals:
            value.populate_proto()
            tmp = self._proto_message.resampledSignals.add()
            tmp.CopyFrom(value._proto_message)

    def serializeAsProtobufString(self) -> bytes:
        self.populate_proto()
        return self._proto_message.SerializeToString()

    @classmethod
    def deserializeFromProtobufString(cls, data: bytes) -> "DataProcessing":
        message = data_processing_pb2.DataProcessing()
        message.ParseFromString(data)
        return cls(
            plugins=[Plugin(value) for value in message.plugins],
            resampledSignals=[Signal(value) for value in message.resampledSignals],
        )

    def serializeAsJsonString(self) -> str:
        self.populate_proto()
        return MessageToJson(self._proto_message)

    @classmethod
    def deserializeFromJsonString(cls, data: str) -> "DataProcessing":
        message = data_processing_pb2.DataProcessing()
        Parse(data, message)
        return cls.deserializeFromProtobufString(message.SerializeToString())

    def __str__(self):
        return self.serializeAsJsonString()