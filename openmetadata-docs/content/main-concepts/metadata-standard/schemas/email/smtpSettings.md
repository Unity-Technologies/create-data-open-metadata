---
title: smtpSettings
slug: /main-concepts/metadata-standard/schemas/email/smtpsettings
---

# SmtpSettings

*This schema defines the SMTP Settings for sending Email*

## Properties

- **`emailingEntity`** *(string)*: Emailing Entity. Default: `OpenMetadata`.
- **`supportUrl`** *(string)*: Support Url. Default: `https://slack.open-metadata.org`.
- **`enableSmtpServer`** *(boolean)*: If this is enable password will details will be shared on mail. Default: `False`.
- **`openMetadataUrl`** *(string)*: Openmetadata Server Endpoint.
- **`senderMail`** *(string)*: Mail of the sender.
- **`serverEndpoint`** *(string)*: Smtp Server Endpoint.
- **`serverPort`** *(integer)*: Smtp Server Endpoint.
- **`username`** *(string)*: Smtp Server Username.
- **`password`** *(string)*: Smtp Server Password.
- **`transportationStrategy`** *(string)*: Must be one of: `['SMTP', 'SMPTS', 'SMTP_TLS']`. Default: `SMTP`.


Documentation file automatically generated at 2022-11-17 03:44:30.373132.