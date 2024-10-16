with 
    staging as (
        select 
            id
            , first_name
            , last_name
            , last_updated_dt
            , country_code
            , dbt_valid_to
            , dbt_valid_from
            
        from {{ ref('snapshot_customers') }}
    )

    select * from staging
    where dbt_valid_to is null
    







with
    source as (

      select * from {{ source('bootcamp', 'js_raw_customers') }}

)

, renamed as (

    select
      id
      , first_name
      , last_name
      , country_code
      , last_updated_dt

    from source

  )

select * 
from staging
where dbt_valid_to is null
