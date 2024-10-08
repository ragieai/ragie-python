# Retrievals
(*retrievals*)

## Overview

### Available Operations

* [retrieve](#retrieve) - Retrieve

## retrieve

Retrieve

### Example Usage

```python
from ragie import Ragie

s = Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.retrievals.retrieve(request={
    "query": "What is the best pizza place in SF?",
    "top_k": 8,
    "filter_": {
        "department": {
            "$in": [
                "sales",
                "marketing",
            ],
        },
    },
    "rerank": True,
    "max_chunks_per_document": 0,
    "partition": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.RetrieveParams](../../models/retrieveparams.md)             | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Retrieval](../../models/retrieval.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorMessageError   | 401                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |