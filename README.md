# Datahouse: Compatibility Predictor
**Usage:**

    python compatibility_predictor.py

**Program Details:**

The solution I developed reads from a input JSON file, calculates compatibility scores based on attributes for each of the applicants, and outputs the results (name,score) to a JSON file.

Compatibility scores are calculated using different weights for each attribute. For team fit, I valued Intelligence more than any of the other attributes, so I gave it a weight of 4. On the other end of the weights, I put spice tolerance as the lowest value as it doesn't contribute toward team fit.

The program is broken down into three separate functions which include load(), predict(), and export().

**load()**: Loads/reads data from the input JSON file and stores applicants and team_member information into separate lists.

**predict()**: Calculates compatibility score for each applicant and team_member

**export()**: Stores applicant names and compatibility scores in a dictionary, converts to JSON, and writes to the output JSON file.

Results are outputted to the terminal as well.
Average Team Compatbility Score is the average score for the entire team. This score can be used and compared to individual scores of applicants. Applicants who have a similar or higher compatibility score compared to the average team score would be seen as a good fit.