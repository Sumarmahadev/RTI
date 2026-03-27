from datetime import datetime

def generate_rti_content(name, address, issue):
    summary = issue.strip().capitalize()

    date = datetime.now().strftime("%d-%m-%Y")
    place = address.split(",")[0]  # extract city

    letter = f"""
To,
The Public Information Officer (PIO),
[Concerned Department Name],
[Office Address]

Subject: Application under the Right to Information Act, 2005

Respected Sir/Madam,

I, {name}, residing at {address}, am a citizen of India. I would like to seek the following information under the provisions of the RTI Act, 2005:

1. {summary}

I request you to kindly provide the above-mentioned information within the stipulated time period as prescribed under the RTI Act, 2005.

If the requested information pertains to another department, kindly transfer the application to the concerned authority under Section 6(3) of the RTI Act.

Thanking you.

Yours faithfully,

{name}

Date: {date}
Place: {place}
"""
    return summary, letter