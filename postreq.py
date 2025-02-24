from api_utills.api_utils import postrequest, fetch_and_validate
from api_manger.course_api_manager import courseurl, courseheaders, get_encoded_payload
from api_manger.login_api_manager import loginheaders, get_login_payload, loginurl

# Define the authtoken here
authtoken = "ede8ec0c23bd49ab1e3a3d9f0d6315891699825ede6dd001dba5b6fafe6bc5694eb4bb2f220bcfef68430f5607c9931a8b530fcc7e1b9a89b3bcb10573e2abae"

malayalam_path = "malayalam/programming/python-zero-to-hero/"
tamil_python_path = "tamil/web-development/python-flask/"

# Login Request  
responsetext = postrequest(loginurl, loginheaders, get_login_payload(authtoken))
fetched = fetch_and_validate(responsetext, "rank","0")
print("Rank:", fetched)

# Course Requests (Pass authtoken dynamically)
coursetext = postrequest(courseurl, courseheaders, get_encoded_payload(malayalam_path, authtoken))
fetched = fetch_and_validate(coursetext, "key","pythonzerotoheromalayalammalayalam")
print("Malayalam Course Key:", fetched)

coursetext = postrequest(courseurl, courseheaders, get_encoded_payload(tamil_python_path, authtoken))
fetched = fetch_and_validate(coursetext, "key","pythonflasktamil")
print("Tamil Course Key:", fetched)


