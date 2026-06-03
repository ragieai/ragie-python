# Elements

## Overview

### Available Operations

* [list](#list) - List Elements For Document
* [get](#get) - Get Element For Document

## list

List the latest elements for a document. The results are sorted by index in ascending order. Results are paginated with a max limit of 100. When more elements are available, a `cursor` will be provided. Use the `cursor` parameter to retrieve the subsequent page

### Example Usage

<!-- UsageSnippet language="python" operationID="list_elements" method="get" path="/documents/{document_id}/elements" -->
```python
from ragie import Ragie


with Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
) as r_client:

    res = r_client.elements.list(request={
        "document_id": "269a3615-37c3-4b93-9a7c-9fa027d282c1",
        "partition": "acme_customer_id",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.ListElementsRequest](../../models/listelementsrequest.md)   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListDocumentElements](../../models/listdocumentelements.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorMessage        | 401, 402, 429              | application/json           |
| models.ErrorMessage        | 500                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get

Returns an element for a specific id

### Example Usage

<!-- UsageSnippet language="python" operationID="get_element" method="get" path="/elements/{element_id}" -->
```python
from ragie import Ragie


with Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
) as r_client:

    res = r_client.elements.get(element_id="d255ee42-ddef-408f-9700-686a6c8fed3c")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `element_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.APIDocumentElement](../../models/apidocumentelement.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorMessage        | 401, 402, 429              | application/json           |
| models.ErrorMessage        | 500                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |