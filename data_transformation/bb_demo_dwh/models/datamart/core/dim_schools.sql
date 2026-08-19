{{ config(
    materialized='external',
    location='s3://bb-s3-demobucket-215520152793-us-east-2-an/curated/dim_schools/dim_schools.parquet',
    format='parquet'
) }}

with schools as (

    select * from {{ ref('stg_schools') }}

)

select
    school_id  as school_key,
    school_id,
    school_name,
    school_type,
    address,
    city,
    postcode,
    email,
    phone

from schools
