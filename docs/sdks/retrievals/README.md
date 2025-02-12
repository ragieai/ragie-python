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

with Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
) as r_client:

    res = r_client.retrievals.retrieve(request={
        "query": "What is the best pizza place in SF?",
        "max_chunks_per_document": 0,
        "partition": "<value>",
    })

    assert res is not None

    # Handle response
    print(res)

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
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorMessage        | 401, 402, 429              | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |