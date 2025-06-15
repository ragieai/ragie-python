# DocumentUpdateWebhookPayload


## Fields

| Field              | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `document_id`      | *str*              | :heavy_check_mark: | N/A                |
| `status`           | *Literal["ready"]* | :heavy_check_mark: | N/A                |
| `partition`        | *str*              | :heavy_check_mark: | N/A                |
| `metadata`         | Dict[str, *Any*]   | :heavy_check_mark: | N/A                |
| `external_id`      | *Nullable[str]*    | :heavy_check_mark: | N/A                |
| `name`             | *str*              | :heavy_check_mark: | N/A                |
| `connection_id`    | *Nullable[str]*    | :heavy_check_mark: | N/A                |
| `sync_id`          | *Nullable[str]*    | :heavy_check_mark: | N/A                |
| `error`            | *Nullable[str]*    | :heavy_check_mark: | N/A                |