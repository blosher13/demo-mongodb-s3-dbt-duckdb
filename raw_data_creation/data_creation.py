import random
from pprint import pprint

from data_template import (
    SCHEMAS,
    generate_id,
    generate_value
)

# ============================================================
# Configuration
# ============================================================

NUMBER_OF_RECORDS = 10


# ============================================================
# Record generation
# ============================================================

def generate_record(schema, references=None):

    references = references or {}

    record = {}

    for column, generator in schema.items():

        # Foreign key referencing a specific key on the target record,
        # e.g. ("reference", "staff_id")
        if isinstance(generator, tuple) and generator[0] == "reference":

            _, target_key = generator

            if column not in references:
                raise ValueError(
                    f"No reference provided for '{column}'"
                )

            record[column] = random.choice(
                references[column]
            )[target_key]

        # Foreign key where the target key matches the column name
        elif generator == "reference":

            if column not in references:
                raise ValueError(
                    f"No reference provided for '{column}'"
                )

            record[column] = random.choice(
                references[column]
            )[column]

        elif generator == "generate_id":

            prefix = column.replace("_id", "").upper()

            record[column] = generate_id(prefix)

        else:

            record[column] = generate_value(generator)

    return record


def generate_records(
    schema,
    number_of_records,
    references=None,
):

    return [
        generate_record(
            schema,
            references=references,
        )
        for _ in range(number_of_records)
    ]


# ============================================================
# Generate schools
# ============================================================

schools = generate_records(
    SCHEMAS["schools"],
    NUMBER_OF_RECORDS,
)


# ============================================================
# Generate students
# ============================================================

students = generate_records(
    SCHEMAS["students"],
    NUMBER_OF_RECORDS,
    references={
        "school_id": schools,
    },
)


# ============================================================
# Generate staff
# ============================================================

staff = generate_records(
    SCHEMAS["staff"],
    NUMBER_OF_RECORDS,
    references={
        "school_id": schools,
    },
)


# ============================================================
# Generate incidents
# ============================================================

incidents = generate_records(
    SCHEMAS["incidents"],
    NUMBER_OF_RECORDS,
    references={
        "school_id": schools,
        "student_id": students,
        "reported_by": staff,
    },
)


# ============================================================
# Generate medications
# ============================================================

medications = generate_records(
    SCHEMAS["medications"],
    NUMBER_OF_RECORDS,
    references={
        "school_id": schools,
        "student_id": students,
        "administered_by": staff,
    },
)


# ============================================================
# Generate care plans
# ============================================================

care_plans = generate_records(
    SCHEMAS["care_plans"],
    NUMBER_OF_RECORDS,
    references={
        "student_id": students,
    },
)


# ============================================================
# Print generated data
# ============================================================

# print("\nSCHOOLS")
# pprint(schools)

# print("\nSTUDENTS")
# pprint(students)

# print("\nSTAFF")
# pprint(staff)

# print("\nINCIDENTS")
# pprint(incidents)

# print("\nMEDICATIONS")
# pprint(medications)

# print("\nCARE PLANS")
# pprint(care_plans)
