# DocumentWithContent


## Fields

| Field                                                                                     | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `id`                                                                                      | *str*                                                                                     | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `created_at`                                                                              | [date](https://docs.python.org/3/library/datetime.html#date-objects)                      | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `updated_at`                                                                              | [date](https://docs.python.org/3/library/datetime.html#date-objects)                      | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `status`                                                                                  | *str*                                                                                     | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `name`                                                                                    | *str*                                                                                     | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `metadata`                                                                                | Dict[str, [models.DocumentWithContentMetadata](../models/documentwithcontentmetadata.md)] | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `partition`                                                                               | *str*                                                                                     | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `content`                                                                                 | *str*                                                                                     | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `chunk_count`                                                                             | *OptionalNullable[int]*                                                                   | :heavy_minus_sign:                                                                        | N/A                                                                                       |
| `external_id`                                                                             | *OptionalNullable[str]*                                                                   | :heavy_minus_sign:                                                                        | N/A                                                                                       |