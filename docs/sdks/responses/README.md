# Responses

## Overview

### Available Operations

* [create](#create) - Create Response
* [get](#get) - Get Response

## create

Create a response. This will generate an LLM or agentic response. At this time the only supported model is `deep-search`. Responses may be streamed or returned synchronously. The `retrieve` tool is currently the only supported tool, more tools will be added in the future. A single partition may be provided in the retrieve tool. If omitted the `default` partition is used.

### Example Usage

<!-- UsageSnippet language="python" operationID="create_response_responses_post" method="post" path="/responses" -->
```python
from ragie import Ragie


with Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
) as r_client:

    res = r_client.responses.create(request={
        "input": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.Request](../../models/request.md)                           | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Response](../../models/response.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorMessage        | 401, 402, 429              | application/json           |
| models.ErrorMessage        | 500                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get

Get a response by its ID. This will return the response and its status. If the response is still in progress, the status will be `in_progress`. If the response is completed, the status will be `completed`. If the response is failed, the status will be `failed`.

### Example Usage

<!-- UsageSnippet language="python" operationID="get_response_responses__response_id__get" method="get" path="/responses/{response_id}" -->
```python
from ragie import Ragie


with Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
) as r_client:

    res = r_client.responses.get(response_id="e613d0b7-4c9a-45ed-b32c-302d7f1c5daf")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `response_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Response](../../models/response.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorMessage        | 401, 402, 429              | application/json           |
| models.ErrorMessage        | 500                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |