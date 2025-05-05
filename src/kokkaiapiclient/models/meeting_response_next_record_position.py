from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import ComposedTypeWrapper, Parsable, ParseNode, ParseNodeHelper, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .meeting_response_next_record_position_member1 import MeetingResponse_nextRecordPositionMember1

@dataclass
class MeetingResponse_nextRecordPosition(ComposedTypeWrapper, Parsable):
    """
    Composed type wrapper for classes int, MeetingResponse_nextRecordPositionMember1
    """
    # Composed type representation for type int
    integer: Optional[int] = None
    # Composed type representation for type MeetingResponse_nextRecordPositionMember1
    meeting_response_next_record_position_member1: Optional[MeetingResponse_nextRecordPositionMember1] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MeetingResponse_nextRecordPosition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MeetingResponse_nextRecordPosition
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        result = MeetingResponse_nextRecordPosition()
        if integer_value := parse_node.get_int_value():
            result.integer = integer_value
        else:
            from .meeting_response_next_record_position_member1 import MeetingResponse_nextRecordPositionMember1

            result.meeting_response_next_record_position_member1 = MeetingResponse_nextRecordPositionMember1()
        return result
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .meeting_response_next_record_position_member1 import MeetingResponse_nextRecordPositionMember1

        if self.meeting_response_next_record_position_member1:
            return ParseNodeHelper.merge_deserializers_for_intersection_wrapper(self.meeting_response_next_record_position_member1)
        return {}
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        if self.integer:
            writer.write_int_value(None, self.integer)
        else:
            writer.write_object_value(None, self.meeting_response_next_record_position_member1)
    

