##CloudSDK API Testing

Evolving Postman collection to test CloudSDK APIs, including postive and negative test cases. Tests include references to TestRail test cases for optional reporting.

#####Note: Tests designed to be run in sequence

Intended to be run using Newman, Postman's command line collection runner. Can also be run by importing into Postman GUI to utilize Runner utility.

Getting Started:
1) Install Newman
2) Install TestRail reporter (optional)
3) Modify environment file for CloudSDK instance under test (baseUrl variable)
4) Run collection


Newman Install and Basics: https://learning.postman.com/docs/running-collections/using-newman-cli/command-line-integration-with-newman/ <br />
Testrail Reporter: https://www.npmjs.com/package/newman-reporter-testrail

