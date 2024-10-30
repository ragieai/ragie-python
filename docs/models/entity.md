# Entity


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `created_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |
| `updated_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |
| `instruction_id`                                                     | *str*                                                                | :heavy_check_mark:                                                   | The ID of the instruction which generated the entity.                |
| `document_id`                                                        | *str*                                                                | :heavy_check_mark:                                                   | The ID of the document which the entity was produced from.           |
| `data`                                                               | Dict[str, *Any*]                                                     | :heavy_check_mark:                                                   | N/A                                                                  |