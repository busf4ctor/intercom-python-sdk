"""
====================
Data Events API Models
====================
`apis/data_events/models.py`

This module contains models used to interact with the Intercom Admins API [1].
These models provide object oriented interfaces for the schemas defined in `apis/data_attributes/schemas.py`.

----
[1] https://developers.intercom.com/intercom-api-reference/reference/lisdataattributes
"""
# Built-ins
import time
import requests
from typing import (
    Any, Union, List,
    TYPE_CHECKING,
)

# From Current API
from . import schemas as dexport_schemas
from . import models as dexport_models

# From Current Package
from ...core.model_base import ModelBase

if TYPE_CHECKING:
    from .api import DataExportAPI

class DataExportJob(ModelBase):
    """ A data export job. """
    def __init__(self, *args, **kwargs):
        self.__job_identifier = kwargs.get("job_identifier", "")
        self.__status = kwargs.get("status", "")
        self.__download_expires_at = kwargs.get("download_expires_at", "")
        self.__download_url = kwargs.get("download_url", "")
        self._api_client: DataExportAPI = kwargs.get("api_client") # type: ignore

    @property
    def api_client(self) -> "DataExportAPI":
        return self._api_client
    
    @api_client.setter
    def api_client(self, value: "DataExportAPI"):
        self._api_client = value
    
    @property
    def job_identifier(self) -> str:
        return self.__job_identifier
    
    @property
    def status(self) -> str:
        return self.__status
    
    @property
    def download_expires_at(self) -> str:
        return self.__download_expires_at
    
    @property
    def download_url(self) -> str:
        return self.__download_url
    
    
    def update(self, **kwargs) -> "DataExportJob":
        """ Update this data export job. """
        job = self.api_client.get_export_job(job_identifier=self.job_identifier)

        self.__status = job.status
        self.__download_expires_at = job.download_expires_at
        self.__download_url = job.download_url
        
        return self
    
    def cancel(self) -> "DataExportJob":
        """ Cancel this data export job. """
        job = self.api_client.cancel_export_job(job_identifier=self.job_identifier)

        self.__status = job.status
        self.__download_expires_at = job.download_expires_at
        self.__download_url = job.download_url
        
        return self
    
    def wait_for_completion(self, timeout=120, frequency=5):
        """ Wait for the data export job to complete. 
        
        Be aware that this method will block your thread until the job is completed.
        Using this method without a timeout is not recommended.

        Params:
            timeout (int): The maximum number of seconds to wait for the job to complete.
            frequency (int): The number of seconds to wait between checking the job status.
        Returns:
            bool: True once the job is completed (regardless of success or failure)
        Raises:
            TimeoutError: If the job does not complete within the specified timeout.
        """
        timeout_time = time.time() + timeout
        while self.status == "pending":
            if time.time() > timeout_time:
                raise TimeoutError(f"Data export job {self.job_identifier} failed to complete within {timeout} seconds.")

            time.sleep(frequency)
            self.update()
        
        return True

    def download(self):
        """ Download this data export job. """
        if self.download_url:
            response = self.api_client.download(job_identifier=self.job_identifier)
            if not isinstance(response, requests.Response):
                return response
            if response.ok:
                return response.content
            else:
                raise ValueError(f"Failed to download data export job {self.job_identifier} \
                                       with error: {response.text}")
    


            


