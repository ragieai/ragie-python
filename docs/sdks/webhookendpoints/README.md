# WebhookEndpoints

## Overview

### Available Operations

* [list](#list) - List Webhook Endpoints
* [create](#create) - Create Webhook Endpoint
* [get](#get) - Get Webhook Endpoint
* [update](#update) - Update Webhook Endpoint
* [delete](#delete) - Delete Webhook Endpoint

## list

List all webhook endpoints sorted by created_at in descending order. Results are paginated with a max limit of 100. When more endpoints are available, a `cursor` will be provided. Use the `cursor` parameter to retrieve the subsequent page.

### Example Usage

<!-- UsageSnippet language="python" operationID="ListWebhookEndpoints" method="get" path="/webhook_endpoints" -->
```python
from ragie import Ragie


with Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
) as r_client:

    res = r_client.webhook_endpoints.list(page_size=10)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `cursor`                                                                            | *OptionalNullable[str]*                                                             | :heavy_minus_sign:                                                                  | An opaque cursor for pagination                                                     |
| `page_size`                                                                         | *Optional[int]*                                                                     | :heavy_minus_sign:                                                                  | The number of items per page (must be greater than 0 and less than or equal to 100) |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.ListWebhookEndpointsResponse](../../models/listwebhookendpointsresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorMessage        | 401, 402, 429              | application/json           |
| models.ErrorMessage        | 500                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## create

Create a webhook endpoint to receive notifications about document status updates, connection sync progress, partition limits, and other tenant events.

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateWebhookEndpoint" method="post" path="/webhook_endpoints" -->
```python
from ragie import Ragie


with Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
) as r_client:

    res = r_client.webhook_endpoints.create(request={
        "name": "<value>",
        "url": "https://crazy-birth.name",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `request`                                                                           | [models.CreateWebhookEndpointPayload](../../models/createwebhookendpointpayload.md) | :heavy_check_mark:                                                                  | The request object to use for the request.                                          |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.WebhookEndpoint](../../models/webhookendpoint.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorMessage        | 401, 402, 429              | application/json           |
| models.ErrorMessage        | 500                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get

Get a webhook endpoint by its id.

### Example Usage

<!-- UsageSnippet language="python" operationID="GetWebhookEndpoint" method="get" path="/webhook_endpoints/{endpoint_id}" -->
```python
from ragie import Ragie


with Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
) as r_client:

    res = r_client.webhook_endpoints.get(endpoint_id="b2685048-407b-4461-ba68-ae1653b337f9")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `endpoint_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.WebhookEndpoint](../../models/webhookendpoint.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorMessage        | 401, 402, 404, 429         | application/json           |
| models.ErrorMessage        | 500                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## update

Update a webhook endpoint's name, URL, or active status. Use this to rotate endpoints or temporarily disable delivery without deleting the endpoint.

### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateWebhookEndpoint" method="patch" path="/webhook_endpoints/{endpoint_id}" -->
```python
from ragie import Ragie


with Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
) as r_client:

    res = r_client.webhook_endpoints.update(endpoint_id="70a542b9-871a-42f4-a4a2-9f03a857e785", update_webhook_endpoint_payload={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `endpoint_id`                                                                       | *str*                                                                               | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `update_webhook_endpoint_payload`                                                   | [models.UpdateWebhookEndpointPayload](../../models/updatewebhookendpointpayload.md) | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.WebhookEndpoint](../../models/webhookendpoint.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorMessage        | 401, 402, 404, 429         | application/json           |
| models.ErrorMessage        | 500                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## delete

Delete a webhook endpoint to stop delivering webhook notifications to its URL.

### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteWebhookEndpoint" method="delete" path="/webhook_endpoints/{endpoint_id}" -->
```python
from ragie import Ragie


with Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
) as r_client:

    res = r_client.webhook_endpoints.delete(endpoint_id="85d9c6f8-9d22-4119-886a-0389b9d5eee3")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `endpoint_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ResponseOK](../../models/responseok.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorMessage        | 401, 402, 404, 429         | application/json           |
| models.ErrorMessage        | 500                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |