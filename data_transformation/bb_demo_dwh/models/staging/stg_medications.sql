-- stg_school_health__medications.sql
with source as (
    select * from {{ source('bb-mdb-democluster', 'medications') }}
),
renamed as (
    select
        _id                                as medication_record_id,
        medication_id,
        student_id,
        school_id,
        administered_by                    as staff_id,
        medication_name,
        dosage,
        frequency,
        administration_status,
        cast(last_administered as timestamp) as last_administered_at,
        cast(expiry_date as timestamp)       as expiry_date,
        quantity_in_stock
    from source
)
select * from renamed