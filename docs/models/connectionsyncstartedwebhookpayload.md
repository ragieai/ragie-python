# ConnectionSyncStartedWebhookPayload


## Fields

| Field                   | Type                    | Required                | Description             |
| ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| `connection_id`         | *str*                   | :heavy_check_mark:      | N/A                     |
| `sync_id`               | *str*                   | :heavy_check_mark:      | N/A                     |
| `partition`             | *str*                   | :heavy_check_mark:      | N/A                     |
| `connection_metadata`   | Dict[str, *Any*]        | :heavy_check_mark:      | N/A                     |
| `create_count`          | *int*                   | :heavy_check_mark:      | N/A                     |
| `update_content_count`  | *int*                   | :heavy_check_mark:      | N/A                     |
| `update_metadata_count` | *int*                   | :heavy_check_mark:      | N/A                     |
| `delete_count`          | *int*                   | :heavy_check_mark:      | N/A                     |