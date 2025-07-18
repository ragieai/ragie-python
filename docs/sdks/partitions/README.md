# Partitions
(*partitions*)

## Overview

### Available Operations

* [list](#list) - List Partitions
* [create](#create) - Create Partition
* [get](#get) - Get Partition
* [delete](#delete) - Delete Partition
* [set_limits](#set_limits) - Set Partition Limits

## list

List all partitions sorted by name in ascending order. Results are paginated with a max limit of 100. When more partitions are available, a `cursor` will be provided. Use the `cursor` parameter to retrieve the subsequent page.

### Example Usage

```python
from ragie import Ragie


with Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
) as r_client:

    res = r_client.partitions.list(page_size=10)

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

**[models.ListPartitionsPartitionsGetResponse](../../models/listpartitionspartitionsgetresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorMessage        | 401, 402, 429              | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## create

Create a new partition. Partitions are used to scope documents, connections, and instructions. Partitions must be lowercase alphanumeric and may only include the special characters `_` and `-`. A partition may also be created by creating a document in it. Limits for a partition may optionally be defined when creating.

### Example Usage

```python
from ragie import Ragie


with Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
) as r_client:

    res = r_client.partitions.create(request={
        "name": "<value>",
        "pages_hosted_limit_monthly": 1000,
        "pages_processed_limit_monthly": 1000,
        "pages_hosted_limit_max": 1000,
        "pages_processed_limit_max": 1000,
        "audio_processed_limit_monthly": 60,
        "audio_processed_limit_max": 60,
        "video_processed_limit_monthly": 60,
        "video_processed_limit_max": 60,
        "media_streamed_limit_monthly": 1024,
        "media_streamed_limit_max": 1024,
        "media_hosted_limit_monthly": 1024,
        "media_hosted_limit_max": 1024,
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [models.CreatePartitionParams](../../models/createpartitionparams.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.Partition](../../models/partition.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorMessage        | 401, 402, 429              | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get

Get a partition by its ID. Includes usage information such as the number of documents and pages hosted and processed. The partition's limits are also included.

### Example Usage

```python
from ragie import Ragie


with Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
) as r_client:

    res = r_client.partitions.get(partition_id="<id>")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `partition_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PartitionDetail](../../models/partitiondetail.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorMessage        | 401, 402, 429              | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## delete

Deletes a partition and all of its associated data. This includes connections, documents, and partition specific instructions. This operation is irreversible.

### Example Usage

```python
from ragie import Ragie


with Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
) as r_client:

    res = r_client.partitions.delete(partition_id="<id>")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `partition_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Dict[str, str]](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorMessage        | 401, 402, 429              | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## set_limits

Sets limits on a partition. Limits can be set on the total number of pages a partition can host and process. When the limit is reached, the partition will be disabled. A limit may be removed by setting it to `null`.

### Example Usage

```python
from ragie import Ragie


with Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
) as r_client:

    res = r_client.partitions.set_limits(partition_id="<id>", partition_limit_params={
        "pages_hosted_limit_monthly": 1000,
        "pages_processed_limit_monthly": 1000,
        "pages_hosted_limit_max": 1000,
        "pages_processed_limit_max": 1000,
        "video_processed_limit_monthly": 3600,
        "video_processed_limit_max": 3600,
        "audio_processed_limit_monthly": 3600,
        "audio_processed_limit_max": 3600,
        "media_streamed_limit_monthly": 1024,
        "media_streamed_limit_max": 1024,
        "media_hosted_limit_monthly": 1024,
        "media_hosted_limit_max": 1024,
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `partition_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `partition_limit_params`                                            | [models.PartitionLimitParams](../../models/partitionlimitparams.md) | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PartitionDetail](../../models/partitiondetail.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorMessage        | 401, 402, 429              | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |