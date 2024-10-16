{{
  config(
    materialized='incremental'
    , incremental_strategy='merge'
    , unique_key='id'
  )
}}

with
  staging as (
    select
      id
      , user_id
      , order_date
      , status
      , last_updated_at
    from {{'source('bootcamp'. 'js_raw_orders') }}
  )

  select *
  from staging
  {% if is_incremental() &}
    where last_updated_dt > (select max(last_updated_dt) from {{this}})
  {% endif %}

  

