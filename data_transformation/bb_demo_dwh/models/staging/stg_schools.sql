with source as (
    select * from {{ source('bb-mdb-democluster', 'schools') }}
),

renamed as (

    select
        _id                as school_record_id,
        school_id,
        school_name,
        school_type,
        address,
        city,
        postcode,
        email,
        phone

    from source

)

select * from renamed
