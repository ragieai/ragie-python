"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .connection import (
    Connection,
    ConnectionMetadataMetadata,
    ConnectionMetadataMetadataTypedDict,
    ConnectionTypedDict,
)
from .connectionbase import (
    ConnectionBase,
    ConnectionBaseMetadata,
    ConnectionBaseMetadataTypedDict,
    ConnectionBaseTypedDict,
    PartitionStrategy,
)
from .connectionlist import ConnectionList, ConnectionListTypedDict
from .connectionstats import ConnectionStats, ConnectionStatsTypedDict
from .connectionsyncfinishedwebhook import (
    ConnectionSyncFinishedWebhook,
    ConnectionSyncFinishedWebhookType,
    ConnectionSyncFinishedWebhookTypedDict,
)
from .connectionsyncfinishedwebhookpayload import (
    ConnectionSyncFinishedWebhookPayload,
    ConnectionSyncFinishedWebhookPayloadConnectionMetadata,
    ConnectionSyncFinishedWebhookPayloadConnectionMetadataTypedDict,
    ConnectionSyncFinishedWebhookPayloadTypedDict,
)
from .connectionsyncprogresswebhook import (
    ConnectionSyncProgressWebhook,
    ConnectionSyncProgressWebhookType,
    ConnectionSyncProgressWebhookTypedDict,
)
from .connectionsyncprogresswebhookpayload import (
    ConnectionSyncProgressWebhookPayload,
    ConnectionSyncProgressWebhookPayloadConnectionMetadata,
    ConnectionSyncProgressWebhookPayloadConnectionMetadataTypedDict,
    ConnectionSyncProgressWebhookPayloadTypedDict,
)
from .connectionsyncstartedwebhook import (
    ConnectionSyncStartedWebhook,
    ConnectionSyncStartedWebhookType,
    ConnectionSyncStartedWebhookTypedDict,
)
from .connectionsyncstartedwebhookpayload import (
    ConnectionMetadata,
    ConnectionMetadataTypedDict,
    ConnectionSyncStartedWebhookPayload,
    ConnectionSyncStartedWebhookPayloadTypedDict,
)
from .createdocumentfromurlparams import (
    CreateDocumentFromURLParams,
    CreateDocumentFromURLParamsMetadata,
    CreateDocumentFromURLParamsMetadataTypedDict,
    CreateDocumentFromURLParamsMode,
    CreateDocumentFromURLParamsTypedDict,
)
from .createdocumentparams import (
    CreateDocumentParams,
    CreateDocumentParamsTypedDict,
    File,
    FileTypedDict,
    Metadata,
    MetadataTypedDict,
    Mode,
)
from .createdocumentrawparams import (
    CreateDocumentRawParams,
    CreateDocumentRawParamsMetadata,
    CreateDocumentRawParamsMetadataTypedDict,
    CreateDocumentRawParamsTypedDict,
    Data,
    DataTypedDict,
    Two,
    TwoTypedDict,
)
from .createinstructionparams import (
    CreateInstructionParams,
    CreateInstructionParamsFilter,
    CreateInstructionParamsFilterTypedDict,
    CreateInstructionParamsScope,
    CreateInstructionParamsTypedDict,
)
from .delete_connection_connections_connection_id_delete_postop import (
    DeleteConnectionConnectionsConnectionIDDeletePostRequest,
    DeleteConnectionConnectionsConnectionIDDeletePostRequestTypedDict,
)
from .deleteconnectionpayload import (
    DeleteConnectionPayload,
    DeleteConnectionPayloadTypedDict,
)
from .deletedocumentop import DeleteDocumentRequest, DeleteDocumentRequestTypedDict
from .document import (
    Document,
    DocumentMetadata,
    DocumentMetadataTypedDict,
    DocumentTypedDict,
)
from .documentdelete import DocumentDelete, DocumentDeleteTypedDict
from .documentdeletewebhook import (
    DocumentDeleteWebhook,
    DocumentDeleteWebhookType,
    DocumentDeleteWebhookTypedDict,
)
from .documentdeletewebhookpayload import (
    DocumentDeleteWebhookPayload,
    DocumentDeleteWebhookPayloadMetadata,
    DocumentDeleteWebhookPayloadMetadataTypedDict,
    DocumentDeleteWebhookPayloadTypedDict,
)
from .documentfileupdate import DocumentFileUpdate, DocumentFileUpdateTypedDict
from .documentget import (
    DocumentGet,
    DocumentGetMetadata,
    DocumentGetMetadataTypedDict,
    DocumentGetTypedDict,
)
from .documentlist import DocumentList, DocumentListTypedDict
from .documentmetadataupdate import (
    DocumentMetadataUpdate,
    DocumentMetadataUpdateMetadata,
    DocumentMetadataUpdateMetadataTypedDict,
    DocumentMetadataUpdateTypedDict,
)
from .documentrawupdate import DocumentRawUpdate, DocumentRawUpdateTypedDict
from .documentsummary import DocumentSummary, DocumentSummaryTypedDict
from .documentupdatewebhook import (
    DocumentUpdateWebhook,
    DocumentUpdateWebhookTypedDict,
    Type,
)
from .documentupdatewebhookpayload import (
    DocumentUpdateWebhookPayload,
    DocumentUpdateWebhookPayloadMetadata,
    DocumentUpdateWebhookPayloadMetadataTypedDict,
    DocumentUpdateWebhookPayloadTypedDict,
    One,
    Status,
    Status2,
    StatusTypedDict,
)
from .entity import Entity, EntityTypedDict
from .entityextractedwebhook import (
    EntityExtractedWebhook,
    EntityExtractedWebhookType,
    EntityExtractedWebhookTypedDict,
)
from .entityextractedwebhookpayload import (
    EntityExtractedWebhookPayload,
    EntityExtractedWebhookPayloadData,
    EntityExtractedWebhookPayloadDataTypedDict,
    EntityExtractedWebhookPayloadDocumentMetadata,
    EntityExtractedWebhookPayloadDocumentMetadataTypedDict,
    EntityExtractedWebhookPayloadTypedDict,
)
from .entitylist import EntityList, EntityListTypedDict
from .errormessage import ErrorMessage, ErrorMessageData
from .eventevent_post import EventeventPostBody, EventeventPostBodyTypedDict
from .get_connection_stats_connections_connection_id_stats_getop import (
    GetConnectionStatsConnectionsConnectionIDStatsGetRequest,
    GetConnectionStatsConnectionsConnectionIDStatsGetRequestTypedDict,
)
from .getdocumentop import GetDocumentRequest, GetDocumentRequestTypedDict
from .getdocumentsummaryop import (
    GetDocumentSummaryRequest,
    GetDocumentSummaryRequestTypedDict,
)
from .httpvalidationerror import HTTPValidationError, HTTPValidationErrorData
from .instruction import (
    Filter,
    FilterTypedDict,
    Instruction,
    InstructionTypedDict,
    Scope,
)
from .list_connections_connections_getop import (
    ListConnectionsConnectionsGetRequest,
    ListConnectionsConnectionsGetRequestTypedDict,
    ListConnectionsConnectionsGetResponse,
    ListConnectionsConnectionsGetResponseTypedDict,
)
from .listdocumentsop import (
    ListDocumentsRequest,
    ListDocumentsRequestTypedDict,
    ListDocumentsResponse,
    ListDocumentsResponseTypedDict,
)
from .listentitiesbydocumentop import (
    ListEntitiesByDocumentRequest,
    ListEntitiesByDocumentRequestTypedDict,
    ListEntitiesByDocumentResponse,
    ListEntitiesByDocumentResponseTypedDict,
)
from .listentitiesbyinstructionop import (
    ListEntitiesByInstructionRequest,
    ListEntitiesByInstructionRequestTypedDict,
    ListEntitiesByInstructionResponse,
    ListEntitiesByInstructionResponseTypedDict,
)
from .pagination import Pagination, PaginationTypedDict
from .patchdocumentmetadataop import (
    PatchDocumentMetadataRequest,
    PatchDocumentMetadataRequestTypedDict,
)
from .patchdocumentmetadataparams import (
    PatchDocumentMetadataParams,
    PatchDocumentMetadataParamsMetadata,
    PatchDocumentMetadataParamsMetadataTypedDict,
    PatchDocumentMetadataParamsTypedDict,
)
from .retrieval import Retrieval, RetrievalTypedDict
from .retrieveparams import RetrieveParams, RetrieveParamsTypedDict
from .scoredchunk import ScoredChunk, ScoredChunkTypedDict
from .sdkerror import SDKError
from .security import Security, SecurityTypedDict
from .set_connection_enabled_connections_connection_id_enabled_putop import (
    SetConnectionEnabledConnectionsConnectionIDEnabledPutRequest,
    SetConnectionEnabledConnectionsConnectionIDEnabledPutRequestTypedDict,
)
from .setconnectionenabledpayload import (
    SetConnectionEnabledPayload,
    SetConnectionEnabledPayloadTypedDict,
)
from .update_connection_connections_connection_id_putop import (
    UpdateConnectionConnectionsConnectionIDPutRequest,
    UpdateConnectionConnectionsConnectionIDPutRequestTypedDict,
)
from .updatedocumentfileop import (
    UpdateDocumentFileRequest,
    UpdateDocumentFileRequestTypedDict,
)
from .updatedocumentfileparams import (
    UpdateDocumentFileParams,
    UpdateDocumentFileParamsFile,
    UpdateDocumentFileParamsFileTypedDict,
    UpdateDocumentFileParamsMode,
    UpdateDocumentFileParamsTypedDict,
)
from .updatedocumentrawop import (
    UpdateDocumentRawRequest,
    UpdateDocumentRawRequestTypedDict,
)
from .updatedocumentrawparams import (
    Data2,
    Data2TypedDict,
    UpdateDocumentRawParams,
    UpdateDocumentRawParamsData,
    UpdateDocumentRawParamsDataTypedDict,
    UpdateDocumentRawParamsTypedDict,
)
from .updateinstructionop import (
    UpdateInstructionRequest,
    UpdateInstructionRequestTypedDict,
)
from .updateinstructionparams import (
    UpdateInstructionParams,
    UpdateInstructionParamsTypedDict,
)
from .validationerror import (
    Loc,
    LocTypedDict,
    ValidationError,
    ValidationErrorTypedDict,
)

