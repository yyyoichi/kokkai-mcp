from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .meeting_speech_record_speaker import MeetingSpeechRecord_speaker
    from .meeting_speech_record_speaker_group import MeetingSpeechRecord_speakerGroup
    from .meeting_speech_record_speaker_position import MeetingSpeechRecord_speakerPosition
    from .meeting_speech_record_speaker_yomi import MeetingSpeechRecord_speakerYomi
    from .speaker_role import SpeakerRole

@dataclass
class MeetingSpeechRecord(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # レコード作成日時 (YYYY-MM-DD HH:mm:ss)。
    create_time: Optional[str] = None
    # 発言者名。
    speaker: Optional[MeetingSpeechRecord_speaker] = None
    # 発言者の所属会派。
    speaker_group: Optional[MeetingSpeechRecord_speakerGroup] = None
    # 発言者の肩書き。
    speaker_position: Optional[MeetingSpeechRecord_speakerPosition] = None
    # 発言者の役割。
    speaker_role: Optional[SpeakerRole] = None
    # 発言者名の読み仮名。
    speaker_yomi: Optional[MeetingSpeechRecord_speakerYomi] = None
    # 発言内容。
    speech: Optional[str] = None
    # 発言ID。"issueID_発言番号"形式。
    speech_i_d: Optional[str] = None
    # 発言順序。
    speech_order: Optional[int] = None
    # 発言テキストへのURL。
    speech_u_r_l: Optional[str] = None
    # 発言が開始されるページ番号。
    start_page: Optional[int] = None
    # レコード更新日時 (YYYY-MM-DD HH:mm:ss)。
    update_time: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MeetingSpeechRecord:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MeetingSpeechRecord
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MeetingSpeechRecord()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .meeting_speech_record_speaker import MeetingSpeechRecord_speaker
        from .meeting_speech_record_speaker_group import MeetingSpeechRecord_speakerGroup
        from .meeting_speech_record_speaker_position import MeetingSpeechRecord_speakerPosition
        from .meeting_speech_record_speaker_yomi import MeetingSpeechRecord_speakerYomi
        from .speaker_role import SpeakerRole

        from .meeting_speech_record_speaker import MeetingSpeechRecord_speaker
        from .meeting_speech_record_speaker_group import MeetingSpeechRecord_speakerGroup
        from .meeting_speech_record_speaker_position import MeetingSpeechRecord_speakerPosition
        from .meeting_speech_record_speaker_yomi import MeetingSpeechRecord_speakerYomi
        from .speaker_role import SpeakerRole

        fields: dict[str, Callable[[Any], None]] = {
            "createTime": lambda n : setattr(self, 'create_time', n.get_str_value()),
            "speaker": lambda n : setattr(self, 'speaker', n.get_object_value(MeetingSpeechRecord_speaker)),
            "speakerGroup": lambda n : setattr(self, 'speaker_group', n.get_object_value(MeetingSpeechRecord_speakerGroup)),
            "speakerPosition": lambda n : setattr(self, 'speaker_position', n.get_object_value(MeetingSpeechRecord_speakerPosition)),
            "speakerRole": lambda n : setattr(self, 'speaker_role', n.get_enum_value(SpeakerRole)),
            "speakerYomi": lambda n : setattr(self, 'speaker_yomi', n.get_object_value(MeetingSpeechRecord_speakerYomi)),
            "speech": lambda n : setattr(self, 'speech', n.get_str_value()),
            "speechID": lambda n : setattr(self, 'speech_i_d', n.get_str_value()),
            "speechOrder": lambda n : setattr(self, 'speech_order', n.get_int_value()),
            "speechURL": lambda n : setattr(self, 'speech_u_r_l', n.get_str_value()),
            "startPage": lambda n : setattr(self, 'start_page', n.get_int_value()),
            "updateTime": lambda n : setattr(self, 'update_time', n.get_str_value()),
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
        writer.write_str_value("createTime", self.create_time)
        writer.write_object_value("speaker", self.speaker)
        writer.write_object_value("speakerGroup", self.speaker_group)
        writer.write_object_value("speakerPosition", self.speaker_position)
        writer.write_enum_value("speakerRole", self.speaker_role)
        writer.write_object_value("speakerYomi", self.speaker_yomi)
        writer.write_str_value("speech", self.speech)
        writer.write_str_value("speechID", self.speech_i_d)
        writer.write_int_value("speechOrder", self.speech_order)
        writer.write_str_value("speechURL", self.speech_u_r_l)
        writer.write_int_value("startPage", self.start_page)
        writer.write_str_value("updateTime", self.update_time)
        writer.write_additional_data_value(self.additional_data)
    

