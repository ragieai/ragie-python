# PartitionDetail


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `name`                                                               | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `is_default`                                                         | *bool*                                                               | :heavy_check_mark:                                                   | N/A                                                                  |
| `limit_exceeded_at`                                                  | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |
| `limits`                                                             | [models.PartitionLimits](../models/partitionlimits.md)               | :heavy_check_mark:                                                   | N/A                                                                  |
| `stats`                                                              | [models.PartitionStats](../models/partitionstats.md)                 | :heavy_check_mark:                                                   | N/A                                                                  |