__all__ = [
    "Connection",
    "ConnectionBase",
    "ConnectionBaseMetadata",
    "ConnectionBaseMetadataTypedDict",
    "ConnectionBaseTypedDict",
    "ConnectionList",
    "ConnectionListTypedDict",
    "ConnectionMetadata",
    "ConnectionMetadataMetadata",
    "ConnectionMetadataMetadataTypedDict",
    "ConnectionMetadataTypedDict",
    "ConnectionStats",
    "ConnectionStatsTypedDict",
    "ConnectionSyncFinishedWebhook",
    "ConnectionSyncFinishedWebhookPayload",
    "ConnectionSyncFinishedWebhookPayloadConnectionMetadata",
    "ConnectionSyncFinishedWebhookPayloadConnectionMetadataTypedDict",
    "ConnectionSyncFinishedWebhookPayloadTypedDict",
    "ConnectionSyncFinishedWebhookType",
    "ConnectionSyncFinishedWebhookTypedDict",
    "ConnectionSyncProgressWebhook",
    "ConnectionSyncProgressWebhookPayload",
    "ConnectionSyncProgressWebhookPayloadConnectionMetadata",
    "ConnectionSyncProgressWebhookPayloadConnectionMetadataTypedDict",
    "ConnectionSyncProgressWebhookPayloadTypedDict",
    "ConnectionSyncProgressWebhookType",
    "ConnectionSyncProgressWebhookTypedDict",
    "ConnectionSyncStartedWebhook",
    "ConnectionSyncStartedWebhookPayload",
    "ConnectionSyncStartedWebhookPayloadTypedDict",
    "ConnectionSyncStartedWebhookType",
    "ConnectionSyncStartedWebhookTypedDict",
    "ConnectionTypedDict",
    "CreateDocumentFromURLParams",
    "CreateDocumentFromURLParamsMetadata",
    "CreateDocumentFromURLParamsMetadataTypedDict",
    "CreateDocumentFromURLParamsMode",
    "CreateDocumentFromURLParamsTypedDict",
    "CreateDocumentParams",
    "CreateDocumentParamsTypedDict",
    "CreateDocumentRawParams",
    "CreateDocumentRawParamsMetadata",
    "CreateDocumentRawParamsMetadataTypedDict",
    "CreateDocumentRawParamsTypedDict",
    "CreateInstructionParams",
    "CreateInstructionParamsFilter",
    "CreateInstructionParamsFilterTypedDict",
    "CreateInstructionParamsScope",
    "CreateInstructionParamsTypedDict",
    "Data",
    "Data2",
    "Data2TypedDict",
    "DataTypedDict",
    "DeleteConnectionConnectionsConnectionIDDeletePostRequest",
    "DeleteConnectionConnectionsConnectionIDDeletePostRequestTypedDict",
    "DeleteConnectionPayload",
    "DeleteConnectionPayloadTypedDict",
    "DeleteDocumentRequest",
    "DeleteDocumentRequestTypedDict",
    "Document",
    "DocumentDelete",
    "DocumentDeleteTypedDict",
    "DocumentDeleteWebhook",
    "DocumentDeleteWebhookPayload",
    "DocumentDeleteWebhookPayloadMetadata",
    "DocumentDeleteWebhookPayloadMetadataTypedDict",
    "DocumentDeleteWebhookPayloadTypedDict",
    "DocumentDeleteWebhookType",
    "DocumentDeleteWebhookTypedDict",
    "DocumentFileUpdate",
    "DocumentFileUpdateTypedDict",
    "DocumentGet",
    "DocumentGetMetadata",
    "DocumentGetMetadataTypedDict",
    "DocumentGetTypedDict",
    "DocumentList",
    "DocumentListTypedDict",
    "DocumentMetadata",
    "DocumentMetadataTypedDict",
    "DocumentMetadataUpdate",
    "DocumentMetadataUpdateMetadata",
    "DocumentMetadataUpdateMetadataTypedDict",
    "DocumentMetadataUpdateTypedDict",
    "DocumentRawUpdate",
    "DocumentRawUpdateTypedDict",
    "DocumentSummary",
    "DocumentSummaryTypedDict",
    "DocumentTypedDict",
    "DocumentUpdateWebhook",
    "DocumentUpdateWebhookPayload",
    "DocumentUpdateWebhookPayloadMetadata",
    "DocumentUpdateWebhookPayloadMetadataTypedDict",
    "DocumentUpdateWebhookPayloadTypedDict",
    "DocumentUpdateWebhookTypedDict",
    "Entity",
    "EntityExtractedWebhook",
    "EntityExtractedWebhookPayload",
    "EntityExtractedWebhookPayloadData",
    "EntityExtractedWebhookPayloadDataTypedDict",
    "EntityExtractedWebhookPayloadDocumentMetadata",
    "EntityExtractedWebhookPayloadDocumentMetadataTypedDict",
    "EntityExtractedWebhookPayloadTypedDict",
    "EntityExtractedWebhookType",
    "EntityExtractedWebhookTypedDict",
    "EntityList",
    "EntityListTypedDict",
    "EntityTypedDict",
    "ErrorMessage",
    "ErrorMessageData",
    "EventeventPostBody",
    "EventeventPostBodyTypedDict",
    "File",
    "FileTypedDict",
    "Filter",
    "FilterTypedDict",
    "GetConnectionStatsConnectionsConnectionIDStatsGetRequest",
    "GetConnectionStatsConnectionsConnectionIDStatsGetRequestTypedDict",
    "GetDocumentRequest",
    "GetDocumentRequestTypedDict",
    "GetDocumentSummaryRequest",
    "GetDocumentSummaryRequestTypedDict",
    "HTTPValidationError",
    "HTTPValidationErrorData",
    "Instruction",
    "InstructionTypedDict",
    "ListConnectionsConnectionsGetRequest",
    "ListConnectionsConnectionsGetRequestTypedDict",
    "ListConnectionsConnectionsGetResponse",
    "ListConnectionsConnectionsGetResponseTypedDict",
    "ListDocumentsRequest",
    "ListDocumentsRequestTypedDict",
    "ListDocumentsResponse",
    "ListDocumentsResponseTypedDict",
    "ListEntitiesByDocumentRequest",
    "ListEntitiesByDocumentRequestTypedDict",
    "ListEntitiesByDocumentResponse",
    "ListEntitiesByDocumentResponseTypedDict",
    "ListEntitiesByInstructionRequest",
    "ListEntitiesByInstructionRequestTypedDict",
    "ListEntitiesByInstructionResponse",
    "ListEntitiesByInstructionResponseTypedDict",
    "Loc",
    "LocTypedDict",
    "Metadata",
    "MetadataTypedDict",
    "Mode",
    "One",
    "Pagination",
    "PaginationTypedDict",
    "PartitionStrategy",
    "PatchDocumentMetadataParams",
    "PatchDocumentMetadataParamsMetadata",
    "PatchDocumentMetadataParamsMetadataTypedDict",
    "PatchDocumentMetadataParamsTypedDict",
    "PatchDocumentMetadataRequest",
    "PatchDocumentMetadataRequestTypedDict",
    "Retrieval",
    "RetrievalTypedDict",
    "RetrieveParams",
    "RetrieveParamsTypedDict",
    "SDKError",
    "Scope",
    "ScoredChunk",
    "ScoredChunkTypedDict",
    "Security",
    "SecurityTypedDict",
    "SetConnectionEnabledConnectionsConnectionIDEnabledPutRequest",
    "SetConnectionEnabledConnectionsConnectionIDEnabledPutRequestTypedDict",
    "SetConnectionEnabledPayload",
    "SetConnectionEnabledPayloadTypedDict",
    "Status",
    "Status2",
    "StatusTypedDict",
    "Two",
    "TwoTypedDict",
    "Type",
    "UpdateConnectionConnectionsConnectionIDPutRequest",
    "UpdateConnectionConnectionsConnectionIDPutRequestTypedDict",
    "UpdateDocumentFileParams",
    "UpdateDocumentFileParamsFile",
    "UpdateDocumentFileParamsFileTypedDict",
    "UpdateDocumentFileParamsMode",
    "UpdateDocumentFileParamsTypedDict",
    "UpdateDocumentFileRequest",
    "UpdateDocumentFileRequestTypedDict",
    "UpdateDocumentRawParams",
    "UpdateDocumentRawParamsData",
    "UpdateDocumentRawParamsDataTypedDict",
    "UpdateDocumentRawParamsTypedDict",
    "UpdateDocumentRawRequest",
    "UpdateDocumentRawRequestTypedDict",
    "UpdateInstructionParams",
    "UpdateInstructionParamsTypedDict",
    "UpdateInstructionRequest",
    "UpdateInstructionRequestTypedDict",
    "ValidationError",
    "ValidationErrorTypedDict",
]
