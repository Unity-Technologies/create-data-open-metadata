# generated by datamodel-codegen:
#   filename:  schema/entity/data/metrics.json
#   timestamp: 2021-12-10T11:30:44+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field, constr

from ...type import basic, entityHistory, entityReference, tagLabel, usageDetails


class Metrics(BaseModel):
    id: basic.Uuid = Field(
        ..., description='Unique identifier that identifies this metrics instance.'
    )
    name: constr(min_length=1, max_length=64) = Field(
        ..., description='Name that identifies this metrics instance uniquely.'
    )
    fullyQualifiedName: Optional[constr(min_length=1, max_length=64)] = Field(
        None,
        description="A unique name that identifies a metric in the format 'ServiceName.MetricName'.",
    )
    displayName: Optional[str] = Field(
        None, description='Display Name that identifies this metric.'
    )
    description: Optional[str] = Field(
        None,
        description='Description of metrics instance, what it is, and how to use it.',
    )
    version: Optional[entityHistory.EntityVersion] = Field(
        None, description='Metadata version of the entity.'
    )
    updatedAt: Optional[basic.DateTime] = Field(
        None,
        description='Last update time corresponding to the new version of the entity.',
    )
    updatedBy: Optional[str] = Field(None, description='User who made the update.')
    href: Optional[basic.Href] = Field(
        None, description='Link to the resource corresponding to this entity.'
    )
    owner: Optional[entityReference.EntityReference] = Field(
        None, description='Owner of this metrics.'
    )
    tags: Optional[List[tagLabel.TagLabel]] = Field(
        None, description='Tags for this chart.'
    )
    service: entityReference.EntityReference = Field(
        ..., description='Link to service where this metrics is hosted in.'
    )
    usageSummary: Optional[usageDetails.TypeUsedToReturnUsageDetailsOfAnEntity] = Field(
        None, description='Latest usage information for this database.'
    )
    changeDescription: Optional[entityHistory.ChangeDescription] = Field(
        None, description='Change that lead to this version of the entity.'
    )
