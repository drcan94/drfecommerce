# product         -> name                           (string)    (required)
#                 -> description                    (text)      (required)
#                 -> is_digital                     (boolean)   (required)
#                 -> brand FK
#                 -> category FK

# category        -> name                           (string)    (required)
#                 -> parent TFK

# brand           -> name                           (string)    (required)

# product line    -> price                          (float)     (required)
#                 -> sku (stock keeping unit)       (string)    (required)
#                 -> stock_qty                      (integer)   (required)
#                 -> product FK

# product image   -> name                           (string)    (required)
#                 -> alternative_text               (string)    (required)
#                 -> url                            (string)    (required)
#                 -> product_line FK

# attribute       -> name                           (string)    (required)

# attribute_value -> value                          (string)    (required)
#                 -> attribute FK


# (all of tables have a unique primary key (pk or id -> BigAutoField))
