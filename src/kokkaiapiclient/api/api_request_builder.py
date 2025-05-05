from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .meeting.meeting_request_builder import MeetingRequestBuilder
    from .meeting_list.meeting_list_request_builder import Meeting_listRequestBuilder
    from .speech.speech_request_builder import SpeechRequestBuilder

class ApiRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ApiRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api", path_parameters)
    
    @property
    def meeting(self) -> MeetingRequestBuilder:
        """
        The meeting property
        """
        from .meeting.meeting_request_builder import MeetingRequestBuilder

        return MeetingRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def meeting_list(self) -> Meeting_listRequestBuilder:
        """
        The meeting_list property
        """
        from .meeting_list.meeting_list_request_builder import Meeting_listRequestBuilder

        return Meeting_listRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def speech(self) -> SpeechRequestBuilder:
        """
        The speech property
        """
        from .speech.speech_request_builder import SpeechRequestBuilder

        return SpeechRequestBuilder(self.request_adapter, self.path_parameters)
    

