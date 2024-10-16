{{
  config(
    materialized='incremental'
    , incremental_strategy='merge'
    , unique_id='id'
  )
}}

select * from {{ ref('audit_dim_customers') }}
