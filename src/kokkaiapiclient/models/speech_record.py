from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .image_kind import ImageKind
    from .name_of_house import NameOfHouse
    from .speaker_role import SpeakerRole
    from .speech_record_closing import SpeechRecord_closing
    from .speech_record_pdf_u_r_l import SpeechRecord_pdfURL
    from .speech_record_speaker import SpeechRecord_speaker
    from .speech_record_speaker_group import SpeechRecord_speakerGroup
    from .speech_record_speaker_position import SpeechRecord_speakerPosition
    from .speech_record_speaker_yomi import SpeechRecord_speakerYomi

@dataclass
class SpeechRecord(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # 閉会中フラグ。nullの場合あり。
    closing: Optional[SpeechRecord_closing] = None
    # 開催日付 (YYYY-MM-DD)。
    date: Optional[str] = None
    # 資料種別。
    image_kind: Optional[ImageKind] = None
    # 号数。"第issue号"形式。
    issue: Optional[str] = None
    # 会議録ID。
    issue_i_d: Optional[str] = None
    # 会議録テキスト表示画面へのURL。
    meeting_u_r_l: Optional[str] = None
    # 院名。
    name_of_house: Optional[NameOfHouse] = None
    # 会議名。
    name_of_meeting: Optional[str] = None
    # 会議録PDF表示画面へのURL。nullの場合あり。
    pdf_u_r_l: Optional[SpeechRecord_pdfURL] = None
    # 検索対象箇所。
    search_object: Optional[int] = None
    # 国会回次。
    session: Optional[int] = None
    # 発言者名。
    speaker: Optional[SpeechRecord_speaker] = None
    # 発言者の所属会派。nullの場合あり。
    speaker_group: Optional[SpeechRecord_speakerGroup] = None
    # 発言者の肩書き。nullの場合あり。
    speaker_position: Optional[SpeechRecord_speakerPosition] = None
    # 発言者の役割。nullの場合あり。
    speaker_role: Optional[SpeakerRole] = None
    # 発言者名の読み仮名。nullの場合あり。
    speaker_yomi: Optional[SpeechRecord_speakerYomi] = None
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SpeechRecord:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SpeechRecord
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SpeechRecord()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .image_kind import ImageKind
        from .name_of_house import NameOfHouse
        from .speaker_role import SpeakerRole
        from .speech_record_closing import SpeechRecord_closing
        from .speech_record_pdf_u_r_l import SpeechRecord_pdfURL
        from .speech_record_speaker import SpeechRecord_speaker
        from .speech_record_speaker_group import SpeechRecord_speakerGroup
        from .speech_record_speaker_position import SpeechRecord_speakerPosition
        from .speech_record_speaker_yomi import SpeechRecord_speakerYomi

        from .image_kind import ImageKind
        from .name_of_house import NameOfHouse
        from .speaker_role import SpeakerRole
        from .speech_record_closing import SpeechRecord_closing
        from .speech_record_pdf_u_r_l import SpeechRecord_pdfURL
        from .speech_record_speaker import SpeechRecord_speaker
        from .speech_record_speaker_group import SpeechRecord_speakerGroup
        from .speech_record_speaker_position import SpeechRecord_speakerPosition
        from .speech_record_speaker_yomi import SpeechRecord_speakerYomi

        fields: dict[str, Callable[[Any], None]] = {
            "closing": lambda n : setattr(self, 'closing', n.get_object_value(SpeechRecord_closing)),
            "date": lambda n : setattr(self, 'date', n.get_str_value()),
            "imageKind": lambda n : setattr(self, 'image_kind', n.get_enum_value(ImageKind)),
            "issue": lambda n : setattr(self, 'issue', n.get_str_value()),
            "issueID": lambda n : setattr(self, 'issue_i_d', n.get_str_value()),
            "meetingURL": lambda n : setattr(self, 'meeting_u_r_l', n.get_str_value()),
            "nameOfHouse": lambda n : setattr(self, 'name_of_house', n.get_enum_value(NameOfHouse)),
            "nameOfMeeting": lambda n : setattr(self, 'name_of_meeting', n.get_str_value()),
            "pdfURL": lambda n : setattr(self, 'pdf_u_r_l', n.get_object_value(SpeechRecord_pdfURL)),
            "searchObject": lambda n : setattr(self, 'search_object', n.get_int_value()),
            "session": lambda n : setattr(self, 'session', n.get_int_value()),
            "speaker": lambda n : setattr(self, 'speaker', n.get_object_value(SpeechRecord_speaker)),
            "speakerGroup": lambda n : setattr(self, 'speaker_group', n.get_object_value(SpeechRecord_speakerGroup)),
            "speakerPosition": lambda n : setattr(self, 'speaker_position', n.get_object_value(SpeechRecord_speakerPosition)),
            "speakerRole": lambda n : setattr(self, 'speaker_role', n.get_enum_value(SpeakerRole)),
            "speakerYomi": lambda n : setattr(self, 'speaker_yomi', n.get_object_value(SpeechRecord_speakerYomi)),
            "speech": lambda n : setattr(self, 'speech', n.get_str_value()),
            "speechID": lambda n : setattr(self, 'speech_i_d', n.get_str_value()),
            "speechOrder": lambda n : setattr(self, 'speech_order', n.get_int_value()),
            "speechURL": lambda n : setattr(self, 'speech_u_r_l', n.get_str_value()),
            "startPage": lambda n : setattr(self, 'start_page', n.get_int_value()),
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
        writer.write_object_value("closing", self.closing)
        writer.write_str_value("date", self.date)
        writer.write_enum_value("imageKind", self.image_kind)
        writer.write_str_value("issue", self.issue)
        writer.write_str_value("issueID", self.issue_i_d)
        writer.write_str_value("meetingURL", self.meeting_u_r_l)
        writer.write_enum_value("nameOfHouse", self.name_of_house)
        writer.write_str_value("nameOfMeeting", self.name_of_meeting)
        writer.write_object_value("pdfURL", self.pdf_u_r_l)
        writer.write_int_value("searchObject", self.search_object)
        writer.write_int_value("session", self.session)
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
        writer.write_additional_data_value(self.additional_data)
    

