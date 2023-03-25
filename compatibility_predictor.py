import json

def load():
    # load and read data from json input file
    with open('input.json') as data:
        input = json.load(data)

    # store applicant and team_member information in a list
    applicants = input['applicants']
    team_members = input['team']

    predict(applicants,team_members)

# predicts compatibility score based on attributes
def predict(applicants, team_members):
    # weigh attributes differently
    intel_weight = 4
    strength_weight = 1.5
    endurance_weight = 2
    spicy_weight = 1 

    # calculate average compatibility score of the team
    total_compat = 0

    # iterate through all team_members
    for person in team_members:
        # grab attributes from the team member
        attr_members = person["attributes"]

        # calculate compat score by using specified weights and attributes
        compat_score = 0
        compat_score += intel_weight * attr_members["intelligence"] 
        compat_score += strength_weight * attr_members["strength"]
        compat_score += endurance_weight * attr_members["endurance"]
        compat_score += spicy_weight * attr_members["spicyFoodTolerance"]

        total_compat += round((compat_score / 100),2)

    average_compat = round(total_compat / len(team_members),2)

    print("Average Team Compatibility Score:", average_compat)
    
    # iterate through applicants and calculate total comptabibility score
    for person in applicants:
        attr_app = person["attributes"]

        # calculate compat score by using specified weights and attributes
        compat_score = 0
        compat_score += intel_weight * attr_app["intelligence"] 
        compat_score += strength_weight * attr_app["strength"]
        compat_score += endurance_weight * attr_app["endurance"]
        compat_score += spicy_weight * attr_app["spicyFoodTolerance"]

        attr_app["compatibility"] = round((compat_score / 100),2)

    export(applicants)

# export applicants name and compatbility score information to an output json file
def export(applicants):
    scoredApplicants = {}
    scoredApplicants['scoredApplicants'] = []

    # iterate through applicants and store their name and compatibility score in dictionary 'scoredApplicants' for output
    for person in applicants:
        attributes = person['attributes']

        scoredApplicants['scoredApplicants'].append({"name":person['name'],"score":attributes['compatibility']})

        print(person['name'],":", attributes['compatibility'])

    # convert to JSON
    scored_output = json.dumps(scoredApplicants, indent=4)

    # write to output json file and store applicant name and compatibility score there
    with open('output.json','w') as outputFile:
        outputFile.write(scored_output)
    
# main function 
if __name__ == "__main__":
    load()