with source as (
    select * from {{ source('bb-mdb-democluster', 'students') }}
)
select
    _id                           as student_record_id,
    student_id,
    school_id,
    first_name,
    last_name,
    cast(date_of_birth as date)   as date_of_birth,
    gender,
    year_group,
    parent_name,
    parent_email,
    parent_phone,
    parent_relationship
from source