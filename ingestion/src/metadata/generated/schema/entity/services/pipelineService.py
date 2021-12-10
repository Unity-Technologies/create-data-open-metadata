# generated by datamodel-codegen:
#   filename:  schema/entity/services/pipelineService.json
#   timestamp: 2021-12-10T11:30:44+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import AnyUrl, BaseModel, Field, constr

from ...type import basic, entityHistory, schedule


class PipelineServiceType(Enum):
    Airflow = 'Airflow'
    Prefect = 'Prefect'
    Glue = 'Glue'


class PipelineService(BaseModel):
    id: basic.Uuid = Field(
        ..., description='Unique identifier of this pipeline service instance.'
    )
    name: constr(min_length=1, max_length=64) = Field(
        ..., description='Name that identifies this pipeline service.'
    )
    serviceType: Optional[PipelineServiceType] = Field(
        None, description='Type of pipeline service such as Airflow or Prefect...'
    )
    description: Optional[str] = Field(
        None, description='Description of a pipeline service instance.'
    )
    displayName: Optional[str] = Field(
        None,
        description='Display Name that identifies this pipeline service. It could be title or label from the source services.',
    )
    version: Optional[entityHistory.EntityVersion] = Field(
        None, description='Metadata version of the entity.'
    )
    updatedAt: Optional[basic.DateTime] = Field(
        None,
        description='Last update time corresponding to the new version of the entity.',
    )
    updatedBy: Optional[str] = Field(None, description='User who made the update.')
    pipelineUrl: AnyUrl = Field(..., description='Pipeline Service Management/UI URL.')
    ingestionSchedule: Optional[schedule.Schedule] = Field(
        None, description='Schedule for running metadata ingestion jobs.'
    )
    href: Optional[basic.Href] = Field(
        None, description='Link to the resource corresponding to this pipeline service.'
    )
    changeDescription: Optional[entityHistory.ChangeDescription] = Field(
        None, description='Change that lead to this version of the entity.'
    )
