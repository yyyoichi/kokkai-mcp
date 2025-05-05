from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import ComposedTypeWrapper, Parsable, ParseNode, ParseNodeHelper, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...models.error_response import ErrorResponse
    from ...models.meeting_list_response import MeetingListResponse

@dataclass
class Meeting_listGetResponse(ComposedTypeWrapper, Parsable):
    """
    Composed type wrapper for classes ErrorResponse, MeetingListResponse
    """
    # Composed type representation for type ErrorResponse
    error_response: Optional[ErrorResponse] = None
    # Composed type representation for type MeetingListResponse
    meeting_list_response: Optional[MeetingListResponse] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Meeting_listGetResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Meeting_listGetResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        result = Meeting_listGetResponse()
        from ...models.error_response import ErrorResponse

        result.error_response = ErrorResponse()
        from ...models.meeting_list_response import MeetingListResponse

        result.meeting_list_response = MeetingListResponse()
        return result
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ...models.error_response import ErrorResponse
        from ...models.meeting_list_response import MeetingListResponse

        if self.error_response or self.meeting_list_response:
            return ParseNodeHelper.merge_deserializers_for_intersection_wrapper(self.error_response, self.meeting_list_response)
        return {}
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_object_value(None, self.error_response, self.meeting_list_response)
    

