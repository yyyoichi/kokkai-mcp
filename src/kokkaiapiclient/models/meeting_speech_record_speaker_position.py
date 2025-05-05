from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import ComposedTypeWrapper, Parsable, ParseNode, ParseNodeHelper, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .meeting_speech_record_speaker_position_member1 import MeetingSpeechRecord_speakerPositionMember1

@dataclass
class MeetingSpeechRecord_speakerPosition(ComposedTypeWrapper, Parsable):
    """
    Composed type wrapper for classes MeetingSpeechRecord_speakerPositionMember1, str
    """
    # Composed type representation for type MeetingSpeechRecord_speakerPositionMember1
    meeting_speech_record_speaker_position_member1: Optional[MeetingSpeechRecord_speakerPositionMember1] = None
    # Composed type representation for type str
    string: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MeetingSpeechRecord_speakerPosition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MeetingSpeechRecord_speakerPosition
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        result = MeetingSpeechRecord_speakerPosition()
        if string_value := parse_node.get_str_value():
            result.string = string_value
        else:
            from .meeting_speech_record_speaker_position_member1 import MeetingSpeechRecord_speakerPositionMember1

            result.meeting_speech_record_speaker_position_member1 = MeetingSpeechRecord_speakerPositionMember1()
        return result
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .meeting_speech_record_speaker_position_member1 import MeetingSpeechRecord_speakerPositionMember1

        if self.meeting_speech_record_speaker_position_member1:
            return ParseNodeHelper.merge_deserializers_for_intersection_wrapper(self.meeting_speech_record_speaker_position_member1)
        return {}
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        if self.string:
            writer.write_str_value(None, self.string)
        else:
            writer.write_object_value(None, self.meeting_speech_record_speaker_position_member1)
    

