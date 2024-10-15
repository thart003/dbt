{{

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


