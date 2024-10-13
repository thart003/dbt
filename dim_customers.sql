with
  stg_customers as (
    select
      id
      , first_name
      ,last_name
      , last_updated_dt
      , country_code
      , dbt_valid_to
      , dbt_valid_from
    from {{ ref('stg_customers') }}
  )
  , country_codes as (
      select
        code
        , name
      from {{ ref('country_codes') }}
    )

    .joined as (
      select
        code
        , name
      from {{ ref('country_codes') }}
    )

    , joined as (
      select
        stg_customers.id
        , stg_customers.first_name



