# BoundingBoxLocation

Location within a paginated document using normalized coordinates.


## Fields

| Field                               | Type                                | Required                            | Description                         |
| ----------------------------------- | ----------------------------------- | ----------------------------------- | ----------------------------------- |
| `location_type`                     | *Optional[Literal["bounding_box"]]* | :heavy_minus_sign:                  | N/A                                 |
| `left`                              | *float*                             | :heavy_check_mark:                  | Left coordinate (0.0 to 1.0)        |
| `top`                               | *float*                             | :heavy_check_mark:                  | Top coordinate (0.0 to 1.0)         |
| `width`                             | *float*                             | :heavy_check_mark:                  | Width of the element (0.0 to 1.0)   |
| `height`                            | *float*                             | :heavy_check_mark:                  | Height of the element (0.0 to 1.0)  |
| `page_number`                       | *int*                               | :heavy_check_mark:                  | Page number                         |