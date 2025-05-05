from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import ComposedTypeWrapper, Parsable, ParseNode, ParseNodeHelper, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .meeting_response_meeting_record_closing_member1 import MeetingResponse_meetingRecord_closingMember1

@dataclass
class MeetingResponse_meetingRecord_closing(ComposedTypeWrapper, Parsable):
    """
    Composed type wrapper for classes bool, MeetingResponse_meetingRecord_closingMember1
    """
    # Composed type representation for type bool
    boolean: Optional[bool] = None
    # Composed type representation for type MeetingResponse_meetingRecord_closingMember1
    meeting_response_meeting_record_closing_member1: Optional[MeetingResponse_meetingRecord_closingMember1] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MeetingResponse_meetingRecord_closing:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MeetingResponse_meetingRecord_closing
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        result = MeetingResponse_meetingRecord_closing()
        if boolean_value := parse_node.get_bool_value():
            result.boolean = boolean_value
        else:
            from .meeting_response_meeting_record_closing_member1 import MeetingResponse_meetingRecord_closingMember1

            result.meeting_response_meeting_record_closing_member1 = MeetingResponse_meetingRecord_closingMember1()
        return result
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .meeting_response_meeting_record_closing_member1 import MeetingResponse_meetingRecord_closingMember1

        if self.meeting_response_meeting_record_closing_member1:
            return ParseNodeHelper.merge_deserializers_for_intersection_wrapper(self.meeting_response_meeting_record_closing_member1)
        return {}
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        if self.boolean:
            writer.write_bool_value(None, self.boolean)
        else:
            writer.write_object_value(None, self.meeting_response_meeting_record_closing_member1)
    

