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

select * from renamed
