 -- models/staging/school_health/stg_school_health__staff.sql

with source as (
    select * from {{ source('bb-mdb-democluster', 'staff') }}
),

renamed as (
    select
        _id                                       as staff_record_id,
        staff_id,
        school_id,
        first_name,
        last_name,
        email,
        phone,
        job_title,
        qualification,
        cast(qualification_expiry as timestamp)    as qualification_expiry
    from source
)

select * from renamed