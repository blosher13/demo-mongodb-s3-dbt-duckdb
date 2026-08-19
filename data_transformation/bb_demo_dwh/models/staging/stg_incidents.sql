with source as (

    select * from {{ source('bb-mdb-democluster', 'incidents') }}

),

renamed as (

    select
        _id                                     as incident_record_id,
        incident_id,
        student_id,
        school_id,
        reported_by                              as reported_by_staff_id,
        incident_type,
        severity,
        status,
        investigation_status,
        location,
        description,
        action_taken,
        witness_name,
        parent_notified,
        notification_method,
        cast(incident_date as timestamp)         as incident_date

    from source

)

select * from renamed
