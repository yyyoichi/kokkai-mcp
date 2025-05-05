from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .image_kind import ImageKind
    from .meeting_response_meeting_record_closing import MeetingResponse_meetingRecord_closing
    from .meeting_response_meeting_record_pdf_u_r_l import MeetingResponse_meetingRecord_pdfURL
    from .meeting_speech_record import MeetingSpeechRecord
    from .name_of_house import NameOfHouse

@dataclass
class MeetingResponse_meetingRecord(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # 閉会中フラグ。
    closing: Optional[MeetingResponse_meetingRecord_closing] = None
    # 開催日付 (YYYY-MM-DD)。
    date: Optional[str] = None
    # 資料種別。
    image_kind: Optional[ImageKind] = None
    # 号数。"第issue号"形式。
    issue: Optional[str] = None
    # 発言ID。"issueID_発言番号"形式。
    issue_i_d: Optional[str] = None
    # 会議録テキスト表示画面へのURL。
    meeting_u_r_l: Optional[str] = None
    # 院名。
    name_of_house: Optional[NameOfHouse] = None
    # 会議名。
    name_of_meeting: Optional[str] = None
    # 会議録PDF表示画面へのURL。
    pdf_u_r_l: Optional[MeetingResponse_meetingRecord_pdfURL] = None
    # 検索対象箇所。
    search_object: Optional[int] = None
    # 国会回次。
    session: Optional[int] = None
    # 発言リスト。
    speech_record: Optional[list[MeetingSpeechRecord]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MeetingResponse_meetingRecord:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MeetingResponse_meetingRecord
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MeetingResponse_meetingRecord()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .image_kind import ImageKind
        from .meeting_response_meeting_record_closing import MeetingResponse_meetingRecord_closing
        from .meeting_response_meeting_record_pdf_u_r_l import MeetingResponse_meetingRecord_pdfURL
        from .meeting_speech_record import MeetingSpeechRecord
        from .name_of_house import NameOfHouse

        from .image_kind import ImageKind
        from .meeting_response_meeting_record_closing import MeetingResponse_meetingRecord_closing
        from .meeting_response_meeting_record_pdf_u_r_l import MeetingResponse_meetingRecord_pdfURL
        from .meeting_speech_record import MeetingSpeechRecord
        from .name_of_house import NameOfHouse

        fields: dict[str, Callable[[Any], None]] = {
            "closing": lambda n : setattr(self, 'closing', n.get_object_value(MeetingResponse_meetingRecord_closing)),
            "date": lambda n : setattr(self, 'date', n.get_str_value()),
            "imageKind": lambda n : setattr(self, 'image_kind', n.get_enum_value(ImageKind)),
            "issue": lambda n : setattr(self, 'issue', n.get_str_value()),
            "issueID": lambda n : setattr(self, 'issue_i_d', n.get_str_value()),
            "meetingURL": lambda n : setattr(self, 'meeting_u_r_l', n.get_str_value()),
            "nameOfHouse": lambda n : setattr(self, 'name_of_house', n.get_enum_value(NameOfHouse)),
            "nameOfMeeting": lambda n : setattr(self, 'name_of_meeting', n.get_str_value()),
            "pdfURL": lambda n : setattr(self, 'pdf_u_r_l', n.get_object_value(MeetingResponse_meetingRecord_pdfURL)),
            "searchObject": lambda n : setattr(self, 'search_object', n.get_int_value()),
            "session": lambda n : setattr(self, 'session', n.get_int_value()),
            "speechRecord": lambda n : setattr(self, 'speech_record', n.get_collection_of_object_values(MeetingSpeechRecord)),
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
        writer.write_collection_of_object_values("speechRecord", self.speech_record)
        writer.write_additional_data_value(self.additional_data)
    

