"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .audiomodalitydata import AudioModalityData, AudioModalityDataTypedDict
from .connection import (
    Connection,
    ConnectionMetadata,
    ConnectionMetadataTypedDict,
    ConnectionTypedDict,
    DisabledBySystemReason,
    Source,
    SourceTypedDict,
)
from .connectionbase import (
    ConnectionBase,
    ConnectionBaseMetadata,
    ConnectionBaseMetadataTypedDict,
    ConnectionBaseTypedDict,
    PartitionStrategy,
)
from .connectionlimitparams import ConnectionLimitParams, ConnectionLimitParamsTypedDict
from .connectionlist import ConnectionList, ConnectionListTypedDict
from .connectionstats import ConnectionStats, ConnectionStatsTypedDict
from .connectorsource import ConnectorSource
from .createdocumentfromurlparams import (
    CreateDocumentFromURLParams,
    CreateDocumentFromURLParamsMetadata,
    CreateDocumentFromURLParamsMetadataTypedDict,
    CreateDocumentFromURLParamsMode,
    CreateDocumentFromURLParamsTypedDict,
)
from .createdocumentparams import (
    CreateDocumentParams,
    CreateDocumentParamsMode,
    CreateDocumentParamsTypedDict,
    File,
    FileTypedDict,
    Metadata,
    MetadataTypedDict,
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
from .createpartitionparams import CreatePartitionParams, CreatePartitionParamsTypedDict
from .delete_connection_connections_connection_id_delete_postop import (
    DeleteConnectionConnectionsConnectionIDDeletePostRequest,
    DeleteConnectionConnectionsConnectionIDDeletePostRequestTypedDict,
)
from .delete_partition_partitions_partition_id_deleteop import (
    DeletePartitionPartitionsPartitionIDDeleteRequest,
    DeletePartitionPartitionsPartitionIDDeleteRequestTypedDict,
)
from .deleteconnectionpayload import (
    DeleteConnectionPayload,
    DeleteConnectionPayloadTypedDict,
)
from .deletedocumentop import DeleteDocumentRequest, DeleteDocumentRequestTypedDict
from .deleteinstructionop import (
    DeleteInstructionRequest,
    DeleteInstructionRequestTypedDict,
)
from .document import (
    Document,
    DocumentMetadata,
    DocumentMetadataTypedDict,
    DocumentTypedDict,
)
from .documentchunk import DocumentChunk, DocumentChunkTypedDict
from .documentchunkdetail import (
    DocumentChunkDetail,
    DocumentChunkDetailTypedDict,
    ModalityData,
    ModalityDataTypedDict,
)
from .documentchunklist import DocumentChunkList, DocumentChunkListTypedDict
from .documentdelete import DocumentDelete, DocumentDeleteTypedDict
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
from .documenturlupdate import DocumentURLUpdate, DocumentURLUpdateTypedDict
from .documentwithcontent import (
    DocumentWithContent,
    DocumentWithContentMetadata,
    DocumentWithContentMetadataTypedDict,
    DocumentWithContentTypedDict,
)
from .entity import Entity, EntityTypedDict
from .entitylist import EntityList, EntityListTypedDict
from .errormessage import ErrorMessage, ErrorMessageData
from .get_connection_connections_connection_id_getop import (
    GetConnectionConnectionsConnectionIDGetRequest,
    GetConnectionConnectionsConnectionIDGetRequestTypedDict,
)
from .get_connection_stats_connections_connection_id_stats_getop import (
    GetConnectionStatsConnectionsConnectionIDStatsGetRequest,
    GetConnectionStatsConnectionsConnectionIDStatsGetRequestTypedDict,
)
from .get_partition_partitions_partition_id_getop import (
    GetPartitionPartitionsPartitionIDGetRequest,
    GetPartitionPartitionsPartitionIDGetRequestTypedDict,
)
from .getdocumentchunkcontentop import (
    GetDocumentChunkContentRequest,
    GetDocumentChunkContentRequestTypedDict,
    MediaType,
)
from .getdocumentchunkop import (
    GetDocumentChunkRequest,
    GetDocumentChunkRequestTypedDict,
)
from .getdocumentchunksop import (
    GetDocumentChunksRequest,
    GetDocumentChunksRequestTypedDict,
)
from .getdocumentcontentop import (
    GetDocumentContentRequest,
    GetDocumentContentRequestTypedDict,
)
from .getdocumentop import GetDocumentRequest, GetDocumentRequestTypedDict
from .getdocumentsourceop import (
    GetDocumentSourceRequest,
    GetDocumentSourceRequestTypedDict,
)
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
from .link import Link, LinkTypedDict
from .list_connections_connections_getop import (
    ListConnectionsConnectionsGetRequest,
    ListConnectionsConnectionsGetRequestTypedDict,
    ListConnectionsConnectionsGetResponse,
    ListConnectionsConnectionsGetResponseTypedDict,
)
from .list_partitions_partitions_getop import (
    ListPartitionsPartitionsGetRequest,
    ListPartitionsPartitionsGetRequestTypedDict,
    ListPartitionsPartitionsGetResponse,
    ListPartitionsPartitionsGetResponseTypedDict,
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
from .oauthurlcreate import (
    Config,
    ConfigTypedDict,
    Mode,
    OAuthURLCreate,
    OAuthURLCreateMetadata,
    OAuthURLCreateMetadataTypedDict,
    OAuthURLCreateTypedDict,
    Theme,
)
from .oauthurlresponse import OAuthURLResponse, OAuthURLResponseTypedDict
from .pagination import Pagination, PaginationTypedDict
from .partition import Partition, PartitionTypedDict
from .partitiondetail import PartitionDetail, PartitionDetailTypedDict
from .partitionlimitparams import PartitionLimitParams, PartitionLimitParamsTypedDict
from .partitionlimits import PartitionLimits, PartitionLimitsTypedDict
from .partitionlist import PartitionList, PartitionListTypedDict
from .partitionstats import PartitionStats, PartitionStatsTypedDict
from .patchdocumentmetadataop import (
    PatchDocumentMetadataRequest,
    PatchDocumentMetadataRequestTypedDict,
)
from .patchdocumentmetadataparams import (
    PatchDocumentMetadataParams,
    PatchDocumentMetadataParamsTypedDict,
)
from .responseok import ResponseOK, ResponseOKTypedDict
from .retrieval import Retrieval, RetrievalTypedDict
from .retrieveparams import RetrieveParams, RetrieveParamsTypedDict
from .scoredchunk import ScoredChunk, ScoredChunkTypedDict
from .sdkerror import SDKError
from .security import Security, SecurityTypedDict
from .set_connection_enabled_connections_connection_id_enabled_putop import (
    SetConnectionEnabledConnectionsConnectionIDEnabledPutRequest,
    SetConnectionEnabledConnectionsConnectionIDEnabledPutRequestTypedDict,
)
from .set_connection_limits_connections_connection_id_limit_putop import (
    SetConnectionLimitsConnectionsConnectionIDLimitPutRequest,
    SetConnectionLimitsConnectionsConnectionIDLimitPutRequestTypedDict,
)
from .set_partition_limits_partitions_partition_id_limits_putop import (
    SetPartitionLimitsPartitionsPartitionIDLimitsPutRequest,
    SetPartitionLimitsPartitionsPartitionIDLimitsPutRequestTypedDict,
)
from .setconnectionenabledpayload import (
    Reason,
    SetConnectionEnabledPayload,
    SetConnectionEnabledPayloadTypedDict,
)
from .syncconnectionop import SyncConnectionRequest, SyncConnectionRequestTypedDict
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
from .updatedocumentfromurlop import (
    UpdateDocumentFromURLRequest,
    UpdateDocumentFromURLRequestTypedDict,
)
from .updatedocumentfromurlparams import (
    UpdateDocumentFromURLParams,
    UpdateDocumentFromURLParamsMode,
    UpdateDocumentFromURLParamsTypedDict,
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
from .wordtimestamp import WordTimestamp, WordTimestampTypedDict


__all__ = [
    "AudioModalityData",
    "AudioModalityDataTypedDict",
    "Config",
    "ConfigTypedDict",
    "Connection",
    "ConnectionBase",
    "ConnectionBaseMetadata",
    "ConnectionBaseMetadataTypedDict",
    "ConnectionBaseTypedDict",
    "ConnectionLimitParams",
    "ConnectionLimitParamsTypedDict",
    "ConnectionList",
    "ConnectionListTypedDict",
    "ConnectionMetadata",
    "ConnectionMetadataTypedDict",
    "ConnectionStats",
    "ConnectionStatsTypedDict",
    "ConnectionTypedDict",
    "ConnectorSource",
    "CreateDocumentFromURLParams",
    "CreateDocumentFromURLParamsMetadata",
    "CreateDocumentFromURLParamsMetadataTypedDict",
    "CreateDocumentFromURLParamsMode",
    "CreateDocumentFromURLParamsTypedDict",
    "CreateDocumentParams",
    "CreateDocumentParamsMode",
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
    "CreatePartitionParams",
    "CreatePartitionParamsTypedDict",
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
    "DeleteInstructionRequest",
    "DeleteInstructionRequestTypedDict",
    "DeletePartitionPartitionsPartitionIDDeleteRequest",
    "DeletePartitionPartitionsPartitionIDDeleteRequestTypedDict",
    "DisabledBySystemReason",
    "Document",
    "DocumentChunk",
    "DocumentChunkDetail",
    "DocumentChunkDetailTypedDict",
    "DocumentChunkList",
    "DocumentChunkListTypedDict",
    "DocumentChunkTypedDict",
    "DocumentDelete",
    "DocumentDeleteTypedDict",
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
    "DocumentURLUpdate",
    "DocumentURLUpdateTypedDict",
    "DocumentWithContent",
    "DocumentWithContentMetadata",
    "DocumentWithContentMetadataTypedDict",
    "DocumentWithContentTypedDict",
    "Entity",
    "EntityList",
    "EntityListTypedDict",
    "EntityTypedDict",
    "ErrorMessage",
    "ErrorMessageData",
    "File",
    "FileTypedDict",
    "Filter",
    "FilterTypedDict",
    "GetConnectionConnectionsConnectionIDGetRequest",
    "GetConnectionConnectionsConnectionIDGetRequestTypedDict",
    "GetConnectionStatsConnectionsConnectionIDStatsGetRequest",
    "GetConnectionStatsConnectionsConnectionIDStatsGetRequestTypedDict",
    "GetDocumentChunkContentRequest",
    "GetDocumentChunkContentRequestTypedDict",
    "GetDocumentChunkRequest",
    "GetDocumentChunkRequestTypedDict",
    "GetDocumentChunksRequest",
    "GetDocumentChunksRequestTypedDict",
    "GetDocumentContentRequest",
    "GetDocumentContentRequestTypedDict",
    "GetDocumentRequest",
    "GetDocumentRequestTypedDict",
    "GetDocumentSourceRequest",
    "GetDocumentSourceRequestTypedDict",
    "GetDocumentSummaryRequest",
    "GetDocumentSummaryRequestTypedDict",
    "GetPartitionPartitionsPartitionIDGetRequest",
    "GetPartitionPartitionsPartitionIDGetRequestTypedDict",
    "HTTPValidationError",
    "HTTPValidationErrorData",
    "Instruction",
    "InstructionTypedDict",
    "Link",
    "LinkTypedDict",
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
    "ListPartitionsPartitionsGetRequest",
    "ListPartitionsPartitionsGetRequestTypedDict",
    "ListPartitionsPartitionsGetResponse",
    "ListPartitionsPartitionsGetResponseTypedDict",
    "Loc",
    "LocTypedDict",
    "MediaType",
    "Metadata",
    "MetadataTypedDict",
    "ModalityData",
    "ModalityDataTypedDict",
    "Mode",
    "OAuthURLCreate",
    "OAuthURLCreateMetadata",
    "OAuthURLCreateMetadataTypedDict",
    "OAuthURLCreateTypedDict",
    "OAuthURLResponse",
    "OAuthURLResponseTypedDict",
    "Pagination",
    "PaginationTypedDict",
    "Partition",
    "PartitionDetail",
    "PartitionDetailTypedDict",
    "PartitionLimitParams",
    "PartitionLimitParamsTypedDict",
    "PartitionLimits",
    "PartitionLimitsTypedDict",
    "PartitionList",
    "PartitionListTypedDict",
    "PartitionStats",
    "PartitionStatsTypedDict",
    "PartitionStrategy",
    "PartitionTypedDict",
    "PatchDocumentMetadataParams",
    "PatchDocumentMetadataParamsTypedDict",
    "PatchDocumentMetadataRequest",
    "PatchDocumentMetadataRequestTypedDict",
    "Reason",
    "ResponseOK",
    "ResponseOKTypedDict",
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
    "SetConnectionLimitsConnectionsConnectionIDLimitPutRequest",
    "SetConnectionLimitsConnectionsConnectionIDLimitPutRequestTypedDict",
    "SetPartitionLimitsPartitionsPartitionIDLimitsPutRequest",
    "SetPartitionLimitsPartitionsPartitionIDLimitsPutRequestTypedDict",
    "Source",
    "SourceTypedDict",
    "SyncConnectionRequest",
    "SyncConnectionRequestTypedDict",
    "Theme",
    "Two",
    "TwoTypedDict",
    "UpdateConnectionConnectionsConnectionIDPutRequest",
    "UpdateConnectionConnectionsConnectionIDPutRequestTypedDict",
    "UpdateDocumentFileParams",
    "UpdateDocumentFileParamsFile",
    "UpdateDocumentFileParamsFileTypedDict",
    "UpdateDocumentFileParamsMode",
    "UpdateDocumentFileParamsTypedDict",
    "UpdateDocumentFileRequest",
    "UpdateDocumentFileRequestTypedDict",
    "UpdateDocumentFromURLParams",
    "UpdateDocumentFromURLParamsMode",
    "UpdateDocumentFromURLParamsTypedDict",
    "UpdateDocumentFromURLRequest",
    "UpdateDocumentFromURLRequestTypedDict",
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
    "WordTimestamp",
    "WordTimestampTypedDict",
]
