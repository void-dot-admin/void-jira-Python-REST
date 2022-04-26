from atlassian import Jira

jira = Jira(
    url="http://localhost:8080/",
    username="Type your username here",
    password="Type your password here!",
    verify_ssl=False  # this is not required, but in case you get the SSL error when running the script
)
for x in range(20):  # this will create 20 tickets
    jira.issue_create(fields={
        'project': {'key': 'SCRUM'},  # add your Project Key here
        'issuetype': {'name': 'Task'},  # add your issue Type name
        'summary': 'Test Python REST API',
        'description': 'This is the description',
        'customfield_10500': 'Test text string',  # Single Text line customField
        'customfield_10501': {'value': 'Second Option'}  # Single select option customField
    })
