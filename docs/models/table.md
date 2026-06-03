# Table


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `type`                                                               | *Optional[Literal["Table"]]*                                         | :heavy_minus_sign:                                                   | N/A                                                                  |
| `content`                                                            | *str*                                                                | :heavy_check_mark:                                                   | The Table in HTML.                                                   |
| `description`                                                        | *str*                                                                | :heavy_check_mark:                                                   | A brief summary of the content in the table.                         |
| `header_range`                                                       | *OptionalNullable[str]*                                              | :heavy_minus_sign:                                                   | Optional normalized header rows range used for <thead> construction. |