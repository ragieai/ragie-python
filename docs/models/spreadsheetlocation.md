# SpreadsheetLocation

Location within a spreadsheet using cell ranges.


## Fields

| Field                              | Type                               | Required                           | Description                        |
| ---------------------------------- | ---------------------------------- | ---------------------------------- | ---------------------------------- |
| `location_type`                    | *Optional[Literal["spreadsheet"]]* | :heavy_minus_sign:                 | N/A                                |
| `range`                            | *OptionalNullable[str]*            | :heavy_minus_sign:                 | Excel-style range like 'A1:C10'    |
| `sheet_name`                       | *OptionalNullable[str]*            | :heavy_minus_sign:                 | Name of the sheet                  |
| `sheet_index`                      | *OptionalNullable[int]*            | :heavy_minus_sign:                 | 0-based index of the sheet         |