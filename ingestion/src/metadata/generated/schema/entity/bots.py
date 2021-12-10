# generated by datamodel-codegen:
#   filename:  schema/entity/bots.json
#   timestamp: 2021-12-10T11:30:44+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field, constr

from ..type import basic, entityHistory


class Bot(BaseModel):
    id: Optional[basic.Uuid] = Field(
        None, description='Unique identifier of a bot instance.'
    )
    name: Optional[constr(min_length=1, max_length=64)] = Field(
        None, description='Name of the bot.'
    )
    displayName: Optional[str] = Field(
        None,
        description="Name used for display purposes. Example 'FirstName LastName'.",
    )
    description: Optional[str] = Field(None, description='Description of the bot.')
    version: Optional[entityHistory.EntityVersion] = Field(
        None, description='Metadata version of the entity.'
    )
    updatedAt: Optional[basic.DateTime] = Field(
        None,
        description='Last update time corresponding to the new version of the entity.',
    )
    updatedBy: Optional[str] = Field(None, description='User who made the update.')
    href: Optional[basic.Href] = Field(
        None, description='Link to the resource corresponding to this bot.'
    )
    changeDescription: Optional[entityHistory.ChangeDescription] = Field(
        None, description='Change that lead to this version of the entity.'
    )
