from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .speech_record import SpeechRecord
    from .speech_response_next_record_position import SpeechResponse_nextRecordPosition

@dataclass
class SpeechResponse(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # 次開始位置
    next_record_position: Optional[SpeechResponse_nextRecordPosition] = None
    # 総結果件数
    number_of_records: Optional[int] = None
    # 返戻件数
    number_of_return: Optional[int] = None
    # The speechRecord property
    speech_record: Optional[list[SpeechRecord]] = None
    # 開始位置
    start_record: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SpeechResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SpeechResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SpeechResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .speech_record import SpeechRecord
        from .speech_response_next_record_position import SpeechResponse_nextRecordPosition

        from .speech_record import SpeechRecord
        from .speech_response_next_record_position import SpeechResponse_nextRecordPosition

        fields: dict[str, Callable[[Any], None]] = {
            "nextRecordPosition": lambda n : setattr(self, 'next_record_position', n.get_object_value(SpeechResponse_nextRecordPosition)),
            "numberOfRecords": lambda n : setattr(self, 'number_of_records', n.get_int_value()),
            "numberOfReturn": lambda n : setattr(self, 'number_of_return', n.get_int_value()),
            "speechRecord": lambda n : setattr(self, 'speech_record', n.get_collection_of_object_values(SpeechRecord)),
            "startRecord": lambda n : setattr(self, 'start_record', n.get_int_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("nextRecordPosition", self.next_record_position)
        writer.write_int_value("numberOfRecords", self.number_of_records)
        writer.write_int_value("numberOfReturn", self.number_of_return)
        writer.write_collection_of_object_values("speechRecord", self.speech_record)
        writer.write_int_value("startRecord", self.start_record)
        writer.write_additional_data_value(self.additional_data)
    

