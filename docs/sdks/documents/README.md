# Documents
(*documents*)

### Available Operations

* [list](#list) - List Documents
* [create](#create) - Create Document
* [create_raw](#create_raw) - Create Document Raw
* [create_document_from_url](#create_document_from_url) - Create Document From Url
* [get](#get) - Get Document
* [delete](#delete) - Delete Document
* [update_file](#update_file) - Update Document File
* [update_raw](#update_raw) - Update Document Raw
* [patch_metadata](#patch_metadata) - Patch Document Metadata
* [get_summary](#get_summary) - Get Document Summary

## list

List all documents sorted by created_at in descending order. Results are paginated with a max limit of 100. When more documents are available, a `cursor` will be provided. Use the `cursor` parameter to retrieve the subsequent page.

### Example Usage

```python
from ragie import Ragie

s = Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.documents.list(request={
    "filter_": "{\"department\":{\"$in\":[\"sales\",\"marketing\"]}}",
})

if res is not None:
    while True:
        # handle items

        res = res.Next()
        if res is None:
            break


```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.ListDocumentsRequest](../../models/listdocumentsrequest.md) | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.ListDocumentsResponse](../../models/listdocumentsresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorMessage        | 401,404                    | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |

## create

Create Document

### Example Usage

```python
from ragie import Ragie

s = Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.documents.create(request={
    "file": {
        "file_name": "your_file_here",
        "content": open("<file_path>", "rb"),
    },
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.CreateDocumentParams](../../models/createdocumentparams.md) | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.Document](../../models/document.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorMessage        | 400,401                    | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |

## create_raw

Ingest a document as raw text

### Example Usage

```python
from ragie import Ragie

s = Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.documents.create_raw(request={
    "data": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `request`                                                                 | [models.CreateDocumentRawParams](../../models/createdocumentrawparams.md) | :heavy_check_mark:                                                        | The request object to use for the request.                                |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |


### Response

**[models.Document](../../models/document.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorMessage        | 400,401                    | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |

## create_document_from_url

Create Document From Url

### Example Usage

```python
from ragie import Ragie

s = Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.documents.create_document_from_url(request={
    "url": "http://frightening-quartz.name",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `request`                                                                         | [models.CreateDocumentFromURLParams](../../models/createdocumentfromurlparams.md) | :heavy_check_mark:                                                                | The request object to use for the request.                                        |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |


### Response

**[models.Document](../../models/document.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorMessage        | 400,401                    | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |

## get

Get Document

### Example Usage

```python
from ragie import Ragie

s = Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.documents.get(document_id="<DOCUMENT_ID>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `document_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | The id of the document.                                             | <DOCUMENT_ID>                                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.Document](../../models/document.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorMessage        | 401,404                    | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |

## delete

Delete Document

### Example Usage

```python
from ragie import Ragie

s = Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.documents.delete(document_id="<DOCUMENT_ID>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `document_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | The id of the document.                                             | <DOCUMENT_ID>                                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.DocumentDelete](../../models/documentdelete.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorMessage        | 401,404                    | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |

## update_file

Update Document File

### Example Usage

```python
from ragie import Ragie

s = Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.documents.update_file(document_id="<DOCUMENT_ID>", update_document_file_params={
    "file": {
        "file_name": "your_file_here",
        "content": open("<file_path>", "rb"),
    },
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 | Example                                                                     |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `document_id`                                                               | *str*                                                                       | :heavy_check_mark:                                                          | The id of the document.                                                     | <DOCUMENT_ID>                                                               |
| `update_document_file_params`                                               | [models.UpdateDocumentFileParams](../../models/updatedocumentfileparams.md) | :heavy_check_mark:                                                          | N/A                                                                         |                                                                             |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |                                                                             |


### Response

**[models.DocumentFileUpdate](../../models/documentfileupdate.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorMessage        | 401,404                    | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |

## update_raw

Update Document Raw

### Example Usage

```python
from ragie import Ragie

s = Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.documents.update_raw(document_id="<DOCUMENT_ID>", update_document_raw_params={
    "data": {},
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               | Example                                                                   |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `document_id`                                                             | *str*                                                                     | :heavy_check_mark:                                                        | The id of the document.                                                   | <DOCUMENT_ID>                                                             |
| `update_document_raw_params`                                              | [models.UpdateDocumentRawParams](../../models/updatedocumentrawparams.md) | :heavy_check_mark:                                                        | N/A                                                                       |                                                                           |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |                                                                           |


### Response

**[models.DocumentRawUpdate](../../models/documentrawupdate.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorMessage        | 401,404                    | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |

## patch_metadata

Patch Document Metadata

### Example Usage

```python
from ragie import Ragie

s = Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.documents.patch_metadata(document_id="<DOCUMENT_ID>", patch_document_metadata_params={
    "metadata": {
        "classified": "null (setting null deletes key from metadata)",
        "editors": [
            "Alice",
            "Bob",
        ],
        "title": "declassified report",
        "updated_at": 1714491736216,
    },
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       | Example                                                                           |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `document_id`                                                                     | *str*                                                                             | :heavy_check_mark:                                                                | The id of the document.                                                           | <DOCUMENT_ID>                                                                     |
| `patch_document_metadata_params`                                                  | [models.PatchDocumentMetadataParams](../../models/patchdocumentmetadataparams.md) | :heavy_check_mark:                                                                | N/A                                                                               |                                                                                   |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |                                                                                   |


### Response

**[models.DocumentMetadataUpdate](../../models/documentmetadataupdate.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorMessage        | 401,404                    | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |

## get_summary

Get a LLM generated summary of the document. The summary is created when the document is first created or updated. Documents of types ['xlsx', 'csv', 'json'] are not supported for summarization. This feature is in beta and may change in the future.

### Example Usage

```python
from ragie import Ragie

s = Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.documents.get_summary(document_id="<DOCUMENT_ID>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `document_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | The id of the document.                                             | <DOCUMENT_ID>                                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.DocumentSummary](../../models/documentsummary.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorMessage        | 401,404                    | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |
